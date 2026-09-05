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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a0a0780-434f-3b42-9ef3-1417f0100caa | -7.283 | -61.11487 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e8bab265-04a9-39e4-96c0-49700b21c5eb | -6.65735 | -59.95573 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 07d21a18-658c-38c9-a86f-04b2a49c79fc | -6.67579 | -59.93385 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7df7881-406b-36a0-a4d5-17e021590b24 | -6.65974 | -59.94035 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 8e304c8c-17f2-32ab-aa86-1b82235b8a07 | -6.59581 | -59.91471 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 01b591f9-9798-306c-99bf-25cb825c8e4e | -7.26724 | -61.10506 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6accecc1-15a0-3251-a0f6-c9f6f89e2e7c | -6.5778 | -59.89216 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ef561b6-a4c0-3c74-8f63-bf5364691d0d | -6.64978 | -59.95849 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 075a5efe-7d6f-38e4-9396-52b7622cd16b | -7.54458 | -61.34174 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 499a7487-cdfe-3f56-9f73-57d4b6b50430 | -9.41555 | -68.99371 | 2026-09-05 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea9df943-6925-3f44-aae0-71d236b1c4cb | -6.65795 | -59.95188 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3f1e93c4-c4d5-328f-af94-f4f30e86df8e | -6.66961 | -59.94582 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb098000-312e-3a6b-8908-3627da8394ee | -7.55242 | -61.33562 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5845e82b-2b75-3406-a30e-b02e250344ff | -6.15199 | -59.94326 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d4f6033-c18e-3dfb-8558-68bcac22050a | -5.65368 | -60.23741 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1ecdfd2-55ec-3d63-944a-ed2dfe1be07f | -10.2293 | -68.65392 | 2026-09-05 05:42:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08323f10-ce90-3fc6-9444-b45d3dd94d30 | -6.58534 | -59.91311 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d5719b0-79d1-39ba-8c87-f053fc28b70a | -9.41394 | -68.99477 | 2026-09-05 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dddf72c5-87f6-3494-bc0e-cabc3c92a18c | -6.65098 | -59.95078 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 972c8bcd-c6c6-318c-b216-ca1437a4b322 | -9.13403 | -67.80798 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1deb13de-1562-36e6-ac11-fc1b34235295 | -9.46309 | -67.43272 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21e655e-9d50-37eb-93fd-dcabdc450524 | -6.68507 | -59.96675 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bb5e850-fbb4-3282-a2b3-f6083fcf7173 | -6.69319 | -59.98368 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03180ce2-226b-34fc-b2e4-a91c4cd921a5 | -5.60005 | -60.24422 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd4b36e2-503e-30f0-839e-cccb6b391908 | -6.69668 | -59.9842 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d5fb32c-7789-3690-b9c9-d556e4331770 | -6.66552 | -59.94912 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 835026d6-a800-324e-9a97-2330aa7ce80f | -9.0508 | -67.64019 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6fbccab-9c30-3ad4-8aa6-abf02ed9a95a | -5.46391 | -60.04545 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e9b73ef-896e-3c69-95f2-264fa8fbcc66 | -6.66024 | -59.9601 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c61464c-ad4d-3e56-9c27-ee34b1c99920 | -8.5394 | -67.1608 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a3293a-71ea-39a3-adcb-99837cd0e69f | -6.65038 | -59.95464 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 907c1949-6bca-32b9-807a-31066d534976 | -5.76786 | -59.18164 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54f5632e-58ed-3903-9922-a71124e92293 | -6.6469 | -59.95407 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 507e4024-7c28-34c2-b336-5336fdb2861e | -6.13404 | -59.92104 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4a95d82-bf25-3657-9967-3d3c55a6fc9c | -6.59232 | -59.91419 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d69a7198-e0f1-3838-a1c3-3744a7138ea3 | -7.55578 | -61.33616 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba214e07-329f-31d1-a70e-a6f37dd957b7 | -9.05168 | -67.63503 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a272772-e0ab-3536-90f5-339884b51c18 | -8.86946 | -68.48764 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0860c726-0d61-31db-93c7-3d02bbc6e475 | -5.47176 | -60.05809 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16817a52-01fa-330a-8922-cc109261ef7d | -7.26386 | -61.10453 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac49b028-487f-3d1b-ad6d-51363ee1af5e | -6.58824 | -59.9175 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98aadfd6-4f91-3639-a505-04d26aaf6112 | -6.66084 | -59.95625 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9290abd8-32a7-304a-aaaf-c2cc354e889f | -9.5457 | -60.83029 | 2026-09-05 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ddc61bf-fa9b-3f52-8735-9bdde5746ea1 | -5.43149 | -60.18476 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f533724a-fe40-3860-8a7f-ca947dd147f8 | -7.28244 | -61.11847 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a753aa21-d04d-36b4-a5dd-20d7104aa88c | -6.02684 | -60.16787 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa978082-9938-3239-a182-88f00580f719 | -9.55203 | -60.83516 | 2026-09-05 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8622c690-4c2f-33f7-bff5-d0618ddab54c | -6.59522 | -59.91859 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 690bd384-3623-3be5-8a55-efd59a103554 | -5.60063 | -60.24053 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 934be804-5de5-361f-8e8d-36b189b47074 | -8.88887 | -70.54572 | 2026-09-05 05:42:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d330d6-8920-3c07-96cc-3c77b50aec1f | -6.13772 | -59.88723 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f652b5-aaab-3739-80c2-acb70c00210a | -9.54511 | -60.83409 | 2026-09-05 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5e9480e-ed72-3481-b13f-1826ff994f9c | -9.46926 | -67.4214 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86050189-d998-3efa-9744-ee84dc100888 | -8.63191 | -67.01646 | 2026-09-05 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48c3d1c9-74d5-340e-82ad-ebd3e819f393 | -8.75117 | -69.23112 | 2026-09-05 05:42:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f109e3d-081d-3b40-a8b7-102c0ff4a912 | -6.6737 | -59.94249 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15623f2c-77ff-310e-b513-f9554b47ccca | -10.31647 | -59.14746 | 2026-09-05 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa786317-cc48-39d8-89bb-a5fcdd229654 | -5.46332 | -60.04917 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c35827d-deb7-33ff-b84a-bae795efad0a | -8.62664 | -67.00073 | 2026-09-05 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efd6a92c-504e-3bbc-a7da-b8f0e084beae | -7.56096 | -61.41357 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 62a2ee76-39a8-33e6-9b0a-74fa6e7ad0bb | -6.59291 | -59.91031 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15e518b3-3a3f-3ea6-8aec-13cb54e8305f | -6.58883 | -59.91365 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2422ca3-5285-3d17-8e73-b74d77422bbb | -9.41826 | -68.99554 | 2026-09-05 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c50c621a-cbd3-376d-be2e-4685744487b4 | -8.54414 | -67.15653 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40d10a69-1701-304e-b7f7-85024fca2187 | -6.65855 | -59.94804 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d53a66c3-dcd6-3bb4-a840-4541d015feb3 | -9.18473 | -68.26566 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 487ee9b6-c3a8-37e6-8ba6-6735686cb4df | -5.65426 | -60.23373 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 982c5875-3eee-392c-99a8-bce96bd0c448 | -6.66672 | -59.94143 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2ee51038-fd44-30d5-abe6-e9223bf8c216 | -8.62197 | -67.00488 | 2026-09-05 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9559e373-654a-3d62-8eb2-8b20b1a0ad9c | -5.65689 | -60.23738 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bec4666c-6ee7-3fb0-b211-e917211a37cc | -5.77019 | -59.1903 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d891bc5-ef3e-3dc5-a57e-4a0866cc786d | -6.68332 | -59.97828 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b4e3ef8-ae89-3d0e-95f8-2726b5eae600 | -6.12828 | -59.92488 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8c5f019-fc85-3e25-a798-cbcefaae5eb8 | -5.59378 | -60.23949 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 880f2895-27da-3594-bda7-15f6dc60e5bd | -8.5399 | -67.15909 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 731ff40e-422c-3c10-b323-70c7fc6c3993 | -6.66433 | -59.95678 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e387981-8982-3124-af5c-bbf1aa104130 | -6.69377 | -59.97987 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b9ae369-3856-338a-bba6-dc78ef3ece9e | -6.6743 | -59.93864 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 157d3a75-b9f4-38c5-b9e3-01030e27e845 | -6.65675 | -59.95958 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 1471e58d-b5b0-3acc-82b8-07448c666410 | -6.59173 | -59.91805 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8dfe8f03-3731-3842-88a9-db42e608e974 | -5.46659 | -60.04583 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e143702-2bcc-3109-9a95-ed1bf6adae9b | -6.65506 | -59.94748 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1303b182-67c8-34c3-ba05-7d2a6198a2e0 | -5.66031 | -60.23792 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 396c28ae-2e3c-32ce-8499-198dc4d6d476 | -8.54329 | -67.16148 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbb77df7-865a-384a-9025-ad11943e3b19 | -9.18538 | -68.2619 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae814f4d-e591-3b52-aed7-85c7c6c81185 | -7.55186 | -61.3392 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1312c7b3-aa79-39bc-8595-2118d207e9b8 | -8.62583 | -67.00552 | 2026-09-05 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d56841ee-492c-3ad6-9e6a-828763833bef | -6.15605 | -59.93996 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a432cd-b678-3b57-8e0b-c94aab81608e | -6.66841 | -59.95348 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3bf3a3f8-3c44-3d54-99ce-0c5aeef28068 | -6.64869 | -59.94253 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 897626d0-c539-33e9-9493-4133b0d6d3db | -6.13235 | -59.9216 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d455198-7fe6-3add-b8d0-28b854568d9a | -7.55693 | -61.35094 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d0e6b34-c080-30c6-9fcc-ea35fb998ba6 | -9.46535 | -67.42073 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 649d7a56-2f42-3c67-afae-bda0ae144f8f | -5.33524 | -60.13271 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51c85487-5fa8-3074-9d0c-348671d03df8 | -6.59464 | -59.92244 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ab2e8fe-1524-3fbf-aaf9-4e438f5427dd | -5.59948 | -60.2479 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b14c4b-f580-3b0c-a899-aaf44b36b3c6 | -5.77081 | -59.18625 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e95909d5-cb7d-32b1-8ff8-86c76eff1784 | -6.64809 | -59.94638 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e554fb75-818b-3aed-a1a9-7dfa40f6a63c | -7.5604 | -61.41713 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a62ad775-d385-31f9-baf2-bda38bc798ee | -5.84623 | -60.25465 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |


[Clique aqui para ver as próximas entradas](README31.md)
