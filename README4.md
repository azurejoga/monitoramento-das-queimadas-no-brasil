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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 107df464-5445-3ca9-88aa-acc98f6a1f0d | -9.0222 | -65.922 | 2025-10-22 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ecdf65ce-4c49-3841-9c6f-19308b3db8b8 | -3.0169 | -49.4694 | 2025-10-22 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 736a7df0-83f9-350f-9473-1a3219efbf7b | -4.4443 | -43.263 | 2025-10-22 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6da78237-1ffc-3cad-a59b-ff6f669c94d2 | -9.0036 | -65.9226 | 2025-10-22 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 8ef2c6e6-7062-323e-b519-c3c8ffa2d030 | -9.0036 | -65.9226 | 2025-10-22 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 473dcaf5-56e7-3395-a3fb-5558648da649 | -9.0036 | -65.9412 | 2025-10-22 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 359e6c94-3814-359d-9c78-77ae9fdee1bc | -4.4632 | -43.2386 | 2025-10-22 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 8eedf3fd-3831-32ef-991e-9b8504525ed6 | -10.3406 | -62.8401 | 2025-10-22 02:40:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 384092c0-3490-309d-b7df-6e6a0bade95d | -4.4445 | -43.2397 | 2025-10-22 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 8792355f-cb3a-370f-8379-d8c9c386b4c5 | -3.0169 | -49.4694 | 2025-10-22 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d11b4e5c-7034-306f-8940-c4eb8a0a8518 | -4.4632 | -43.2386 | 2025-10-22 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 162.2 |
| dd32e063-8f5e-3497-a7e9-2a09eb9790fe | -4.463 | -43.2619 | 2025-10-22 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d1dede28-8e39-387a-a81f-8e0765b8d6f7 | -4.4445 | -43.2397 | 2025-10-22 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 07153fe1-06d0-3ac0-b802-bfeed54187d5 | -9.0036 | -65.9412 | 2025-10-22 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6016a5c9-5941-3da8-917c-157434876bc8 | -10.3406 | -62.8401 | 2025-10-22 02:50:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d3db00c8-d96a-398f-9f64-290bbce6f598 | -9.0036 | -65.9226 | 2025-10-22 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 0d96e440-b047-30e9-b2a5-851ac2547ce2 | -9.0222 | -65.922 | 2025-10-22 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 325cb207-e51b-3d9d-8faf-e6e8093dc431 | -9.0036 | -65.9226 | 2025-10-22 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| aab0598b-b167-3a65-a94a-d04e3a78ad56 | -4.4445 | -43.2397 | 2025-10-22 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 61bd87c8-de52-3d40-a892-61552eecc9d8 | -9.0036 | -65.9412 | 2025-10-22 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 7ca43136-6915-3c5d-a27f-916be87929b2 | -10.3406 | -62.8401 | 2025-10-22 03:00:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a279782d-7014-3e79-9bc1-50ef2939f7e8 | -4.4632 | -43.2386 | 2025-10-22 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 8f88bef0-6416-335d-b48e-c2f4cae15d9a | -4.4632 | -43.2386 | 2025-10-22 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 88be70b8-823a-39ae-b928-13499d62995b | -9.0036 | -65.9412 | 2025-10-22 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9885c8ae-509f-3f2a-bdbe-2bfcc660176d | -9.0036 | -65.9226 | 2025-10-22 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c1d3126f-a234-3a97-a6e4-bd2897f9c1c7 | -4.4445 | -43.2397 | 2025-10-22 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 08922893-48fe-3ab9-aa85-ee4572cf7225 | -4.90589 | -38.92756 | 2025-10-22 03:15:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| edc66182-8145-331c-8f99-b833a917b634 | -3.67005 | -40.48352 | 2025-10-22 03:15:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15d714fe-33eb-3ebd-ab3f-474db5f42243 | -3.66629 | -40.48832 | 2025-10-22 03:15:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 426121ec-671c-39a8-93e0-b2d53a03f057 | -6.50255 | -35.31773 | 2025-10-22 03:15:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63961e57-ad5b-3c77-bc76-cdbeae5128b8 | -4.90498 | -38.93282 | 2025-10-22 03:15:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c74a445d-1ff6-33da-a083-e11a25b4b9ff | -5.6586 | -38.31371 | 2025-10-22 03:15:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 09b67274-6892-37e9-83b5-8141e97f7c37 | -6.4976 | -35.31693 | 2025-10-22 03:15:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 55c86f2c-aa77-3ef1-afe3-e7293f606a74 | -5.15468 | -37.64828 | 2025-10-22 03:15:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f288c4cb-807d-39aa-b400-07e3dc93cf61 | -4.91229 | -38.92873 | 2025-10-22 03:15:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ac09ee5-d2c4-3253-8091-ceddc5985442 | -3.66771 | -40.48009 | 2025-10-22 03:15:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 086f2b05-de59-30cb-ad20-c869f7418a89 | -5.29839 | -35.97823 | 2025-10-22 03:15:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 143cf89b-5ee9-3bbe-8798-d2b2b2cb3dbe | -5.07251 | -40.47911 | 2025-10-22 03:15:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 91f6b771-541e-3edc-8e66-7b8cb5baa6e1 | -4.91223 | -38.93186 | 2025-10-22 03:15:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb1cbe7d-4048-3dae-b9f7-6fc6d04de222 | -5.07081 | -40.47425 | 2025-10-22 03:15:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9ab5ee28-636c-3421-8fed-e6abb5147a2e | -9.27113 | -35.62767 | 2025-10-22 03:15:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9bf9a62a-e234-34ff-a930-2066f90a9840 | -6.501 | -35.32044 | 2025-10-22 03:15:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88aef3fc-3f06-33b1-bb8e-1f4b3e83e84f | -5.06959 | -40.48086 | 2025-10-22 03:15:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 66957517-5067-3392-ac59-92611d71dc73 | -4.90582 | -38.93074 | 2025-10-22 03:15:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0438a07e-ceab-3599-aad6-b2f9663cb94c | -3.66247 | -40.48473 | 2025-10-22 03:15:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e8b2c86b-642f-363f-aa3a-5aab12655d82 | -5.15543 | -37.64405 | 2025-10-22 03:15:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 548767db-aefa-365d-b886-0a5fe4ad507a | -5.65892 | -38.30976 | 2025-10-22 03:15:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 55267e59-7fc3-35e8-b626-d9e05c274344 | -9.27594 | -35.62851 | 2025-10-22 03:15:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bb8fddd6-b64b-34e3-8046-1fe908445b4f | -4.90673 | -37.20258 | 2025-10-22 03:15:00 | NPP-375D | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3112b8ba-c75b-3d95-ab52-f7b274009dce | -7.29674 | -34.81784 | 2025-10-22 03:15:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| de23d7f7-c558-3b79-b185-945bea5e07b0 | -5.06552 | -40.47781 | 2025-10-22 03:15:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 521ca54c-5d13-35f9-950b-c18d0890a8dd | -6.49605 | -35.31964 | 2025-10-22 03:15:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c1fc43c0-2eeb-3ad9-b329-7ea8f6303f50 | -5.65809 | -38.31429 | 2025-10-22 03:15:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 33313da2-28e6-373a-8828-b7da5ac999ca | -19.08928 | -44.34587 | 2025-10-22 03:17:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1c323c7-3a69-3892-a1d8-9eb8692b6f38 | -9.62286 | -40.34558 | 2025-10-22 03:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ccc8ef74-3424-36f5-91e3-dd883d37bcbe | -20.44199 | -44.85343 | 2025-10-22 03:17:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9b43f34-5c9e-3e89-a1c5-53824e64e488 | -9.62391 | -40.34016 | 2025-10-22 03:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4be226b-0ece-3e96-8d86-b80ade0bd57a | -20.44036 | -44.85991 | 2025-10-22 03:17:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdf78b5b-5731-32ee-807e-7f62080489de | -21.24389 | -45.141 | 2025-10-22 03:17:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8c5d3dd4-8dcb-3eec-b776-638809047eba | -4.4445 | -43.2397 | 2025-10-22 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 209.2 |
| 1d626cff-c3a9-369c-b2e5-e2489c29453e | -4.4443 | -43.263 | 2025-10-22 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c08e4260-a0c8-31d2-99a5-10cc2354c5a0 | -9.0036 | -65.9226 | 2025-10-22 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 97355203-9cee-3956-850c-78cc7e972d61 | -9.0036 | -65.9412 | 2025-10-22 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1feeba6f-07ac-335f-b57d-8839bb0d6c9c | -4.4446 | -43.2164 | 2025-10-22 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4a50ca44-2de4-30fe-9754-184f5b98edbc | -4.4632 | -43.2386 | 2025-10-22 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| bfbdd147-002c-3984-9112-fbb192f849f3 | -4.4632 | -43.2386 | 2025-10-22 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 0883ca5d-4d26-3b52-b7b8-a061e13ed87c | -9.0036 | -65.9412 | 2025-10-22 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| ccd46630-99b7-3b59-9f86-a499f985b920 | -4.4445 | -43.2397 | 2025-10-22 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 3476ac3f-a05a-3987-a1b3-81877bee87af | -4.4633 | -43.2152 | 2025-10-22 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e7d119fe-08e7-3ead-8aff-8f58d2a3cd6e | -9.0036 | -65.9226 | 2025-10-22 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| d0e5fce9-c98b-3b3e-951b-21991a5e9622 | -4.463 | -43.2619 | 2025-10-22 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d66ced9d-8b72-351f-a5df-8b07cd980565 | -4.4443 | -43.263 | 2025-10-22 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e83f0bb4-dd56-3df4-a289-316b860c443b | -6.49719 | -35.31584 | 2025-10-22 03:34:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1788c6e8-8a40-3a13-a220-bfe6763178b3 | -4.19968 | -42.98346 | 2025-10-22 03:34:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdc26cd7-ad45-369f-9438-25800cff4e1d | -2.83727 | -40.17648 | 2025-10-22 03:34:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 19495a68-c2b5-320b-a598-b2825dfbad8e | -6.64209 | -43.61097 | 2025-10-22 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b99e6b67-5689-37ac-90ee-d1f7ce0779e9 | -4.83276 | -42.11643 | 2025-10-22 03:34:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90ab35a2-ab1e-37fe-98cd-3a2eef4f9fc5 | -6.64775 | -43.61202 | 2025-10-22 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25932977-394a-3aa2-b144-9f285a1c4fb3 | -2.98989 | -39.96371 | 2025-10-22 03:34:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2faed4ff-73e6-3f88-a9ef-147fd4e1a876 | -3.99369 | -43.28074 | 2025-10-22 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f318bee0-fe56-3199-8550-0633b8ed449a | -3.45006 | -41.85178 | 2025-10-22 03:34:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 781229c9-6949-35d9-b61c-982ee9a088ab | -4.39537 | -43.30647 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 40b248e7-f81e-3c24-811c-3819e4e62009 | -5.24019 | -37.735 | 2025-10-22 03:34:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77aa2022-1ee2-3e09-8aae-58f28eb9ad26 | -4.90868 | -38.92852 | 2025-10-22 03:34:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1a2b5760-29c2-3711-aa7e-c6ccb8ad762a | -5.07137 | -40.47582 | 2025-10-22 03:34:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| af69b7e2-693d-3133-8dc5-650dc4b4f12e | -6.53634 | -44.36293 | 2025-10-22 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c35af550-2c3b-37d2-9742-3c954a0052bf | -4.19903 | -42.98726 | 2025-10-22 03:34:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9f37bba-0f21-3e1d-bc48-a0873a817bd6 | -6.50061 | -35.31638 | 2025-10-22 03:34:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c8a448b3-312f-348d-ab87-c8aa95f4fb18 | -4.39451 | -43.30801 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 708495f5-8da2-39b0-8d9e-74969dc50837 | -6.32342 | -41.88462 | 2025-10-22 03:34:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 95da9fa1-ce53-327a-a1b6-f2d3a0f7f854 | -7.02261 | -38.8277 | 2025-10-22 03:34:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2524d2e1-6e8b-3bf0-90ec-84a1a8a80ee6 | -3.99907 | -43.28422 | 2025-10-22 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e57dcbb9-1170-311b-9fb2-a7aafd95400c | -4.45441 | -38.44441 | 2025-10-22 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a257d53f-07ec-3944-9da0-1caa5ba5db51 | -5.65614 | -38.31224 | 2025-10-22 03:34:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e49382ed-f0d8-392b-a2f5-b53fd2943c4f | -4.38806 | -43.31111 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0c2009bd-1c14-3ee5-ad5e-407bd48b9957 | -6.52971 | -41.43559 | 2025-10-22 03:34:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07f22bab-485c-3158-af1c-ff47730affbd | -4.44683 | -43.24929 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42ad4e1d-0779-34d5-ba42-81536d7b70ac | -7.4861 | -37.06589 | 2025-10-22 03:34:00 | NOAA-20 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d1872c0-e361-30f3-a378-0f3f6d9f5105 | -4.3952 | -43.30397 | 2025-10-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 30224c31-b9cb-3fc9-9326-de774e422dc7 | -6.50092 | -35.31635 | 2025-10-22 03:34:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
