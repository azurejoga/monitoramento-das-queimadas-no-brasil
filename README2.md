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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 122217a4-9742-3486-b3d4-7045ac1d6046 | -6.6377 | -59.0795 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 463.6 |
| c87d41c2-d3e5-37ca-89e4-d7cf4f75c64d | -6.8781 | -58.973 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f2e412c9-b669-31c5-bf11-a515910b4653 | -7.4259 | -60.01 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c2652f86-a9b4-39a8-a385-4e7407c600e7 | -8.9041 | -60.5577 | 2026-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 4986fc54-388a-31c6-ae18-303884f43456 | -6.6198 | -58.9836 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 02d8a7ee-652c-3630-956b-a4502c3eceae | -6.7122 | -58.9606 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| b2a655eb-c589-3c1f-a79f-6e2f5ab19169 | -6.6014 | -58.9844 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 08caeab3-e4ad-39e6-b922-5df84918bb5c | -6.6193 | -59.0802 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 264.6 |
| b52352cc-b4f1-359b-9055-36cbeab92672 | -6.6194 | -59.0609 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 196.9 |
| 7545cf7f-93eb-397e-912b-317adddd67ed | -14.3919 | -51.9081 | 2026-08-16 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a69c0cb3-e2a2-323c-b3fc-74a1332dca18 | -6.3137 | -43.6178 | 2026-08-16 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 4f3c92ce-f8c2-3852-9b71-4aadeaefff20 | -6.8596 | -58.9931 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| c1c5751b-022c-34e1-8224-65b032e3fab9 | -6.7123 | -58.9412 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 201.4 |
| 5826412e-6b6b-3f09-a5b0-08c75bbef6e7 | -6.8202 | -56.4353 | 2026-08-16 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 2b3ea529-2306-39bf-a0e7-8e81030d98cb | -6.1108 | -57.7035 | 2026-08-16 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 8b857978-30a1-35b9-a210-a49f69b9e093 | -6.8597 | -58.9738 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 0603a55b-c74b-3de6-9b78-25e1ff3af47f | -6.0923 | -57.7238 | 2026-08-16 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 03106fd5-0537-3705-95a8-8e648e41590f | -6.6938 | -58.942 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| e7e8d61a-8fe3-34ed-8533-c16f62c34e2c | -8.8855 | -60.5586 | 2026-08-16 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 64b5201a-4552-3b04-8bc2-4d59ad5e6293 | -12.6825 | -48.4779 | 2026-08-16 00:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 5d24f415-d1ff-3f6c-b39d-b2158eb08e9a | -6.6937 | -58.9613 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 4a587e47-8b05-388b-aea2-d1125bcf89ba | -14.0612 | -58.7449 | 2026-08-16 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 759cca77-537a-3197-a573-d533e2323a6f | -6.1107 | -57.723 | 2026-08-16 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| ee1d928c-29a5-3858-8904-c98f29b1eb34 | -6.8572 | -56.4335 | 2026-08-16 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 646a879e-3ad6-32d8-8617-f4439cd68537 | -6.6376 | -59.0988 | 2026-08-16 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 65d710b8-6f75-3470-89dc-d3c6efa6d347 | -9.1033 | -46.3836 | 2026-08-16 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ec999931-c2c1-3cbb-a7dd-8855b94c67ab | -7.5871 | -60.8845 | 2026-08-16 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 255575cf-90da-341f-9a5c-2d51c65bb5d3 | -14.3923 | -51.8867 | 2026-08-16 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 95a4a6c1-6777-307c-88ae-cca2db8c8879 | -6.7307 | -58.9405 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a4f9702e-10f0-3f3b-b564-b8ee80be6e20 | -6.6014 | -58.9844 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f7250732-3819-39a0-831a-8209aa0b2cbb | -6.0923 | -57.7238 | 2026-08-16 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b3ade1c6-5c18-3315-8f68-1f5888c8e305 | -6.6378 | -59.0602 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 249.4 |
| 154c072d-72bc-3a2e-9429-819bedcef65b | -14.0612 | -58.7449 | 2026-08-16 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| eeeba9a5-d20e-3054-82da-5a608c59c648 | -8.9041 | -60.5577 | 2026-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| ffc501ca-2787-3b46-83e8-8f807533ddf9 | -6.6194 | -59.0609 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 200.4 |
| 5bf3519a-56e9-3cf8-822b-3da6d9b3f092 | -6.7122 | -58.9606 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| eb6264b6-02d8-3e72-a2e9-1d1016c8c338 | -6.8387 | -56.4344 | 2026-08-16 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| d0ca2a0f-7b5a-34bc-a85e-3fc8745e59d4 | -6.1107 | -57.723 | 2026-08-16 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 746605d8-de39-34eb-bdd9-34fdcbf05407 | -6.8597 | -58.9738 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 65ff4269-98b6-311e-b50b-5a0a4e872829 | -6.8598 | -58.9545 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 31c7fdb3-2ceb-3f18-952e-51819ac6f011 | -6.8572 | -56.4335 | 2026-08-16 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 91a31703-447c-3399-89d2-751bd15a0863 | -6.6193 | -59.0802 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 259.5 |
| 3f797bfc-951b-3be8-bbd1-70e0afc96d5c | -8.9038 | -60.5962 | 2026-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| a0fc201e-0a5c-3599-922b-fd2f3de7c94b | -6.8596 | -58.9931 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ceb8967e-0837-3d47-9db5-c72b76d716e6 | -6.6377 | -59.0795 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 345.5 |
| e19407b5-16ea-3a29-aa34-cbc66bcbb572 | -6.8781 | -58.973 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2167d2bd-44dc-3f43-ae29-ff3eecf47545 | -6.6937 | -58.9613 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 928f1f73-143e-3507-a348-b2ce78bc14b4 | -14.3919 | -51.9081 | 2026-08-16 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 30128f19-0278-38c2-a316-43c5ff5be852 | -6.7124 | -58.9219 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 089f9bcf-2f70-36c3-97e9-fe711880bfd0 | -6.8385 | -56.4542 | 2026-08-16 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| c659a0fe-4819-3f34-96e5-db3d0fe2e448 | -6.82 | -56.4551 | 2026-08-16 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 59a1e651-7fcb-35af-a64d-bd74fe4d9126 | -9.4898 | -51.6458 | 2026-08-16 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c0ec55be-cc39-3849-9dc1-9f897a37a57b | -6.6198 | -58.9836 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6fa80f82-7ab0-3c41-b3b7-7c38712e713e | -6.8412 | -58.9746 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6f348acd-9bbc-3dbc-ba80-487adc1ec517 | -6.7123 | -58.9412 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 196.6 |
| 3ce6973a-3116-34b8-bf77-cbf9bea2d682 | -6.8202 | -56.4353 | 2026-08-16 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f660e284-b0c5-3633-ad43-f6338357118c | -14.0803 | -58.7433 | 2026-08-16 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 35492001-0adf-3a61-b5bc-f8e8fdcc277a | -6.6938 | -58.942 | 2026-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| f71a3ab5-0bcd-3106-8534-b0d85824ea36 | -8.9039 | -60.5769 | 2026-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| cf4eff62-999d-3f75-98f2-4fb4ce98f260 | -6.1108 | -57.7035 | 2026-08-16 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 1a5bdc08-81e9-3d4f-b48c-11891d728027 | -13.8034 | -53.7911 | 2026-08-16 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 7105eac8-9803-345b-b4cc-0c349f49eb89 | -6.0923 | -57.7238 | 2026-08-16 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9f6a394b-133a-3473-83d7-df957230f46b | -13.7842 | -53.7934 | 2026-08-16 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 3dd4b1a6-c793-3c3e-949e-462c86bbbfad | -6.8572 | -56.4335 | 2026-08-16 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6c7d5dfe-dc60-3f1b-af3b-9f8b4248ff53 | -6.8596 | -58.9931 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 266c53dc-b549-30bf-bd81-75db2b1489f2 | -13.8034 | -53.7911 | 2026-08-16 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| fbb306f1-5b04-3c14-bbe4-0a88fb1aeda3 | -6.8412 | -58.9746 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c3421eb3-581a-3214-bc55-e150b443b8ac | -6.1106 | -57.7425 | 2026-08-16 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 7f50c103-1a44-3121-abf5-5e621c8d648d | -6.82 | -56.4551 | 2026-08-16 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| b19fc077-3541-3d10-ad03-541943921baa | -12.8166 | -41.5133 | 2026-08-16 00:40:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 235.8 |
| 4b983472-5d24-369b-9d84-21bd6cdaafaf | -8.9041 | -60.5577 | 2026-08-16 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| de3d902f-8623-3ba2-9648-54f41f4ab36e | -12.7977 | -41.4922 | 2026-08-16 00:40:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 52.7 |
| e394dd26-48cf-3960-b85c-5fa0060208b2 | -6.6938 | -58.942 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 22bc439c-13c2-3fa2-8878-94e98966b0b8 | -14.3919 | -51.9081 | 2026-08-16 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3700c048-3a61-3973-b18a-f31e520f64bf | -6.1107 | -57.723 | 2026-08-16 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| fd71bb31-3c94-37d5-91ac-851e6cfeac06 | -8.9038 | -60.5962 | 2026-08-16 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 274ca91c-610f-38b3-b424-3bef1426befe | -6.1108 | -57.7035 | 2026-08-16 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| c7406274-83eb-3f09-9cf3-8ccd2e1ca8ce | -6.6937 | -58.9613 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| c832ad95-a449-3bf8-874c-da23f3c9a444 | -6.6198 | -58.9836 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f57de697-1b8d-3cfc-bdfb-13dcf2e07143 | -14.0612 | -58.7449 | 2026-08-16 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 04be8e15-6224-39e7-8731-a37a94fb3b2f | -6.6194 | -59.0609 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 718761bc-ae9e-3c92-b36b-3cf14f9f1c9d | -6.8202 | -56.4353 | 2026-08-16 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 7962dfa2-1132-3719-b694-fcfeed3663be | -12.8172 | -41.4886 | 2026-08-16 00:40:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 83db5b99-dea8-32b0-964b-68c05ebd35a4 | -6.8597 | -58.9738 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 308fa408-6112-3662-a8b1-cc6f1373e988 | -6.6193 | -59.0802 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 08364a7e-cb10-382e-bced-97e1bb9f93d4 | -6.6377 | -59.0795 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 343.6 |
| 6cd31d3c-e44d-3dfb-a506-53726afa5713 | -8.9039 | -60.5769 | 2026-08-16 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 82478a42-7715-343a-9dd6-31f6b4b768b7 | -6.7122 | -58.9606 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 748bad41-8dbd-3c99-bb12-cc87c5b73b00 | -6.7307 | -58.9405 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 41e8ce51-90fb-37a3-aa05-126892a51f7f | -6.6378 | -59.0602 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 226.5 |
| 3f31184c-50d7-31f8-8e1b-b23e5df4e2a5 | -6.8387 | -56.4344 | 2026-08-16 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| a9720649-7981-3803-9cdc-bbde1cf7c686 | -6.7124 | -58.9219 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 7eb25f1e-e8ff-39c6-b7e6-f4bd94725d16 | -12.7972 | -41.5169 | 2026-08-16 00:40:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 191.0 |
| 9114bd1b-7df8-3cfa-a6d5-f878fca82408 | -6.8385 | -56.4542 | 2026-08-16 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5eafa82b-be8d-39d4-9f56-c55562a51346 | -6.6014 | -58.9844 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 630593fe-6aa9-32c4-a706-57b6702a0ced | -6.8781 | -58.973 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7b8b1b55-bdfd-3ee8-9f7c-23477bf2e773 | -6.7123 | -58.9412 | 2026-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 211.0 |
| 3f29a5e4-1ba6-3e4e-846a-b6a4b71cf2cf | -14.0803 | -58.7433 | 2026-08-16 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 493c0421-1626-3b9d-a836-357c30009f24 | -6.7122 | -58.9606 | 2026-08-16 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 597b5740-eeb8-3d88-ba3b-7f3c5e2f1284 | -6.8572 | -56.4335 | 2026-08-16 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |


[Clique aqui para ver as próximas entradas](README3.md)
