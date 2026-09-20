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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f3352d7-bf16-33fe-a968-fec5ba27fedf | -3.69103 | -60.6059 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08771098-6e27-30d7-925f-2a29720b50b8 | -12.527 | -50.0358 | 2026-09-20 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e507bc6d-60eb-3cde-88fc-f7e20f66b3f2 | -5.73499 | -51.75856 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caf8ffde-dcb5-36ee-b9b7-e078b886b1e7 | -12.3408 | -50.68908 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 184fc095-dfa6-36b7-9d8b-1c2a83fc5980 | -15.32242 | -49.56343 | 2026-09-20 05:25:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0f37528e-5de4-3c0e-99fb-76dbc12d092b | -13.88008 | -48.57986 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7c97662d-0baf-3e5c-9ef7-7524edebfb08 | -10.88177 | -54.07732 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0ea8d67-7633-332d-84db-42209e2e7a8c | -14.66873 | -54.45942 | 2026-09-20 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9769e463-0959-3339-b34e-5616e1a2c60e | -6.09405 | -57.64865 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0f236eab-234c-3efa-9bbf-1fe2c54fba0d | -5.89344 | -55.56094 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31ced974-1754-3a23-bcd5-ec5c5eafa664 | -3.68995 | -60.6128 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 908c209a-f0f1-3344-9e00-03a6295a8545 | -5.74318 | -57.58003 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb21d1bd-caab-3947-a2cf-fd00fa84cca1 | -6.33072 | -55.26746 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bff82138-f4b7-3e5a-8605-08519f394f10 | -15.86758 | -49.91125 | 2026-09-20 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9a76abb4-3fb2-3042-9164-3da0dc03c1d2 | -10.89859 | -53.98742 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2401794b-e1b4-3212-9559-214f0cebf061 | -11.27557 | -54.12538 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afaaa292-c35b-3ddd-af68-ffa910e70aa3 | -4.40703 | -55.49819 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4b062c7-0774-3c16-ae68-4bf197476114 | -11.04734 | -54.15488 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ad56f79c-6c6a-36e1-b1c9-68c0d377ee57 | -11.02129 | -54.1301 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c927256-7d9d-3ccc-8519-769050b604ac | -11.3918 | -51.38638 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76fda120-ff0d-380f-9094-170ab6529039 | -5.79702 | -47.36774 | 2026-09-20 05:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 10fa6dae-0647-3aba-911f-e992a48872ea | -3.79916 | -60.71828 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c66fee77-0b43-37a9-a057-151edf35326e | -11.37203 | -51.40445 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61b098db-dc7c-3a34-8471-c819e9eaaac9 | -3.68779 | -60.6266 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ae48bd9-06e4-3147-b609-bc7321c40089 | -3.79007 | -59.48986 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa7435b-bc82-3377-bbb6-cfa1cca0bb14 | -5.84953 | -53.55197 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57d05f86-5996-3627-939d-5f638e99693d | -6.38996 | -51.67987 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bb2990b-0323-3470-84ab-80e60ed8d71b | -12.3115 | -50.72854 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ebc366d-7d24-3156-a938-a73ea2d4820e | -5.15186 | -56.18391 | 2026-09-20 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d39db3e5-34f1-3262-8856-f14df1660efb | -11.28038 | -54.126 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d334a83-efd8-3d8b-b2ae-68af7b33faf4 | -5.82671 | -47.77436 | 2026-09-20 05:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9cf646e2-ff1a-39ed-b4bd-3f84757478a5 | -10.87213 | -57.14322 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec865b02-834c-308b-889e-970d044c9039 | -5.81348 | -55.7026 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe9a0c73-66f5-374c-8091-150346fa52c9 | -3.86219 | -58.89159 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4eb48e80-af4f-3c08-8c4f-c4decadd7d93 | -3.39641 | -61.07277 | 2026-09-20 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f7d78da-1f56-33c3-8850-b2333d2668de | -3.79645 | -59.71014 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bdd3e3e-6d26-3c55-8397-557419a1f2a8 | -6.66856 | -50.89405 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8cd8e777-08ab-3a2a-8207-6eb1784fd0dd | -7.52997 | -47.33702 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b30175cd-37c1-3e9b-ae6e-18d01222cd56 | -4.21085 | -56.34171 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8965d7bb-247e-30ee-b9a3-534392f31276 | -5.86324 | -52.03294 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dab8eaf1-5a7c-3d3a-8a19-cfebecf4ea88 | -4.22168 | -56.21486 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 952077f9-cf42-39af-bdec-0fcce112cdb5 | -3.40153 | -61.30102 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee4e9f20-70b5-3609-a651-dda1210f1675 | -11.12381 | -54.01997 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f2d16b2a-80a7-3ff8-b937-4c8c5030b05a | -6.4587 | -48.44011 | 2026-09-20 05:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84b54a83-214b-3072-a26d-3d6557a7fc26 | -3.69609 | -60.6385 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df5ea463-60f2-38f6-b93a-b82240ca4c46 | -12.64397 | -50.92686 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89f66749-0b97-31b4-981f-39fd67bb5185 | -6.30327 | -47.6349 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da2dfdb0-de5e-3327-a874-7bc7680a2e87 | -4.41157 | -55.07843 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91d6fa79-5f64-3a86-868b-491f9abdc1e2 | -7.17027 | -47.45822 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7d41355-bf3e-39c7-932e-1db0ea2ee5fc | -14.04613 | -52.08227 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5d225b2c-a382-315f-a9db-562e4b62ecc9 | -3.69645 | -60.5714 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f74ee56-f05a-39fd-aeb1-1f6ab64de9f3 | -11.39229 | -51.38221 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c22e5470-23f3-36a5-84b5-ca1b0846983a | -5.81694 | -57.54362 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28fb8091-ffae-3e25-a1e4-949d90aa2e2a | -13.88905 | -48.58372 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f90d6428-0774-3cb6-a062-603ccf61ae62 | -5.76556 | -57.45717 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a752b52-1492-3b82-a292-aec5fd987ec7 | -3.73128 | -60.60859 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 252b4815-e672-3e3b-a983-e94f74898b9b | -5.7969 | -47.36694 | 2026-09-20 05:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 860379e3-e958-3b1e-bf10-7885dfe462cc | -10.75098 | -55.99798 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a47bbe9f-fa27-3476-a372-cb3e5e2681d8 | -3.68833 | -60.62315 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56d9b19d-d423-33ab-b91c-1c6a972fcca7 | -11.94325 | -55.92246 | 2026-09-20 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f15d8fe4-5c49-3daa-86ab-4fbf05bb6b88 | -5.77798 | -57.58384 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c309970-bff9-30c1-8386-dbbb57bc3863 | -10.90334 | -53.98299 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f83d676f-465c-3f4a-89ae-0b3b35f45524 | -5.81071 | -57.73022 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef036764-9381-32ac-9191-698de4e14b31 | -16.88487 | -50.59674 | 2026-09-20 05:25:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| f9a3501b-c4a9-3ea6-a20e-29770e6abfe0 | -3.36857 | -61.33588 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1d10a9e-1cd1-3bd9-b33c-e01ee7a58874 | -7.17112 | -47.4514 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a81adb96-fe6c-3c95-96dc-d06cc0982c38 | -11.11275 | -54.02919 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 50e6a5ad-db25-3d33-afba-2ae80a13ec5f | -4.48879 | -55.48672 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47110ee3-1976-3c7b-98ed-7743b3ad961a | -11.21222 | -54.08403 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03966f28-714c-3f61-9075-5ceac7ccc97f | -6.10285 | -57.68785 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7d7df74-6e1f-35f5-8fe5-35dd88388d60 | -14.04567 | -52.08653 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f1a9a385-1725-3c54-9b51-37625b3857e5 | -10.92537 | -53.96425 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4998753-189b-35a8-a576-4c2f21bddb35 | -11.09275 | -54.03175 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 1c6f5067-00af-36c0-bc4b-133c717a3375 | -3.49057 | -59.97211 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0b696bf-1d06-33eb-bb98-75f5e4f2c95c | -9.94078 | -60.7247 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7f11f841-2cdd-35c4-b35c-c4aa46d03884 | -3.69386 | -60.63108 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41b79123-f371-395c-8773-e785c2e1cffb | -3.73073 | -60.61203 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7176870-906f-3c40-baa3-f404ff82cee7 | -7.18418 | -47.90197 | 2026-09-20 05:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14ca5a96-f6e6-3770-9909-680021144b3d | -11.04255 | -54.1543 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1cca5e9e-0f51-35c9-aeda-e3ce914eb0d0 | -15.86702 | -49.91679 | 2026-09-20 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4416d08c-f70f-3668-b943-11b9bf2a16ef | -5.85759 | -53.52836 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 297ed639-1e1e-3aa0-b6c5-98c67130d79f | -4.55305 | -54.90767 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f15add9-d297-30b2-9b7e-f139f754e893 | -11.21289 | -54.07866 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 264ef5a5-b0e8-3be8-bcd1-7471ac3303ae | -3.69651 | -60.59261 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3dd84b2-94ae-3f20-b884-89a8a736fa7e | -4.06157 | -56.24903 | 2026-09-20 05:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff258715-88bf-3eae-8419-935134d5b432 | -11.04463 | -54.17587 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2c6e520-0253-33fe-a1f5-3a3f429e48d2 | -6.10067 | -57.62864 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f7f5e744-3a65-3938-a21c-1fc6eb2947c5 | -12.77303 | -52.85646 | 2026-09-20 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21c51aac-c612-3034-bd29-65be48e6c236 | -6.66293 | -50.89339 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00a3ec7c-69c6-34ed-98cc-f0cd5905f1c0 | -3.63256 | -60.56498 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cab08bfb-a3f5-3898-a8e9-df821cd72ab7 | -3.71372 | -60.63415 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3880ba80-d618-3677-a3ae-026878546ef2 | -3.69218 | -60.62022 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a82aa230-859e-3c4d-94cd-6b3ed9ecbed0 | -3.48519 | -59.59079 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 731b937d-98f0-382e-bf38-02bd08688bf6 | -6.29988 | -47.60838 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b9a242b-0f8b-392a-bc93-e14b49535196 | -11.11243 | -54.02561 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c94f3517-8b36-37a8-8179-b2a7fc1ba4fd | -4.38629 | -55.25192 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a747950-a879-3dbb-a324-956626ed841c | -5.33094 | -50.09054 | 2026-09-20 05:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58fe7d1b-4faa-37c5-adff-dff5789703ca | -14.9326 | -49.90522 | 2026-09-20 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 215bdbf1-4070-3995-b22e-9ed13aa9db55 | -4.51952 | -55.47125 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb5fd523-8fcc-3a66-bd71-8985d7c31903 | -15.86492 | -49.90922 | 2026-09-20 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README98.md)
