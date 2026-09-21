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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b750aa2-3a11-3c5e-b3f9-ab47561dd4a0 | -6.2759 | -47.6506 | 2026-09-21 17:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 749091ca-6775-3e29-9de9-f4fb40e86130 | -11.4001 | -44.076 | 2026-09-21 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 321.2 |
| f7047d8a-a3f1-3e4d-9a29-f96ffd106ff8 | -5.9151 | -59.9522 | 2026-09-21 17:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a89729c5-28d6-3c4c-b1e0-8544579c89da | -6.5257 | -44.9342 | 2026-09-21 17:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 9158e472-e7d7-3a74-8628-8b0bd302959e | -6.5449 | -44.8871 | 2026-09-21 17:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 40edf5c2-cdc3-3049-af1a-5104df273020 | -9.3577 | -50.0943 | 2026-09-21 17:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 3bcd2ec1-ba6d-396d-bda4-30c5999be956 | -9.0034 | -72.7059 | 2026-09-21 17:50:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 402005bc-8ac0-3e0c-ace6-ba242de3c4ce | -6.7863 | -58.8995 | 2026-09-21 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 10178132-474a-3a7e-ba9a-baa9d06e7b7b | -5.1838 | -49.3358 | 2026-09-21 18:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 66df2f6e-4545-32f7-909b-eacd08c9385e | -4.8865 | -55.8846 | 2026-09-21 18:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 1bf92f7f-9a9d-3883-a605-ac1c469555c7 | -11.0048 | -49.7325 | 2026-09-21 18:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 45ddeeab-002e-319c-88bf-e1cc3d02da33 | -9.8683 | -48.4689 | 2026-09-21 18:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 188.4 |
| b3ed36bf-4646-3f5b-ba05-3e678c704239 | -3.8651 | -58.7056 | 2026-09-21 18:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e5dc88c2-6a82-33a6-8488-374cf8f33c5b | -6.7484 | -59.075 | 2026-09-21 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| f2dbc59f-69b2-3164-ba0c-f8bf0215e6db | -2.8608 | -57.7994 | 2026-09-21 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 179.4 |
| 0db7db9e-1d3c-33cc-b74a-4767a9725334 | -10.6878 | -50.751 | 2026-09-21 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ac8e1079-c352-330b-a03a-5abaa4e51412 | -8.8198 | -71.8108 | 2026-09-21 18:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9238e415-98d8-3c28-9439-8065dde19517 | -8.4566 | -48.4555 | 2026-09-21 18:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| eb8dd36b-4da5-3708-b556-47e9e13f70ec | -6.2766 | -57.7358 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 29a6f58e-91ca-3ad8-8f83-b309d358e9d0 | -3.2955 | -59.4476 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a227c8e7-6b08-3089-8650-fc93ee1ca03e | -3.4599 | -59.5209 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b1d7aea2-dae1-3d6d-8709-4d57d2d70128 | -10.7073 | -50.7064 | 2026-09-21 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ea6e0bde-0fde-35e7-b0fe-966b71f0be85 | -6.3842 | -55.265 | 2026-09-21 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| fe49e8a1-19aa-3398-bbd7-1355d5a91c22 | -7.3259 | -55.6153 | 2026-09-21 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9fa8907a-d640-3eff-bf79-8b23ca407c95 | -0.803 | -48.6611 | 2026-09-21 18:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2afa4914-2438-339c-8e46-d2f18d8657e6 | -10.0898 | -50.2795 | 2026-09-21 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| cf576270-1a44-31a3-bd78-e63b53ab7e26 | -6.8985 | -41.6976 | 2026-09-21 18:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 193.0 |
| a23c4f5d-23ac-39ed-8159-1e08a568c548 | -3.3137 | -59.4664 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 97f4f031-d56b-3683-a34f-961fdad85359 | -7.6264 | -57.615 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e0c22a36-8997-33ca-83b6-e819c94abed7 | -7.5705 | -57.657 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 34ec414f-f08d-315b-ba24-4fa2e716ddcb | -5.3955 | -45.8746 | 2026-09-21 18:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b174a52b-79b2-3363-a83a-3625b1f0ee15 | -5.5846 | -45.5703 | 2026-09-21 18:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 6eca920a-39be-3661-ae73-c691d250c01e | -8.7729 | -44.2568 | 2026-09-21 18:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 13894105-9dc7-37f2-8db4-8a4b87713998 | -8.8635 | -68.8169 | 2026-09-21 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1ebb7a44-a222-3e1a-9a48-720ff1520a07 | -10.2546 | -68.7494 | 2026-09-21 18:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1fed74ae-2efa-3763-b13b-264eea8ae4c8 | -9.3577 | -50.0943 | 2026-09-21 18:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 9e0641b1-2564-38c5-9ed9-e0eb5e711b78 | -9.1708 | -50.0049 | 2026-09-21 18:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| bbfc80a1-17ec-3158-94ed-0a77113b2af6 | -6.2949 | -57.7545 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 02d3da82-4d22-3518-9a27-2ebef8b18472 | -7.6448 | -57.6337 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 4aeadfbc-4248-33e4-b36a-11411f477a36 | -7.8789 | -44.8348 | 2026-09-21 18:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 257.6 |
| f888497c-e113-34e9-af0d-f2efd76aa4bc | -2.9157 | -57.7983 | 2026-09-21 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| dcbec4f5-760a-36b0-9d71-030043bd1389 | -5.9818 | -57.7087 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e418b17c-19a0-38e8-83b4-44a7830614dd | -11.3996 | -44.0995 | 2026-09-21 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 251.2 |
| 9d4ecc1e-0afa-3beb-b5ef-3cfa5c8dcedb | -6.8651 | -55.2807 | 2026-09-21 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 8f85a7e8-133e-3681-830e-d26899d10e01 | -3.4032 | -60.19 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| aecf72b4-5390-3303-bbbf-c749647931f0 | -9.2754 | -60.6162 | 2026-09-21 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 4902205c-87cb-3bb1-8005-0d76b0c95b60 | -3.6264 | -58.9228 | 2026-09-21 18:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ad0752ad-5019-31dd-82da-c2a49aad85b0 | -11.2587 | -43.4147 | 2026-09-21 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| f7f9d0fd-49ae-34a1-912b-e29dbcdbb005 | -6.3434 | -55.8442 | 2026-09-21 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6c407f29-c2bd-3bdc-94ce-dc95f2ec56d1 | -9.2753 | -60.6355 | 2026-09-21 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 219.8 |
| 845bc9b8-3fe8-3e96-9278-140352dd158e | -10.236 | -68.7498 | 2026-09-21 18:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 8b0e14a5-d0dd-3212-b9c5-0313634ce6d5 | -12.3025 | -50.6774 | 2026-09-21 18:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f50ab988-2d1d-3f32-8e00-d794edd037de | -3.3321 | -59.4469 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 44959890-a8b7-3570-af9c-7c12693bce43 | -8.754 | -44.2589 | 2026-09-21 18:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 6faaa197-9fca-3b88-b68e-65f35ed72b8d | 1.2794 | -50.8718 | 2026-09-21 18:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.4 |
| e3a30b98-4758-3a63-9e4e-e4c33fe5c5bd | -3.6033 | -60.5664 | 2026-09-21 18:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 6cfbb090-6041-33db-9ffa-ff9bc403cfa2 | -5.8159 | -57.7346 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 301.4 |
| d8e8528a-93e3-3996-9c9d-26a0b51f7dba | -5.6594 | -43.4139 | 2026-09-21 18:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e113f4f0-4c0a-3343-8269-d8debe4f5065 | -2.9525 | -57.72 | 2026-09-21 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 21e420f7-c514-3864-8752-d39ddd176f13 | -5.5661 | -45.5491 | 2026-09-21 18:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ce3184d2-9aa7-3de9-ab8b-93978b8a60cf | -11.4001 | -44.076 | 2026-09-21 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 244.9 |
| 745aa15e-f5f4-31fa-974f-6f5b4728c3b7 | -8.1686 | -54.7634 | 2026-09-21 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ef907a26-6f18-3a1c-9af3-5f7035990619 | -9.1813 | -60.7747 | 2026-09-21 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 4bcb78b0-c97b-3a5b-8b60-f6a82de24599 | -2.9326 | -58.3397 | 2026-09-21 18:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| babd2e1c-8298-3ab2-b927-1f95a38a7263 | -3.3311 | -59.8101 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 909be150-2175-3391-8fc3-367faf692bf4 | -2.9157 | -57.8177 | 2026-09-21 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 34cc80c0-2295-36a4-8615-498d9110bc52 | -6.1662 | -57.7013 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 6942ffbe-ceff-3bd0-900f-fb23216057f7 | -6.295 | -57.735 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 62216ec9-253e-32aa-8c32-c5d41259c928 | -7.5891 | -57.6561 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 210.7 |
| 908af2e2-9fe5-3716-a387-20818dc74bea | -11.2783 | -43.388 | 2026-09-21 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 43e52a20-1e32-3522-a9be-55de01589ef4 | -6.3135 | -57.7342 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 7b80dc11-6ff7-313b-b5f5-e122550ad0a9 | -10.7064 | -50.7703 | 2026-09-21 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 227c3d15-f78d-3b9e-8795-f52678b9e9ca | -6.7119 | -58.9992 | 2026-09-21 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 295.0 |
| 585877fa-c8df-34be-a971-d0aa91669792 | -6.5759 | -45.5419 | 2026-09-21 18:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 773c633d-d5df-3d8c-aaf6-9f7d0f495392 | -3.4974 | -59.1944 | 2026-09-21 18:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| e4244d6b-31ee-32a8-b4f3-ce0506c0b76c | -6.1175 | -59.9452 | 2026-09-21 18:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| b8a0c51d-eaf5-3396-ba25-746e4068bc91 | -7.5661 | -61.3239 | 2026-09-21 18:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 5ec010d6-ad79-3a24-91d8-a8aa30f4a6dc | -6.3567 | -59.9559 | 2026-09-21 18:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 3485bdb0-ac0c-31dc-9fc1-d9152e74b61d | -10.7624 | -50.8282 | 2026-09-21 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 2f61cfbe-2325-3c97-9d61-d05741f8f4c9 | -6.3014 | -59.9579 | 2026-09-21 18:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 29465e06-1370-39d5-8923-dbd0584748f3 | -9.6665 | -54.3332 | 2026-09-21 18:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 0c5ad91d-b905-35cf-a61c-58186c319723 | -3.1698 | -58.5859 | 2026-09-21 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c4365b2b-4ea9-3483-864b-a8e8234ab234 | -3.1357 | -57.697 | 2026-09-21 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| a3ce9453-fe11-3fb9-acf5-8d3e2a155bed | -3.713 | -60.5642 | 2026-09-21 18:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 59a01afd-f18a-3601-930e-d30acf2e1911 | -5.3645 | -56.0447 | 2026-09-21 18:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 412653c0-cc7b-3c6a-8516-14e09bc4aebd | -9.8686 | -48.447 | 2026-09-21 18:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e921f0c3-5748-3e1a-bad3-39126aaa4c46 | -7.4186 | -73.1537 | 2026-09-21 18:00:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 36582930-0cbb-3c17-b95c-39a1cd5e385e | -10.7061 | -50.7915 | 2026-09-21 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0f2f76ae-028b-3647-a006-0142a363dcc3 | -6.325 | -55.8451 | 2026-09-21 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| cc6e49eb-94aa-3203-af86-ea5358f970fa | -7.6079 | -57.616 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 09e4462f-deb7-396e-8fd0-f63236941377 | -6.3436 | -55.8243 | 2026-09-21 18:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 34c1ffec-425d-3a65-a8f9-8b7ac3d28455 | -6.9034 | -42.9341 | 2026-09-21 18:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.9 |
| e192df3a-9087-3c4c-8489-315b22ce04a6 | -11.6609 | -43.4239 | 2026-09-21 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 0e69f808-55f3-3cfe-aa11-606ec2e1d778 | -3.3138 | -59.4472 | 2026-09-21 18:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 5446a716-d880-3feb-9d0b-04f5506340ab | -6.513 | -58.3099 | 2026-09-21 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| ffcbdf89-0fd6-33f1-a84f-1d29555ea6b5 | -11.6066 | -45.3904 | 2026-09-21 18:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a03721aa-7e51-3fc2-982a-70f721c366f6 | -6.922 | -42.9559 | 2026-09-21 18:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |
| 34f34194-f9f5-3709-b1c5-304d84032e3d | -3.7913 | -40.1675 | 2026-09-21 18:00:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 81.7 |
| c6577112-4fa2-34d5-8ebd-fabf411d6441 | -2.8791 | -57.8184 | 2026-09-21 18:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 76f8db76-b223-3c11-8892-1186a9309f3f | -10.6875 | -50.7722 | 2026-09-21 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |


[Clique aqui para ver as próximas entradas](README183.md)
