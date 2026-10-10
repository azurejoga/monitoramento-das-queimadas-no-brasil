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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9b1b886-a372-3244-9c83-95dd40dcd358 | -5.18175 | -60.30845 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf13a89a-be41-32bd-8806-25f50b32bde7 | 2.72988 | -60.26613 | 2026-10-10 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c0b291ec-f8cb-3c3b-b7b2-3746e8b3b2e0 | -5.18761 | -60.31522 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 059990cf-fcf0-3298-aee5-6d55d11230ce | -5.08298 | -60.21687 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb4e423b-d255-3d1e-8e9e-b7e036027973 | -5.18842 | -60.30944 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 40d59961-3c22-3b1b-9399-7ef237f25bc0 | -8.68065 | -62.39954 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd1c9d84-cff6-3277-b8ad-ba1f1deede3d | -8.5165 | -67.02946 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b656112b-307b-3682-89ab-022e0b69405e | -8.69293 | -62.40135 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4ac93c2-d1fb-3eb3-b0b2-8c79a7ff6a8a | -8.53322 | -66.97678 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8728ce4-da21-3d77-9492-18d1f7a4a28c | -8.521 | -67.0301 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b37fd8c-96e2-3b30-8e82-f0a0ab1ae2b1 | -6.93878 | -59.24917 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd8fe878-bcb4-37be-8fda-56a4a1418e3e | -6.93137 | -59.25418 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50e19204-45bf-3293-9f1a-3d0c1e356b6e | -9.25182 | -62.30975 | 2026-10-10 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 973f92a1-6cfd-31e5-b96b-de1c04dafc41 | -7.45806 | -63.63288 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6360520-c05f-3bfc-b38e-499acf2e8fa8 | -6.49184 | -62.84629 | 2026-10-10 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f956a79-a4e7-310e-a75c-5308128419ae | -5.18924 | -60.30365 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e50a139a-a79b-3a2a-a0fd-c6eff9de3565 | -8.69232 | -62.406 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6efd7b0-88cd-3859-ab2d-159bdaaaedc6 | -3.98237 | -59.3598 | 2026-10-10 06:25:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e43527d-01f3-381e-973c-9112b1179873 | -6.94196 | -59.11133 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99400187-efea-3320-9ee7-531cea136db8 | -5.21817 | -60.04831 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea251b04-83ac-3229-95bd-6159e4b2b2ee | -9.25246 | -62.30471 | 2026-10-10 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1402e21-da8a-35b4-b456-9b67c631c66f | -6.62136 | -59.94406 | 2026-10-10 06:25:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c69847cd-5c07-3611-8f9b-415f03e966e3 | -3.16315 | -58.62301 | 2026-10-10 06:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f916492-a233-3e77-a246-2e8e22fdebcd | 3.04095 | -60.55319 | 2026-10-10 06:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a56a9b63-6ff6-384a-8a37-c52f0c022aa4 | -7.45098 | -63.64319 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0f33d72-03b4-334f-8f66-c5d06421f6d4 | -7.6998 | -73.10184 | 2026-10-10 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f549dbc7-5fcb-3be2-8c34-d71f88753eca | 3.04471 | -60.53987 | 2026-10-10 06:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 234f9ae3-ba6f-3773-8985-1260f1f4e040 | -7.45148 | -63.63948 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c13c7369-50c0-3e9e-a082-5e7a68859256 | -3.73009 | -59.46172 | 2026-10-10 06:25:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0688f7bd-2f4b-3802-bd48-abcc60178cb5 | -6.49129 | -62.85037 | 2026-10-10 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b38f87dc-ba16-36f2-a280-8e333dc11a3c | -5.18257 | -60.30263 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e088950-fdda-3008-93cb-5acd7a960359 | -7.46264 | -63.64104 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a777443f-5614-3353-932f-8d145ec2d7b6 | 2.72755 | -60.26389 | 2026-10-10 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| df4218f6-47e1-3ed5-9eed-e3a5f78def45 | 3.0454 | -60.54398 | 2026-10-10 06:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ddd817a-78e7-3dd5-af5e-4d29ba71dde7 | -8.68005 | -62.40423 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a74578d8-a313-3fcb-aba3-c726d25c163c | -8.68678 | -62.40052 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6ff3410-e1bf-3c3d-b778-ff59c5d4b833 | -6.93232 | -59.24666 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1136b145-66ab-387e-a948-60e345e7d984 | -3.53036 | -59.57632 | 2026-10-10 06:25:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c3fbc84-8d5d-31d3-863b-d576da8b0e01 | -6.93866 | -59.25487 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5605fe3-c888-3479-b613-50751cdccec6 | -8.41955 | -70.1263 | 2026-10-10 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0d8e1ed-e7d4-3652-b7f3-e10f6eccdf89 | -6.93048 | -59.25602 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9513ecc-31f9-30ab-864c-76d0d762dbe1 | -3.79123 | -59.37297 | 2026-10-10 06:25:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 105b34b9-eefc-3e64-85b4-50dd69cda029 | -7.45605 | -63.64766 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f4b8320-3a11-352b-adce-afde96e726a6 | 2.72316 | -60.26276 | 2026-10-10 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6e83b86-10f5-3fb6-80ae-9167a587f3bf | -7.44308 | -63.55301 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ada999a4-b38d-3f70-88ff-a1cb90cde3ee | -8.688 | -62.39105 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca32d768-bee6-34ac-8677-ca9da71a0e88 | -9.2587 | -62.30548 | 2026-10-10 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fd3e544-86cd-383e-994a-6ad21aff2faf | -8.51122 | -72.47038 | 2026-10-10 06:25:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 646bc152-97c5-30bd-a46d-a6d3e8f6377c | -8.69353 | -62.39663 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fcd4329-7fe3-390a-a9c3-9966c398d14c | 1.98357 | -60.61531 | 2026-10-10 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a67a2839-73d1-342c-9423-73e63837e760 | -5.08969 | -60.21784 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 473aa3bc-c218-37a5-80f6-a213ee4ae68c | -8.63107 | -66.78172 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e73fb88-2e5e-349b-b3be-9bb56538ebc4 | -5.07547 | -60.22173 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 973dae79-838a-3e71-9076-8d18249cfc25 | -9.25807 | -62.31038 | 2026-10-10 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffb95114-6f20-378b-bf63-754f81cf1fbe | -8.42021 | -70.12196 | 2026-10-10 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ec0f379-804e-36cf-a6d4-1791bf0c7ab3 | -5.2258 | -60.04324 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2849e813-f359-3127-bcce-44972f53cc6f | -5.08217 | -60.22272 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ebb1380-feb4-3db6-adf9-d9c560f3485d | -3.79242 | -59.37401 | 2026-10-10 06:25:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 500abe1d-2e46-3442-af1c-3732ae12e247 | -8.68737 | -62.3959 | 2026-10-10 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96301ef2-65c4-3519-a0d8-aeab692001ef | -5.07628 | -60.21589 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8225aac1-09d9-380f-b153-76163f9dbbff | -8.42183 | -70.1245 | 2026-10-10 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8044ab8d-c838-3dcd-8ede-5e920ad1328e | 2.72914 | -60.26178 | 2026-10-10 06:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| d499a081-fe85-3149-a856-f3238cd27111 | -7.45756 | -63.63657 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0418571b-1a21-3c0b-8058-648b62038f5e | -9.08895 | -61.04768 | 2026-10-10 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b601cfb-813d-3c9a-abac-8cf8a6ef17c1 | -9.08822 | -61.05352 | 2026-10-10 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9aff53ba-d108-37bc-b6cf-d1f74fb9210a | -8.66768 | -67.12006 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d38a1055-1529-33b4-bd30-3a37c92e6cd2 | -7.45655 | -63.64397 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffb16cdb-3ebe-3351-85b6-23daadf02d39 | -3.18068 | -58.63373 | 2026-10-10 06:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a3517bd-27e5-3fa9-874f-594cba7858ed | 3.03512 | -60.55417 | 2026-10-10 06:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ea53cbf-472e-32d3-8cfb-1ba1d1e122ff | -6.93961 | -59.24738 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf8acb23-4989-3311-8eaa-1a3bd6a04f92 | -6.93147 | -59.24852 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90dbae0e-c522-3d8b-9d7a-665dc3a6d712 | -3.1674 | -58.62456 | 2026-10-10 06:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56400bd5-053e-3163-bca4-b6bac2128e2a | -3.03626 | -59.16214 | 2026-10-10 06:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6370fe9a-d915-3d03-81c3-0d4541e05c52 | -5.22496 | -60.04924 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63df6b2b-d6d0-36bf-8600-33eb3e28beab | -7.45706 | -63.64027 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef4272d7-4e65-3c82-97c2-76081ffae878 | -3.78453 | -59.37947 | 2026-10-10 06:25:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 376be136-6c76-31db-8220-308ad5a89f79 | -3.18678 | -58.64178 | 2026-10-10 06:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 057270ee-b758-382a-85fb-4637b8850371 | -9.16286 | -61.40665 | 2026-10-10 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4c76ce0-27d8-3c76-a5d8-9d92fcdeefbb | -3.7834 | -59.37837 | 2026-10-10 06:25:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42b6633d-4776-3200-a6ac-22dbcb594418 | -6.92949 | -59.26341 | 2026-10-10 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e9d3f2e-86fe-37f7-8b90-933e2092fbdf | -7.44869 | -63.55379 | 2026-10-10 06:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98eb5945-afa3-367a-885a-6fa09971f608 | 1.98287 | -60.61107 | 2026-10-10 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 857c7a8c-bb5c-3804-aa4b-db7097d6689b | -3.98841 | -59.3673 | 2026-10-10 06:25:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 321723f3-50dc-3107-a16a-4f9639b75238 | -8.52036 | -67.03455 | 2026-10-10 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3218bd6a-4ccd-382b-adc2-5240cd66b2da | -5.08887 | -60.22369 | 2026-10-10 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8067191-06fe-35e2-840e-078e57233fe9 | -10.54821 | -68.73746 | 2026-10-10 06:27:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a5077c8-48ea-3c0a-a382-45e1faaeeaa9 | -10.53874 | -68.53591 | 2026-10-10 06:27:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e60f7976-f51b-371d-bc52-82669749ee09 | -10.27755 | -68.83417 | 2026-10-10 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e81d5e73-ca19-3cc4-a7d4-c671052f5ec4 | -10.62398 | -67.92546 | 2026-10-10 06:27:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4be9c8f-7620-3b21-8d46-ab834be1c4e8 | -10.16537 | -69.06694 | 2026-10-10 06:27:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c8a1bea-aab1-3d7b-b59b-b2b7a5bdd31d | -10.27704 | -68.83779 | 2026-10-10 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 538427d1-ef81-3685-bdfe-e13fd3d1a300 | -10.88445 | -68.63797 | 2026-10-10 06:27:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9718bad-460f-31ab-a81a-b465a855c39e | -9.46357 | -68.54414 | 2026-10-10 06:27:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc3b7deb-486f-357f-98e4-c6b823d5adaa | -10.16976 | -68.35152 | 2026-10-10 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bb87684-ac03-3572-8741-4adfede34835 | -10.61961 | -67.9249 | 2026-10-10 06:27:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75b55318-a049-35a9-845d-4a90952dab7a | -10.41021 | -69.14433 | 2026-10-10 06:27:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a864814-2dfe-370a-9883-21dd4ad25cbc | -9.61615 | -67.97826 | 2026-10-10 06:27:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab344f65-85bb-3371-be18-1f53df8a5aba | -10.60641 | -69.25778 | 2026-10-10 06:27:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c360da51-ceff-3b86-af22-795c2282476a | -10.10812 | -68.36235 | 2026-10-10 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0783f117-09a3-390e-9846-2be9b69f5ce6 | -9.48608 | -68.47535 | 2026-10-10 06:27:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README149.md)
