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
| a8543f88-a85a-3672-9718-1114f3be636c | -8.11483 | -44.18508 | 2026-05-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df5b24e2-9ddf-39cb-a32c-70ff28c05dd4 | -9.46549 | -40.33342 | 2026-05-14 04:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 93d5e0d3-006e-3e92-904b-7240e4ba2928 | -10.12054 | -47.93845 | 2026-05-14 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d45b5c4-5daa-3163-aecf-856aa56f0c0a | -10.39704 | -46.64876 | 2026-05-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78791ccc-d8d9-3513-962b-ecc00beb04a1 | -8.85348 | -50.21338 | 2026-05-14 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8033116-ce06-3886-9b4a-ea02dc013dbf | -8.11526 | -44.18192 | 2026-05-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1285967a-ebcd-31b1-becf-2f9362a064a2 | -8.54109 | -45.97912 | 2026-05-14 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bc855bf-276b-3e5b-aaa5-0daa8d8a4dfc | -8.5387 | -51.57997 | 2026-05-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21cd5e08-3312-3146-b7a8-dcc638e33f65 | -10.39765 | -46.64435 | 2026-05-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c9fd80b-b10d-39b2-a3ac-f5a70989ddb3 | -9.46223 | -40.33709 | 2026-05-14 04:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0836061d-1423-32d7-91a7-08bbb548be22 | -13.68611 | -44.29471 | 2026-05-14 04:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ffe7ff-6573-399e-8bb3-6f2cecd69c57 | -11.7508 | -54.79016 | 2026-05-14 04:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 849769ae-d5f9-3769-8958-8da14dcfe21e | -13.68657 | -44.29082 | 2026-05-14 04:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1dab56c-3dea-3dc2-b93f-0e7a2fb51fb0 | -11.31128 | -54.03677 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a95716a-ce95-3433-b30f-87d616861dd8 | -11.18679 | -55.92175 | 2026-05-14 04:55:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71a3c22f-13a6-3438-8912-e3685b1b9d51 | -11.73797 | -54.23673 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb591329-7c87-3e4c-b658-611d90bbb79b | -11.93797 | -43.36984 | 2026-05-14 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99e70034-ac30-3d25-9e32-be98c4f808a5 | -12.46142 | -54.45066 | 2026-05-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5097e966-722a-35d1-9f88-781a5170277b | -12.54341 | -54.61655 | 2026-05-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48cddae2-ca4b-33db-994e-7bff5bbd149e | -11.76313 | -47.06211 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c9185ec6-3515-35f0-8c91-897450f3dd59 | -12.11547 | -43.64328 | 2026-05-14 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 821fed4d-d80d-3a19-a8ef-1fa478958c30 | -12.04642 | -55.36126 | 2026-05-14 04:55:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 10cd83b3-d706-3cbd-8aa7-7c571bb53401 | -14.30487 | -49.24794 | 2026-05-14 04:55:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a104bff-edd8-3883-853c-a7ec00e0c633 | -11.76042 | -47.06353 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf415505-1277-35e1-8fa7-cf53c1ceae13 | -15.42416 | -56.31392 | 2026-05-14 04:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a07fd7e-3cf2-3e48-84d4-8095fc886426 | -12.65029 | -47.09071 | 2026-05-14 04:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc98bc13-f9cb-33b9-92cb-20d6239cee8c | -11.18332 | -55.92115 | 2026-05-14 04:55:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd09b588-d4a1-31f3-8064-55e390ea6376 | -11.76254 | -47.06668 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4bd15ad-89ba-32af-9279-8d110f533a0c | -11.7374 | -54.24026 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7273ec4f-aba1-389b-b59b-c924f159f113 | -12.4581 | -54.45011 | 2026-05-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 896e684d-52a8-3f49-af6d-6b824cd47545 | -11.92986 | -54.09849 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e96fac33-7f1c-316d-a42b-f2fc21b538e2 | -12.36888 | -54.74918 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34db58f1-469a-368f-9d2b-037f6c9c725a | -14.65115 | -49.756 | 2026-05-14 04:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49882032-9e97-3361-9e0b-c0bc94c47a9a | -11.09019 | -45.9314 | 2026-05-14 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70e62f8d-8d6c-3a97-9b32-c2ff54e9ea22 | -11.96671 | -46.78577 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0b2c2eb-0b2b-3962-a733-522dde81dd26 | -11.63231 | -54.15432 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9812ba87-c466-3d49-807e-b0b7f1ecab07 | -12.04702 | -55.35758 | 2026-05-14 04:55:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3b0d9ae-dae7-3846-bbae-853ac8977f07 | -10.40386 | -49.44087 | 2026-05-14 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e06edb5-935e-3f45-98b2-a094a96a10e5 | -10.48856 | -49.36077 | 2026-05-14 04:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 058d82a9-035a-3cc4-8651-e839e0996f41 | -11.2892 | -54.02592 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 305a5876-2469-31d5-b4e1-71a85ea653e7 | -11.42026 | -47.09267 | 2026-05-14 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92870b79-1b83-3ae3-b6b8-50543618fe67 | -11.17922 | -55.92442 | 2026-05-14 04:55:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ddf764b7-5cd5-3511-b5fb-971dd245bead | -12.04471 | -45.28433 | 2026-05-14 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b91bf655-ed0c-3f99-9c87-a9e02b7b825a | -10.34381 | -53.60594 | 2026-05-14 04:55:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c302a6b-5529-3c58-8766-121e68152f1c | -16.47721 | -55.19226 | 2026-05-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| ebc0064b-ed84-3f4e-9786-a8755217788b | -12.03278 | -54.24161 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28084724-e89b-333b-99b2-8213ae922929 | -11.93168 | -43.36784 | 2026-05-14 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1446de24-6946-3e8f-9f7f-566f39b7c196 | -15.42077 | -56.31331 | 2026-05-14 04:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b090df1-c826-3f47-80f6-446242545cb5 | -12.05018 | -45.28195 | 2026-05-14 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b978c850-b7d5-3758-9c5a-4873bb9f5eb4 | -13.83392 | -52.61435 | 2026-05-14 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da634a09-ef7b-3675-9812-265d0b20b616 | -12.35165 | -54.7755 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 873ee90a-20ef-3de0-8d77-9e785519351f | -12.21389 | -46.57546 | 2026-05-14 04:55:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06aef096-4810-3a4b-8d69-a99073aed166 | -11.30909 | -54.02919 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30229eef-a512-3afe-8f5a-6c173dd73282 | -12.35108 | -54.77908 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 655b57ef-bc9d-3e20-9377-9eadcb18a97b | -11.79601 | -54.02219 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 091ffa07-7b1c-320e-856e-f11326174cb3 | -11.93739 | -43.36903 | 2026-05-14 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f0d909c-5ae5-3438-b90a-d5354f61888b | -12.11226 | -43.64172 | 2026-05-14 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dc836f2-9f2c-3b84-a7d5-944576841118 | -12.37221 | -54.74973 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e1e8095-110a-369f-b9ef-2a3842c13eed | -11.73409 | -54.23971 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 679cfb7b-d9bb-3bd0-b07a-6f2b27223014 | -11.57965 | -54.56713 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 35e00ead-5979-3005-b645-717b80e1484f | -13.83336 | -52.61806 | 2026-05-14 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f218dbe5-fd3d-30ab-9f6f-aaedf1f9e055 | -11.92929 | -54.10201 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 114766cf-c19f-3a47-b09f-acee9d393be6 | -11.17985 | -55.92056 | 2026-05-14 04:55:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 626172bd-efc6-3190-9605-d7731412f095 | -11.74129 | -54.23728 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a19ed20-4aa6-3ea9-8758-abf05e228805 | -11.97101 | -43.84075 | 2026-05-14 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2f7b7f8-0a3f-34ea-9b3a-f009778a57c2 | -12.54008 | -54.616 | 2026-05-14 04:55:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d322ce3-80f8-3dcf-990a-22069cbf42dd | -11.6345 | -54.16192 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab290dd1-16d9-31fe-983a-3a0f97e901d3 | -11.97147 | -43.83694 | 2026-05-14 04:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53f480c3-1ba1-3ece-ae5a-87f8d450e8b2 | -11.42532 | -47.08887 | 2026-05-14 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 965cc300-c34b-30cf-a922-a7b1d8f3c8e7 | -12.30262 | -47.90636 | 2026-05-14 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3531c8e-6b9f-3427-9fc5-071ad791ba68 | -12.61621 | -44.51841 | 2026-05-14 04:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b12e34d-5c4a-3cec-bed1-af383831dd7c | -9.76096 | -55.62563 | 2026-05-14 04:55:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71e242d1-544b-3f67-901b-a4e3b4509db8 | -11.43484 | -54.0934 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68538c36-b6a9-3ff2-8bda-8d331eada191 | -11.26245 | -54.70216 | 2026-05-14 04:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5794a7e-1c6a-3262-bb75-cd5d961b7ffe | -11.98443 | -46.79289 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c31e964-2a01-396b-a1c4-5fadc9167d9c | -11.30853 | -54.0327 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96d23d29-21be-3f2d-b7f9-d79485e8e53f | -11.30797 | -54.03622 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a2ab39f-f834-3117-a216-68336c195cfb | -12.3017 | -47.90559 | 2026-05-14 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f37dc232-8035-3320-8745-0ddc8b3d57f7 | -11.93226 | -43.3686 | 2026-05-14 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34cb28bd-f373-320a-a890-3fe44790c838 | -9.42744 | -55.95365 | 2026-05-14 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d26a5951-0a94-30cd-a246-c60b48b62ed2 | -11.93704 | -54.09606 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 210b7738-22f2-3640-b22e-926b0b44a462 | -11.7446 | -54.23783 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caaca90b-9ba3-3075-a6c3-675063242f54 | -12.05526 | -45.28262 | 2026-05-14 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 795a9d7f-f13f-310a-b240-b327e7493cdc | -16.37652 | -55.39708 | 2026-05-14 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13e6db71-4f3a-35c4-afa7-e59adb384ab2 | -11.63174 | -54.15785 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a973e643-f1e2-3fe1-82da-494bfd6414c7 | -11.29252 | -54.02647 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d12a2cf-978a-3dcb-94b1-d7e7e111bcd8 | -12.04979 | -45.285 | 2026-05-14 04:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ade6048-942d-340b-8a27-b2f452c3d698 | -11.76761 | -47.0628 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 188c8b9e-6ba5-35aa-9ef4-a9e8892d244f | -10.66555 | -49.71492 | 2026-05-14 04:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5bb1369-3b52-3d25-8a26-b7e044fd4f42 | -12.1118 | -43.64564 | 2026-05-14 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bb32427-29ca-34cd-afa4-c523c6b4d530 | -11.57908 | -54.5707 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be7230f1-adb6-3696-ac78-8ee865868875 | -10.48544 | -49.35549 | 2026-05-14 04:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9aaa91a0-93d8-3d97-a381-a635d5cf6f6d | -11.43816 | -54.09394 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40f1982e-0a73-37a1-b75c-e1d1944d8a4f | -11.42087 | -47.08822 | 2026-05-14 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d931b64e-0d2c-3b99-8986-e6072805a101 | -11.7927 | -54.02164 | 2026-05-14 04:55:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 81cda4be-85ae-3789-8b8f-531f38bac1b1 | -11.45034 | -55.10801 | 2026-05-14 04:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 732c05bc-dc0f-3374-856b-b3c07fe06e5e | -11.44147 | -54.09449 | 2026-05-14 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cf3ec2d-de05-343f-b8e5-2ddfff865bbe | -16.26715 | -60.00265 | 2026-05-14 04:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d477496-eb27-3812-bb3f-ea01a3d12982 | -11.96608 | -46.79052 | 2026-05-14 04:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 800c7d96-7fea-3321-805c-857d0731a498 | -12.11498 | -43.64719 | 2026-05-14 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
