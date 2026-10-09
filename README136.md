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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49b1780d-4d36-3ccf-8586-41cc9109df2d | -6.44766 | -52.70658 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb7c281a-4a55-3030-bb0d-c80ccc1df46c | -3.26122 | -54.04403 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642be6d5-02f7-3b82-a113-f526718d2512 | -3.46438 | -59.26327 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce3b26a6-89e3-3bdb-94b2-a4e459c5667b | -6.46196 | -55.49085 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6efea9a0-b715-39b7-a80f-09c89e6ee9d1 | -2.82765 | -57.62141 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 843040f7-a49d-3091-b27c-7ebb143998d0 | -11.06146 | -44.06566 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edaff2dc-e4ba-3197-af85-e5dbdcd0a28e | -6.72848 | -48.11407 | 2026-10-09 05:04:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e42e8b6e-55fb-3965-a043-c67910d54f81 | -11.77396 | -43.52951 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc029222-179b-3d7c-8c83-64934b5a89da | -8.32038 | -45.45329 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 328b2522-8617-3d40-9a41-1e48b13d9bc9 | -2.57803 | -56.17363 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c42913d-b643-330d-8504-b5bea5738e3b | -2.84054 | -57.48822 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b4ea48a-0466-337d-85fa-f2c0004dc9e7 | -5.95225 | -55.35225 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f72ff922-f7a2-331a-9fcf-8a7ecec7e4a1 | -3.02794 | -54.05938 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 794c9ea1-ebd8-33f3-ac2f-4fb3cb483802 | -3.31344 | -54.05228 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fb7bca9-1e49-38e6-9723-92a4cb740b66 | -7.37816 | -47.01878 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d85fee-81a3-35b0-9840-34278ad4f491 | -4.63741 | -50.95401 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa09eea2-8bcf-3e7e-8a7c-b0881d786d83 | -7.8175 | -50.2193 | 2026-10-09 05:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96bdf89b-562b-35c3-bd09-9447b093b284 | -4.11081 | -54.01569 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 204e93ef-55f7-3f9a-a4b5-e52374ec129e | -4.2937 | -54.8025 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f92d6880-4cf1-3db3-8cdc-ee2ae7953983 | -3.02194 | -54.18498 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dfe34c33-66bc-38f9-86bc-15c2bd357f2d | -5.95067 | -55.33957 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 500a3fef-0bde-3a40-9c3a-b7ab9a7bfc1b | -3.25076 | -54.04242 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3115a541-7f0c-3754-be52-712f4e0c7951 | -5.70529 | -53.46149 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9f2d6b1-fa03-3719-8f66-d66d9ef4c6b5 | -9.89762 | -58.12058 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97a7e925-cac5-393c-9fd7-3d06f870c615 | -5.89779 | -52.0358 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c657372-0519-3f84-81a1-7f80d61edb09 | -7.441 | -63.55124 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c59e954d-d121-350f-acf4-4dbd3d31f733 | -3.03963 | -54.23163 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31aeea89-dc33-347a-9ebe-50d9e0813c05 | -11.39822 | -47.5812 | 2026-10-09 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1210cbeb-cc9a-3b43-a7f7-488d689134b6 | -3.84872 | -55.82109 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cd76dc47-3f3d-34d1-ba54-ddb063eaf9e5 | -3.84197 | -55.83861 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49e8e72f-1e4d-3e5a-8379-1372c93aecec | -3.46603 | -59.25307 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 637a1e62-2ee3-35a0-8e2d-3033ea488cfb | -4.12278 | -54.02924 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88ce7329-88ba-3c14-afae-31d44e41b510 | -3.46009 | -50.58654 | 2026-10-09 05:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f5c5f142-b1af-322c-9c02-55f54fa044b0 | -5.2714 | -55.95444 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f522b4a-df76-3280-a049-40d50a600ca6 | -7.4368 | -63.55473 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce9d5266-86b5-3f29-9fdf-d6544a54741f | -6.13184 | -55.68669 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a42c079-f346-3cb2-ba46-edde37be54b1 | -4.80408 | -54.6778 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d866d6f-9c28-352b-8ed0-a33094a46ff7 | -3.00157 | -54.06395 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8960cc00-08c0-31cc-854f-566b75ae8674 | -2.5551 | -58.02922 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc9516f1-90ec-369a-a658-e9cad585d2c0 | -7.9061 | -54.71379 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e82c63cb-315b-3111-a4e2-f35a452a46d8 | -6.31329 | -54.80405 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3e917ee-5a51-3270-899a-87bb0edf8a64 | -3.75189 | -59.49984 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c8b4d52-f08d-3a91-90ea-144a6331e7ea | -6.24316 | -52.85929 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a70ce87-3d1e-3e97-ba08-ba1b60824d52 | -3.23836 | -54.66025 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14c7bcf7-5596-308e-89ae-f0448a349ca6 | -9.69163 | -58.09263 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6518e95-289d-32db-8b41-dd49e5353028 | -8.32588 | -45.44884 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5406e90-0db5-32df-b34c-36cba51615e8 | -3.85358 | -55.95823 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ae4622b-fe9d-3e1b-a52c-3a24bb5a1464 | -7.44615 | -63.55669 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58fbfc86-ae47-30a7-b531-789ea2e2942c | -6.03401 | -53.48829 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de841242-c6b5-3581-9cbf-d5129f63e0e9 | -2.9314 | -54.14371 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfa70492-f69c-3b93-965f-651202598a92 | -2.99926 | -53.89933 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edf12ebe-c62e-34c3-98f2-388567a21b80 | -3.26346 | -54.05222 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78105160-5224-3aa4-8ba0-38ab7cfb8e78 | -7.47368 | -42.83688 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 184aece6-0942-3a50-bbde-4eb52f0a7b0e | -2.63334 | -57.46368 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f4f967b-854e-3bff-9360-048101326e0f | -8.97112 | -45.14402 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 368743e6-6aea-341d-a7c7-0102e8f6ad7f | -2.99808 | -54.06339 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 436b9459-2b4d-3e11-abb5-581e1e7404b5 | -3.01047 | -54.74213 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 270583a8-37b4-331b-9c40-9c55ef853c75 | -3.30587 | -54.05499 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d70bcc9-1f76-3338-91bc-7ffd34186b13 | -3.04159 | -54.15239 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b5155018-09c6-38f5-91ac-0b7cb3141859 | -8.27527 | -45.73462 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ed9f0b0-5ffd-345f-9e9a-2b7ca3c12039 | -8.33167 | -49.12412 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1bfa2c6-d717-3f95-844b-c3aa3fec5e53 | -3.60672 | -61.62441 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2c58d4b-28de-346f-b2a8-e1fc99715260 | -6.50222 | -55.3879 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a41d7a0-5a66-34f9-802a-207b605bf3a2 | -3.485 | -54.62266 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbac7d0a-0fe4-35e5-a0b9-ed85b7aa9709 | -3.21718 | -53.89 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2536c529-50e5-3a9a-988a-8682dc5cf799 | -10.99045 | -45.39615 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b834f953-c1b0-3d0b-98c5-65e3be312091 | -4.05977 | -49.10809 | 2026-10-09 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 096a0993-1f74-3e59-9f94-eff85f592060 | -3.56841 | -54.68387 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 96101817-0539-3aaa-8a81-6bd7104aa72c | -8.57924 | -53.10408 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13aa9b69-e8f5-39ea-bfc0-c4bc45d21f19 | -3.29057 | -51.53927 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44eafc48-1934-3153-9ae0-ebd9cc8f82e8 | -3.98267 | -59.34991 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f99f2e57-ee45-3458-a9a8-2be854f63c6c | -2.90649 | -54.02525 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20826268-89e6-3b16-98f3-f019f4c34004 | -7.4122 | -44.76179 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f288577-d1b8-3d87-a48c-fb659a368188 | -3.54626 | -54.67357 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fee2450-a370-30bf-a79e-e0c166422d05 | -4.0398 | -54.22657 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9b57003-bc4a-3728-b3fd-76a0be5f3177 | -3.1223 | -54.16845 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| a4247f1f-9a6b-39c6-9292-60e9a7d2e782 | -9.29417 | -47.43992 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fb15144e-3972-3935-8f6e-628f183132d9 | -3.17099 | -57.49809 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c0e65b6-a1f0-3bf2-9dc4-654cb7bea585 | -3.51221 | -54.63512 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5a5f0f5-4cba-34bc-a8d6-88d9a3407d2e | -3.09739 | -53.9609 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2876e5c-d200-395c-94d1-a3eb5ec9bbdf | -4.57344 | -55.99574 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5dde78d-8710-35bd-ac7b-03f7aa99f894 | -5.69634 | -53.45275 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf936bae-547f-3dbe-a81f-9ce98cc382ab | -8.3011 | -45.7352 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e80dfb0-5d91-3e14-9837-0511b2bdf9c0 | -8.27992 | -45.73564 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f455a21c-51ff-3f32-aa53-aa28186d0746 | -2.94807 | -54.17429 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e0cef8-82dd-36fb-ad04-cfa9e8cb0533 | -11.07611 | -44.08211 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97c1eb6e-bf4f-3eed-b3cb-2ed06ac910cb | -7.26571 | -45.34802 | 2026-10-09 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4037525-9ec2-3f98-91a0-a4ee400382a3 | -3.47079 | -59.25386 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e44fac7b-a0c9-3603-94fd-2ab2d7f92563 | -11.86426 | -43.55822 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51e716d3-e5ad-3a38-8591-8877ec7751e3 | -5.26694 | -55.95829 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 591912e0-6889-3dcf-84ec-f8037f9f3c67 | -11.42105 | -47.57588 | 2026-10-09 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19f52593-6443-3959-9094-f98fa4b301c0 | -3.13782 | -54.36289 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8235685-c1e8-3539-8291-5615e0e919ca | -2.31052 | -57.98409 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 442aa9b5-03de-3176-8310-a2328dc28730 | -2.98772 | -54.76078 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e773c92b-9176-353d-8f46-5b515beabcbe | -3.93938 | -55.71825 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d448999-850c-3bf1-93e9-efa388bac3c4 | -3.09757 | -53.9375 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecd70f7c-81be-3233-99f7-b341bf5b478d | -5.48715 | -45.22602 | 2026-10-09 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 906bf099-3635-38f0-bb58-2080492f228b | -5.44363 | -43.44498 | 2026-10-09 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1c09c07-4083-34c0-a997-b1f2aa3cfa73 | -10.73528 | -52.02883 | 2026-10-09 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12fc06d4-aa80-3baf-a064-8dc409443351 | -3.17536 | -53.84117 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README137.md)
