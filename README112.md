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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65e93d95-7548-3789-9253-4ac6ba811508 | -10.60804 | -64.39746 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 24546d8e-5c8e-3f1f-b623-a3a85b74637b | -10.59412 | -64.53534 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dca826a0-46e4-3686-b8c8-b78bab436297 | -10.58648 | -63.9859 | 2024-10-11 05:42:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b590de03-2351-31d9-9ff4-6db32e0203b2 | -10.58591 | -63.98969 | 2024-10-11 05:42:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d1ecba-21b6-3a93-ac2c-7bb5c85d657f | -10.58016 | -64.39697 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b378134e-76a4-3193-82ac-403224ea8751 | -10.577 | -64.48742 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a0e42e9-d901-3f81-9364-4d1f8d5c9189 | -10.41758 | -64.27353 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eedf7105-544e-389d-bedf-7d8f2f093b67 | -12.04743 | -64.72073 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2064b504-7abc-30c1-89ff-f13749488902 | -12.04687 | -64.72448 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b37fa351-9847-3472-92b7-0531170e1453 | -12.04402 | -64.72019 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30279eb3-2a9d-3f55-8d34-642f8f55758a | -12.36749 | -64.33022 | 2024-10-11 05:42:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5dbaea56-5f79-39f4-b46b-fb3b07d97713 | -12.364 | -64.32977 | 2024-10-11 05:42:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 497bfed7-02ff-35b6-893f-3d252c8e4a9a | -7.35274 | -64.67188 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 741a076b-76e0-3392-95dc-44484463bfbf | -7.34333 | -64.68839 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3a43257-234d-30db-9196-e4303cd5a216 | -7.30935 | -64.66509 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cac8e14-6081-3b4e-8f4a-0c90fcd89ecf | -7.30771 | -64.67563 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6558a2e3-32e5-309c-9e44-8dd3a75baa24 | -7.30717 | -64.67913 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73c35078-6d93-39cd-ba84-f6b8692b7cef | -7.30601 | -64.66457 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a05b975d-a4d4-3e58-af78-0d44f724f677 | -7.30437 | -64.6751 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71d10135-37cd-3c4f-9e52-d4043f22a27f | -7.29491 | -64.67003 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dbe83bc-c59c-3c78-9774-2225a40237ba | -7.29157 | -64.66951 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51d5932a-c755-3f8e-bce7-d70c494384ed | -7.29102 | -64.67301 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f40acc0f-765e-3856-a913-514acf3395ae | -7.34995 | -64.66784 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 002d5eea-4775-3fb9-bfbb-0fa7855b2eda | -7.34716 | -64.66381 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e423d47e-86df-3ef4-8933-58586edbbe3e | -7.30383 | -64.6786 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4d460a0-442e-38b7-b22a-5ef66fec9cb6 | -7.29484 | -64.64845 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95f9c7cb-68d0-37b1-a81a-3ecf270d1be6 | -7.29429 | -64.65195 | 2024-10-11 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a9bdeea-1d29-3f35-adba-8a36f73f916f | -9.44787 | -64.45818 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c6a85ff-e2f3-3e2a-b22e-55f310ca96f7 | -9.44154 | -64.38642 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e731103-e36c-3bc5-999b-4ccbe85608f5 | -9.39994 | -64.45445 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb3a66e2-3f04-3229-8847-8750b28225a3 | -9.39871 | -64.41703 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6688de1f-3b1e-3700-97f5-59dba036c415 | -9.39656 | -64.45393 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3163332a-850b-30c6-b2cc-ceed07d90e91 | -9.35301 | -64.35088 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1589c60d-35af-3c95-9aa7-b00b5822699f | -9.35245 | -64.35452 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a86f7d87-c142-3f6b-8290-8d97204db119 | -9.34962 | -64.35036 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69b10b4b-159f-3e9e-86e8-a4b00d909804 | -8.66047 | -64.29706 | 2024-10-11 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d5a9158-660b-3120-90a7-0797e808d0d4 | -8.65991 | -64.30067 | 2024-10-11 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd97d15e-6c66-3b84-9db0-7c94b1e9159f | -10.7069 | -65.32184 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7a46581-83c5-3d8c-b272-27a4d8a8c7b5 | -10.70355 | -65.32131 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 575ca85c-eb0c-39f4-aa08-4727170d23a2 | -10.59969 | -64.95714 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0100d93a-5aae-3ef7-ae8e-9f7f24ec293d | -10.59914 | -64.96075 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f495091-30be-3963-a881-7eb26a9d6c44 | -10.47237 | -65.28488 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b292ebb2-32bd-36a3-8849-172ae62636c9 | -10.46903 | -65.28436 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 642eca4f-fb2d-3b95-bdce-b6e315357ed8 | -9.96619 | -64.71567 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 324c9a54-ce9d-30a2-9b16-524f8737c910 | -9.96563 | -64.71928 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c00d9ae9-fce8-3f1c-8d9c-639b78c1d9e6 | -9.95889 | -64.71823 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94a3a763-09df-359c-8dee-d5bfc8b1a830 | -9.95833 | -64.72183 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dfd13cf-4063-3f14-bc3d-da9ecc3ff256 | -9.95552 | -64.7177 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efd8bc00-8e1b-3234-8a02-b9b5bb5c58f7 | -9.95496 | -64.72131 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d676fd1-dbb9-3a27-8b7c-f9ed2171a9ed | -9.56603 | -64.62399 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d40c5e76-dec6-3b10-9518-b44662ef30f4 | -9.56569 | -64.62074 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8050dff0-0d5a-3b89-82da-cbd177c33f42 | -9.56513 | -64.62434 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce233355-d3f2-34df-b471-05784a008cb8 | -9.89848 | -64.81937 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7e87f53-c2e6-30aa-af9d-db3526acc926 | -9.89225 | -64.79261 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5374524-ecfe-38d4-8e08-ba5e3e7079d8 | -9.8917 | -64.7962 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4accacf6-3b7a-3dc9-b934-6f97cd457d51 | -9.88834 | -64.79567 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0883ca77-2e9b-302a-a33b-a714663a685a | -9.88779 | -64.79928 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44cc58bf-9872-3411-bd04-4a535bd0c68e | -9.75203 | -64.8884 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09ef757c-3530-3192-84e4-866b7de5738f | -9.74867 | -64.88789 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93f0a8e7-3ec7-36b3-bb8b-032f6fa1de2c | -9.74587 | -64.88378 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e2867cd-ecfc-3f01-bca4-04b07a8e6758 | -9.7384 | -64.87926 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 00765902-4fbe-3817-90c7-452849ba9208 | -9.73504 | -64.87874 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d2c50f96-468a-3b60-bce8-76153f32a50a | -9.73449 | -64.88231 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c829716c-a5d1-35c2-8f20-1c1914c87257 | -9.65417 | -64.95731 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06a90730-a7a4-3828-b20e-ffaa0155efb4 | -9.65363 | -64.96088 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f45bab71-a204-35c6-9152-686e56151433 | -9.65137 | -64.95322 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2178d305-7895-3443-afb1-e35e84a2009c | -9.65082 | -64.95679 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 12977b9d-473a-3805-9302-230a0a178ab3 | -9.65028 | -64.96035 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6ac8efc3-869b-3906-8811-124e31b69d88 | -9.64973 | -64.96391 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 819d2ab2-b1c1-3b4e-a485-0a8ac9d57cbc | -9.64918 | -64.96747 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58a1d22f-d8f8-39f1-8836-5c6a8e91d82c | -9.64802 | -64.9527 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d17bd585-243b-3003-8bb9-0a564b8449bb | -9.64747 | -64.95626 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 578a9289-7409-3cf4-ab8b-115d2ca50862 | -9.64692 | -64.95982 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ad17aeaa-189e-3f42-a8d2-b82ad664d444 | -9.64638 | -64.96339 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08a97ceb-234c-37fa-8094-5a2b7fdd001d | -9.64412 | -64.95573 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3e47feb9-4739-3349-ac77-876f5db44b9b | -9.64357 | -64.95929 | 2024-10-11 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a92f1140-921a-3775-a417-237924a1a53c | -10.09402 | -64.84248 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efc4440b-b850-3841-9062-00660a9e2fd1 | -10.09066 | -64.84194 | 2024-10-11 05:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98eefee1-ad19-3793-9381-87cd09546218 | -11.68142 | -65.22418 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a8fcd3b-8bbb-3a34-93a0-27a104f18266 | -11.64826 | -65.19304 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbb82c61-6a3c-3d38-80fd-5627a7c7f0a0 | -11.68087 | -65.22779 | 2024-10-11 05:42:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9191b8a-3069-3b29-a41a-a0af46f156e2 | -8.60985 | -69.73145 | 2024-10-11 05:42:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32c17622-c975-3644-b3fb-3aa1875e6b73 | -8.60907 | -69.73615 | 2024-10-11 05:42:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc2a6816-c391-35d7-8f2b-8384697e4dd3 | -9.75362 | -69.13537 | 2024-10-11 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d59e307-9763-3b91-a138-16835128792b | -9.7425 | -69.06837 | 2024-10-11 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0bdf3b3-5129-3678-92dc-cb672503eed5 | -9.69226 | -69.10076 | 2024-10-11 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c01d9148-21ef-33da-b1ad-67eae7ca9236 | -17.72059 | -56.26538 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 57399113-f7c9-38de-bff9-1ce32c4c12f3 | -17.71555 | -56.25908 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c99e0eac-de54-32f4-beb1-ea2e4ed250d7 | -17.71506 | -56.26386 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 08b526cd-c522-3017-aa4d-d431e61464e5 | -17.71493 | -56.2599 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7c25a97b-48cc-3df5-bfd1-b974473df0e0 | -17.71447 | -56.2647 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| be8b58c1-d3c4-36a9-831d-12632869f0c3 | -17.71125 | -56.29816 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| df96375d-3873-3530-90a1-11de0cec3370 | -17.71112 | -56.30196 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 98dd37f9-6a8f-3b6d-91cc-70456443df9b | -17.71079 | -56.30291 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cddb4eea-6324-3771-958c-8804b5296555 | -17.71063 | -56.3067 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8611e627-7c84-3ff0-858d-3402eafa6a1e | -17.71033 | -56.30766 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c59e1817-bc0c-322a-83f1-8858d10d6f75 | -17.71014 | -56.31143 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| afbd5f17-3a68-31b2-b247-ebead76c0357 | -17.70988 | -56.3124 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 16977176-a9cd-342a-ab9b-5b502bc5bb86 | -17.70881 | -56.25923 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9be0c99e-807a-323c-bbae-f1d05ca9f41f | -17.70551 | -56.29654 | 2024-10-11 05:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README113.md)
