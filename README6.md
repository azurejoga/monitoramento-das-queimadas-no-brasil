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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1f990f2-06ce-36de-81ac-a11947846eb0 | -9.31245 | -48.58258 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 76ef4c5e-7843-3591-97c8-47c8f5595051 | -8.78883 | -44.8394 | 2026-05-08 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd0da4f1-ff10-3131-a4d3-6abf29b3bd8f | -8.78936 | -44.83585 | 2026-05-08 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20789684-02b6-3f42-879c-98689348426d | -9.41243 | -50.6788 | 2026-05-08 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b7a288e-3d39-39a4-bdd1-7dfebc4934bb | -9.29765 | -48.58788 | 2026-05-08 04:46:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45111f36-affc-3d23-aad1-3e744bd8cfa5 | -9.47246 | -46.14502 | 2026-05-08 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9195871a-7868-3dfa-b6e8-30943a122a1c | -10.04101 | -51.66613 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba5404ed-c7fa-3672-bf07-d2e9d6c076e9 | -8.69487 | -49.09594 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e6721140-742a-3306-aa3e-59431c3f2ec7 | -10.04716 | -51.67084 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a213324-db5b-3f6a-bfa3-9a6bfce99fb7 | -8.79091 | -44.83901 | 2026-05-08 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8f4aa9f-c219-3e1f-a768-8ffa63354c80 | -8.69486 | -49.07402 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba545f07-5b86-375c-96bd-03c742d25b53 | -10.04496 | -51.66307 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9e8b8ac-4ee2-38e4-9d43-f1240ba1e19a | -9.30904 | -48.58207 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92eb663d-2abc-3d73-8af0-6b9af53013bd | -9.47317 | -46.14026 | 2026-05-08 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b13e4c17-7ff3-3e05-a88f-c2b7e1ce12fd | -10.04994 | -51.67501 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aecf0c5d-60c7-3b9b-9884-9540fbd4a835 | -10.03763 | -51.66557 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e869e97-8b18-3fab-bde1-bafbac45848e | -8.36457 | -48.07738 | 2026-05-08 04:46:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3de7b748-6adb-374d-a022-b5267f274919 | -8.69542 | -49.09238 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| becdd595-fbea-3548-a9aa-3ec04abbabce | -10.14062 | -52.18935 | 2026-05-08 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9478a113-e1a5-3991-bae8-d9677626b784 | -11.94532 | -43.37672 | 2026-05-08 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f46b011-2409-31ad-bc10-2280e8eb24c0 | -8.69655 | -49.09601 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d07b1f0f-37bf-3130-b25b-e2902443f50f | -11.12231 | -45.11559 | 2026-05-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca2714d6-c1ef-336d-bd2e-862f205756af | -10.95264 | -48.84532 | 2026-05-08 04:46:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa159c7e-b5f7-3fee-81dc-a3e4a9953309 | -10.58565 | -53.51699 | 2026-05-08 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27947a67-8a99-3de8-a0bd-e20a1159611d | -8.6971 | -49.09245 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fe27c1d1-6dec-3a07-b191-a30fb24090c0 | -11.77352 | -43.6498 | 2026-05-08 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6724e72d-330d-3257-8051-e12435c4f487 | -8.36802 | -48.07791 | 2026-05-08 04:46:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55eb2aac-fe34-3a2c-ab5a-24f31d02804d | -8.69207 | -49.09185 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f59e8263-8679-3f13-9a40-49b13731685b | -9.30106 | -48.58841 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30bcfb1e-b3ea-3fb0-bfc2-e69c36c92f8a | -9.56312 | -44.57096 | 2026-05-08 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82ecfb42-2dc1-3b74-9cb4-98513cc6d141 | -8.78989 | -44.83224 | 2026-05-08 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83b942fc-2a0a-365f-ba43-7d73e28a037e | -11.12596 | -45.12012 | 2026-05-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbd539aa-1366-3e87-9e21-a6c4015875c4 | -10.6674 | -49.70406 | 2026-05-08 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1e5a152-d00c-3953-970c-50cb6cc7230d | -10.04159 | -51.66252 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ccc0c57-389c-3e0c-b23a-c8237976e70c | -9.56255 | -44.57488 | 2026-05-08 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbbff93e-1aca-3041-81f7-102e8e51472f | -9.30505 | -48.58525 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5136234-e6b0-3a42-adae-f5e486eb71d9 | -10.94081 | -49.44503 | 2026-05-08 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3c2d850-a4d5-32d5-ae24-f664ac67878d | -10.67075 | -49.70459 | 2026-05-08 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf5e8a31-3b06-375f-8348-43c8ab49c92f | -9.31188 | -48.58628 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d155fa8b-bc82-3e72-b3d8-ddcb5a0e3234 | -9.2948 | -48.58366 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c71287c-cb18-3a68-9ab1-1008a7ab0f4f | -10.49779 | -48.11396 | 2026-05-08 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ffd9e85-a83e-33bb-a669-179a0dfbe1c0 | -8.69598 | -49.08882 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7d25e0d-adad-36f9-8dcf-690e746ad850 | -9.56679 | -44.57555 | 2026-05-08 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee5eebad-d8c1-3ef4-a0bc-44b87cfa7588 | -11.42636 | -47.09041 | 2026-05-08 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58b14eae-fcfd-32ff-95ec-529adb5caaf5 | -8.69599 | -49.09957 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ee73e444-d527-3e9c-87e8-b65daf8b81dc | -10.40937 | -44.93577 | 2026-05-08 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4059bc35-6631-381d-8fb6-d56cb2fbc4b3 | -9.00855 | -41.99361 | 2026-05-08 04:46:00 | NPP-375D | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 202e55c6-b91b-3bad-ba53-1e0f3363ffef | -8.6993 | -49.07818 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42205d08-6c45-3297-a3b5-9a0021e9c860 | -10.87935 | -48.77704 | 2026-05-08 04:46:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed8fc349-cd79-3cb8-a809-9cfb67859877 | -11.06907 | -49.47255 | 2026-05-08 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13ae0025-ce7b-3b7c-8236-bb37580dcb6d | -9.29879 | -48.5805 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12e84264-66f4-3369-b793-521ece398825 | -9.41131 | -50.68582 | 2026-05-08 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7917a083-1970-316a-8af3-ba08bd1fb967 | -8.69431 | -49.0995 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 60a0a8fc-f441-3fed-aca2-e5f6ada34d9d | -11.01723 | -45.13304 | 2026-05-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b4648f3-4103-3d07-b9fd-47d1a1b8e991 | -10.93518 | -49.43675 | 2026-05-08 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70fa07e1-bea8-3149-9061-055076a444b8 | -8.50772 | -50.15316 | 2026-05-08 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 406c68ea-3c55-3ee5-a604-2860b169c3a0 | -8.71097 | -47.86386 | 2026-05-08 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad6dd138-2102-3702-935a-59970237cd47 | -10.04774 | -51.66724 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bcb47970-793e-3540-a6a3-7310342e2374 | -11.38654 | -47.81963 | 2026-05-08 04:46:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7a8e89d-c9da-3e0a-9c88-12fa2b8fd51b | -0.08813 | -51.27948 | 2026-05-08 04:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e67a6726-1787-32e0-96ec-f06bc6f65221 | -10.04437 | -51.66668 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 579cb7f2-eef2-3800-9d60-237af81bc3ad | -10.04657 | -51.67445 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 728f2304-79e3-3a16-9b68-e37a6e48ae32 | -10.05053 | -51.67141 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40a33386-6b66-3fbf-8693-f4163e8f4e89 | -5.3238 | -44.69315 | 2026-05-08 04:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70856530-1de7-37d4-8b1f-9d6f2707149f | -11.76885 | -43.64911 | 2026-05-08 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bdf8f31-e391-3c8e-b1f8-eb9d77907641 | -9.30447 | -48.58894 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5bcfa716-fe58-3fac-aa77-bb50686b5322 | -10.03705 | -51.66917 | 2026-05-08 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d73db8a-6388-322e-8a63-26dabf73cab2 | -10.24312 | -47.42048 | 2026-05-08 04:46:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39df0902-07cb-37ad-8d1a-9260fe7eb069 | -10.94979 | -48.84104 | 2026-05-08 04:46:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbdb22c5-9036-38c8-a0d7-443b9674a1a7 | -9.41464 | -50.68636 | 2026-05-08 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cf629c6-da41-3fb1-af01-17420eb22f0c | -11.1265 | -45.11616 | 2026-05-08 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e56e7686-198f-374f-a003-6841c1ddd7a6 | -9.29822 | -48.58419 | 2026-05-08 04:46:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71503104-1b28-3e91-b8bf-332e0f480b62 | -10.94137 | -49.44143 | 2026-05-08 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ec972e6-2168-3e31-96fe-e87d499a0381 | -8.69822 | -49.07455 | 2026-05-08 04:46:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c30f961-3f3d-335e-8f1a-2da582ef06de | -10.23925 | -52.22876 | 2026-05-08 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd9c93e3-29af-3593-8d45-a3997cb63933 | -10.23583 | -52.22819 | 2026-05-08 04:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d661a94-603e-3169-a42b-449ed6163d0d | -16.59906 | -58.24414 | 2026-05-08 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0db95e1e-177f-350f-acea-4e586f922c68 | -16.15261 | -58.48532 | 2026-05-08 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b6c26a80-cc93-36f8-80c6-0344bc9fb610 | -5.78098 | -45.13011 | 2026-05-08 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a560fba-2dec-3edf-bcd1-85baeb13ad6d | -11.79409 | -47.09732 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f648d9bb-228b-3777-9bb6-4ed5848426e1 | -12.8509 | -43.76078 | 2026-05-08 04:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9696101f-d657-3c6a-b93c-51009c59bf80 | -11.82152 | -47.33612 | 2026-05-08 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9226daef-8adc-370e-9b23-ce93c9c6639d | -12.86031 | -43.76211 | 2026-05-08 04:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fcd81edf-23e5-391f-9611-8ebc33630f4a | -11.79848 | -47.10027 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3db6bd9-1918-3662-93f5-6657c9fb3837 | -11.93332 | -46.75149 | 2026-05-08 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ce58057-4226-3ef6-8491-ebc33a0fbd6b | -11.84415 | -55.01405 | 2026-05-08 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caa244bd-6314-3843-a0d7-d20522d986b3 | -11.82089 | -47.3405 | 2026-05-08 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e42e1d6c-ab81-32f1-93c2-a36c3638ae35 | -5.78169 | -45.12532 | 2026-05-08 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b25f2e3-824d-3b46-8261-d094b8a4cfb1 | -11.82025 | -47.34487 | 2026-05-08 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99c30c9a-e3b1-3688-b4ba-8330e031767f | -15.61731 | -46.51251 | 2026-05-08 04:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a30ccbcd-df39-32c5-8ad4-42ceb65d0d22 | -17.10173 | -51.34848 | 2026-05-08 04:49:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7551dd5e-9d73-3484-aa08-cb46da4fb20d | -11.79035 | -47.09677 | 2026-05-08 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69abd44c-29f1-3651-9ef6-658736b98cdf | -12.42426 | -54.21787 | 2026-05-08 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6aaaa2c-271e-377a-a94b-1c2528ac68ba | -13.47948 | -48.91914 | 2026-05-08 04:49:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0c4c67d-1cb5-3c39-ae06-1134b542df42 | -15.61273 | -46.51566 | 2026-05-08 04:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a7f04d5e-d2ed-39f4-85e9-469d2fc98c03 | -17.69706 | -51.67097 | 2026-05-08 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed307276-9377-384c-94a4-e7f369654897 | -14.19615 | -57.42235 | 2026-05-08 04:49:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4f3d028-0ff5-3473-b460-0c3b300a48ee | -16.59988 | -58.23983 | 2026-05-08 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ee7f5bc5-3af5-34d7-b82e-bc65a5ef67f6 | -19.18253 | -47.34943 | 2026-05-08 04:49:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6da0a0ad-56b8-35f6-af4f-0a87671f3b3e | -5.78242 | -45.12051 | 2026-05-08 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README7.md)
