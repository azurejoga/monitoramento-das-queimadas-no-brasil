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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8162747-ee5d-3224-a344-dba813ffbfb3 | -7.4259 | -60.01 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9bf781c0-a8db-3e84-95e0-750400c30903 | -6.8202 | -56.4353 | 2026-08-16 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 90f21825-c712-3a75-8569-3fdbb4d9be25 | -8.9038 | -60.5962 | 2026-08-16 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| f8670135-c711-389e-ba3f-f826697d109d | -6.6378 | -59.0602 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 15a84baf-30bb-3d3e-890d-19eb726a559d | -6.82 | -56.4551 | 2026-08-16 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 994ea024-9982-3548-9034-95e32d660cba | -6.8597 | -58.9738 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 7c7fff0e-a0b5-3c1c-ade4-fde9d9f28272 | -6.8385 | -56.4542 | 2026-08-16 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4be1c208-9506-3867-b809-620a41e60763 | -6.6193 | -59.0802 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 4ae713a1-2f7c-39a5-ae28-ac099bc75501 | -6.6938 | -58.942 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d6214db3-98b2-3683-9033-9dd282df3081 | -8.9041 | -60.5577 | 2026-08-16 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a7409dc4-9e08-32c0-9f70-6d8c154d3ec2 | -6.2192 | -47.7419 | 2026-08-16 01:50:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 0ea208bd-82d6-3db9-b089-d0faa183b7d8 | -6.0923 | -57.7238 | 2026-08-16 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 79e48cb2-aa92-3c44-9d9e-3ad5a7ec3ba9 | -6.1108 | -57.7035 | 2026-08-16 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5b29de59-11b0-3f23-8175-7e0b497c4267 | -6.8387 | -56.4344 | 2026-08-16 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| dc99c19e-4316-31f1-be1f-df8a279f663c | -14.0803 | -58.7433 | 2026-08-16 01:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 389.4 |
| a3e094af-ad42-32b4-bc11-81fc2d89f3c7 | -6.6014 | -58.9844 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7ba736ed-df00-3484-b95a-cc9ec17b2616 | -6.6377 | -59.0795 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.1 |
| be6d5bae-ca2f-38be-8513-eba12e353877 | -7.4259 | -60.01 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c124de8f-2964-3617-9bfe-73e62d7e4a59 | -14.0801 | -58.7632 | 2026-08-16 01:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 3ea2d1ad-e7eb-31ad-a7d6-9495dcc2ca47 | -6.7124 | -58.9219 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f51c4de4-f81c-365e-9b93-077ff82fabb7 | -6.6937 | -58.9613 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 6cfcf07f-6d8b-3450-adb3-8351da4ae74d | -6.7122 | -58.9606 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| aa38a652-6d83-31f8-bbb1-8dfe991b7c15 | -14.0995 | -58.7416 | 2026-08-16 01:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| d7638e79-c79e-3d4c-828e-9bae54e1d65f | -14.3729 | -51.8893 | 2026-08-16 01:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 1df6b257-e769-3487-9372-797c037a1dfb | -14.3923 | -51.8867 | 2026-08-16 01:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 93f8bf39-6bfa-36ae-aaca-bad7e8bad475 | -6.6194 | -59.0609 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| be1f6574-bdd0-36bc-aa4f-bf4d094e1ecf | -8.9039 | -60.5769 | 2026-08-16 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| afc44449-6abb-3772-82d5-2debdf6e450f | -6.7123 | -58.9412 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 87b4b651-d930-3009-9cfd-09b8574bdc66 | -6.1107 | -57.723 | 2026-08-16 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 7f9b9cae-3a46-3d6d-b93e-58ba75dcdbd9 | -14.0612 | -58.7449 | 2026-08-16 01:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 959a535f-427c-3c8b-85b6-31bcac53debf | -14.0992 | -58.7615 | 2026-08-16 01:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| a27c7415-a14a-341c-a9b0-279cb00d7d88 | -6.7307 | -58.9405 | 2026-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 90b50777-276b-3766-9d86-c782b5d7ad2c | -6.6377 | -59.0795 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| c5e2ce9a-8b39-3e39-8c29-3a61cbbff96a | -6.1107 | -57.723 | 2026-08-16 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| d2ab772c-4a76-30bf-89c9-1b73cf7c0f15 | -14.3923 | -51.8867 | 2026-08-16 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 9861c0f1-a531-3e0b-9b87-1662178a8dfa | -6.7122 | -58.9606 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 59473134-a01d-388a-94d9-38383dbd0e5e | -14.0995 | -58.7416 | 2026-08-16 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 3f23161f-680c-35a4-aaa1-9e792508653b | -6.6938 | -58.942 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c4349cd9-d2cc-32b0-ad8d-ae555f5395e6 | -6.6014 | -58.9844 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2d0256af-070e-3092-bec4-410a6019fb2b | -6.8572 | -56.4335 | 2026-08-16 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f401d957-c9e8-358d-ad75-a280b707f972 | -6.7123 | -58.9412 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| f9ce5ce2-d31c-3b4d-a208-0d8e49a22f4b | -8.9039 | -60.5769 | 2026-08-16 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e7e0b00c-a96d-3eb5-afe6-001db46e33e7 | -13.7058 | -46.2363 | 2026-08-16 02:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 66b12721-1574-34f8-b809-ef5fe0b97ebc | -6.7124 | -58.9219 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2ee6c9c8-ae3d-3985-9a8b-3ccdab9f5df4 | -6.6193 | -59.0802 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| d925c0f9-c3db-3f8a-a797-6fb6ea03add9 | -8.9041 | -60.5577 | 2026-08-16 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a45c0c72-7e4b-3f8f-b214-ece557db9a91 | -6.6378 | -59.0602 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c3918781-ded1-3e11-8668-10ff236b98d6 | -6.3137 | -43.6178 | 2026-08-16 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b7bc49a6-f8ba-33a8-8785-6913b92ba114 | -6.8387 | -56.4344 | 2026-08-16 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ec92f3e4-47e7-36f0-80a6-4b4edb16fbaa | -6.2194 | -47.72 | 2026-08-16 02:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b27b0502-593b-3283-90ff-c184e2d11814 | -6.8597 | -58.9738 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| d380843c-a01d-391c-a0b7-2c864e18f482 | -6.7307 | -58.9405 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 5b505a3b-1c5d-3467-aaad-39ab40e22320 | -6.0923 | -57.7238 | 2026-08-16 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 16921b84-96fa-3ec3-9aad-9c9d3ca09d2a | -6.2378 | -47.7406 | 2026-08-16 02:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| f0a0ce02-5c55-3b7d-9c81-2d9a8aa4923f | -7.4259 | -60.01 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a8ca346e-8fbd-3bd6-b0a6-13e4a46e00a1 | -8.9038 | -60.5962 | 2026-08-16 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 00872865-e04d-34ae-b5e4-057a44389fcd | -6.1108 | -57.7035 | 2026-08-16 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2b919f12-caf4-399b-be1f-0985e3431a25 | -14.0992 | -58.7615 | 2026-08-16 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| bd1af0d7-5d88-39d4-8915-79dbbbc23871 | -14.0803 | -58.7433 | 2026-08-16 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 59939209-06bc-3e7f-9574-204b49854962 | -6.2192 | -47.7419 | 2026-08-16 02:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 412f7dd8-ef35-37cc-86f3-e325e1997405 | -6.82 | -56.4551 | 2026-08-16 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a41456e1-6216-3ac5-8808-8669f36a4c3c | -6.8385 | -56.4542 | 2026-08-16 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| a3e1262f-dfca-3f20-97dc-924bd53d50d6 | -6.6194 | -59.0609 | 2026-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 3010bec4-33d5-3411-a087-7aea1b603635 | -8.4275 | -62.676 | 2026-08-16 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3b417bd2-30a2-36ae-a992-6739cf8294a1 | -6.8387 | -56.4344 | 2026-08-16 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 89d5fc73-46d2-30de-97a1-bfb3162a3e26 | -6.7124 | -58.9219 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 3fbf4146-1e1f-382f-a0cc-dc34dae73283 | -6.82 | -56.4551 | 2026-08-16 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5e3762c6-6c8a-313b-be90-40eef3fd5f61 | -6.1108 | -57.7035 | 2026-08-16 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 3b13f4d1-0a8f-3759-8575-ac495e9272c7 | -8.9038 | -60.5962 | 2026-08-16 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 30386037-2a4e-3d94-ab31-867e3d1b4fbe | -6.6014 | -58.9844 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| fbade414-cd64-3495-814b-55da59c033d8 | -6.6194 | -59.0609 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 824c979a-b594-3e7c-9a67-e14f7022de68 | -8.9041 | -60.5577 | 2026-08-16 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 13e70d30-0e12-3c36-9c40-9da8a312312a | -6.6377 | -59.0795 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| b4010750-f300-3f97-a578-53c2073bf7bb | -6.6938 | -58.942 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6803bbd9-0876-34bb-8677-919aa95b288a | -6.7123 | -58.9412 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| f95ab444-e60b-3085-b8c1-a3cf3962b141 | -6.8572 | -56.4335 | 2026-08-16 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5556c748-db4b-3a99-9146-481745c3eb0d | -6.7122 | -58.9606 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 924e7fc2-3786-3d0d-8c37-1a812a83c674 | -6.2192 | -47.7419 | 2026-08-16 02:10:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| e3f3af19-9bbc-3cb1-bd4b-e7d495f26002 | -6.8597 | -58.9738 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| d4601914-5897-35a3-aa38-d5720e53ce9b | -8.9039 | -60.5769 | 2026-08-16 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 885b8c07-49b8-3508-815c-25324b0a5730 | -6.8385 | -56.4542 | 2026-08-16 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 62fc6490-79b5-364e-966e-646889c22744 | -6.6193 | -59.0802 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| c525c893-01b4-39ac-948b-e7824f6695bd | -6.0923 | -57.7238 | 2026-08-16 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5d97b647-bf49-3b7d-9cd5-707bc874ce2a | -6.6378 | -59.0602 | 2026-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e60c0798-97f7-3db3-ae7b-4cc1e614f0d2 | -6.1107 | -57.723 | 2026-08-16 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| e1cbda63-630d-3acd-9176-78274595aab9 | -6.8385 | -56.4542 | 2026-08-16 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f748023e-3ced-3584-be0d-a58e956d49b5 | -6.82 | -56.4551 | 2026-08-16 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b9845971-8972-31ba-9f11-fe08df3d743b | -6.6937 | -58.9613 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2ac917de-2899-38bb-aacf-fdedbd82387f | -6.7123 | -58.9412 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 0c257265-4dde-3e09-b501-11b1a30cc421 | -6.6378 | -59.0602 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f2c4ddd0-9e40-33be-ae8d-a1ead73f93e2 | -6.7122 | -58.9606 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2c5c55a7-a24b-3b0b-9036-8ebdf165e6f9 | -6.8387 | -56.4344 | 2026-08-16 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 43513a47-4d5d-3d9f-9776-09a41970dfc5 | -6.0923 | -57.7238 | 2026-08-16 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d77bb1f2-fd38-33c2-93b2-8d4399bdea2f | -6.7124 | -58.9219 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 875d567e-03ff-3744-8e43-0989f28c65e9 | -6.6938 | -58.942 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 63dabcb9-ac15-3002-bd1f-a94d9ca987b1 | -6.1107 | -57.723 | 2026-08-16 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 8aea6c6e-07ca-3805-bece-d4fd363aa3a1 | -8.4275 | -62.676 | 2026-08-16 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 4efce90d-28a6-3796-847d-249b0200f17d | -6.6377 | -59.0795 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 6c5f880a-ebbd-36de-8216-e6c6a8602df4 | -6.8597 | -58.9738 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 4ab741b4-3939-3322-a6c7-86a97246b9de | -6.6014 | -58.9844 | 2026-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |


[Clique aqui para ver as próximas entradas](README6.md)
