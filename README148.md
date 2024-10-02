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
| 36bc216a-7bfd-3e7a-83c7-decbad993b5d | -15.90052 | -57.174 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b16666c-25bb-3c0d-98c2-beeecd4e7308 | -15.89993 | -57.17811 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 881e8c56-55d1-330a-bb41-ca631cf66abe | -15.89935 | -57.18213 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a52a5442-e659-30d0-87b5-9219ae273dd4 | -15.89644 | -57.17758 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e861b6d-ae4a-32c7-9f2b-a5dfdfb9a47f | -15.89517 | -57.17856 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2261ad6c-c380-3f98-82f7-c6702b65a7f3 | -15.89349 | -57.16587 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16215f07-58bb-32c8-9cb6-e54588557bcf | -15.89296 | -57.17704 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 177b4e2f-05f1-3a21-88e3-461bfbd37d8d | -15.89238 | -57.18104 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28734e6b-4d3e-33eb-872b-a6c51d7ff9d4 | -15.89169 | -57.17801 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 325f29d3-1a48-3c36-9137-2287373a6f46 | -15.8911 | -57.18198 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92afee8e-cc19-39f3-a76c-71009c9aa1ba | -15.8906 | -57.16133 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ef138ee0-dc01-376c-9388-4d251a74110c | -15.89 | -57.1654 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 569c133f-a7b8-38fe-a41d-8eb11fa3aa4e | -15.8894 | -57.16942 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40734be3-88c9-3f37-ba6d-0093bf4d81a2 | -15.8888 | -57.17344 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9680bc5b-85b3-3031-a47c-8a49da67049f | -15.88821 | -57.17745 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61511342-5afd-3565-8919-472eee351766 | -15.88762 | -57.18142 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0d2380a-acb3-347d-9462-1fb994b0d83b | -15.8871 | -57.16087 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 82e76447-a7a7-3a44-9abe-c4a3e8c90619 | -15.8865 | -57.16491 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b463f0f6-ea8a-3134-96bd-dd05ac8d7f9a | -15.88472 | -57.17689 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df27fada-f4aa-330e-944a-0dd6e983b5f6 | -15.88414 | -57.18084 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbdade23-c0d7-3eaa-8b08-b471af51846a | -15.8836 | -57.16039 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d30c025-e69a-3ac3-a913-e9ec6c065369 | -15.8801 | -57.15992 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d2c12013-5bd1-3b61-9fb8-0a5f8dc99668 | -15.87661 | -57.15942 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e299c7a0-f010-322e-9e1a-0328a4b704f4 | -16.45742 | -57.36839 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 61aeae92-6020-3132-a6b4-088498a39997 | -16.45741 | -57.3441 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3e861125-0389-3614-a93e-dd0f9c0fe539 | -16.45685 | -57.39659 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4f1d4588-b004-324b-8666-363d3f7a05de | -16.45685 | -57.37234 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 16a27672-eb12-3cd1-aad8-5669e9a7ca76 | -16.45683 | -57.34806 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 89c7e8fb-9d06-3792-8694-1d33dbc9f384 | -16.45682 | -57.32374 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c1617a1b-d518-3515-b332-40aa5b22b14e | -16.45628 | -57.42473 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 848cca56-c497-3e5a-832d-9cde66ff9b20 | -16.45626 | -57.3763 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a7ebdda0-d0fa-38d8-b410-4d04133ff4c4 | -16.4557 | -57.42867 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 659a245b-0d4a-320d-93de-1f52323eed02 | -16.45512 | -57.43262 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 982b2e7d-3b3e-38c6-a1b8-f4440e11e66a | -16.45338 | -57.39605 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e47a999d-b159-3eeb-8067-4f77c2d306ff | -16.45333 | -57.3232 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 70e5b959-8745-3436-bb94-91fd40e827d9 | -16.4528 | -57.39998 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 656af6ef-dd24-3c94-8afb-44e92097f655 | -16.45165 | -57.43207 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b46c5136-cce3-3bec-adb2-2bf6864b7d37 | -16.4499 | -57.39549 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e055de61-a9db-3dae-b7fc-2906a27c453c | -16.44932 | -57.39943 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3fb6b792-1e62-3aca-bb90-c55bc187b26e | -16.44927 | -57.32662 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c0a8927e-9313-32e8-8e08-5cdc8b7b9f5a | -16.4487 | -57.33058 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d833178d-c3c6-3d61-9df6-c74492c32c6b | -16.44818 | -57.43153 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ab9034ac-da0e-3b0a-b6db-43da49f2a42d | -16.44812 | -57.33455 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ecce3eb7-f5df-3476-83e4-4e56c2ed5238 | -16.4476 | -57.43547 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| f8a29c0b-d6ea-39b1-87d3-c6011b04fca1 | -16.44585 | -57.39889 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b9bbcdbf-91d4-3273-8f74-61a098346dbb | -16.44527 | -57.40284 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b7a5a8b1-cd2c-3a2f-8b76-f0c918f2756d | -16.44521 | -57.33003 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f4b50787-3fe9-3acc-9efc-9596337fb015 | -16.4447 | -57.43098 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 639741af-0fc4-34e0-823b-691c29621511 | -16.44464 | -57.334 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8630014a-26ab-33e7-830b-6c993b8d29a1 | -16.44413 | -57.43493 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| e4176b1f-2012-38fc-8161-99c66bb77a76 | -16.44238 | -57.39835 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c0eb7b14-78e7-3af2-95d3-6afc0fa60597 | -16.4418 | -57.40229 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bed0f980-4d87-3f67-85a4-65dc27c6699b | -16.44124 | -57.43044 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b8712498-0c2a-37b8-aea1-7ca55358d500 | -16.44066 | -57.43437 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| d5c18105-a25c-3bd1-9a3e-6d7a94396824 | -16.43428 | -57.40513 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| de6286c0-486c-3b3d-8555-1e7575c5e6d7 | -16.4337 | -57.40907 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e4e7edb6-3efb-3271-94e8-989a339f26e0 | -16.63032 | -57.21906 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 56adb31d-fa31-33f4-8d4d-381238a6aea9 | -16.62741 | -57.21449 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d3109a13-7858-3d20-9a77-58b7e83051df | -16.62682 | -57.21851 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 28ad30f4-b652-3080-893c-49cf0bc1b7f4 | -16.62391 | -57.21394 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5eed5e36-2c58-35fe-9d27-bfa80fbe1d6b | -16.62332 | -57.21796 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 51522ba4-7951-3cf2-9ab0-82d6033677b9 | -16.62272 | -57.22198 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 53fc34b7-8dd8-371a-a640-9b0c9b936103 | -16.6204 | -57.21339 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9592ec76-05fc-3020-9bd6-f9790d37d298 | -16.61981 | -57.21741 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 00ee2890-0640-38b8-a07f-fbaff9e26a94 | -16.61922 | -57.22143 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 1e5e6428-60fe-3492-81ab-7df8e7ac03b2 | -16.61631 | -57.21686 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 9a06f173-3bed-3d88-98be-9ab9919ad876 | -16.61572 | -57.22088 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 92476a00-41ed-3736-8c12-b6242297b9e1 | -16.61222 | -57.22033 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 6e5982f6-0417-3133-80b0-b15ba45e5304 | -16.61219 | -57.24496 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 728f19f0-4ba6-3c26-8a6d-52be74bc0dca | -16.61163 | -57.22435 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| e2f67349-f593-3c8b-a0c9-89e70dea39d5 | -16.6116 | -57.24896 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9bac2257-fe8a-39c2-bee8-ba7e02b4c6c5 | -16.61104 | -57.22836 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 617d0612-107b-3bb9-bc0e-507a3a6f9d12 | -16.61102 | -57.25296 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 30c14a91-2ea0-371d-80e6-18e0d186f394 | -16.61045 | -57.23238 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 6b20c342-4cf1-3bbd-a094-990eeb7b12f1 | -16.60987 | -57.23638 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 397f883c-69c6-3168-ba71-c7a0d6275465 | -16.60928 | -57.2404 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 8dd28929-ffc6-3e87-9b41-99ef28b4b9de | -16.60869 | -57.24444 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 6fc5b703-83f4-3822-9c6e-bb52d1772549 | -16.6081 | -57.24844 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8fb764ce-33ae-3e6d-a5dd-c5a0c25ee340 | -16.60752 | -57.25243 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4c75e03b-10ac-354a-915d-3b03083cc05d | -15.7947 | -57.80251 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2352591c-56f5-3d75-aff2-fb6573fce7de | -15.79299 | -57.79063 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0170c105-b9f7-3199-9b7e-9bdbfcf8c460 | -15.79242 | -57.79442 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ce27482-d2a6-300e-badb-e7c1abcd72ce | -15.79072 | -57.80575 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 812fc4a3-acc9-3973-91cb-a7057dd25f5a | -15.7873 | -57.8052 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8e0c04a-a055-371d-a8a1-a2d587066052 | -15.78674 | -57.80898 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5609e22-2b7e-31af-95a6-0bd8ee4dce2b | -15.76854 | -57.79061 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d83dc218-9514-3a76-90c8-ba3f4d03c267 | -16.58129 | -57.2851 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 04ae011b-10be-3e0e-9035-39d3b305cf98 | -16.5807 | -57.28909 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4956dd22-876c-3a5e-b686-d3041111e056 | -16.58012 | -57.29309 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 470a2d98-b78f-38c2-a0c3-72a902fd18bc | -16.57779 | -57.28455 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d5467b74-2168-383a-8743-a8ed413389b3 | -16.56678 | -57.40873 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 078a558a-69b1-3729-97a2-a30ae8a5658b | -16.5662 | -57.41268 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 45760c38-2aa1-30c6-8f4f-5be43b956437 | -16.56272 | -57.41213 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 55b2d255-ff65-3a0d-b0ac-d8e605cee3af | -16.54709 | -57.42178 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b072c3cd-4518-3c4d-a542-768a1c4b9e8f | -16.53008 | -57.29339 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 2f3c4445-76e0-3bd7-8fe7-1e31fd29f59a | -16.52659 | -57.29284 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c0febd18-9fd3-3e6c-aa5f-6569d9875990 | -16.52601 | -57.29683 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 47b54999-ddf9-37df-bd92-38e2271c98e7 | -16.52544 | -57.2938 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 21561119-0ca9-316e-b016-3a0761b474a8 | -16.5231 | -57.29229 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 70b65e20-b1f2-3621-8702-0eaa063d6a06 | -16.52252 | -57.29627 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README149.md)
