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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67eef8f3-eb6a-3326-b7d3-7054d4e022fb | -4.36847 | -47.7663 | 2026-08-01 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8cc506f7-145e-34fc-a818-7930aca81528 | -8.96662 | -45.20046 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71af0345-b3b2-3d88-94a8-33d6f09eebff | -8.38313 | -48.21256 | 2026-08-01 04:55:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5e8a3ff-2366-3965-9f3c-e47153d9d7c1 | -8.9768 | -45.17035 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c943a4f4-1970-39fd-9cd3-b77f82a39fe7 | -6.56812 | -56.5346 | 2026-08-01 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5a852ac-abdb-3c63-bf1c-1b412918fb85 | -4.6136 | -49.0551 | 2026-08-01 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba154831-2434-3e72-9e7d-e7e523c42ba9 | -7.24968 | -42.13848 | 2026-08-01 04:55:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c47fa3d-bebf-3f00-91fb-f577c47d18a6 | -7.23298 | -43.42539 | 2026-08-01 04:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0890f41-329b-38d3-95fa-eb3c4cd1c53c | -7.835 | -47.09413 | 2026-08-01 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 909e8e67-f19c-31d9-9299-3be4a4e5545a | -7.29769 | -55.31927 | 2026-08-01 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5c4fe8b5-9240-343c-9d42-3dd3d5ec65c3 | -7.49135 | -46.11946 | 2026-08-01 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5192f042-6242-3e8f-8f9b-49ae7b9bd77a | -5.8124 | -44.76081 | 2026-08-01 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72226bb5-07be-32b3-99b2-7c38a7f5fb07 | -2.89024 | -48.02135 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c6e60ed9-1b06-3750-a9f7-551d2734f723 | -6.56542 | -55.14257 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59895a2b-32f4-32c3-b3ff-ed18965cc428 | -6.71697 | -44.01151 | 2026-08-01 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58f1ddd8-bdd9-3bb4-80fa-7a7eb2360b44 | -6.65252 | -43.91352 | 2026-08-01 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ca850a3-35c0-3e1f-be46-30809bf2310f | -3.72838 | -49.27205 | 2026-08-01 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59fbb6f0-1f81-3af8-b0ea-c0d2806df593 | -4.93319 | -41.98405 | 2026-08-01 04:55:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1c2954e-7484-3302-adf0-b9c785f1f9fd | -3.10946 | -47.91089 | 2026-08-01 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b91190aa-96ed-3896-8e0d-fa109560dfbc | -4.61701 | -49.05561 | 2026-08-01 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b7af1da-a435-394b-84c9-a87b7d6f35fd | -7.83891 | -47.09465 | 2026-08-01 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55bf9142-4812-3266-80e7-8c20581d78e6 | -6.66996 | -42.56678 | 2026-08-01 04:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aae8df1a-e9c5-3ad5-a613-ac26d13593c0 | -5.81742 | -44.75718 | 2026-08-01 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54c92dbc-4705-364f-8800-eb6a6855afc5 | -6.6738 | -42.57038 | 2026-08-01 04:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 060cd38d-085f-350f-bd30-78af27ccbff5 | -6.56075 | -55.16838 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32647540-acdb-3890-894f-ca65670e5acb | -6.27615 | -41.87383 | 2026-08-01 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f3f5a210-426a-3411-9ab5-7c0f1a0f6f73 | -3.85311 | -44.09452 | 2026-08-01 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65553454-9249-3c9a-bed9-b22664ac4ff2 | -3.85244 | -44.09887 | 2026-08-01 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1aefb427-091c-38c2-ab43-a7399b34b7d4 | -6.54432 | -55.15327 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ae973f7-e044-3e3b-bbc5-07667ddc86d9 | -5.96581 | -51.39859 | 2026-08-01 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3c9a956-23b2-31e5-a9db-076e90f35430 | -6.76159 | -41.01713 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa57d93a-23aa-3b1e-b80f-59b266895765 | -6.60862 | -44.67095 | 2026-08-01 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcf80b3f-807f-30dc-9e43-a071bd21d085 | -7.77402 | -44.07417 | 2026-08-01 04:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7706232-e2ba-353e-84d2-3639fd60f64a | -6.55791 | -55.16491 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75ad8e92-c82f-3a8c-9458-231d5a106cf1 | -6.75721 | -41.0083 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aaef505c-30ee-3a6d-ad1c-7879e3844ee1 | -8.97583 | -45.16842 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 153ccf9d-63ca-391c-b07f-5f2f16bebe1c | -6.5653 | -55.1644 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5500f5e4-6e65-33aa-a47c-2757f918c2c6 | -6.18275 | -55.52753 | 2026-08-01 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f0e7a3d-4c89-3dea-af61-9cad7090e682 | -2.89084 | -48.0175 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2d98b794-9bb6-3730-9fad-301ff6dae1a1 | -3.96664 | -48.12453 | 2026-08-01 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cfb89f8-ccdf-3413-b0a8-d0ba0f547964 | -7.03892 | -43.21218 | 2026-08-01 04:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d524e854-7b49-3246-ad7c-11b48e7ac396 | -7.64997 | -45.0513 | 2026-08-01 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec43f7d3-03bb-3d93-8718-0c259dfc2ef7 | -3.85759 | -44.09523 | 2026-08-01 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ce3ebfb-82c2-3c0f-8026-045917f66010 | -7.00979 | -45.84879 | 2026-08-01 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 311fccd1-d222-3936-ba6d-07ef255b421a | -6.56317 | -55.15636 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7b69abe0-367c-311c-8651-f8915a5a68c8 | -8.96906 | -45.19358 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fdb2f7d-2dca-38e4-88cb-b4d3696d4d63 | -4.65696 | -42.43449 | 2026-08-01 04:55:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b5650ea-f24d-3aec-bd73-dba784147df4 | -7.29802 | -55.31683 | 2026-08-01 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b7ebabfe-17c0-3ada-bdf8-45d689cc2617 | -6.55866 | -55.16031 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6e3b05ec-5a48-3d10-b1c6-5e233d3cbb99 | -7.19552 | -42.9644 | 2026-08-01 04:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9351da8-12c4-3731-8ccb-561635b87310 | -7.5472 | -43.99156 | 2026-08-01 04:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36362a00-eed1-3701-94d0-6a2687a4fcb8 | -4.27303 | -48.19294 | 2026-08-01 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 834882c3-7c77-3f89-8708-97e7a40a160d | -6.76355 | -41.00517 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be943e13-6cfa-3c8f-8c6d-afe6302f9687 | -3.85692 | -44.09958 | 2026-08-01 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0262e13d-3cfc-37fe-962c-d800578f9c65 | -5.76648 | -47.34298 | 2026-08-01 04:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f84edd37-22e4-3ee3-b7a9-1fd228d86248 | -3.11588 | -47.91591 | 2026-08-01 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b489916-ba40-34dc-9ef5-ba9eed243208 | -4.61018 | -49.05458 | 2026-08-01 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f970249-ea89-3623-8be7-c90ed1623e7d | -7.83859 | -47.09713 | 2026-08-01 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7289171e-62b2-3c0a-b2af-99a1b868a6b2 | -6.10364 | -55.80754 | 2026-08-01 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8053f85f-195c-3f69-b4fb-56abdcb8541b | -3.72782 | -49.2756 | 2026-08-01 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 392c7730-209d-307a-93b9-c5d280d2fc6b | -3.04948 | -48.74249 | 2026-08-01 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ada51b8-4c29-32d4-9bb4-839bfa84d71a | -6.56467 | -55.14721 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4be92080-5a63-31bd-a1d5-66f514332a2a | -8.34072 | -45.98686 | 2026-08-01 04:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54dfdf76-9422-364d-aa0f-24bc09a5cf47 | -7.64615 | -45.04626 | 2026-08-01 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07c44b3a-8f60-3ade-8666-dec892e91f3b | -6.17749 | -55.52937 | 2026-08-01 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd150039-5003-311a-ab05-fd1e67e18f47 | -3.05603 | -39.92662 | 2026-08-01 04:55:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ab3b8cb6-09f7-3e98-9747-db670463121f | -3.11358 | -47.90751 | 2026-08-01 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f7923599-871f-33ed-96fd-d2243ec8303a | -7.00923 | -45.85258 | 2026-08-01 04:55:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6c71858-5dec-3bea-b5f7-e3055b05b64f | -6.27567 | -41.87725 | 2026-08-01 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4a1a5b4e-ac71-38f2-83f0-756e633f187c | -2.16324 | -47.87096 | 2026-08-01 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65bc515b-5069-3642-a669-a681d5f64a1b | -6.09968 | -55.80692 | 2026-08-01 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce013cc2-7aee-3b3d-a236-32050281c89c | -2.32826 | -47.20311 | 2026-08-01 04:55:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03a72711-f3f6-3761-8711-dad6d82e4aa9 | -8.37947 | -48.21196 | 2026-08-01 04:55:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7187f49-2533-335d-9a4b-85dedaf0ef0c | -2.88675 | -48.02081 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 34546ef4-a932-3951-97c7-ec3a456225d3 | -6.76185 | -41.01722 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 044433cb-c933-390e-892a-dce184d0a681 | -7.23404 | -44.53442 | 2026-08-01 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d1018c7-dbfc-3adf-af31-76d1d38567bb | -2.81749 | -60.00382 | 2026-08-01 04:55:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ff6a53f-ec2e-393c-9d58-4a57cc5d3e68 | -5.55832 | -43.96595 | 2026-08-01 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1972d955-3740-381b-b494-654e2b261ebf | -4.00082 | -43.29072 | 2026-08-01 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17a89abd-1b24-3b25-a4a5-015f188421d2 | -2.72402 | -49.78885 | 2026-08-01 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fe35b3f-ee00-30d7-a728-cb9d23c67cec | -8.97178 | -45.19646 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28059c05-7fa0-305b-93dd-4d8da7f7fad7 | -6.56243 | -55.1609 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fdf903cf-9e8e-3a3b-bee7-66964124a9e7 | -6.2663 | -41.86519 | 2026-08-01 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 144c5d08-7ea7-3de0-96e1-b6ca2ce925cf | -3.05346 | -48.73936 | 2026-08-01 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a138cf44-ea6d-3827-b964-609f5bbdf6c0 | -7.01396 | -45.84946 | 2026-08-01 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55c27cc9-63b1-3e67-ad8b-71bffa264451 | -5.31735 | -47.48455 | 2026-08-01 04:55:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa4766c3-8927-3179-9103-499dae596b7d | -5.81322 | -44.76208 | 2026-08-01 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bf6f926-1486-3492-af31-2202647cb8e7 | -14.07521 | -46.242 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f7836fa-442c-3822-b0d3-0aae3ffe4476 | -14.35663 | -48.0358 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a96412ba-e4d2-3dcb-8c15-d2d0ed2a3110 | -12.20728 | -52.8681 | 2026-08-01 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75ab1901-3b07-34f4-9f87-fa87f19798df | -14.08017 | -46.25905 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d6c745a-e2fc-3228-8b23-cad87af90a79 | -12.80934 | -47.17639 | 2026-08-01 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7697d4a-8686-3a4c-bc56-542e1d1c7e23 | -9.47923 | -57.32096 | 2026-08-01 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df30bdbb-1d05-32d8-9285-a8c320e846dd | -12.61201 | -44.60813 | 2026-08-01 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c59a7a4-6ca3-311b-8e54-03aa268cce19 | -14.07061 | -46.26211 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ff07292d-04f6-3448-961f-720346262a2b | -14.07686 | -46.26513 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c949615f-b795-357a-bd5c-61a300d90d7d | -16.04599 | -48.52993 | 2026-08-01 04:57:00 | NPP-375D | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4fa13393-de8f-354c-9195-bfb6045f245b | -14.35191 | -48.04026 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c704e11f-a178-309d-9fef-3213c4cd9f1e | -9.88319 | -48.7342 | 2026-08-01 04:57:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03be88b0-bc69-3bdd-aac9-426a769cff05 | -9.10668 | -49.64598 | 2026-08-01 04:57:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
