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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4945303d-0b25-3349-bfd1-58bded5a01c5 | -6.89877 | -42.41551 | 2026-08-05 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5417f38e-62f1-3dd2-bbba-b6d8eff8eb7a | -12.20081 | -45.278 | 2026-08-05 11:38:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c5c739e5-7c3a-3ef6-ade2-8177a5e6db08 | -7.9967 | -44.17489 | 2026-08-05 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 808092e3-2e14-35ee-809f-dd4560e56b08 | -6.85643 | -44.86707 | 2026-08-05 11:38:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9742820d-4c2e-3e45-a175-57ae64b7c087 | -7.63268 | -45.3044 | 2026-08-05 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c765f89b-e796-3827-9906-b6ff16543a6b | -12.2021 | -45.26896 | 2026-08-05 11:38:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4aae420b-3e5b-308e-83c9-ac4bfc32d8ae | -10.61349 | -46.37885 | 2026-08-05 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7a85f630-aef9-3794-ac49-663dce4579f5 | -6.35209 | -43.41639 | 2026-08-05 11:38:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ad2428b4-a37d-369a-9682-a434517d1efc | -6.98351 | -42.12237 | 2026-08-05 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| 7c7c606a-902b-3374-a343-6b15fe55d65f | -7.21744 | -43.35813 | 2026-08-05 11:38:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e87c9fe1-069a-30fd-bf65-bab214463a19 | -6.90546 | -42.41261 | 2026-08-05 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 52b8580e-2074-3eb1-ad00-6089840cfbea | -6.90682 | -42.40262 | 2026-08-05 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| f78d7389-2196-3967-ba4a-11d59e5a2b2c | -12.03617 | -42.5482 | 2026-08-05 11:38:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2d4d41dc-880f-3e38-8f21-9c842fbbfee2 | -7.23319 | -45.76537 | 2026-08-05 11:38:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 50789044-8aa3-301d-b3ae-4510a7639c3e | -7.4518 | -44.889 | 2026-08-05 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 96f3ae7e-ee17-3f97-8b37-707c1b0500ad | -8.34699 | -45.97792 | 2026-08-05 11:38:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 02718674-b5cd-3e96-9797-ca80b6fbc3ec | -6.89383 | -42.83936 | 2026-08-05 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 55921e4d-9ac7-3588-afbf-406a86d04057 | -10.27582 | -46.35121 | 2026-08-05 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4021efed-209a-3d66-b0ca-dc77308db199 | -7.23186 | -45.7745 | 2026-08-05 11:38:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 655d00bb-523d-3fdd-abb5-acf39484ca24 | -7.63139 | -45.31331 | 2026-08-05 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ae06488a-790d-37a6-9990-81359083341e | -8.49203 | -46.86687 | 2026-08-05 11:38:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f6a8ff51-0559-3dd0-9a5d-18d42685bfe8 | -6.65072 | -43.91263 | 2026-08-05 11:38:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 847adeab-25b4-3ba1-8544-f51a9298bbd3 | -11.30351 | -44.78472 | 2026-08-05 11:38:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc615c48-ced6-356b-8c37-9e2d4557b928 | -7.45053 | -44.89785 | 2026-08-05 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad74fced-12a7-3dba-9757-bfa8bcae42ac | -6.90017 | -42.40554 | 2026-08-05 11:38:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 0b85a028-36e5-30a2-9252-e4f60aa8cf4d | -6.13831 | -47.71861 | 2026-08-05 11:38:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| add93840-aa8c-32e3-aa7b-a5590d136794 | -8.02052 | -45.04911 | 2026-08-05 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9d24df08-3760-3317-ab3f-26853a20757d | -8.49353 | -46.85687 | 2026-08-05 11:38:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 85ba6732-52f8-3327-9ebe-a96108c3a433 | -7.00259 | -44.93013 | 2026-08-05 11:38:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e5ea333-0c75-35a6-9914-92225d4268c9 | -6.65198 | -43.90372 | 2026-08-05 11:38:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d8dc7b0f-807e-3331-9733-55c081a4a5f6 | -8.34564 | -45.98706 | 2026-08-05 11:38:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 89c3112a-f66e-3bc0-af8d-4ee6ceb6fd59 | -8.35594 | -45.97918 | 2026-08-05 11:38:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 2e04d862-e318-3896-adaf-c3ca64016b9b | -12.20338 | -45.25993 | 2026-08-05 11:38:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0cfb8ba-3e8b-32f7-929e-ee8c0e8e0b34 | -10.61214 | -46.38803 | 2026-08-05 11:38:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1aba677b-dbd9-3000-8900-10ad3b71f355 | -8.0218 | -45.04026 | 2026-08-05 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 457f5ac8-e8c8-3246-bb1a-2389b1f7c1c0 | -7.99543 | -44.18382 | 2026-08-05 11:38:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 63165d90-f312-32ac-bdff-7f3ea66d9eb7 | -14.2682 | -45.287 | 2026-08-05 11:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b74c3ab8-1f9f-3f19-9302-59818be33bbe | -14.73715 | -47.13979 | 2026-08-05 11:40:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4ee27fb4-f826-32ec-86cc-b42461e69d82 | -12.58574 | -46.95929 | 2026-08-05 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e418551c-cab1-332e-a23c-3e8484968154 | -14.26446 | -45.28915 | 2026-08-05 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 27f65b14-7ac0-3894-9dff-bf08e9ea50e9 | -16.36546 | -43.69539 | 2026-08-05 11:40:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7419cc26-3b88-39d0-b021-97f9d4a49bcc | -13.99208 | -45.91578 | 2026-08-05 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67a5e3ff-c92b-354c-a4a2-90c3bd3c8dc5 | -15.1436 | -42.1522 | 2026-08-05 11:40:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| eb12a40b-d166-3eb8-98c2-bcd3e7e2fc15 | -12.43198 | -50.52513 | 2026-08-05 11:40:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 729f2c69-d671-3130-8d18-da3386fd3497 | -14.35837 | -47.51556 | 2026-08-05 11:40:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 50e8c7e8-6fa4-3f8a-956e-9fca9e56b9cd | -12.59332 | -46.97014 | 2026-08-05 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2eba594a-9f6c-38ef-bb42-cfd921ffabb0 | -12.59469 | -46.96082 | 2026-08-05 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 2683f1f2-c0bc-3eea-98d4-90a82ccd7011 | -13.99337 | -45.90674 | 2026-08-05 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9120930e-2ebf-3f6f-86d6-1eabbe289610 | -13.21951 | -46.22221 | 2026-08-05 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8f6c75e5-dc27-33f7-8bf1-6fd868bdee99 | -16.5303 | -41.2579 | 2026-08-05 11:40:00 | TERRA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 5f1ecfce-e7ae-3938-a312-f9161ea91555 | -14.26318 | -45.29836 | 2026-08-05 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 2e3da79c-088b-32e5-8a02-ffb1f4bb55c8 | -12.44162 | -50.39192 | 2026-08-05 11:40:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c73ad118-1bb8-379e-86cf-d6cfc247630e | -14.25556 | -45.28787 | 2026-08-05 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 289afec8-dd5f-3ea6-991c-1936a7dceb2a | -12.43205 | -50.5313 | 2026-08-05 11:40:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7083f6ef-bc32-3df1-9f52-73e831b7c957 | -12.44389 | -50.37751 | 2026-08-05 11:40:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d38ed92b-f02d-3336-bf62-70bed38ae5de | -13.37598 | -42.43965 | 2026-08-05 11:40:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 9fe8f739-4b0e-3079-993a-7b0e27c0a96c | -14.43136 | -42.15714 | 2026-08-05 11:40:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 28b0a678-843d-3e11-8f07-a74f3c86cf38 | -14.89729 | -41.35151 | 2026-08-05 11:40:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| cf524431-be03-3ba1-a579-10d264d4eb2a | -11.17079 | -54.9052 | 2026-08-05 11:40:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 49799bff-4d49-3b00-b650-2a28f0b66489 | -12.59744 | -46.94208 | 2026-08-05 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e7832a00-e6bf-3174-ab4e-67294c55176a | -14.25428 | -45.29708 | 2026-08-05 11:40:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d6f91be1-f9fb-3a5c-9c49-7ff036144338 | -11.17686 | -54.87096 | 2026-08-05 11:40:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 4abc1acb-7407-3e66-a8d8-591583bb72c4 | -12.57812 | -46.94873 | 2026-08-05 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 23f7ee28-9d0f-3d34-bc60-b03cd6d0b098 | -12.59606 | -46.95151 | 2026-08-05 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 73476adc-6b85-3e07-b045-c84e548dda9c | -14.17143 | -54.40213 | 2026-08-05 11:40:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| adb78f39-95fe-35b2-83a9-413ed52b79df | -12.49667 | -45.53786 | 2026-08-05 11:40:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b3ec3dcf-1c96-3adb-b09d-2dd3cbb0a0e6 | -14.42969 | -42.1704 | 2026-08-05 11:40:00 | TERRA_M-M | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 0587c224-0d01-3a45-a4e7-7b55f20030fa | -12.59118 | -46.9223 | 2026-08-05 11:40:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 60c3ea5f-27d6-3e69-810a-97567e26825d | -12.43448 | -50.51657 | 2026-08-05 11:40:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| be3afb0d-559a-37d0-8165-0c8d9579726f | -12.4343 | -50.51038 | 2026-08-05 11:40:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d8c5307b-25f6-3c11-b7cc-458c5c8b23cf | -21.65274 | -46.38182 | 2026-08-05 11:42:00 | TERRA_M-M | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fe655f41-0a1a-325b-a574-06539f05b62a | -17.55159 | -46.54482 | 2026-08-05 11:42:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f9b4156-1b2d-30d2-badd-637a9cfcd605 | -18.84777 | -47.92192 | 2026-08-05 11:42:00 | TERRA_M-M | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 590889e0-95fc-3ef4-974f-b2f32f132974 | -19.99697 | -44.25228 | 2026-08-05 11:42:00 | TERRA_M-M | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 2f896723-c879-3af4-9eaf-e4a7dbaf7332 | -17.9901 | -47.15744 | 2026-08-05 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5734e8d7-82d7-3bbf-b333-6c046ffd6c7a | -22.85129 | -49.35101 | 2026-08-05 11:42:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e12b9c35-0f43-34f6-95f3-b20cbd338322 | -20.90003 | -44.91619 | 2026-08-05 11:42:00 | TERRA_M-M | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.6 |
| 975e4549-abee-36a5-9922-ae9094f68f67 | -16.09759 | -48.52928 | 2026-08-05 11:42:00 | TERRA_M-M | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 495432cc-5e72-38c6-9e00-c96a314cfc02 | -17.99143 | -47.14822 | 2026-08-05 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 66ee2597-bd3a-3e77-bdc9-525fba93631a | -20.90147 | -44.90506 | 2026-08-05 11:42:00 | TERRA_M-M | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.8 |
| 4b3e3a9e-ba66-3622-94d2-410195fe6372 | -20.04368 | -47.16562 | 2026-08-05 11:42:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 562df5aa-8a7f-3fbf-a94e-1bcf439bc994 | -18.84916 | -47.91253 | 2026-08-05 11:42:00 | TERRA_M-M | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2915fcb5-5ae8-36c0-9e12-aa44b5ae91d6 | -22.88792 | -46.28736 | 2026-08-05 11:42:00 | TERRA_M-M | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 38414aff-5010-33a6-827b-91a6874cff11 | -18.73966 | -47.46242 | 2026-08-05 11:42:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 24f40a92-4430-38c3-9e53-38826b0e6c19 | -22.75373 | -46.39624 | 2026-08-05 11:42:00 | TERRA_M-M | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 76180768-1531-38e8-a188-d8a1b0a95575 | -21.59864 | -46.30632 | 2026-08-05 11:42:00 | TERRA_M-M | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 4de66c0e-7430-3564-a6cc-4c0fa831b736 | -19.57029 | -44.73355 | 2026-08-05 11:42:00 | TERRA_M-M | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 04a0f33f-770b-3fe0-9c8b-6337b3cb5f76 | -16.09915 | -48.51914 | 2026-08-05 11:42:00 | TERRA_M-M | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1e399341-9b2f-3924-8430-8d4825fd75b4 | -18.00026 | -47.14956 | 2026-08-05 11:42:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2360efd-e085-3c35-b44a-1293d296c078 | -22.84979 | -49.36096 | 2026-08-05 11:42:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9701970d-9e8c-3f1e-b9c9-7372c6104933 | -17.71719 | -42.33821 | 2026-08-05 11:42:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4f07afb9-9e68-34ab-a73d-ce47b939901f | -24.08033 | -48.33089 | 2026-08-05 11:45:00 | TERRA_M-M | RIBEIRÃO GRANDE | SÃO PAULO | Brasil | 3543253 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 156a8a26-fb88-3043-b90a-a1a63fc8f138 | -14.2682 | -45.287 | 2026-08-05 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 6d68e466-1250-335f-b2f1-b5157f57869b | -6.9879 | -42.1201 | 2026-08-05 11:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 04621d6c-647e-3ea3-aa6c-cb7641994079 | -11.1642 | -54.9007 | 2026-08-05 11:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e1c0f63e-5c1a-30da-b50e-4db5520d4815 | -12.5942 | -46.9527 | 2026-08-05 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6448d0e0-14d5-3f4a-b653-5d8ba63ba175 | -11.183 | -54.8991 | 2026-08-05 11:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| fac775d7-613d-3113-ba69-957d22c808f9 | -11.1642 | -54.9007 | 2026-08-05 12:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d891a69f-b9fd-3081-9637-60317d6a6683 | -13.2413 | -54.2683 | 2026-08-05 12:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 7bc4138f-6866-3036-91cd-029fee5e4c14 | -10.6181 | -46.3872 | 2026-08-05 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |


[Clique aqui para ver as próximas entradas](README30.md)
