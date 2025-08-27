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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2fcf70a-9a2a-3a13-bf76-10345599f0ef | -8.25534 | -61.45842 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e7c012c-4a53-3540-940e-13ed93f5cf7f | -9.8082 | -64.24709 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2cb97985-84ed-3019-afc3-3ec2d4766051 | -6.25987 | -60.0169 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75c6e1e2-2bb7-3c1d-b445-88569ddb7264 | -9.19411 | -59.5086 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26deafd3-1c42-315e-afda-72ab7e4c26c3 | -8.90018 | -62.47129 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 480cc425-f670-3911-abf1-ddf17195548d | -9.64824 | -59.62706 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f472dfea-356b-3fff-bf58-3b60fedb4f26 | -7.4408 | -57.62719 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9ba7d2f-d7c3-3c25-bb59-220190b0d02b | -9.56924 | -55.38105 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9627774-73f4-3dad-848b-5503d381bd4e | -10.0935 | -62.8964 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf6f389-7b8d-318e-ba1a-51eb6046e19e | -8.11118 | -61.48156 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bbc31f8-3969-3729-a228-35a6e353a944 | -7.60271 | -61.6292 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05e26035-968c-3089-a02e-1261778dddbb | -9.41246 | -60.52243 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4905a998-c6dd-30db-8b8c-9185b8d82413 | -7.47988 | -61.366 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fa683cb-100a-3bb4-ae3e-6ee81c4f4237 | -6.83637 | -58.96745 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 167d2d50-0a58-37db-a088-f71dc3e306b1 | -8.89848 | -60.56551 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb8a7ca9-69c0-371b-b09e-b652fbc48793 | -10.24436 | -59.66501 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 854f3f16-56f3-3929-a98c-d00ff1810e61 | -12.74788 | -48.19694 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 637164c7-31ae-30a4-a11e-386a59f8bf87 | -6.69063 | -58.85626 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2826fdf7-622e-3f08-b420-445fc8322380 | -6.30322 | -57.9328 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca144cd9-3d64-32b1-a0f7-19d60795e071 | -9.71428 | -62.40088 | 2025-08-27 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e0b0719-6a4b-3770-85ff-eea018417e0e | -8.89293 | -60.77147 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a6ed9a3-4758-37bd-a9e2-02d8549690b8 | -7.17199 | -59.73707 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 158b0bdd-9c84-3e0d-8687-3b15417e151d | -12.88349 | -48.1026 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1b291348-7321-3bf9-ab67-5a5aa9ad2230 | -9.69917 | -61.28458 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 963b1440-ed8e-3d4f-9ba6-a579e5730236 | -9.40526 | -62.48973 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4027dd90-551a-327a-8e7e-2b379ad6a151 | -7.42016 | -60.61921 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 712fa260-374a-3be0-a194-6a05f1e53b40 | -9.80236 | -64.26861 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0204d71f-d963-3381-a4d6-7699dee1596a | -8.09822 | -71.25204 | 2025-08-27 05:18:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31510e10-2a3a-3ae0-898c-aa48dbbf6ae4 | -6.31477 | -59.86417 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c49601f-986c-363e-83a8-2bb24f973e70 | -10.04242 | -64.89558 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ac7d665-1ff8-33e5-be49-620f04e44b41 | -10.52371 | -57.98453 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cd9c566-28c3-3786-bfa9-8bd121483d6c | -9.0801 | -66.06199 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caf63470-32d5-3d3c-9caf-fb2dd10c8b9b | -7.44405 | -63.16301 | 2025-08-27 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9bfa1ca7-240b-3443-bc19-b3c66aef6ac9 | -6.06742 | -59.96505 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9853f90-780d-321b-9e08-1ecddac7e53b | -8.11398 | -62.87836 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17639c46-c751-3231-ac20-7374836169b2 | -8.53196 | -62.65985 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 431fe42e-a3c4-3396-9cf0-31580aed5896 | -6.9476 | -60.07963 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 733b5992-61ed-3a0a-b98c-d24217eaa48e | -6.8779 | -59.89668 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea7f8e75-d768-3d37-9ccf-1a30cddc488f | -8.21659 | -61.3951 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dc7aa0a-f213-34f3-8e22-e3bc80f922a3 | -9.52742 | -60.52649 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31b07120-0755-3d95-8ac5-d00d554e570a | -7.47785 | -61.40021 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7936049-58ad-3201-93b2-f7d927269f7e | -9.40691 | -60.53596 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b97789d-17bf-381c-a225-e662c5e794ff | -8.91535 | -60.7168 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb2a5f2b-cb8e-3ff1-8542-5d258224f02d | -7.47846 | -61.39646 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7730748a-c3da-37aa-8c10-4bb0d96f2ab8 | -10.79916 | -47.06874 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 16302bc0-ff0f-343a-957b-e63a77226058 | -8.61421 | -64.02798 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec9693d6-d4e0-30cc-81f3-59182d33239c | -7.5498 | -63.83923 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e13070a2-bfef-352f-8067-1d13fdf8d437 | -9.79486 | -64.24249 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53ccd0fa-5490-3214-ad0a-eaf3575efa23 | -6.69154 | -58.5437 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82d7117c-71f2-34e6-8288-7f76eae22383 | -6.68017 | -58.85817 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e86ebca-5f37-3d7f-85d2-77105de197f8 | -6.34181 | -58.18855 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db0988de-8f57-30b8-a106-8a2c05afa22e | -10.45417 | -58.00551 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62de754e-b9b7-3b7f-9163-c5db49259a98 | -8.94096 | -65.94797 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f37f073b-730d-391a-9b09-a0e5a957b75c | -6.65162 | -53.1888 | 2025-08-27 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05bb03ea-f4b8-32b7-97af-0e4276a43dd8 | -9.40174 | -62.48917 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa9a7a4d-272a-3e2f-8d71-b1c5c8cf194b | -9.95334 | -46.37381 | 2025-08-27 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9f31fbe3-73b6-3191-9550-0afbe920fd42 | -8.8913 | -60.76027 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2d666c9d-3f07-3252-9823-f858651a6853 | -6.77188 | -59.66283 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d7e7454-0ff4-3346-9c63-a14e9b1dfb85 | -9.56537 | -55.3804 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46484514-d0b7-318d-8936-14c1c3a8c391 | -9.16248 | -59.51369 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7d078b5-ca58-38ef-b7a1-6a8a8dbb7a2e | -6.81377 | -58.96039 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 832729df-8e61-3080-ac65-c333660d0b02 | -6.24142 | -60.00668 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7783b02f-6068-3c57-89df-83da498f39b6 | -6.77079 | -59.66975 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82ea4292-bea5-3111-a947-28d44b738c77 | -8.8935 | -60.76791 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb934224-bfe4-31d1-9a8e-97f40d04039e | -7.61024 | -61.62648 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 221351d4-668e-38bb-bf29-3a06072ee98c | -9.41301 | -60.51892 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f5f8155-3775-344a-a71b-9e9bccf1de13 | -9.25085 | -56.90405 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75a28a36-5992-3161-90d3-7093e17cd7a3 | -7.44202 | -60.02979 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 481ff978-1219-3078-8d65-e2df4168a9eb | -8.88159 | -62.45176 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b75195f-9578-384e-9ee9-608e10763489 | -9.67088 | -67.49921 | 2025-08-27 05:18:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f63de3-36dc-3dfa-a443-a44383921fe5 | -9.40693 | -60.51435 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12ab1c52-f998-34fd-bb0d-109bdacebde6 | -9.41579 | -60.50137 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 986d4e27-2f68-3ae3-b111-e5cb253c20bd | -7.62182 | -61.03249 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df417bde-bcf8-397c-a7e5-015215a85853 | -7.38129 | -64.34605 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 587b5de3-906a-373c-a62c-faad5e8f8a5c | -7.1753 | -59.73759 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d969048a-e034-3c0a-ae3d-647d35d29165 | -8.4626 | -64.04531 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9fc6d35-59f3-3d3c-b20c-bf938c060462 | -11.81548 | -46.81607 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6973478e-b991-3fd8-ad77-ebc87c24ccc8 | -9.18311 | -59.51399 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 661ef703-b947-38d0-b0f0-d2dba21a6c38 | -9.47205 | -57.82461 | 2025-08-27 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d780f66-2a67-34d9-9383-e6003ee6ff92 | -8.85046 | -62.44252 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af14fdc-cca0-38a0-81b2-f68a2d0c97f7 | -9.29796 | -64.53938 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5ed9d68-f031-32d1-b157-fb892a26b454 | -10.72052 | -47.09464 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cacbe158-b97d-311e-b8be-bf842c66a5f9 | -8.11974 | -62.86615 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35b35980-fdf7-337d-af2c-63db0a3cd2d7 | -8.61299 | -62.65084 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59949ef3-e9b4-3af0-b956-18a064a162a4 | -9.15598 | -59.55538 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b6a8666-807b-3bd2-849d-7c59d9896741 | -7.27702 | -57.66949 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 547185f5-6da7-3ecf-9e49-6653b6b1439e | -8.12588 | -55.55301 | 2025-08-27 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccdd048e-29d2-3ad4-80e4-2712f9f6be35 | -7.41624 | -60.62225 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b552870-ece3-3ced-b14f-ef0cfc24d91c | -7.40133 | -64.34938 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3413003-abb9-3c3a-8b92-2d4d8d69eaaa | -7.36408 | -70.1433 | 2025-08-27 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2f7267e-45f9-34d9-9113-2f4567d90c82 | -5.40467 | -60.17489 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87d0c889-17ea-34b6-9f5d-0959b88e59cb | -6.25654 | -60.01639 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d716e4d-e0dd-322d-a40a-be83ede3ecb1 | -5.40523 | -60.17133 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b5e70b4-9d38-35ad-9dfa-e491f1333c0b | -9.80987 | -64.2949 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e68956e-e4ad-3ec9-9764-b1dcb32f480f | -10.93993 | -63.63253 | 2025-08-27 05:18:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d861859a-c6ea-3e45-8dd4-65c7e2a0a0f7 | -6.78948 | -59.63717 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb2bc348-a7c4-34e9-8ee5-643960b40139 | -8.34235 | -62.92694 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10d438ee-3575-396c-9589-2697079918e8 | -9.25797 | -56.90505 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34ba4dad-f16b-3600-9f31-2e303ee4e7e7 | -10.06668 | -58.36549 | 2025-08-27 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfaba7cb-ffba-3a7d-be13-0717954c7f83 | -8.33589 | -62.94342 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README59.md)
