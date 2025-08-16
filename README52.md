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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53e9b78d-b37e-3077-b541-043a53986340 | -8.98579 | -60.54965 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9c63f852-445a-3b6b-be21-cff587dad2de | -8.99739 | -60.54066 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86e80658-71c4-3cdf-9bb2-53193b515de1 | -7.46389 | -60.4115 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 972833a0-9c09-39c5-ad41-7ea4ae637c10 | -6.93846 | -59.65316 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71ff9d8d-f73b-3f09-bf78-276942d106da | -6.94472 | -59.52273 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dafd0c7-bbec-3a22-97f4-ee7bd1e046d2 | -3.23803 | -50.80689 | 2025-08-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca7401c0-4a86-3765-9106-62960d722c98 | -9.50862 | -60.55223 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1d4f77e-34d0-3638-9ab9-9485fef73447 | -7.67766 | -63.31443 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2449f97f-b213-3008-acb8-b8c15e6b7cb5 | -6.63198 | -60.00962 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da8abbda-c1ab-3758-92b2-4b434fd85db4 | -7.08642 | -59.2149 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dd187c5-bd9f-334d-aa14-6f51c6ed358a | -10.93033 | -56.84433 | 2025-08-16 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6147c534-4411-374e-a39d-d898be6860b9 | -9.37115 | -47.98221 | 2025-08-16 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17471ad0-719f-3c6f-b1f1-cb2f0ab2706c | -6.48264 | -62.93114 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9840105-dfa1-3c28-9784-145f44522cee | -8.99834 | -60.49035 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f89b3fa-3179-33f7-a162-797f47f38c30 | -7.43491 | -60.02684 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 171dea1f-02a3-3cfd-af11-c8c0826cd6da | -8.92943 | -62.23364 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b1fed03-770a-364e-8e86-5691c3391783 | -8.96603 | -61.67871 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ec97760b-d755-3afd-9934-8464ec25e82b | -7.95064 | -61.75546 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65ecd6ab-110f-3efc-9802-51eef5c73934 | -9.50575 | -60.52646 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4797936-f4f5-381e-a307-134530827eef | -9.53679 | -63.71636 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34f6ce60-55ac-3c5a-814a-1a5cc06b46c7 | -9.20639 | -59.65869 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1f23cba-bc60-327a-ac91-f075de8a3280 | -9.38752 | -60.54434 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85e3325a-df2c-3dac-bf9c-429cffdfda8f | -8.92831 | -60.72375 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49308443-9456-3c2e-96f6-863afee2f046 | -9.00119 | -60.51605 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd9ecc80-c720-3fa0-ad52-7970faef91d2 | -6.62758 | -60.01609 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b787617b-efbd-3cde-b736-1afee83a501f | -8.56639 | -63.91965 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b69de93d-f881-359d-bdca-6ae4ade28453 | -7.04785 | -59.62622 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb65431a-d86e-3c57-9516-36c5658870fa | -7.61651 | -63.34007 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 295f2a90-5b46-3b64-9291-4cce491c28ae | -10.42481 | -60.27005 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21b8494d-761e-349c-90f9-d2179c2cc1db | -9.1699 | -59.66431 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88be4f93-c106-330c-a283-c2c575e7910a | -7.53339 | -61.33855 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d38b1ec6-004a-39ed-a9a3-e8093d9fa82c | -9.17133 | -59.66083 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17b56208-ccbb-37d4-aab8-bc166f693dfb | -10.1162 | -57.7677 | 2025-08-16 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2283441f-adf8-37e1-a3fd-cf41884152fe | -9.51187 | -60.53102 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e94ecff-784f-36c2-8d3e-411bcd99b671 | -8.46521 | -64.05183 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 052ca325-b000-33dd-a496-5ef86266fc47 | -8.56286 | -63.91908 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed5f1351-b5dd-3719-a194-5190ef7bcc03 | -6.62974 | -60.00209 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f20cb5d3-9c1a-39d2-b28b-687bb07c9fca | -10.05093 | -59.11792 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d82c0ba1-574e-3350-8edf-fc64c16fab2b | -7.0445 | -59.62571 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 886a6c67-2bbf-36ae-926f-8c00d0a818f4 | -7.0484 | -59.62266 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ac792ef-a4e8-305d-9f3c-2f20a5832e6a | -8.91289 | -60.73566 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0c743a6-cdef-3780-898d-8d2c726e06d9 | -6.90768 | -59.6302 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04cbe943-1205-3dd9-abe3-49d11296819c | -9.63004 | -61.457 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7efc46c9-fbc0-3b69-8df3-54a11b70c45a | -7.90223 | -61.52206 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24db0846-9d51-3d82-9c30-1060d8d87919 | -6.93784 | -59.63486 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60f18881-9ccf-3a24-9e00-0c5bc5d19a3b | -7.12798 | -59.65642 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 477c76c6-81b8-3e1e-8f76-ef16a853eb8c | -7.44211 | -60.02435 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9527b75a-45a9-3533-8e3f-5b0cf339cecb | -9.06252 | -58.94358 | 2025-08-16 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3f63c1a1-0b39-3946-9c54-0e55cfbb9257 | -9.38698 | -60.54788 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd99f63-96b1-3f93-989d-0cbd93a0bc75 | -8.99081 | -60.56123 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 098eebab-7857-3ca3-a323-e44879b1db00 | -9.20521 | -59.64346 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0387922-84ce-3335-a7d9-3f2c7e40994f | -8.94224 | -62.21758 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8313c533-2ebe-3af9-a4bd-79863a66e7aa | -7.91634 | -61.73569 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c600c888-dc4f-31ff-aff8-b54cbe38a2b2 | -3.4917 | -51.19103 | 2025-08-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4d13f49-e057-3dbc-9b0f-9c40785473a8 | -7.53284 | -61.34202 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 685834de-c58d-39d0-aef2-77aed81185f2 | -9.20979 | -59.65921 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21c0bb2a-ae1d-399c-bb45-1826eacd1040 | -9.06433 | -58.94298 | 2025-08-16 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e242f16-a8f9-3ed3-9096-6400c0e9245d | -8.99726 | -60.49739 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee0b1fed-5145-3a5f-911f-af5f63fe40b3 | -9.51242 | -60.52748 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 601bf62c-fc75-3200-9994-3a7a688a2651 | -9.18545 | -59.6593 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6882af4b-06f0-3b71-bcd9-9d806c598c16 | -6.91131 | -59.56145 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd40d5cf-3b6c-31f5-8e4e-31964cb08afc | -7.94842 | -61.74794 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a40d1371-a04f-3f3c-9dcc-cf8c355f37b9 | -7.42212 | -60.02126 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e15bb17-fb87-3999-a438-6fc0273c3c7d | -8.9919 | -60.5542 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe7e93b4-f2b5-37d4-a2c5-5ee2afdbda3d | -7.43375 | -60.01223 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a0608594-29c7-3007-ab27-767cdb05c1dd | -6.94706 | -59.55239 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4ff6943f-442f-3f2e-b0b4-03c9e27d4bf7 | -7.42824 | -60.0258 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 817ed0b6-504d-3710-9857-e6b0764fe39f | -6.94235 | -59.65016 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b4ec581-c2c4-397b-80c2-9cb2e258fd44 | -6.93355 | -59.52831 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b60fe63f-3286-3a5e-be6c-b0ac7d0a49a7 | -8.98803 | -60.55719 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dea69e0b-c303-3924-aef5-8149cbb8c921 | -7.92021 | -61.73272 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bc43421a-0365-3ab7-a91c-57db04646439 | -8.59239 | -63.87081 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbd87b0b-caf5-3984-a6ef-8dc75f5bbe60 | -7.49924 | -61.383 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b603ab1-5c8b-3846-ad3e-2906b7276512 | -7.9495 | -63.22034 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8779cdb-db12-30c4-abe5-7c09641ab273 | -7.4672 | -60.41201 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3187579-9ee0-3e54-a717-b73d91de1a8f | -8.98182 | -61.70976 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 029bd6a1-ff0c-32c5-aa39-07584f984fbc | -7.08698 | -59.21125 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c42917f2-58c6-39a2-99d6-3ef8d076ae5c | -7.49933 | -61.31541 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b8e9ebc-089b-3ec5-8b86-ccf7994782b9 | -7.4205 | -60.03178 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23bbd82f-ab79-3047-8c2b-3214393ed3da | -7.09604 | -59.22013 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e040307-06ae-3a44-b734-43639d1c228d | -7.59759 | -55.19424 | 2025-08-16 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d46d7da7-29a0-3254-a795-9a239796aff7 | -9.50521 | -60.53 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95443f8f-6060-3432-9ca8-c5c3093a3fd7 | -7.49979 | -61.37953 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc0218b6-a5c0-352f-ac20-382463d17c7d | -8.99061 | -60.49635 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ce49d3ba-8539-3bad-a383-8b63d565c0a0 | -7.91412 | -61.74968 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eac10450-4086-309b-8257-045e6f5cface | -7.30553 | -60.62103 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 968e64b8-49cc-3e48-88dc-712675c06f5c | -8.94553 | -62.23985 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c4e4900-965d-3461-9503-ba78d2574c59 | -7.52406 | -61.37623 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02f5404f-4939-3acf-ae13-19d5ee59f46e | -8.99841 | -60.512 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cec49742-f8b3-30f5-8552-516389cfa04b | -6.48398 | -62.9387 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 901c3f31-5e26-3c51-ad91-97b50fd2e60f | -9.50854 | -60.53051 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 84a56c33-9fb4-3e94-b36b-fb6ac98ff91a | -9.17272 | -59.62324 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cf1623a-6603-3a80-8c18-a8e35b64918c | -8.92497 | -62.24018 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd04b833-a986-3ddd-ada7-d977ed4f3125 | -7.41933 | -60.01723 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbbb2736-6dc5-330b-af37-95bc074fa8af | -8.94666 | -62.23278 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fea87614-c581-3d38-9066-027c94d9ea82 | -6.93137 | -59.54263 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb3547f0-b27c-3b9a-9676-006ff3e5ad61 | -6.62866 | -60.00911 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49155e5b-81bb-3780-ab05-f66a05ceee6a | -9.50304 | -60.54414 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b33bd947-b628-34c4-9b2a-d2ccc5945f9a | -7.50021 | -63.82677 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1ca0ded4-679e-32c9-b5c1-001cc8a7a79d | -6.93949 | -60.00032 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README53.md)
