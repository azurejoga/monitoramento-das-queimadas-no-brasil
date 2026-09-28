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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c50030f-3f87-3ab6-903c-b8416947da94 | -14.17688 | -41.83067 | 2026-09-28 15:29:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 81821fb7-0a02-3ae2-b7b5-c2207a2ed988 | -14.88524 | -39.07845 | 2026-09-28 15:29:00 | NOAA-21 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 31a988f4-64fa-3c44-a5c9-c95810d79033 | -14.20362 | -41.32573 | 2026-09-28 15:29:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 1761aa26-5aa7-34b7-9c0c-19465f3ed7bf | -14.58422 | -41.23308 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 077b8336-5143-3466-bde2-29899133a379 | -6.25087 | -41.59941 | 2026-09-28 15:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 74f0b456-d177-3af1-b591-6ef8acc38856 | -15.34061 | -42.16735 | 2026-09-28 15:29:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 6cb513e9-0172-3ba2-8c76-59b588d05df8 | -11.70576 | -41.75625 | 2026-09-28 15:29:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| a4740b5f-b06a-34b4-beac-cda1b4bcf603 | -5.21363 | -36.75238 | 2026-09-28 15:29:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 3fa4e745-a6d8-30d8-9659-7f8a336aad5e | -12.52935 | -42.08073 | 2026-09-28 15:29:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c6dfee62-05ca-369d-a2df-f0af1694c423 | -14.74836 | -41.96412 | 2026-09-28 15:29:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 41313e50-6893-3639-bc29-2f7cfa3be707 | -9.34031 | -35.60573 | 2026-09-28 15:29:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e3d15fa4-6a38-38d0-9e8d-add8adaadcf0 | -14.1018 | -40.72007 | 2026-09-28 15:29:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 890e873f-1f56-3fc8-8739-e98cbade1bc9 | -5.89413 | -42.43727 | 2026-09-28 15:29:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e3913acd-e8a5-3a8f-8382-1d022e0d87c0 | -11.1474 | -40.30322 | 2026-09-28 15:29:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f3808fd7-54e0-3f89-9267-a022b504d51a | -15.55185 | -41.73421 | 2026-09-28 15:29:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 3397e0f5-5a6e-3787-a49e-708cc5237097 | -5.18967 | -36.87046 | 2026-09-28 15:29:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4937c6f3-5c4c-39ca-a9e9-6c9d9e3f3e72 | -11.60134 | -37.71331 | 2026-09-28 15:29:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9f56e578-4764-3a62-ad34-8b4e7b276c7d | -3.66896 | -39.00031 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c8ef9c97-cc14-3a4d-8a37-86932c02f820 | -3.87918 | -40.83835 | 2026-09-28 15:29:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 78d25c27-0c6e-3eed-8a5e-a75b29e3c10d | -9.18588 | -40.04752 | 2026-09-28 15:29:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| b71a0e44-388d-3976-a75c-81faf9d5dc8a | -14.58739 | -41.22958 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 1ae471ed-bb22-3a99-b3b2-2df25e8760d0 | -11.35809 | -41.49998 | 2026-09-28 15:29:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| e28cf6e6-7f87-3318-b379-50dce793eb87 | -10.05934 | -39.4584 | 2026-09-28 15:29:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 04baeb27-fbc2-3c23-a32f-f759ae4c8051 | -14.77606 | -41.14743 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 4dc5a73e-bc32-34f7-bbdf-9ab65c7c0259 | -15.21891 | -41.47652 | 2026-09-28 15:29:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| c8f60041-1df5-3da6-a0f4-3a3de1c085d6 | -15.4551 | -41.45 | 2026-09-28 15:29:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| 81d14943-7f70-3ec5-9e6c-f25452236e15 | -14.86919 | -41.02493 | 2026-09-28 15:29:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| 43a12051-f489-3af5-87b8-05de939c3959 | -14.23834 | -40.94761 | 2026-09-28 15:29:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 143eb0ab-cfc9-3ba2-b794-28dd7374fb98 | -13.3644 | -40.97288 | 2026-09-28 15:29:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 3664e45c-e76d-34e9-bd18-ef4728f4b7d7 | -14.45334 | -40.80095 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 2f7ec7c4-c7d7-30de-8b04-a65ef9ca394b | -14.58796 | -41.23542 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 3bce525e-2e75-3d02-b421-a12dcfe5b5c4 | -14.2435 | -40.94433 | 2026-09-28 15:29:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 872c0cf1-a31f-32a2-8a51-d3ea6cb790a8 | -14.20731 | -41.32843 | 2026-09-28 15:29:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| d3d493f4-9d19-386b-8a69-49fa19cd71e9 | -14.86463 | -41.02152 | 2026-09-28 15:29:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 7440ff4c-20ac-3caa-a77b-2c46f1e32a2d | -6.2502 | -41.5945 | 2026-09-28 15:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 132b5c07-02d5-3072-9760-a8b85319e589 | -13.87371 | -40.80592 | 2026-09-28 15:29:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2cef3e77-d1bc-3e2d-bb08-b7ec40e0651a | -9.26763 | -40.81209 | 2026-09-28 15:29:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8f280b88-8f2c-3cb3-97d9-5ca90d0cb434 | -14.79825 | -41.37919 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 7c285535-3493-3d94-b5b1-119663c7369d | -11.52383 | -41.67825 | 2026-09-28 15:29:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5d148e0c-bd39-3124-a9d4-49546e527837 | -14.20056 | -41.32888 | 2026-09-28 15:29:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 81c61daa-7dc9-309c-a54d-9bc8e097e716 | -11.43713 | -41.98806 | 2026-09-28 15:29:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dbfe3be9-60a1-37c5-9a67-20bd2280c761 | -14.45293 | -40.80099 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| d2dac1b6-bad2-3304-a123-e5bad11b15f9 | -12.08101 | -38.87138 | 2026-09-28 15:29:00 | NOAA-21 | SANTANÓPOLIS | BAHIA | Brasil | 2928307 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 48b79962-c1d7-3e3b-9ede-fd6be0973ba1 | -14.55884 | -40.74103 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 871ac836-770b-31b7-9c4f-f29a2ee69477 | -5.13772 | -35.58696 | 2026-09-28 15:29:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d2d5d5b9-cc97-3271-883e-aa774d5a9e64 | -10.06247 | -39.45663 | 2026-09-28 15:29:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2952000a-cc16-3413-a2ed-2f447da9f767 | -5.4984 | -36.44703 | 2026-09-28 15:29:00 | NOAA-21 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 62111ea4-6689-3742-a284-622eef2480f8 | -14.7918 | -41.95728 | 2026-09-28 15:29:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1c1dbb24-5cc9-3acc-856a-1105da55919d | -16.2882 | -40.19864 | 2026-09-28 15:29:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 5ae271e1-6105-36bc-988d-b03fbab21ba5 | -6.59237 | -42.93529 | 2026-09-28 15:29:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0f0a4882-0b37-3f49-9271-00b76f743def | -12.2723 | -50.1657 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| dc561c2a-cafc-3cdf-aad9-feff30ed5eaf | -11.7332 | -50.5516 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| c0afcdd0-e3ee-3e35-a6cf-8258a70a7d47 | -12.2897 | -50.2712 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 57917adf-5de4-35ff-b972-090f752bcf2f | -12.2639 | -50.7034 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 829eb49e-411d-3c21-840f-c6bfb92e63d8 | -13.3439 | -51.3187 | 2026-09-28 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3cd8fa89-bc1b-3bbc-bbc4-6b7c08d99275 | -12.3088 | -50.2688 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 387331c4-3c9b-3c0d-afee-aa3b2ea30170 | -11.5161 | -47.3703 | 2026-09-28 15:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| b36d8304-b857-34f8-a211-872ddb3ab3e1 | -12.4351 | -44.1497 | 2026-09-28 15:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 265.7 |
| 8c71a49f-7d0c-388c-bb26-ac5a5634f7dc | -13.161 | -48.5437 | 2026-09-28 15:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 153.3 |
| d4534b2d-517b-37a6-92cf-1588bec6a3b8 | -7.6852 | -54.7532 | 2026-09-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| ab3e4c8a-c6d4-3e19-9fda-68f4aa476d7f | -15.0984 | -54.7189 | 2026-09-28 15:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 189.5 |
| c3d4afeb-dbe7-3a1e-a0cc-9ec0eb140301 | -13.5911 | -51.458 | 2026-09-28 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 50f75b66-021b-3777-a106-fde47a152d05 | -10.2065 | -50.0113 | 2026-09-28 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 522.3 |
| 47a8d47e-8f7d-3269-94ec-fc83c7085523 | -12.1872 | -50.7339 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6d543a8d-63bc-33e7-9c87-ae8a6014a831 | -15.4003 | -47.9035 | 2026-09-28 15:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 31ea5840-80d4-3b01-af29-975d0398f488 | -11.5625 | -50.5283 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| fccafcd4-31e4-380d-845e-87fe30a36085 | -11.497 | -47.3727 | 2026-09-28 15:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| eb4c5897-a108-3f5a-a98e-e1a502a84239 | -10.0148 | -50.2443 | 2026-09-28 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0d619efa-a7c0-359b-9c6d-26d313df2d5a | -11.2118 | -54.0797 | 2026-09-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 66751f10-cc46-3dec-b485-7fbdf67d324d | -3.0798 | -58.0276 | 2026-09-28 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 7458a7e4-ccaa-3153-b905-e606393fdd4c | -12.1685 | -50.7147 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 41460347-9052-3f1d-8b1b-6600e229e003 | -11.9783 | -50.6943 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3bb77e66-9bd2-33ad-a87b-96c24074375b | -11.5352 | -47.3678 | 2026-09-28 15:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 1e4f46d2-a608-3dfb-a0ef-63fe06ec7f9b | -10.7115 | -60.7312 | 2026-09-28 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 49de6eac-e998-31a2-a56f-1c24579695d8 | -12.1115 | -50.7001 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 0034d238-623f-32a2-8da8-33471fece592 | -9.1525 | -49.9639 | 2026-09-28 15:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 3863114b-9a77-31f9-8e12-f90286003fa2 | -12.2636 | -50.7248 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 0b70849a-2022-3949-9aab-445b8e5c1da0 | -12.6263 | -47.3075 | 2026-09-28 15:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 0e2dd838-c911-3a06-a134-c6bcad3e4a6a | -11.3043 | -51.3434 | 2026-09-28 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 4891d728-1168-3f78-945a-17c72f162ef0 | -10.8185 | -57.2391 | 2026-09-28 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 49b24a48-447a-3c63-a191-3bba23779093 | -7.3306 | -54.995 | 2026-09-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| c81c8e44-f8c8-3356-b6c7-a1b1b13b644a | -11.3436 | -54.1086 | 2026-09-28 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8da310f2-b4d7-31ee-8f57-67153344d59b | -12.3283 | -50.2449 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 1edb476c-be8f-35a1-8199-b8478276e442 | -9.1057 | -60.9511 | 2026-09-28 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 7cddf8da-d917-318d-a46e-4b7cc9176b82 | -10.8532 | -54.0916 | 2026-09-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 75d0c3d5-4f46-3b20-82d3-39d5e336c474 | -12.0921 | -50.7237 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| efa46c09-74a4-3ed7-8010-6322eeac8bf8 | -12.2251 | -50.7508 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| ea2ae24a-3652-3a92-b1df-a8e75beda04b | -12.9457 | -51.0695 | 2026-09-28 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f67f650b-13ef-358a-bb9f-f95f65b4ef6c | -9.9784 | -50.1412 | 2026-09-28 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 1f88e499-1d6f-31cd-ada6-e5f5f3819b8d | -12.2057 | -50.7745 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| c1474459-f7b0-350e-b5e3-24260c571d8b | -11.6951 | -50.556 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 79875a00-a08b-3833-99ba-86a8601a00fe | -7.4869 | -44.5751 | 2026-09-28 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| a21f84f4-4736-37c3-838a-f84b0efe5b2b | -10.9538 | -50.6592 | 2026-09-28 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 905c7cff-9c51-3b52-971d-ec63990d579d | -12.2502 | -50.362 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c0be4772-cdea-30c6-aca3-4870a3d2123d | -10.6928 | -60.7322 | 2026-09-28 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a4b61fea-a00e-3b65-a16f-aa188a76fba5 | -12.2123 | -50.3451 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 15d1c78d-e0ed-332e-9021-46f760a0b18f | -11.5815 | -50.5261 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 85422727-3f9e-3ccf-9014-1149a3f1575a | -11.1966 | -44.7805 | 2026-09-28 15:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 628.9 |
| 3c2eac11-3ea7-3b1d-9cae-78a1f2c178e9 | -10.9349 | -50.6612 | 2026-09-28 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 262fa18a-e931-378b-8813-a7715326dbc3 | -11.4173 | -51.3948 | 2026-09-28 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |


[Clique aqui para ver as próximas entradas](README88.md)
