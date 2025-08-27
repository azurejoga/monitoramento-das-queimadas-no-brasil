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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dadd0c7a-b479-34ad-bd70-44eb6b01f6c1 | -8.90506 | -60.76353 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 942d5c88-a972-336a-a566-511512dac938 | -9.42015 | -60.52228 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56e24d7b-fedd-32c3-abc6-75843da9618e | -7.54795 | -63.83766 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d7a4e1c-de6f-3806-a4dd-cd27bb0d0407 | -7.37999 | -64.36195 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17da718a-9304-3c1b-9c05-b61937a55d48 | -7.54399 | -63.84079 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b8f8f6b-023a-38fd-9a9c-2ee9c47b71a9 | -7.16997 | -59.73783 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0016b3b4-e9e2-39c5-8769-ac02682ac3ee | -6.94832 | -60.07955 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e715083-25e1-3739-9c63-a88aeec6553c | -7.35629 | -59.66752 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eea7eea-dcbe-3713-9151-816df6bc3f67 | -5.79798 | -59.21265 | 2025-08-27 05:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1dfde37-8788-367c-b52c-d3b4e7d293c0 | -9.27962 | -56.90733 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18b3ea85-c5d4-3e3f-9341-dc963e9f0d56 | -4.11774 | -56.34058 | 2025-08-27 05:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df9b9ddc-276d-3954-b420-1ff412bae02b | -5.73181 | -59.8847 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e714d46b-9b92-3a51-bacc-7fc59aff1064 | -6.77181 | -59.66695 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 927eeb6e-95a3-3873-8d43-16be53f915bf | -9.40165 | -60.50438 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9d1b256e-c19b-3082-b05c-c81185eb8c5a | -9.18861 | -59.52731 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09022bfc-ae39-30aa-adbd-946eda25dacc | -4.95524 | -55.81426 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfbfc788-8716-3dfa-b1f3-d96d3b322eec | -6.25545 | -60.00866 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c4dd34c-9733-3e85-8850-e8756ae63620 | -8.8995 | -60.77351 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e492c8e-3e69-3e9b-8612-32a61dbab2f3 | -9.40057 | -60.51183 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e549d8e-da01-3f05-b0e3-5201f2d05a2f | -8.71942 | -64.02229 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 873d9847-f130-31d0-bd85-9ae23c97b1de | -9.15923 | -59.54493 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0496e81-2ce6-3953-b620-e008a8fc1463 | -9.40255 | -60.5273 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a6a6f3dd-e763-3428-9845-17a0257b4501 | -8.90001 | -60.76999 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2da0b6b-7ac0-39a1-98c4-acea93e52a8b | -9.27856 | -56.91048 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21a9a487-3e78-39c2-b5de-fe23f4e0bdc9 | -6.70157 | -58.55714 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d894319-0440-3ecf-9f89-2af9f67d061f | -9.4171 | -60.51426 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 613c77e7-3ce1-3d9e-b02f-b0e7ee852cbb | -9.4135 | -60.50994 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7df5af7-413f-3a58-899f-0975c6e7cec2 | -5.5255 | -60.21044 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b873c43c-fba6-3b68-a8b8-fb0f78a8ed6b | -8.88488 | -60.76055 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4879047c-4ef2-3ea6-8925-401cd8b4104a | -7.3867 | -64.363 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d064ba4-be5f-37d5-83ae-cb966d87c10e | -8.64312 | -62.62092 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60554001-523e-38e6-b72c-0f296f305fbd | -6.7008 | -58.55494 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04afa5cf-88a1-3864-b509-3d22d00eb33f | -7.61617 | -62.7233 | 2025-08-27 05:44:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4854ce40-e127-30d4-9517-ceb7f1c794ce | -9.19119 | -59.54087 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50b73e29-937a-37fb-a048-b33949b4e458 | -9.41743 | -60.54089 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e20c752-2dc8-3073-9aad-8648b15134d9 | -6.76648 | -59.67413 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89c8936a-c515-3cba-804f-d827b4d51e33 | -7.43164 | -60.62042 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e6b844e-4b91-3dfe-87ac-d9351cf5f163 | -9.41296 | -60.51366 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53a4e37e-6e10-3f1a-b9da-987d7b1f47b8 | -9.64739 | -59.62826 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46b43ad1-8834-31ad-9761-ef0cb4a9e71b | -8.85939 | -62.44315 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f457581-9536-34f1-a6b5-803320adbfda | -9.23465 | -60.91581 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 74f47aa1-b842-3852-8292-8c61e9da73a9 | -9.1077 | -60.30977 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7acac628-0520-309a-add7-9813369f3d34 | -7.74676 | -61.07994 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47c7fc35-e658-3c5e-9530-a26610ce2b68 | -9.1848 | -59.52241 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eed36722-23a5-3e10-8b7c-54fdfecab546 | -9.11187 | -60.31039 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a6f70a4-a716-39f0-b6bc-9068a0967619 | -6.84485 | -58.96618 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 530ef08f-0333-3fe0-8007-bd8ac19fe53e | -8.53613 | -62.64038 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aab49a13-d684-3b58-be5e-86b031b5df95 | -6.69314 | -58.55121 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c085dfe0-bc61-3725-ae30-d20beea66463 | -8.6395 | -62.62037 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aea97cc-298e-348c-bc30-0437d10e707c | -8.90431 | -62.46737 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80edaa2e-70b5-3430-bdad-3ceeb7ad7f65 | -9.10299 | -60.31294 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3041789c-e997-3722-88f6-03e1cad367b9 | -8.34378 | -62.93296 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6a90eeb-f950-3b0b-b1e2-6d3ae3fc0118 | -5.35366 | -60.39994 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9b8a463-0f35-32df-9a83-845de73cd6b6 | -9.18119 | -59.45142 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78362cea-51ff-32e2-9163-9538e338b584 | -9.40398 | -60.5465 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e1385bc-3fe6-3dbf-9769-e3acd925a1fc | -8.51719 | -63.88546 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d166306b-fdad-3cb8-95c9-0332e4d0d748 | -6.6767 | -58.86235 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 308c1a80-4e81-362b-82c1-28ce1801f9e8 | -7.41493 | -60.62318 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09e434d3-10d3-3ccd-be35-38956d072a3a | -7.35227 | -57.63325 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f106f564-3bc0-3eca-a325-9d56049654ff | -6.79258 | -59.64226 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d15e8a-30b5-30e3-a7d6-e63c4b897b8e | -7.4805 | -61.34871 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83fc8c1f-8be0-3378-8ecf-146ba85a9c92 | -9.4056 | -60.53534 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 918e6998-9ceb-34a8-a9c1-19274ac08afb | -4.95572 | -55.81104 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7101679-24d2-39e4-8f9e-709de1e4a50f | -7.35572 | -59.67146 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 837a8e9b-cadc-39b0-a094-5cbcf10820bc | -9.4047 | -60.51244 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d98e6ae7-6c51-3e9a-9a74-c7671e1f94da | -9.10716 | -60.31356 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df9c9fea-82bf-3966-ad86-b492b4940563 | -7.55136 | -63.83818 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4b10f91-f8cd-3587-a678-8ec507e430f5 | -9.40362 | -60.51989 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04cb4753-022f-3922-b6da-de4d2cabe926 | -9.26427 | -56.90168 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 492ce294-0641-3f63-bc64-b6397eed52d3 | -9.58662 | -55.37451 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bc0ccef-fba2-35a4-aa40-d34bba9567eb | -9.28385 | -56.91116 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7b15fab-1f35-3bec-9ce8-dd6bfe45445f | -9.15745 | -59.55778 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 34e4f03c-981c-38d7-a169-868087fef567 | -9.47369 | -57.8245 | 2025-08-27 05:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 15d927af-ced2-3f11-aed0-10b4240fc637 | -8.2389 | -61.45413 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50d61c45-43c0-337f-8dd3-299bc8006987 | -8.51775 | -63.88175 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 866054f4-e40c-3526-a6b9-25738724dac0 | -9.10244 | -60.31673 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fbe1d88-2d4d-3f55-9800-aec8cba3ab23 | -8.23824 | -61.45868 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e94fa661-c2a6-3a79-8bb1-d58c07559735 | -6.71389 | -58.56818 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be92da8b-d9f2-35a4-ba7a-10c23200f748 | -9.64169 | -59.64236 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94b68f4c-fe36-387a-bec8-45da74efbe90 | -6.25383 | -60.01941 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d7f39f-afc2-3b09-aba2-33f05d50a135 | -7.99899 | -70.29108 | 2025-08-27 05:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5e27c6c-3a53-388c-a1fd-343e886a065d | -8.84844 | -62.4415 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad2d8cf6-34f8-3610-aa2d-322995fafe2c | -9.22178 | -59.67253 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af984b97-27eb-3521-8bd9-fcdac29274f8 | -9.15714 | -59.59226 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eabd276a-5f08-34e1-95b5-6c1c60007eef | -6.94151 | -59.56342 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db7ca2a7-128a-31ba-b798-47b9b717f69a | -6.91422 | -59.35915 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec2ca573-cb73-34cb-8dcc-a08501a59d33 | -9.17556 | -59.45946 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e5bf091-d6d3-35bc-b989-bffbbefa769e | -8.89245 | -60.76526 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 845ec093-27e4-3a66-851f-462fc07dd9a2 | -8.95089 | -63.37094 | 2025-08-27 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7878c49e-dffb-3a1c-844a-dd7eee296a85 | -8.85637 | -62.43833 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 055fd95e-4108-3fcb-852b-15eb944d793e | -6.82631 | -58.97407 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55466df7-812d-3315-b7f1-f1de58645199 | -8.57879 | -63.91778 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e864711-2477-3c82-b81f-e45b9412ba87 | -8.57912 | -62.60021 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adf9a480-e557-320f-847e-3fe5b3f89018 | -6.62318 | -58.54758 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29a0d1a2-9f5c-3768-9901-dda0b42e6e24 | -9.17174 | -59.45449 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bc948cf-835f-3dc4-9bff-abf2edab1e44 | -8.86003 | -62.43888 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a5485d2-d36d-3e66-b427-6b5ed89bfa78 | -8.88791 | -60.76818 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5448561-cb92-3d95-ad7a-461db8816788 | -9.36854 | -61.52521 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d49c0ee9-0880-37c1-b391-4a6a7813abe9 | -8.84781 | -62.44577 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e3cf210-a031-3265-b2f4-a77b19ee2ce6 | -9.41513 | -60.49874 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README72.md)
