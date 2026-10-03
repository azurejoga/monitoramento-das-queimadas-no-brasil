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
| ba758c22-42b9-3331-8c0b-b84b29273da4 | -11.6228 | -43.541302 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12084b05-d8ae-3b3e-a5ef-cc1b9d8f9b18 | -1.0781 | -54.108799 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddba926-6e60-3ab1-aa2f-13bf608b2ee8 | -1.1982 | -47.775002 | 2026-10-03 00:30:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c3efee-2091-3e09-9a41-e28266823605 | -3.9109 | -54.417 | 2026-10-03 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17a1fe0f-df11-3f9a-8807-1d5e4f7266c8 | -3.6948 | -50.6525 | 2026-10-03 00:30:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da8a671-145f-3321-a3db-05a1a069592e | -5.8606 | -53.470001 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58b68449-666d-3bf3-90d0-ecbbc030fabe | -4.7917 | -55.713001 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66dac82d-f75e-378b-8a16-2f8664f68372 | -3.1719 | -54.069099 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2815e29b-5167-3805-b96b-0f3aec33942f | -2.9316 | -54.145699 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10693cc5-b3ae-37d1-9507-f550d44383e3 | 1.8059 | -55.572601 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed1a496-3483-3eeb-8f2a-dd32c070aca8 | -6.2143 | -60.010799 | 2026-10-03 00:30:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b47dd86-fe77-327a-b1e4-397904c520f7 | -6.2403 | -53.146301 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63a01233-19eb-3e99-a060-bff22044e2c2 | 1.7479 | -50.7971 | 2026-10-03 00:30:00 | METOP-B | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cf20f070-f52a-32c7-bd9a-6ae96ceef09d | -5.728 | -45.030201 | 2026-10-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8543e69f-16c3-3957-88ae-ba47b589d5c5 | -2.9054 | -54.121399 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f4c78a3-d1f0-3438-a705-7fee51749570 | -2.1468 | -59.208199 | 2026-10-03 00:30:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd4e3bd-710b-38ab-a7a8-b81e3a0ae50e | -11.6873 | -43.4734 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a0a6f1b-76a7-3e35-a994-dcc5a4800c80 | -5.2491 | -55.914101 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 292204fc-db9b-33a7-8b15-7f405d9a6d06 | 1.7799 | -55.596401 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcb976e3-0deb-30f6-aa4e-09e944d6c3ff | -3.2924 | -53.828899 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e687c8a8-9041-37e1-aad0-40b1de06249f | -11.7387 | -43.433899 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c914fb81-fbf5-3c33-ab10-671613f89d05 | -3.1251 | -53.727798 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe8cc1d5-aab4-3501-9399-f4e2978293c9 | -11.4382 | -43.388699 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1aa7e914-5419-37fb-afc9-ead8bb138a58 | -2.5427 | -57.990799 | 2026-10-03 00:30:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37324a04-4979-3bea-8d02-f9bd9554a8c7 | -6.2369 | -53.131599 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73faa83e-cf21-3e5d-ae9b-c49f34e298cb | -6.0192 | -53.532299 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b3438c9-3ec2-3d42-ae88-a72143b9ce5a | -6.0209 | -53.539501 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce52322c-d573-39be-a0ef-aa3f62a8a2b2 | -3.1234 | -53.720402 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4f02886-f651-3830-aff7-fc1435070a78 | -11.4734 | -43.4048 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 482a2d23-e3df-3d7f-84fb-203434e904c5 | -4.4277 | -55.743599 | 2026-10-03 00:30:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24273ab1-c00f-34c2-92ba-96fc7911c0d6 | -1.2589 | -54.542198 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1caaab2-ce04-3020-80ea-d767b20a4314 | -2.9661 | -53.257198 | 2026-10-03 00:30:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bea0719a-7057-3af7-9de2-ff53edca2c16 | -1.2164 | -54.536701 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13458053-0faa-3d07-ac5f-9aab228d8286 | -3.1203 | -53.752102 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ba49b7-b832-314d-90c8-1036fd9fc98b | -2.5442 | -57.4011 | 2026-10-03 00:30:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94886fc5-fcc5-3b70-8bc6-5b7ff463a735 | -11.6969 | -43.470798 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77c2bcff-7c8f-3f35-9756-bacc7a480206 | -15.2913 | -42.775398 | 2026-10-03 00:30:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ffd101b3-2179-34cd-baad-b6e90fb016d1 | -2.8746 | -45.397499 | 2026-10-03 00:30:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1275647-195a-3d86-8d85-6ee4240ec724 | -1.2148 | -54.529499 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8d0efb-8bab-3db7-83c0-1317fc35c547 | -4.4402 | -47.9212 | 2026-10-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf1c0b33-879b-36a6-a540-82d338c14b5b | -5.9423 | -43.636002 | 2026-10-03 00:30:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39ec4c64-5403-3cbf-9426-71740131e0d6 | -3.216 | -53.9454 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 840bfbb3-3282-352d-addd-b46887e47e6d | -3.1866 | -54.088501 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd97cc64-61bf-3de8-a650-440c69f598e7 | -3.2143 | -53.938202 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fcfb820-9f2a-305b-a8a4-25ac7e8768e2 | 1.8027 | -55.5867 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3483d055-302a-3b7a-a632-4593813e5459 | -2.484 | -56.082199 | 2026-10-03 00:30:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4365c8c4-deb1-3a52-96a5-ea91fdf23180 | -3.0575 | -54.155102 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4f6bdb7-c09b-3ed1-a8cc-88deba79b11f | -6.2386 | -53.139 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1fb7c24-f9d9-3b8a-8659-6d500d571721 | -11.6351 | -43.587799 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e20ba7bd-34e3-3b5e-a8da-92ee3b7a180e | -2.9087 | -54.090401 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d64ca6b9-4249-3b7b-91a7-a3aa398c0e2a | -10.9831 | -59.114601 | 2026-10-03 00:30:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| baa435af-0b9e-3e41-9ce1-470e2d2013b0 | -6.7215 | -44.131401 | 2026-10-03 00:30:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9708bf9-1708-3cd2-8951-ee6423fda609 | -2.0193 | -54.304699 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea07cb2-1845-3703-8b50-e08569e26dae | -5.9399 | -43.667 | 2026-10-03 00:30:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26ee1d4c-3323-35ae-b037-a0437e804fda | 0.6291 | -54.3951 | 2026-10-03 00:30:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406e488a-de6d-34d6-a57c-1db82f0f6aa4 | -3.2941 | -53.836201 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07a4d0d7-443e-3f62-b3a0-a406cb3ae4a8 | -3.1366 | -53.733002 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81fc3dbf-90d9-30c6-aac6-09bc72d4ee12 | -13.5252 | -44.099998 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0cfb75cc-e744-3e9c-947a-215c218439e9 | -2.9333 | -54.152901 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10fe0564-4af3-36eb-a07f-12766168e039 | -3.1135 | -53.722599 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10ad57a5-b93d-3ace-baee-dc8e3ae515bb | -5.6087 | -44.3848 | 2026-10-03 00:30:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 258c3130-c635-3911-9935-3b49270741e1 | -2.0177 | -54.297501 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbf9cb00-b5cc-3dc9-a4b5-914397512867 | -4.1176 | -55.0098 | 2026-10-03 00:30:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1362d569-a086-333f-8ef7-63ff458d54ea | -11.403 | -43.372501 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86d647d8-a206-3a94-bb88-2e84c43746ba | -2.9709 | -54.091599 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eab04c1-683f-3ebc-900c-e32dad181f4e | -4.041 | -54.218102 | 2026-10-03 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d434a46-7313-31eb-8c2e-1de4c26f6557 | -5.9327 | -43.638401 | 2026-10-03 00:30:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cf84426-f463-3a78-ab60-34d200d74ba1 | -11.7731 | -43.525002 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ce4c811-5195-3484-9fc5-cffd27ef69a7 | -6.0239 | -57.683899 | 2026-10-03 00:30:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b8660f0-2d63-3ea8-aea4-c1faf2a35cf7 | -6.114 | -53.089901 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6f571e-04d6-3797-993a-5c2cdf2d1330 | -2.9692 | -54.0844 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f6012e3-90e5-3905-8609-bdbf10c0424d | -3.5081 | -54.595299 | 2026-10-03 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a10a33-a873-3823-a6dd-25a30f845d76 | -11.7127 | -43.491501 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35134933-5127-3c86-9d3d-ea75f76f6822 | -2.8972 | -54.0854 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 914e77cf-9525-380c-ae18-bd8dee8a462c | -1.1406 | -54.156898 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c31ea1f8-41d5-39d4-ba4f-0b891dcdab58 | -5.373 | -56.053398 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbd5dd29-31d5-37ce-a93a-099b0120383f | -3.7045 | -50.650299 | 2026-10-03 00:30:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58b99944-32e9-3aee-b106-87a8e67b5501 | -4.4464 | -47.9035 | 2026-10-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a712f769-b988-37bc-8b74-e8da4fcac83f | -4.1135 | -54.401001 | 2026-10-03 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 580c2cd8-777e-3ec7-a6e5-aaa1b8a23151 | -2.3807 | -56.629299 | 2026-10-03 00:30:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 861f481e-33d9-36b8-a41d-ea235f80fca8 | -9.6993 | -57.444401 | 2026-10-03 00:30:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 937dc8ca-62f4-31ae-99b2-05f09ee430bc | 1.9153 | -55.7729 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e98f3b6c-ba62-333a-8272-fab5d70587b5 | -3.1382 | -53.740398 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de116110-ba7a-38ef-805b-7f7e2c0f6976 | -3.1349 | -53.725601 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb687fee-62f0-3323-afb0-b3cdcf580733 | -3.1807 | -57.897598 | 2026-10-03 00:30:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f50263d5-bd0d-33a6-960d-9536a987aed7 | -6.0792 | -53.298302 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 168fb00f-fe65-3e61-a82c-2920bb9a01d6 | -6.2121 | -60.000401 | 2026-10-03 00:30:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5a6a838-b437-3ddb-820e-cfc48fdbf26c | -6.0649 | -53.461498 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecd49868-5209-3a54-ba09-f3c5cc7b77ce | -6.0176 | -53.5252 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d052508c-145c-35f3-9a31-66ca2a9927c1 | -9.7011 | -57.452801 | 2026-10-03 00:30:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf852a64-8473-3ce6-8a62-52410fd35439 | 1.7783 | -55.603401 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8258d7-41e7-3564-bed4-aa7955098ded | -2.9071 | -54.128502 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8ee8030-65e6-31b4-bb23-fba13dd863e9 | -3.2826 | -53.8311 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80fc66c7-849e-33be-bf27-d55059cc8a80 | -1.0863 | -54.099201 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd2d9836-b740-39c0-9352-043d8f2e1ba0 | -2.3261 | -60.0555 | 2026-10-03 00:30:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00aa7472-56ad-3e6e-a522-31655a312408 | -11.7037 | -43.418201 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ebca0169-a324-32c5-b7a4-78b3815a8355 | -5.7217 | -45.129398 | 2026-10-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f9d2d63-52d2-3f74-be16-5f7ff05bb715 | -2.8891 | -54.140099 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dee60119-1225-38c6-a12a-069fe5411431 | -2.9054 | -54.076 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bca690f7-97e0-3299-9c51-9f61e22201f9 | -3.0178 | -53.890701 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
