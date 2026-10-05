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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85120e55-6864-3dc6-a538-b88e71b5c086 | -1.12336 | -57.27758 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ed9f0ad5-c66c-38d2-abff-b13c60fc03e3 | -2.51968 | -57.48166 | 2026-10-05 17:17:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7e9079e7-1091-3146-a8b7-2b3560e54c9c | -3.30366 | -58.64021 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f059a0fc-17e5-3c20-94e2-347d38b1997a | -1.37718 | -55.99934 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18c270ba-08ff-3414-8f1b-f914c0e8eb44 | -3.36211 | -59.89166 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5e197153-0708-317c-9088-528a7fea5a55 | 2.03118 | -50.96828 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1ff9f4f2-4d55-33f6-8456-67f0b7e247f3 | 1.9322 | -50.96098 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bd993774-e2a0-3878-b080-2087dc789b56 | -3.50625 | -59.55936 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 87f9138b-982c-3f2f-b4d0-c1c3831b1bc8 | -2.90596 | -54.08082 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f518b782-e3b5-3144-8401-9cc4ca4f65ff | -1.2231 | -47.72371 | 2026-10-05 17:17:00 | NPP-375 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| aa6147d3-8a10-3a71-b9bc-28487056dfbc | -2.93448 | -54.11176 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e07035e7-4468-357a-ac10-c5e06ae59cdf | -3.61993 | -64.34124 | 2026-10-05 17:17:00 | NPP-375 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9d55e986-32a9-3bd0-8290-8548487ec243 | -1.46181 | -53.60057 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec06c696-1d36-39f2-9471-e409b0da7b23 | -2.9366 | -54.12557 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4c90c024-3608-3206-8854-08c546e56823 | -3.75143 | -59.2899 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d4b24a28-8fec-3c75-8c71-b323164d1186 | -2.97953 | -54.10048 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a0ef661d-6dd8-3360-bc18-15aff9d799ac | 1.77195 | -55.601 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa3f8c08-ba2e-3060-a52d-5e9c1395a666 | 1.93757 | -55.71167 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 35026fdc-5401-3dea-b2a2-28454fb2b3a6 | 1.73459 | -55.62352 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc819717-2039-3e0d-943b-23262675a6c6 | 2.09994 | -50.73015 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 577610dc-bbf7-33b2-82fa-c6996b7ac0d2 | -1.61965 | -55.11308 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5e2eebe7-45e7-3f0c-a640-a371b3c55b6d | -2.02142 | -54.29071 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea4ba5f2-6635-3c63-ad5a-49e80e5ad2cd | -2.93241 | -53.94855 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 34cc2e8e-1f69-39ff-9ee7-5e49a986743e | -1.12854 | -48.88654 | 2026-10-05 17:17:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7004d1f-f507-3bfd-adf0-d627e08484fd | -1.78637 | -66.55342 | 2026-10-05 17:17:00 | NPP-375 | JAPURÁ | AMAZONAS | Brasil | 1302108 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4e2120ce-9e6f-35c9-a717-2a5d3565f786 | 1.07334 | -67.58684 | 2026-10-05 17:17:00 | NPP-375 | SÃO GABRIEL DA CACHOEIRA | AMAZONAS | Brasil | 1303809 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7560777d-235e-34c9-bb79-37a91b021d75 | 1.16199 | -50.74437 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 790ad09f-fc39-3181-abd9-eee2dd6abbfa | -1.44763 | -47.75241 | 2026-10-05 17:17:00 | NPP-375 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d501960b-c066-349e-a3b0-9d88a7c4d93c | -1.80491 | -55.72985 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0510578b-d7e0-3fbd-aa72-f0ab659f4c92 | -3.51504 | -59.5618 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d9635ba5-aaa5-3a60-9624-72afebf4c1d6 | -1.21469 | -54.5417 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 808efafb-4480-3797-8815-845d574041b0 | -1.69511 | -50.82804 | 2026-10-05 17:17:00 | NPP-375 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 95511a6d-3cf7-333b-957e-243bc11a25bc | -2.94816 | -54.16177 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 28a2bf4d-7e1a-321f-b2ce-7cfc08b463b8 | -0.39901 | -52.00418 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 0a1180cf-ebef-33a0-893c-43a40e756d87 | 1.11065 | -52.5923 | 2026-10-05 17:17:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e27ff77f-9e65-3a78-bb58-9f179ec70f40 | -1.64154 | -55.14513 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d8b2b3c0-8990-3895-843d-88e3692de04c | -0.25642 | -48.67349 | 2026-10-05 17:17:00 | NPP-375 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1c5ffee6-31e2-3392-b2f9-da8fa4c171e3 | -2.94512 | -54.11983 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c667f1b-d86e-3749-8c11-33e7e68152db | -2.88377 | -54.09125 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55e3c742-4e76-357e-a28c-78ec2412eb90 | 3.37299 | -51.55235 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9678ef94-55d4-3f8e-ab73-ac57a97b4eca | 2.07175 | -50.88724 | 2026-10-05 17:17:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| db6c4557-7528-3e90-baed-7367d2117371 | -3.37482 | -58.1989 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| cdd0b353-3821-3764-8fd4-a5b39adb755b | -1.19679 | -53.38345 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1cdc6d91-e4eb-326d-8f3e-431dfd5ae2c6 | -2.8281 | -54.12505 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 79ecc92f-5080-3968-9807-a67cd217e9e5 | -2.96967 | -54.1691 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9b45e28-2f28-384d-827d-2caa26c2e1b5 | -2.87804 | -54.12031 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 78d6dc0e-3678-379c-8022-0355e80743a1 | -2.43709 | -58.01679 | 2026-10-05 17:17:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 60cfcb03-067a-3eb0-b60b-ff43a7023717 | -3.09055 | -59.19073 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4d8575cc-5e1d-3996-bb5c-25076297ab2c | -1.81121 | -55.19583 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3870e3db-19fe-3569-80ba-4fa4e3e6f873 | -3.67522 | -59.67559 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83829a88-8221-335b-9878-f417bb9c3297 | -3.74889 | -59.41518 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 452dcfa6-2ec7-3ca4-bafc-60518afa5989 | 2.48516 | -51.26965 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c5a059cc-0202-3895-b35e-4a91cbb3a773 | -2.88271 | -54.08434 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 08f23c45-02ed-3de1-9d58-2397c4fc8497 | -1.42685 | -52.72595 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a3c472c-0840-3286-921e-e6677e2631ac | -2.96878 | -65.1917 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 83d15353-2517-3a03-9688-4663e1b2c606 | -3.30837 | -59.5369 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 81304149-15ea-3fe0-af8c-ba340129fae1 | -2.1906 | -56.63969 | 2026-10-05 17:17:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb0a9aa8-2baf-3c96-9205-3eb12b82b1af | -1.26336 | -54.68228 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 447cbf94-1cc2-3080-a689-081b0b75f327 | -2.22401 | -53.71157 | 2026-10-05 17:17:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a2f08c89-13ea-39cd-9fe5-782c65aea3df | -1.52215 | -54.80413 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| d6dffee6-4d55-3b37-bb12-365d95c1330e | -2.89879 | -54.07837 | 2026-10-05 17:17:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08621f0c-bd6b-3ab2-b28d-f12ecdb0cf20 | -3.82005 | -61.13529 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cdfd62c0-ed40-32b6-95ed-c3e1054b4637 | -2.98285 | -54.09998 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c733423f-896e-3581-9031-dc7b2c751c1e | 1.84516 | -55.80623 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 604cf88f-5563-3642-bea2-b0e6a3f82e1c | -1.32907 | -56.41147 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| de0ab6c6-5278-311b-95ec-8f9d4c365a47 | 1.83008 | -55.55033 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 581eb42e-ce7f-3eae-a03f-a189e621bcd2 | -1.74382 | -55.23874 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cedafed0-e588-31bf-a7ce-ed63e3f895b7 | -0.40681 | -52.00716 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bbb1571e-43cc-3178-b69d-24452128f55f | -1.19412 | -49.25445 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 17114fb2-72cb-3fde-ab76-5f7db98a78da | -2.96066 | -54.11041 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 0c9448ba-2fca-3292-894e-be698efde0bd | -3.16025 | -64.87598 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c60a2b2c-0662-3635-b085-ef59d73609a9 | -0.73501 | -57.97134 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3d189fb9-dc1d-3373-bdff-371db5edfc06 | 1.84078 | -55.81263 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 27eb1278-8cb4-3785-a7ab-ecce19520b38 | -2.37718 | -56.12463 | 2026-10-05 17:17:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6b6e185-8331-3d53-9959-8aafd3cfa9fb | -2.97672 | -54.76536 | 2026-10-05 17:17:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5acc610f-e530-3027-bf1e-3a6ffe795f49 | -0.38339 | -51.99824 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 24f07c1e-486b-3169-a8ce-d9d4f271fd87 | -0.1069 | -49.68788 | 2026-10-05 17:17:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4088923f-656e-36ad-adf0-6ba271dcc5cb | -3.82397 | -61.1299 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 63d21865-7d63-3d2f-84fd-72104f831aa2 | -2.96119 | -54.11386 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d73724f2-9cef-3072-8d9e-08c8ec57bea9 | 3.39982 | -51.53179 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c069edbe-65b4-35a0-92e8-da95f6b8e91f | -1.85243 | -50.6233 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1be041d8-ab2e-3a23-a3bf-2ae38dc30fec | -1.51484 | -54.82285 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2e72514a-ec9e-304c-b8b4-9ed8587903c7 | -1.3307 | -54.66054 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 603c3fb4-dc97-3659-ae01-46e3d51676e9 | -3.4486 | -60.27985 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c1878a11-4730-367d-92e6-f213657501c5 | -1.85335 | -50.63409 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e116861c-a0e1-34a6-8c69-dcdad710a216 | -2.87751 | -54.11686 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b2c41cb7-4cc1-38d1-89ed-dea7676d55fa | -1.93651 | -48.39841 | 2026-10-05 17:17:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee937e7b-5c15-34d2-83cb-08ba165eb69c | -1.0899 | -52.27748 | 2026-10-05 17:17:00 | NPP-375 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| aa5bfd6b-70da-3c8e-bb5f-252cb2a51a24 | -2.98839 | -65.21678 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 21de7ce5-37d8-343c-a0e6-f92eff4a11c6 | -3.06448 | -58.41801 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 53152738-50de-3dff-b71e-8a44f837ed22 | -2.18574 | -49.75905 | 2026-10-05 17:17:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| aeeacbfc-4ec5-3f92-b519-d32c848743f9 | -1.30694 | -56.92611 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 926a29f6-c659-3060-b946-8c519b714b8c | 1.57766 | -55.98388 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| baa5d7c2-a7e7-3ba5-a573-b276df30dff6 | -0.71544 | -57.96956 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 597477e7-398c-3e24-bde4-9e2b68c95f39 | 2.48819 | -50.9336 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c39881e2-bff8-3bf6-bf07-43590faa2382 | -1.98298 | -52.64056 | 2026-10-05 17:17:00 | NPP-375 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 966a1f46-06da-31f7-af87-c4d8811a9c9a | -3.32394 | -59.48208 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 61075e1f-36f2-3518-a92a-20d226b88908 | 2.35431 | -50.75343 | 2026-10-05 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5481441b-d915-34b3-93a1-0bc1ed8de7d9 | -2.93904 | -58.32671 | 2026-10-05 17:17:00 | NPP-375 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d6ba62ba-7771-37a0-a7e7-b84ed0ecf496 | -1.17675 | -49.25319 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |


[Clique aqui para ver as próximas entradas](README130.md)
