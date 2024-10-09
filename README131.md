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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb35a81a-fa84-3011-bc24-ace4e8f4db09 | -9.8114 | -60.43707 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ebc126d-f582-36f1-9a34-918846761dd6 | -9.81137 | -56.41729 | 2024-10-09 04:40:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0b529c7-c637-3aa4-a232-5da1cdf9e014 | -9.81065 | -60.44107 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d5bdc30-b412-3909-98d8-191100100358 | -9.80568 | -60.43591 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68fbf694-6c5a-3e31-96ad-68ae12d39223 | -9.80492 | -60.43993 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b017c84-a08a-3c03-ae95-47523a5a4543 | -9.80416 | -60.444 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bf12cdb-6704-3f67-a9c0-1884e84cfd20 | -9.79327 | -57.45759 | 2024-10-09 04:40:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcbfbb32-da69-39e6-98bd-5811fa589eb6 | -9.75717 | -62.37027 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d32273b0-847b-376c-8d74-0792a8ce0912 | -9.75076 | -62.36879 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea67220c-3556-32e0-b43a-9b7168e0fac9 | -9.73245 | -64.2334 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 799686c8-9833-3151-b94c-2c4c9a2731c1 | -9.73235 | -56.98231 | 2024-10-09 04:40:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2704cd8b-9d9f-336f-8a70-5c26bb84b580 | -9.72966 | -64.23689 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1a18bb1-874c-3a07-a963-9fe485aafbbd | -9.72888 | -56.97858 | 2024-10-09 04:40:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aefd7470-83c3-37e4-ae2e-9a92e876f3c6 | -9.72806 | -56.98328 | 2024-10-09 04:40:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3b1f6b8-cd0f-3ceb-ba41-90fd6c7e5ebf | -9.72779 | -56.98145 | 2024-10-09 04:40:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04464c1a-46f5-3bc7-9a5a-5aa735d454b1 | -9.72585 | -57.80406 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bb6e247-4962-305a-a69e-77c5ae41a821 | -9.72539 | -64.23142 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46055753-e6e0-3211-954a-37e1e06ff6c2 | -9.72379 | -64.23913 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98ccf5a4-0337-3639-abfd-6608445e7088 | -9.7225 | -64.23532 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb8f8cd7-24d7-3976-943e-47594ac7e860 | -9.58232 | -57.5665 | 2024-10-09 04:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec03749e-122a-3b96-a488-515d40a8ae7e | -9.57937 | -64.1103 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23a0ad78-732d-3ae7-8061-dbf48bd1722f | -9.57229 | -64.10854 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fa8dcd3-db1b-3f3b-bff4-b5a517782e27 | -9.57091 | -64.11551 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 072f2088-0575-39b7-bdc2-ea15fde38a7b | -9.54208 | -57.90507 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ebc6c8d-76a9-3f90-a4b7-eaac427aaf68 | -9.5386 | -57.90688 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfd0fd32-25be-392c-8012-74efe72dfb55 | -9.48143 | -57.93372 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04b1efc8-2fab-32a3-a35c-b9a3ae580227 | -9.47653 | -57.93288 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eca6fb47-c2bb-3c16-aee3-f46b59174306 | -9.40264 | -63.65613 | 2024-10-09 04:40:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64915b16-284c-3494-86fb-7181fa3e574e | -9.39713 | -63.65894 | 2024-10-09 04:40:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2da49203-9b54-3120-bf3f-fa1254ee60dc | -9.39562 | -63.65489 | 2024-10-09 04:40:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54ea981a-9959-3faa-b51f-a7fe76f7c56b | -9.38878 | -63.41814 | 2024-10-09 04:40:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d5b3c7b-8b2d-3a28-9d83-93797243aaf2 | -9.38771 | -63.41673 | 2024-10-09 04:40:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cbe91ca-45f1-3744-be7d-cbc2cb2fc742 | -9.38186 | -63.41685 | 2024-10-09 04:40:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e4d4c01-7d42-3248-9262-e8ee6fc341d7 | -9.36283 | -63.81458 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b8d0b97b-78cd-3a4a-aa44-949c0a8e8e32 | -9.35961 | -63.81105 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8af0962-0c4c-370c-b95d-d716dcedfd25 | -9.35839 | -63.81717 | 2024-10-09 04:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8159b43d-9bd8-36f3-ad94-4248a75ee526 | -9.33352 | -60.31325 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba422bc7-2e19-31d2-bb38-80f58f3b22e5 | -9.33343 | -60.31506 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6d94110-94c5-3901-9942-f6baf1968e6f | -9.33278 | -60.31723 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b1d3914-e01a-37ea-84e6-94e271ff6ab9 | -9.33268 | -60.31903 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eebc7fe5-a06d-3372-95f9-a80b92e41b4b | -9.32778 | -60.31214 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e14e9623-da2e-3c3b-b1fb-52c7f4235f32 | -9.24032 | -60.42942 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae714c07-dc8e-3f97-9601-0617f39a0b60 | -9.23954 | -60.43353 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab65a83f-f98e-35e8-aab1-1e249a2b89cb | -9.18039 | -62.28192 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dfc7db32-ddb0-35ea-88cd-798f95e43e5f | -9.17987 | -62.27887 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c060014a-7830-346e-adca-1217e3569487 | -9.17879 | -62.28437 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41032900-1a8f-34ef-bdc3-f281ef7febb2 | -9.17391 | -62.28062 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a98ecdfb-5dbd-31ad-b40d-e949c0aa5b4f | -9.16192 | -61.57153 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2abd6542-8597-3d7d-ab51-5c0e0a1861ad | -9.16098 | -61.57646 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b8a04e62-bbfd-31b8-8a3d-8a4e58759b78 | -9.15845 | -62.22081 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b14eeac0-2896-3549-bc62-8dbeb6479cc3 | -9.15569 | -61.57037 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0481293e-36ea-37f2-b751-d1879bb3e1f9 | -9.15476 | -61.57525 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5fedf345-11c3-3bb1-aa14-6edede0a7ca2 | -9.15199 | -62.21956 | 2024-10-09 04:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0007cf2-2dd0-3262-8861-eb5280a135d6 | -9.09939 | -61.13887 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd5376d6-c606-3a12-bfcb-71df8b807c5c | -9.0985 | -61.14353 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a077a75-1ccc-3b1b-a681-07d9e888ac44 | -9.09422 | -61.13306 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f25902c-3b89-3917-90f9-1a005d18b265 | -9.09333 | -61.1377 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac0d25e8-a37e-3398-b651-11b9360d1161 | -9.08815 | -61.13197 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 801c2d2a-4613-37d3-bd7b-cf2fd451cb08 | -9.08726 | -61.13661 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ab8790b-cac4-34ef-8935-f2254745d8a6 | -9.05463 | -63.23528 | 2024-10-09 04:40:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63b01ae6-fcf1-3409-8232-89a53be4998a | -9.05444 | -63.23564 | 2024-10-09 04:40:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28971ff3-7e91-32bf-be09-5fba54bf6ebd | -9.05338 | -63.24171 | 2024-10-09 04:40:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c43ca527-8550-3055-ba76-4f702b52ac1d | -9.05314 | -63.24205 | 2024-10-09 04:40:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8618e839-e4c6-32e5-9895-94c72bd162c4 | -9.0512 | -60.4529 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b20e339-d324-3810-b0fa-549c76092d9b | -9.05045 | -60.45694 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbebf513-c806-3b17-883b-37b030f1e3a0 | -9.04778 | -63.23388 | 2024-10-09 04:40:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c6d2245-9b73-3a29-b456-58421f5585fb | -9.04652 | -63.2403 | 2024-10-09 04:40:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5158fd2e-b731-3744-a3b2-f70ca03447d4 | -9.04545 | -60.45149 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b424077d-6029-3714-87a8-3c10a5c0b2fd | -9.04467 | -60.45567 | 2024-10-09 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ed0fad4-6fe3-35ac-8ba6-5ce3aac71242 | -17.33857 | -55.0228 | 2024-10-09 04:40:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e8311e50-4dea-3acf-8299-60ad75c1db06 | -17.33572 | -55.01781 | 2024-10-09 04:40:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6f351108-3748-37c9-a2d2-d2e42b291a90 | -17.33496 | -55.02213 | 2024-10-09 04:40:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2030e6da-e926-3f51-99d7-32f7fc630830 | -17.32833 | -55.03871 | 2024-10-09 04:40:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 79fc04bc-6db2-3e09-b47e-5c10436e1946 | -17.31885 | -55.00306 | 2024-10-09 04:40:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 176d54af-f034-3355-87e1-69735b0e10cc | -17.31812 | -55.00737 | 2024-10-09 04:40:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9baf942f-2759-3f5b-bc88-5e01bba97389 | -17.2165 | -57.33395 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e4834d13-e850-3c33-8a82-de957fb2d63b | -17.21309 | -57.32932 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 441bcaf9-4f52-3879-a99b-0bfa336ae5bb | -17.21239 | -57.33312 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2a6aed02-b3f7-322f-b949-5d200060c7e3 | -17.2117 | -57.33694 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1cccf29b-111b-32d6-9018-99701800da31 | -17.21039 | -57.32085 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a6c7e522-fb40-3f34-8bab-a5212ff43fba | -17.20969 | -57.32467 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4f540544-0561-3d0a-a63c-20e7a1cb9350 | -17.20899 | -57.32848 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b63d133f-8d1e-3ddf-a767-96c86426cad7 | -17.20759 | -57.33611 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d6c42e8a-f015-31f4-82b4-b6455e04798e | -17.20629 | -57.32001 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 903a58df-ba13-36d8-b9e9-de2da1bc3aa4 | -17.20219 | -57.31918 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7645c1c4-f664-3802-947e-e1b7248cab6f | -17.18508 | -57.31966 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d41aed1f-01dc-32c9-b9ab-e3f100cbd5b7 | -17.17758 | -57.31419 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 53308606-8d2e-35ff-ad16-3034b92349e3 | -17.17687 | -57.31801 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c4316057-eb4f-3434-a897-ca6389dd1dab | -17.17418 | -57.30956 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 40b11b2a-9416-32dd-9ba9-e4ff5d417608 | -17.17347 | -57.31336 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 754a4f2d-760a-39d3-ac90-8867c1ee7d33 | -17.17277 | -57.31717 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f4767c17-4c32-33c2-8c67-34cb86c62754 | -17.17206 | -57.32099 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| caeb6f3c-3d18-3006-ae1f-96a54c2748d8 | -17.17122 | -57.44075 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 1e4128fd-21e1-30cb-8ee3-b1b74e63b3a5 | -17.1705 | -57.44463 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| e12a752e-9125-3978-9767-d8bb27fd9fb9 | -17.16979 | -57.44852 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7cf59ba4-a1c3-3a44-af54-a2c267f6572d | -17.16866 | -57.31635 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cd437972-5229-39c6-b0f3-19a8454d892e | -17.16781 | -57.43602 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c87c798f-c1ce-30b9-be82-ed8a254702ae | -17.16709 | -57.4399 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b72182c7-adc8-3b65-a952-f0f112c56cdc | -17.16637 | -57.44378 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 473fb230-16ea-3cd1-8675-7009a90e9911 | -17.16583 | -57.42355 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README132.md)
