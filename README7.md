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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41da542f-77a9-3078-85dd-10af2e255c10 | -8.76569 | -48.43993 | 2026-06-05 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1855030-7d38-342d-b2ce-6ef7d0f9b8d5 | -8.3185 | -46.99632 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5970497-2588-3790-954b-9139f6139741 | -11.38391 | -47.81918 | 2026-06-05 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54a3d92d-1d53-3e5b-9651-adafed22b26b | -10.93551 | -46.95206 | 2026-06-05 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e62105a-aac9-38e3-a90d-87364378cb25 | -9.08943 | -50.61373 | 2026-06-05 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 93f42bf4-662b-3a00-986d-9ff130529dec | -8.7286 | -47.9818 | 2026-06-05 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60bda3c5-c599-3f63-9653-fccb05bdb090 | -10.84051 | -53.75418 | 2026-06-05 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bb17d53-8d92-3905-accf-a52e11613b92 | -8.39754 | -46.90406 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d454fff-12b9-3a7c-accc-d991110c89fd | -8.37481 | -46.79004 | 2026-06-05 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dc8382b-2012-348b-8ee9-64fa14840cba | -8.50232 | -50.29454 | 2026-06-05 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f884e6b-ecbd-35ab-aba5-6787b4d3da76 | -10.93749 | -46.94013 | 2026-06-05 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db7fa3bc-2141-3fd4-8321-f748d158930c | -7.95271 | -46.84033 | 2026-06-05 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a0090b9-ef70-3125-b76d-72ff40e4ae4a | -7.64989 | -45.23576 | 2026-06-05 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c899700-515d-3291-a15a-846f5218d485 | -7.64367 | -45.23097 | 2026-06-05 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 482203a8-957c-3676-856f-bfd612a110a9 | -7.9169 | -46.19318 | 2026-06-05 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dec1dd13-3fee-36ea-b58c-edb941a809be | -7.6493 | -45.23944 | 2026-06-05 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6fec73e-3ad1-30b5-9ac5-a7a2b2f4bb1a | -7.95219 | -46.841 | 2026-06-05 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3436cc6-a588-3e8c-abde-2ec68248eb0f | -7.34433 | -49.83514 | 2026-06-05 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 19915921-b55a-3711-befa-e58203315622 | -6.85075 | -47.94359 | 2026-06-05 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53917005-5d3e-3e15-a7e1-97cb15a4a89f | -6.98871 | -42.88384 | 2026-06-05 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| c5af56a1-c8fe-391a-b7b9-da1b9f397393 | -6.84768 | -47.93788 | 2026-06-05 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c84b24e8-f552-3c08-b277-cc4042020b56 | -7.35169 | -49.81897 | 2026-06-05 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80ae4ca5-3ebb-3364-befe-14327ff7dd0d | -7.63967 | -45.2341 | 2026-06-05 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd39581d-b422-3b6c-a935-d1682021e12f | -6.90917 | -48.04821 | 2026-06-05 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 933a3501-7b3f-3faf-b6c0-786c76dda000 | -7.95633 | -46.84097 | 2026-06-05 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76a31967-8b2e-3ef9-a808-a367fbe26b38 | -6.98538 | -42.88332 | 2026-06-05 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| bd32d559-70bb-3f31-ad9b-2063dd86f972 | -7.45961 | -49.74179 | 2026-06-05 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85407f24-e024-3d6f-8d7e-b33958b58373 | -7.64649 | -45.2352 | 2026-06-05 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e02659a3-aa48-3699-a4b1-4f8453d13e20 | -7.35535 | -49.82395 | 2026-06-05 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bd0db03-5c61-3fff-a19b-6e053d27666e | -7.64708 | -45.23152 | 2026-06-05 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bf4a2cb-9359-3b1c-80f9-1865170f6cbc | -7.91756 | -46.18917 | 2026-06-05 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9d90e63-8fff-30b0-b36d-74180416f610 | -7.92041 | -46.19384 | 2026-06-05 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 909621f4-4e91-3e1c-bcfa-a4f453af05f8 | -6.84684 | -47.94291 | 2026-06-05 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c834e57d-81e3-3459-8721-f3d348cab8b5 | -8.03377 | -46.9782 | 2026-06-05 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6680ac0-cc7c-3baa-8866-210595ca7e01 | -7.95562 | -46.84517 | 2026-06-05 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d1e8a8c-7f28-3af9-8a9a-ad8e885a6d21 | -7.92107 | -46.18981 | 2026-06-05 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e73675a-0894-3ff2-b18b-86d0c9ba32e7 | -7.46014 | -49.74138 | 2026-06-05 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 758ec48d-f0e3-3165-8d6a-0bc3e4b0e364 | -7.34507 | -49.83091 | 2026-06-05 04:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74f99c83-e1b3-3a9f-a8bd-88984439cd1c | -15.43306 | -46.33576 | 2026-06-05 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c835523-ee3b-3187-8135-95527cc101eb | -12.4449 | -58.48389 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9f538dc-2f5d-353b-8d58-a8d7e73338e5 | -11.54915 | -52.80173 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8f0573fa-5ef3-3a58-900d-3db103d708a1 | -12.45465 | -58.4725 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89f71c15-2351-3073-8a08-726bb3a460ee | -13.51889 | -54.31148 | 2026-06-05 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51a85a94-636f-3dc9-b120-daf38f034b38 | -13.51954 | -54.30812 | 2026-06-05 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 253b1245-f1a1-3073-b069-85d6588bfdfb | -12.09071 | -51.99425 | 2026-06-05 04:25:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbd8a5a3-446b-3375-9d44-61e8a8b7cd1c | -10.57309 | -57.3202 | 2026-06-05 04:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d336116-cacc-3df2-b7a9-0c642d8f63ed | -11.00758 | -54.30969 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0b98c4b-26da-303e-ad79-ed7caefc934b | -12.72599 | -54.73806 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42047b33-1927-319b-98d0-5fd4e5a79528 | -17.78339 | -50.46788 | 2026-06-05 04:25:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c544e0eb-06c8-3af3-87d9-382d7d24a382 | -12.44767 | -58.47116 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae7f5710-c60e-3991-84cc-d064962f7e30 | -12.7323 | -54.73532 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4b913a6-73b8-3198-ab10-2ea4dfb445f9 | -16.60222 | -58.24425 | 2026-06-05 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| eb87fa28-4b59-30df-913b-9ad599d4a1df | -12.06262 | -48.07166 | 2026-06-05 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58767482-4122-3831-b3a6-0c78aa3903a6 | -12.73079 | -54.74289 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e2bba97-3706-3316-a1ad-cc53da4c440a | -14.05052 | -53.36684 | 2026-06-05 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 336522fc-ef40-32b4-8df2-cda7fb9d9457 | -12.4445 | -58.49421 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3138f291-a259-32c1-93ef-c6e7544b8989 | -12.52453 | -46.27597 | 2026-06-05 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 129e5f8b-8be9-372d-94df-20a0147f4f74 | -10.85768 | -53.7331 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 819a7325-5c46-3631-b069-dd934e94351a | -11.6029 | -55.33939 | 2026-06-05 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e42450d-20f5-33e1-aa88-9e6e06e855d6 | -10.84238 | -53.75464 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1258bde-35bc-30d4-a499-c67d2d1dfea1 | -11.60043 | -55.3418 | 2026-06-05 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebb7753a-13ff-340c-9a57-c447dcf5c176 | -12.50611 | -46.34528 | 2026-06-05 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e629351-3030-306f-aa10-f07d6459814d | -12.92667 | -43.61884 | 2026-06-05 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61c962cb-89a0-380f-a049-3aa360d8e010 | -12.45568 | -58.47559 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 301c533d-dc68-31ef-b8cb-857777615ce6 | -16.95662 | -50.4902 | 2026-06-05 04:25:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fa41347-2af5-3e23-bc0d-6e6a9940b7f1 | -11.88595 | -57.82803 | 2026-06-05 04:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22cb943d-5633-323e-9fc6-7b4e195683ba | -14.0495 | -53.37119 | 2026-06-05 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d336f93c-e021-375d-afe2-47f27fe2a3f6 | -13.42931 | -49.64904 | 2026-06-05 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 999e9733-7f6e-3cef-9e64-01fa612155a2 | -11.95326 | -49.30213 | 2026-06-05 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a56d1ab-a729-3835-947f-090b26a5af07 | -12.4439 | -58.42191 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01e2a226-5cbf-3040-adc6-748bbf4e348d | -12.43995 | -58.40682 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef5c2c71-bef2-3b3e-91f6-13a1708e750b | -14.77013 | -52.677 | 2026-06-05 04:25:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42232ca2-e84e-30a1-9fe0-0b4f2b4555f3 | -15.31108 | -46.92868 | 2026-06-05 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3499d9d7-8f63-335f-835b-6a531c3ab43f | -16.59587 | -58.24269 | 2026-06-05 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| f687be11-4dfc-37a4-8ec9-1bc0680d21e8 | -11.54803 | -52.80756 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ba6f43d-0b42-3fb8-a220-552330cd26a2 | -14.15306 | -51.59452 | 2026-06-05 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ec5caf7-8a71-380a-b94c-a5e91c6eefd5 | -13.66785 | -47.75504 | 2026-06-05 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c58b917-ff20-357e-8176-5af05667ebc3 | -11.57062 | -54.58797 | 2026-06-05 04:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9212ca2e-4c9c-3fb7-a9e5-bd999c72caa7 | -16.5971 | -58.23708 | 2026-06-05 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8fe1f173-9a1f-3e31-a0aa-92a6159900f0 | -13.31515 | -54.6888 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3afb7fa0-cf0b-3f1e-90b4-cfe5967ffeb3 | -12.50271 | -46.34469 | 2026-06-05 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d07cfcbb-9209-3bfa-b04e-88337ca62d3c | -14.77109 | -52.67197 | 2026-06-05 04:25:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de34907a-b1d2-3032-9b58-002aee8c45a4 | -19.97588 | -44.85554 | 2026-06-05 04:25:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9401dd8e-f2c7-34b6-a592-3d3c6d224a4f | -12.43853 | -58.41334 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9b6e124-5c13-3c30-b6a9-be80a9d1b95f | -14.0983 | -59.39354 | 2026-06-05 04:25:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e34ceb3-d00c-3092-ae54-4bb29dd78973 | -12.73377 | -54.72788 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a54f941a-b572-3278-bc2c-137cd43a9a62 | -14.37308 | -45.58611 | 2026-06-05 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f11b8e4b-b37c-31b3-82b8-1a1b5e85441c | -12.31283 | -54.1281 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42018729-14f2-3578-8a28-787e82511e0a | -10.57184 | -57.32627 | 2026-06-05 04:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85ab0029-7d12-3c3e-8263-292c65cb744d | -10.86046 | -53.74762 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e6bdfa9-3ea5-3159-adc6-75a438df31d6 | -11.56108 | -52.7976 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2c1baa4b-ce44-3631-88e5-ec811b5901c4 | -12.44602 | -58.41833 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1c91bc6-746a-3646-be52-b71a8c26b140 | -14.0998 | -59.38667 | 2026-06-05 04:25:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86ae82b9-f4f3-349a-9a98-2fa244b3b7e8 | -11.56521 | -52.7989 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 950476f4-0452-3baa-b8ae-20b26244b294 | -12.44871 | -58.47421 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30f750fe-2fe0-3660-94c0-c9bcbd7c65f6 | -11.60374 | -55.33508 | 2026-06-05 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3212fc6e-a867-33bc-ba9e-257f582d7dc2 | -11.55505 | -52.80233 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f39f4a31-6366-3001-9d96-45b73d231ac3 | -13.51726 | -54.30777 | 2026-06-05 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f231a1f-0957-3b3f-9d57-9f83c93287a7 | -11.60629 | -55.34303 | 2026-06-05 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c2f1208-1eb5-3b0d-9f07-20b85bf845cb | -12.44344 | -58.49062 | 2026-06-05 04:25:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README8.md)
