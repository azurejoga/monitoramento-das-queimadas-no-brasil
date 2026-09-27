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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42138f5e-4557-38ff-948b-24b9ce6c17b4 | -12.7221 | -47.3161 | 2026-09-27 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 45a9263e-c77c-3cad-a115-7da7791cccfc | -6.8408 | -43.5021 | 2026-09-27 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 285.0 |
| 76f924a9-0290-3418-ad2c-7460b5e2d4f2 | -7.3653 | -42.1058 | 2026-09-27 12:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 91ba2bab-f7d9-3277-b49b-ba490b9d2d7c | -12.1366 | -50.3112 | 2026-09-27 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| a3caef84-d330-3604-ba23-18910ac0418e | -12.1362 | -50.3328 | 2026-09-27 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1274a336-84d6-3f4e-9462-150d99303da2 | -6.8405 | -43.5254 | 2026-09-27 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 1428d0a6-cc03-3463-a1b1-c0b493785d77 | -12.2307 | -50.3858 | 2026-09-27 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| fad86c00-45cc-3526-a22c-980271b0d852 | -12.1175 | -50.3135 | 2026-09-27 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d7ca5d41-4ac5-3312-8e29-997065457b3b | -11.905 | -50.5103 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 2eb81f34-0429-3247-8050-2a68a4e4ae2a | -12.0178 | -50.6041 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| dc37292e-9cdd-354b-88b8-baee8779b619 | -7.365 | -42.1298 | 2026-09-27 12:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 865ebd9a-a931-363f-8376-0bf8d6bd8d88 | -12.2639 | -50.7034 | 2026-09-27 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a7530716-ff02-368c-a1cd-33534c9784de | -12.1175 | -50.3135 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 9ed6de1a-f612-36ba-a665-190e49de1f61 | -12.2307 | -50.3858 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 2e9aa52e-7d70-3299-b4aa-fb875318180f | -10.0159 | -50.1588 | 2026-09-27 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 53ea1cd6-46e5-3e41-973b-7620bb5fccd3 | -12.1362 | -50.3328 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 7be66005-6153-3fdd-bfa0-5fef7f0fbd79 | -11.9053 | -50.4888 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3beb27f8-7d9b-3406-ae34-e870d995f3bb | -12.1369 | -50.2897 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| dd68031c-012a-3e37-9644-be8c049f5f55 | -10.0162 | -50.1374 | 2026-09-27 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| a1d9e1e2-ce4a-34f0-9019-f97912b415ee | -11.8862 | -50.4911 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2d306447-c24b-39ee-a62e-a0f0be39cbcb | -12.7028 | -47.3189 | 2026-09-27 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| def989c9-28de-32b9-abc6-f62002745af9 | -10.0909 | -50.194 | 2026-09-27 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 84cd8eea-e395-3a92-9e81-af6823810fcb | -12.1557 | -50.3089 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b1a070de-2f60-3fee-a4cc-4a1cad38044d | -11.9244 | -50.4866 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e2c36756-965d-3caa-bc82-ec742d92d191 | -10.072 | -50.1959 | 2026-09-27 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 583af5a3-f14a-3812-9a5b-381a11b6e255 | -12.1366 | -50.3112 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 40959ff3-5d91-382f-9d68-e99cda5df66d | -12.2643 | -50.682 | 2026-09-27 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 3dfb63e7-170b-3748-a8a8-9338f3cf39c4 | -6.8408 | -43.5021 | 2026-09-27 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 288.9 |
| 480adf7b-539a-3b53-b64c-8f7a94137db5 | -7.3653 | -42.1058 | 2026-09-27 12:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| bafd2158-bbbf-3254-a5b0-783091fa6a89 | -6.8405 | -43.5254 | 2026-09-27 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 53fbc605-8d3b-3ab3-bf01-a24bbaace452 | -12.2448 | -50.7057 | 2026-09-27 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e0515d38-22ab-35d4-9041-a77d8a35db27 | -11.924 | -50.5081 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| aaaa41fb-a240-36c4-965e-abbd1cc1f1b3 | -11.8859 | -50.5125 | 2026-09-27 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5c9f8790-f940-32fb-b2d1-07c11a2f81ed | -12.0178 | -50.6041 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f281ac8b-f37d-3c15-8f8a-83cf605fd37a | -10.0531 | -50.1978 | 2026-09-27 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 43351f7f-aa1d-3eb6-9566-f7cb71f38253 | -11.7329 | -50.573 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 141a73dc-6240-3c68-9a1f-6e023d4ceb03 | -20.2029 | -46.1918 | 2026-09-27 12:50:00 | GOES-19 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e77d609b-de82-3d90-a641-25c339466a12 | -11.7141 | -50.5538 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 65f9a768-a01f-3075-8207-0509e3aad4ad | -12.1366 | -50.3112 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1b007890-68bc-33c3-b05a-3ddac0e627d4 | -12.2311 | -50.3643 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9a3f54f7-58da-3aa0-a5dc-ce3a3b9a08ca | -12.7221 | -47.3161 | 2026-09-27 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 8aa5eebb-3f28-34aa-aa68-38cfa30b0460 | -10.072 | -50.1959 | 2026-09-27 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a2c80c48-2a54-3768-b4c8-1e6968c25355 | -13.9103 | -42.1126 | 2026-09-27 12:50:00 | GOES-19 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 15c9192a-3b2c-3df8-a57e-1fcc7aab8e0c | -8.3583 | -44.187 | 2026-09-27 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 023313d3-3cff-35f7-a8ba-c8935536a497 | -6.8594 | -43.5237 | 2026-09-27 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 71e76393-879d-3608-a121-4e013fb710f5 | -7.3653 | -42.1058 | 2026-09-27 12:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 99e9354c-895c-3c84-9e26-29435ad0e613 | -12.2257 | -50.7079 | 2026-09-27 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| aa8e5fab-2780-352b-9d3e-727625631bde | -13.9108 | -42.088 | 2026-09-27 12:50:00 | GOES-19 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 99.0 |
| e4189acb-c145-3c18-b4a2-44eb0248475b | -12.2643 | -50.682 | 2026-09-27 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 0521f0c7-8ce5-32e3-8214-edcb685887c9 | -8.3422 | -45.4487 | 2026-09-27 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ef98cebd-4148-368e-9c58-abbec19ac0d7 | -8.3778 | -44.1386 | 2026-09-27 12:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 60e722bb-e308-3a26-8528-03f4cd49af87 | -8.3589 | -44.1406 | 2026-09-27 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 497.1 |
| 1e37a8e3-b7ea-31ce-b3b4-b06e88e16f00 | -12.1362 | -50.3328 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 07756325-cb27-3732-9cc3-82e23c1dc49b | -7.3842 | -42.1039 | 2026-09-27 12:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 5b992f7b-6137-31ac-ad01-fe29d2303528 | -6.8596 | -43.5003 | 2026-09-27 12:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d19d5130-14f2-3342-b38a-3b00ac2c4e60 | -10.0717 | -50.2173 | 2026-09-27 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1d35a10a-66b4-3b00-ad13-18ec6872ef13 | -10.0909 | -50.194 | 2026-09-27 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 944a5d4a-e773-36e2-8c76-0c5f51648614 | -6.8408 | -43.5021 | 2026-09-27 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 193.0 |
| bd0f2235-2bc6-31d4-9074-c4c78ef5e044 | -12.2495 | -50.405 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 769f6de4-2af8-3765-a754-c2f66ac4ed48 | -6.8405 | -43.5254 | 2026-09-27 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 5fdb0858-ff4f-388a-bbce-380c79a543ad | -7.365 | -42.1298 | 2026-09-27 12:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 14f164a7-c8c8-31a6-8119-8a73338a2895 | -12.1175 | -50.3135 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 83121ec5-7f0d-3922-a2d6-5f65124b8154 | -10.0162 | -50.1374 | 2026-09-27 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b701df5e-7b84-3742-996c-c4f5586bdd3d | -10.0159 | -50.1588 | 2026-09-27 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e7f8ed8e-1224-314b-ac24-1bb1d984246c | -12.2307 | -50.3858 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 184.8 |
| deb67b20-7725-34a0-a18d-d8daf6a2e58c | -11.9619 | -50.5251 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 386f9cc6-db48-3fcf-b8af-295f966aaf54 | -12.2834 | -50.6797 | 2026-09-27 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3ff76803-de7e-3969-9894-b73cecae5cf5 | -11.1181 | -51.1091 | 2026-09-27 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f1e899cf-18a6-3690-9020-eaad8b53a437 | -12.2498 | -50.3835 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9d541214-1e66-3731-b532-a45ab5cf84c1 | -12.2304 | -50.4073 | 2026-09-27 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9500b679-f04d-3641-be32-10cea1a05302 | -10.0906 | -50.2154 | 2026-09-27 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4599877d-2ccd-369a-b0ea-0d1f54cb8baa | -8.3586 | -44.1638 | 2026-09-27 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 830.4 |
| 19052323-1cd3-360e-b0a7-487f74d97319 | -12.2307 | -50.3858 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| b07e2ec0-10ce-3e32-bcc0-4cd4b5a55a3f | -6.8405 | -43.5254 | 2026-09-27 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 256.0 |
| 4b83c9e8-3ad5-3a24-b89d-900ef3256e5d | -12.2448 | -50.7057 | 2026-09-27 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5bfe115d-ac17-31a0-a475-f32d7c50c772 | -10.072 | -50.1959 | 2026-09-27 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4410c3a7-cbfc-3e3b-a16c-0b2c8b64ba9d | -12.1175 | -50.3135 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 018d3597-aa13-3112-aadf-3cc8373e9239 | -11.9968 | -50.7349 | 2026-09-27 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 97aca3d9-9697-3ce1-82f6-4d8d519f6398 | -11.0235 | -54.0354 | 2026-09-27 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f1a39aa7-630d-362d-b393-2b8e1a6233c7 | -10.0717 | -50.2173 | 2026-09-27 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a5e6268e-4ad8-35a5-9ed5-157a7e6b8676 | -12.1362 | -50.3328 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 594a7f2d-a1e8-39b3-bc29-01ffd4618ffa | -11.0619 | -52.4812 | 2026-09-27 13:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 140c99a1-9e05-3ff9-a27c-887ed3b9b7ce | -12.0178 | -50.6041 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| ba9e515a-d97d-3b24-b27f-d3900321d5e0 | -12.7028 | -47.3189 | 2026-09-27 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| f93b58f6-1fd5-3343-aa51-3eacadbbe3d0 | -12.2257 | -50.7079 | 2026-09-27 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0c3f23f4-51cf-3148-8c76-986e45d65c8c | -12.1171 | -50.335 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8ccbb294-daa3-3247-9366-7f8ecf97e7bb | -11.9396 | -50.7415 | 2026-09-27 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6abe4c6d-4a4e-3013-991b-ad5075d01150 | -10.0162 | -50.1374 | 2026-09-27 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| dfd25751-3c71-33e7-8bfc-5537471b5383 | -7.3653 | -42.1058 | 2026-09-27 13:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| caadb6db-0552-33a7-8534-b46a01b4426d | -12.2834 | -50.6797 | 2026-09-27 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 17aba2c5-d3e9-3d84-bb5a-487b7469dd15 | -7.365 | -42.1298 | 2026-09-27 13:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| ed8aadc1-044e-3087-9e11-0efcd812a867 | -12.2498 | -50.3835 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 4df095eb-74aa-3cb3-aafc-86840ce303c9 | -10.0159 | -50.1588 | 2026-09-27 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 9084f290-c1f6-3bbc-a160-fdb6d4c0efb3 | -12.0806 | -50.232 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 86ba18af-65b0-3204-a6a1-58e1b1f39eda | -12.2643 | -50.682 | 2026-09-27 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e06c745e-51ec-35ca-840d-bf0eb4e0ccf2 | -6.8596 | -43.5003 | 2026-09-27 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 79d9d547-8a6e-3de8-8444-01a8ad595e5d | -12.1366 | -50.3112 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| a7972e00-1170-3ae8-9bdb-bb4c8f93110b | -11.79 | -50.5664 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 43de778a-3ea5-3b8e-8844-68bf27de8e5d | -6.8408 | -43.5021 | 2026-09-27 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 275.2 |
| c283e22c-42dc-3514-95cf-3a44e19cd5bd | -12.2502 | -50.362 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |


[Clique aqui para ver as próximas entradas](README56.md)
