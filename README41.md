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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84d3e7c0-210c-3668-8654-2efbe9f9037e | -11.1194 | -65.057602 | 2024-10-03 01:50:38 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b61bc4c-e391-3188-aaca-b49479800280 | -10.8421 | -64.167702 | 2024-10-03 01:50:39 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e51a936-7769-3d82-87a6-82badc01e7b4 | -10.8439 | -64.175598 | 2024-10-03 01:50:39 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 72e27387-fff1-30da-9432-f3faa506f2af | -10.8262 | -64.188004 | 2024-10-03 01:50:39 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c7fc920c-2f53-3ce6-92dc-6fef36cc6c1a | -10.828 | -64.1959 | 2024-10-03 01:50:39 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6157c43f-69ed-39a7-8b54-f08564cc4191 | -10.8299 | -64.203697 | 2024-10-03 01:50:39 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7d9c9511-e437-35b8-b62f-1e1544fa1ac0 | -10.6986 | -64.126999 | 2024-10-03 01:50:41 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 84c7b291-1c8c-3a52-929e-9eee3e9d1e00 | -10.7004 | -64.134903 | 2024-10-03 01:50:41 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1e6c6e-1203-3f82-81cf-e42bfffa2926 | -10.7022 | -64.142799 | 2024-10-03 01:50:41 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc3b12b8-b862-3b95-bc3e-9b40a186aa9b | -10.6924 | -64.145103 | 2024-10-03 01:50:41 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7947ca3f-94cc-397d-b8ce-98110a7a97c6 | -10.6943 | -64.153 | 2024-10-03 01:50:41 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf117015-6a12-3f89-83f8-2c085fe99f2a | -10.6826 | -64.1474 | 2024-10-03 01:50:41 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca5cd99-023c-337d-a02d-e74069952e75 | -10.6061 | -64.040001 | 2024-10-03 01:50:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c801c4aa-c9a9-3a5b-9830-24a38861320f | -10.6079 | -64.047997 | 2024-10-03 01:50:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8027d04d-2084-3ab4-9989-9a7a99518e5c | -10.6098 | -64.056 | 2024-10-03 01:50:42 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42b10c8f-7cf4-38f3-8686-0caa384ef56d | -10.5735 | -63.988701 | 2024-10-03 01:50:43 | METOP-B | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c8ea9ff-15d4-3c92-a80b-f6fd1a3b9375 | -10.5753 | -63.9967 | 2024-10-03 01:50:43 | METOP-B | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 08c407de-52f6-32f7-848a-05a8d50cb4b3 | -10.5981 | -64.405998 | 2024-10-03 01:50:44 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37bfb6aa-7894-3a50-a3b8-c972752f40e5 | -10.6211 | -64.505798 | 2024-10-03 01:50:44 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1c00776d-a216-3fd8-ba70-696c02a5b5e5 | -10.6229 | -64.513496 | 2024-10-03 01:50:44 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 19aabc50-3e74-3d29-b516-0f854ba2416e | -10.6247 | -64.521103 | 2024-10-03 01:50:44 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cb9e42e0-db91-34ec-b83e-e3df0afbf467 | -10.6114 | -64.508102 | 2024-10-03 01:50:44 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e096539b-9d08-3b96-9e61-da6a5f9edec4 | -10.6132 | -64.5158 | 2024-10-03 01:50:44 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4301851e-0802-3f9b-bfe4-79eb98d3c6cf | -10.5518 | -64.473701 | 2024-10-03 01:50:45 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf06945c-7c49-34e0-b7ca-326d6ced091d | -10.5536 | -64.4814 | 2024-10-03 01:50:45 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9f5ff8-bf27-3732-95a2-ff6f8bfffb5c | -10.5554 | -64.488998 | 2024-10-03 01:50:45 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51fb091b-6950-3c64-bb9f-bb6cee265e09 | -10.5571 | -64.496696 | 2024-10-03 01:50:45 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5bdf86cf-e5d2-3b5a-9254-437e79535972 | -9.9559 | -62.984402 | 2024-10-03 01:50:49 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 30b1575a-0d1b-3cbf-bfec-8f1d548dcfdb | -9.9581 | -62.9935 | 2024-10-03 01:50:49 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de218ed8-8122-3270-86d9-5ee4cb0a0aca | -9.3859 | -61.035702 | 2024-10-03 01:50:50 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adb7b2e2-6876-3085-8fd0-a33478194c98 | -9.3888 | -61.047798 | 2024-10-03 01:50:50 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb8b792-240c-35c5-8227-7cc20be0df3c | -9.3762 | -61.038101 | 2024-10-03 01:50:51 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37b84792-f53f-399e-9af4-c25a8a3df43e | -9.3791 | -61.050201 | 2024-10-03 01:50:51 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| caea49cb-7ece-3c5a-bcdc-416ba7d99038 | -10.1033 | -64.408096 | 2024-10-03 01:50:52 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40394220-6465-3ca5-beaf-89ce9e516f88 | -10.1051 | -64.415802 | 2024-10-03 01:50:52 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2661d08f-7458-3e78-8e42-b9b45450c77c | -10.9801 | -68.4506 | 2024-10-03 01:50:52 | METOP-B | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e037ca6e-8b83-3da6-a06d-6338cfeb07c7 | -10.0508 | -64.403999 | 2024-10-03 01:50:53 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 95eb3f46-a69d-35c9-bdbb-a8dc1d47c386 | -9.4806 | -62.373402 | 2024-10-03 01:50:54 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6a5eb0-b2f0-319c-becb-4506e80ed0b2 | -9.483 | -62.3834 | 2024-10-03 01:50:54 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45e11028-0f6a-3ddc-a465-b2adefdc6147 | -9.4709 | -62.375801 | 2024-10-03 01:50:54 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a57ce58b-d263-3226-8d0b-cce8fab1efa6 | -9.4757 | -62.395802 | 2024-10-03 01:50:54 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e7ef9ce-481c-39e8-8bce-2bdd3dd42495 | -9.4611 | -62.378101 | 2024-10-03 01:50:54 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e473958-92d4-3b7e-91be-faf4c22b8e07 | -9.4635 | -62.3881 | 2024-10-03 01:50:54 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba081ab4-ef98-3341-becb-3b7525cc5d11 | -9.9865 | -64.750999 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a746b28-b2cb-35d6-828c-812f062d16a6 | -9.9882 | -64.758499 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 60a6bdce-9447-323b-b244-93326416c2d0 | -9.99 | -64.766098 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23fac954-1908-3d98-a3c0-2f5d65b0f911 | -10.0366 | -64.968697 | 2024-10-03 01:50:55 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bfd57b14-d481-3844-9ec3-7629e49c561f | -9.7753 | -63.929501 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba20a92-85df-3455-be45-3db2588ddcf1 | -9.7772 | -63.937801 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 590c4ff6-bae1-3935-bb30-0e9a8d875d39 | -9.9686 | -64.7631 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e05b122b-315e-3e9e-885d-388f6ce90020 | -9.7655 | -63.931801 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3110df05-a90e-335a-aa22-b6fec237e207 | -9.7674 | -63.940102 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9c003fa3-4fc5-3c51-9cc2-ede61303c4c0 | -9.9588 | -64.765404 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7335bf18-6651-31fa-a30c-576a20f84383 | -9.9606 | -64.773003 | 2024-10-03 01:50:55 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b8c93658-e670-37dc-962d-83aff94c654b | -9.0774 | -61.124401 | 2024-10-03 01:50:56 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a81e7c4a-1fc4-3224-ba05-3845932f0dda | -9.5066 | -62.917301 | 2024-10-03 01:50:56 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 777a129a-096c-3626-9355-3a6923bdf0be | -9.9278 | -64.764801 | 2024-10-03 01:50:56 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fe375fda-b57f-3af2-a739-db248dbcd19e | -9.539 | -63.1418 | 2024-10-03 01:50:56 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 919d8eaa-db4f-37f6-ae05-7600857356f6 | -9.5412 | -63.150902 | 2024-10-03 01:50:56 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 546187e2-c1e3-303f-b27c-c4cf10c50b4d | -9.7341 | -63.9739 | 2024-10-03 01:50:56 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 60adb22c-5c94-38c8-a7ac-20433845dd0c | -9.736 | -63.982101 | 2024-10-03 01:50:56 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e6600b9d-67cc-368b-8842-6865f7fa9184 | -9.7243 | -63.9762 | 2024-10-03 01:50:56 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3c7dccf-a89b-3de0-8259-5ce8b15c29fe | -9.7262 | -63.984402 | 2024-10-03 01:50:56 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4287c27d-bbb5-3d89-9b9a-7268cea5e805 | -9.9377 | -64.897301 | 2024-10-03 01:50:56 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2246d5ac-ed48-353f-82f9-365a55838deb | -9.9394 | -64.9048 | 2024-10-03 01:50:56 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| adc1ca3e-1141-3c80-9712-622f9b9e5ed5 | -9.1647 | -61.6572 | 2024-10-03 01:50:56 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 41b3fee6-4252-30fe-8cc9-eb503e63042b | -9.155 | -61.659599 | 2024-10-03 01:50:57 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 90acb797-f0b8-3302-8ef8-93bc9399e59c | -9.1576 | -61.670799 | 2024-10-03 01:50:57 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 32c70c75-052d-37fe-a42d-c0fc2ea92ec7 | -9.1603 | -61.6819 | 2024-10-03 01:50:57 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b1b1446-f655-3ad7-a6f5-8a941b494a6a | -9.7545 | -64.283096 | 2024-10-03 01:50:57 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d56850f-4c58-3d0e-8858-893ec3974d8e | -9.7563 | -64.291 | 2024-10-03 01:50:57 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 15a9b5b2-31eb-3c07-9057-c7d86066c925 | -9.7447 | -64.2854 | 2024-10-03 01:50:57 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68e8e213-e216-3e07-be5a-c6edd1a97f1a | -9.7201 | -64.224098 | 2024-10-03 01:50:57 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27c9757e-1703-392c-8806-5627d62147af | -9.722 | -64.232101 | 2024-10-03 01:50:57 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7370d80-3c80-3ca7-9258-021742742119 | -9.7085 | -64.218498 | 2024-10-03 01:50:57 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7edc72e-f648-3c75-b20b-097e63020587 | -9.7103 | -64.226402 | 2024-10-03 01:50:57 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68d2d516-42fa-3f9d-8663-2bb0e8e43e06 | -9.7122 | -64.234398 | 2024-10-03 01:50:57 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b90ac764-b69a-3959-88d4-7aa5b4865d0c | -10.5276 | -67.838898 | 2024-10-03 01:50:57 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 36d09917-1ece-3cbd-8ca9-4c940ebc668b | -10.5292 | -67.846001 | 2024-10-03 01:50:57 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0054bf-02c8-3f86-a061-cd61ae721d6a | -9.8455 | -64.855499 | 2024-10-03 01:50:58 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 616e18a2-e7f6-3156-9c87-6d19ef2878f4 | -9.8473 | -64.862999 | 2024-10-03 01:50:58 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78cbf01a-f290-380c-998d-6688292b5599 | -10.9247 | -69.766602 | 2024-10-03 01:50:58 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 05404877-a9c7-3e83-9cf8-3930d6d55474 | -10.506 | -67.880997 | 2024-10-03 01:50:58 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 96d89c24-ee0d-3021-b8d1-9338512c628d | -10.5076 | -67.8881 | 2024-10-03 01:50:58 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a07833ea-3e7d-36d9-b539-36442d3fe6c8 | -10.4962 | -67.883202 | 2024-10-03 01:50:58 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fabcde8f-22af-3fed-a296-43210bf5e9b5 | -10.4978 | -67.890297 | 2024-10-03 01:50:58 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c93bc08c-b2ef-3a26-a045-e0694e01bdb8 | -9.5132 | -63.602699 | 2024-10-03 01:50:58 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 255fd489-3de1-3bd5-aa37-8fd906196505 | -9.8138 | -64.942001 | 2024-10-03 01:50:58 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 82b85305-520d-3b1f-92c7-b206d16ba18c | -9.8155 | -64.949501 | 2024-10-03 01:50:58 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 10004297-2e5d-3c90-9d59-7306da5bf829 | -10.587 | -68.391197 | 2024-10-03 01:50:58 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a1a7bc3a-80ac-3b6a-9b15-6520407f7243 | -10.6267 | -68.715302 | 2024-10-03 01:50:59 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c517dacb-657b-3a7b-8ccd-9e712d31e05b | -10.6283 | -68.722801 | 2024-10-03 01:50:59 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 31edfb4a-48e5-330f-aa48-810ca23d7ad3 | -9.6781 | -64.710899 | 2024-10-03 01:51:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0332948d-0b40-390a-abbf-cd4eb1582036 | -9.6798 | -64.718498 | 2024-10-03 01:51:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fee49e63-116f-3a0e-abd2-631b80acef0b | -10.392 | -67.876602 | 2024-10-03 01:51:00 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ee4fc38f-f98a-30f3-97c4-b0cad5e765ad | -10.4622 | -68.243599 | 2024-10-03 01:51:00 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d65235ee-5896-3710-8985-62962a5ae2cd | -10.7073 | -69.373398 | 2024-10-03 01:51:00 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9c8b74-df59-373f-8d2f-974541a0c33d | -10.709 | -69.381302 | 2024-10-03 01:51:00 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f0840daf-e155-3ba8-bf62-29539f42cf0c | -9.5501 | -64.247398 | 2024-10-03 01:51:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d28edd2b-f011-397b-8641-e862ebfd1620 | -9.5905 | -64.421501 | 2024-10-03 01:51:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README42.md)
