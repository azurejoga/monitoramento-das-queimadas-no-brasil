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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9d60f7a-7bfc-3be0-b541-51b8f9336e12 | -4.08957 | -46.67218 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2734bc38-3fdd-3e6a-b52e-b97a7d325669 | -6.61865 | -39.18219 | 2024-12-12 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b392ce9-4cd2-3547-840d-5a6b10019e03 | -4.49455 | -47.94028 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ccce4a6-26d5-3d27-be31-aab902e2ccdf | -2.56556 | -51.884 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52281524-ca37-3cce-a70c-6778868026a6 | -6.53401 | -39.28266 | 2024-12-12 04:14:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 426e4919-8b35-3b1b-903e-2f6068b12f70 | -3.89696 | -42.5503 | 2024-12-12 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2da578c6-af74-3bfd-b3c5-a09eae08cb1d | -6.12344 | -42.53357 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 11ad990e-95ab-32c1-aecf-bac95acdea59 | -5.23895 | -38.50276 | 2024-12-12 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 18eb2028-3350-3895-aa11-ceda4365ec82 | -2.79306 | -46.98824 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c44bfc54-d3ac-3ca8-b78f-5daca99ec722 | -4.07781 | -46.12206 | 2024-12-12 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cbd7ed9-fae1-3f2b-9a24-db73c28e33f5 | -4.83667 | -42.1264 | 2024-12-12 04:14:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14c1a1b9-e8ae-38c0-ba32-63aa02fdc4fd | -5.59948 | -41.38537 | 2024-12-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a31a0714-8311-3da4-b65f-93145b0750db | -4.19027 | -42.43404 | 2024-12-12 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c7a9a15-89df-322f-9280-c1d831d9a40c | -6.50301 | -41.59648 | 2024-12-12 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85398e35-658d-3221-9108-550c91ce9a03 | -6.12398 | -42.53009 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 613bc35e-335c-3adf-81be-660f907fade1 | -6.28902 | -43.84964 | 2024-12-12 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 408d9f67-1fec-3fa5-b2ac-a7337790286a | -3.8214 | -44.1197 | 2024-12-12 04:14:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1fb77f9-30d1-3d0a-8256-3689fb5df2c4 | -2.71154 | -47.55324 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea06f9e1-78f1-3984-8f9c-88147a984a0e | -2.67471 | -44.29379 | 2024-12-12 04:14:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c03be84-9988-33c6-91ec-f205d67b7232 | -4.80156 | -50.82469 | 2024-12-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f000e06c-f7fd-3dd1-a016-193d1ae5a378 | -4.02076 | -47.02814 | 2024-12-12 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bebcd51e-24d9-3b33-b3be-8c8f958a2961 | -4.82688 | -48.83397 | 2024-12-12 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac7d5030-5ba3-3f70-9a3f-df9fe34f44b9 | -6.14243 | -43.91572 | 2024-12-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d122ac74-c505-3fb2-ae1e-8012eff98229 | -1.82077 | -45.34136 | 2024-12-12 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9b64725-e893-35ff-b160-469d8572eadd | -4.31742 | -49.39197 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1678b02e-1eb2-3c70-92dd-46e7b5210bb7 | -3.98733 | -48.39417 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bb9f564-dc6e-306d-ad7a-e07dd47b1891 | -5.35632 | -42.12836 | 2024-12-12 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f5dfd47-ca06-3873-9aea-b324860ce5f9 | -3.65632 | -45.70393 | 2024-12-12 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79e8ea9a-c771-3042-9be1-282eec5556e9 | -5.90264 | -44.01331 | 2024-12-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6e4b080-68c8-3449-9d1b-02fe5b49327d | -2.07984 | -52.27823 | 2024-12-12 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fc5e8e8-37cc-319b-9a6b-72651a586b73 | -5.29826 | -48.31452 | 2024-12-12 04:14:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81388e96-10dd-3541-a8a2-79b15122d6dc | -6.92146 | -43.5247 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fccfcb1e-b63e-3650-8bc8-ed83c9eb846a | -10.55832 | -44.58308 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32f82eae-7a99-34d0-8603-48d83f63ae05 | -7.88315 | -45.92035 | 2024-12-12 04:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c09893c8-ed3a-327d-9e88-a2b2a67c5777 | -7.80161 | -46.20517 | 2024-12-12 04:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6b5c75a-7f8c-34cd-83fd-b65edcc9c2e0 | -8.69797 | -50.19611 | 2024-12-12 04:16:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 958c69d5-688f-3027-9e16-41665415b84d | -8.6214 | -50.01754 | 2024-12-12 04:16:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ffe46f9-3f9d-3a42-a105-c9a470bee07e | -5.92059 | -48.05446 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 75a64c62-20fe-34b8-9f09-fb0a51b4b739 | -11.18466 | -44.62347 | 2024-12-12 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d37fa1ed-54d0-3d36-b68d-88ff135a748d | -10.09804 | -55.43377 | 2024-12-12 04:16:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72d7caf2-b354-310e-b42d-e2869505ed88 | -12.672 | -43.43708 | 2024-12-12 04:16:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fb87dc3-967a-378a-8c68-5127ebec032a | -11.97021 | -49.11861 | 2024-12-12 04:16:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e06f8d12-77d4-34ff-a3ea-0d3770dc1f1f | -11.11703 | -54.65289 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ace33b9e-2a58-37f1-a751-1ef31796cf22 | -9.03679 | -44.41709 | 2024-12-12 04:16:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1729bc78-8a47-3063-a2e6-21cb08f310fc | -6.93029 | -43.53316 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 35c3e8a9-c910-3636-a7f3-dbd35764cdf8 | -12.50297 | -46.34781 | 2024-12-12 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3181e0c5-18e1-32fb-962d-2164c6320ef6 | -13.86929 | -43.06498 | 2024-12-12 04:16:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4867c790-9b30-3113-a3f1-a8934f5b78d7 | -7.47172 | -44.73925 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 534d9062-b4ea-3328-b139-b3aa512e038a | -6.92584 | -43.5183 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 9daab1da-abcc-3a52-a3df-3412fc76b594 | -7.43261 | -44.74779 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e35fdc-b31c-3308-848e-c85836093f6d | -6.93852 | -43.52383 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3cc626d-00c1-3b73-9f59-30914cd4ef05 | -7.86664 | -43.08833 | 2024-12-12 04:16:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51011a86-64b0-302b-80e6-3e227d3ba400 | -8.6443 | -46.05213 | 2024-12-12 04:16:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01dd1fc0-1c38-3f57-b571-2846be5bf186 | -6.922 | -43.52124 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 42c38062-fe04-3e46-8a0e-832ac9923902 | -6.92807 | -43.52573 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f869a1f3-00cf-3406-8f21-5b9baaed97f5 | -6.94021 | -43.53471 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a0e65f-2ec9-3374-81a6-1fd6c60fa5e5 | -11.20428 | -53.84098 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5086f90-b2ce-3e6c-9e95-a22e8f499947 | -12.70793 | -47.63073 | 2024-12-12 04:16:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 108b05a5-9ce3-3292-9556-fe523d64e1f0 | -7.71749 | -45.66045 | 2024-12-12 04:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60bdffdc-7ea8-3702-80dd-18a6a1e756f0 | -11.20559 | -53.83418 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5c2d6c4-dd05-3720-8990-8b30718acbf4 | -6.96582 | -43.00018 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a25ae6d1-56f7-38ff-b54a-3c3749a5e498 | -13.15386 | -43.95633 | 2024-12-12 04:16:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 084d1445-a1b5-31a8-a1e1-44de24f23db8 | -7.29966 | -44.5162 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dd02d03-8800-3f29-8fc7-ae1b8112f1b5 | -6.94075 | -43.53125 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87474476-7a80-3c5d-ac17-93ea89bbfa36 | -10.84082 | -44.6038 | 2024-12-12 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1ae68001-0746-3551-9c31-58afdad4786b | -12.49959 | -46.34725 | 2024-12-12 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dbf1fcc-7971-3b13-982f-fa8308d2f09c | -6.76623 | -44.82858 | 2024-12-12 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caeca736-55aa-30a5-ae57-3152b66a579a | -6.93198 | -43.54405 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 926678e1-e656-3db4-9710-54e48baf97b9 | -8.39271 | -41.82914 | 2024-12-12 04:16:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f2b60ae3-7a54-3265-8c73-8bdbc4ffbc6b | -11.11627 | -54.65688 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf4105c7-a92f-3c39-b9b3-94e8abf664bb | -11.11991 | -45.29172 | 2024-12-12 04:16:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96061d7b-b832-3d48-b5a9-67f2a5684e68 | -7.86341 | -35.15273 | 2024-12-12 04:16:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4aaa3bd5-7f62-39e2-9efa-c0e5c4412a54 | -10.45516 | -45.06363 | 2024-12-12 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 772983dc-1df2-3239-9248-ca8450144264 | -6.98103 | -42.81386 | 2024-12-12 04:16:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b034bdc2-ba96-38ff-bf2a-73042b8d3a2f | -6.92308 | -43.51433 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8058d6f9-b68e-3e60-9073-20553b3b37e0 | -12.10968 | -44.752 | 2024-12-12 04:16:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 945d795f-593c-304f-8b64-415d3f9ce6b8 | -9.23596 | -46.66912 | 2024-12-12 04:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1eb2bce1-9125-3581-bd84-f41c1018146c | -6.9336 | -43.53368 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ee39068d-dd69-3180-b763-0bf3691d981b | -5.92187 | -48.06228 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7efca66c-f156-3a76-9b7a-5986d8c9579f | -13.17775 | -43.57156 | 2024-12-12 04:16:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd9b85fe-e5ed-379a-a585-75767f069a95 | -11.19982 | -53.8187 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c67648bb-36ad-3076-b0bc-74c78e69bc77 | -6.7696 | -44.82908 | 2024-12-12 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c3abed5-9181-3b67-8df2-3de8e818651a | -10.8365 | -44.43469 | 2024-12-12 04:16:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4472b894-60ac-3bb9-b32f-feec4aee929a | -10.59402 | -44.98168 | 2024-12-12 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7414e5d-0405-374e-8241-560a57e4f93d | -7.79284 | -35.13627 | 2024-12-12 04:16:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 90ae73fa-729a-35cb-b9fa-79589cf1eaf2 | -9.78984 | -36.21932 | 2024-12-12 04:16:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 94aa2d7b-cbb2-36b0-88e1-90e12a39d70c | -11.20154 | -53.8265 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 119578c4-5aad-3b71-a530-4f304cbe6b94 | -11.45138 | -48.00528 | 2024-12-12 04:16:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4bc965ad-08af-303b-a0b4-e0adfd12974e | -5.92585 | -48.06291 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9f535212-416f-37b9-858e-d27f5e355911 | -8.11772 | -35.07079 | 2024-12-12 04:16:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 02db552e-4fd0-3179-9237-dfa9d76be3bb | -6.91869 | -43.52073 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4a17aaf2-6892-3a84-870f-a0b572850c91 | -6.77297 | -44.82959 | 2024-12-12 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33ea224b-09b6-3810-a756-e42e0e3a4201 | -10.02351 | -47.56154 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fd20d3e-a7e0-3724-8e27-d0eb8a1d2ea8 | -6.93744 | -43.53074 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efe3d1cf-112c-3548-bcae-fba62cf69bc3 | -12.26155 | -49.3219 | 2024-12-12 04:16:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c948039-0e14-3c36-a6d1-95837d663687 | -6.94405 | -43.53177 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddcb1bbb-d4c5-34f6-bd62-4852f1943cad | -11.20755 | -53.82402 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cddd0ff9-7160-3bea-9d18-d138d0efe46e | -5.92671 | -48.05774 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 2411bcbc-6570-3746-a474-697c7cd17323 | -11.20142 | -53.8399 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3491410-ed25-3a15-97ec-2955d2312e9f | -8.64367 | -46.05595 | 2024-12-12 04:16:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)
