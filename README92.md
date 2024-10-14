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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a15838e2-abe4-3a62-bd2f-1a0413b0f0d8 | -17.89491 | -57.29313 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.7 |
| 1d7c9a84-5460-3e60-9ffc-41b50901f475 | -17.89362 | -57.27872 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1dabff2b-4501-39c0-9317-754770a3b2d1 | -17.89281 | -57.28329 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 28786b33-3617-3f07-afa4-50981d92e719 | -17.89201 | -57.28785 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 1f78cc0e-613a-3892-b929-36197f1898cd | -17.88832 | -57.28713 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| b3dd5382-9d57-30ef-9d55-f2e0eae0564a | -17.88799 | -57.31073 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 17e72aac-a201-3a3a-a98f-571f7b4ff780 | -17.88253 | -57.27656 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 99216d52-5abd-3bab-a885-5656cad199de | -17.8822 | -57.30014 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 886b3613-02b1-36a1-a0cb-887baaf2a9b3 | -17.88092 | -57.28569 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| fc61e36f-8034-323f-94be-ad91144b172f | -17.88012 | -57.29026 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.8 |
| 32c0c682-ca41-3437-ae9a-367f73f08222 | -17.87931 | -57.29484 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.8 |
| f6dc5adf-b6ed-3030-9993-3d7da2b49ff8 | -17.8785 | -57.29943 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4953c652-7adb-36b2-9ca0-d3d30baedc5e | -17.87769 | -57.304 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f6030902-4f93-364f-b09a-f74deea151da | -17.87642 | -57.28954 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.8 |
| 30f29da2-5dcc-32f3-9eee-246685041b9e | -17.87561 | -57.29412 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.8 |
| e097df62-397b-390a-9aea-2f6b1e891a1a | -17.87481 | -57.2987 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d6e0292a-f126-31e1-bcd6-ae81b13a38b4 | -17.87399 | -57.30329 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 700e3047-6e58-311b-a17b-795a61a2d665 | -17.87319 | -57.30786 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2a65230a-627d-3ebf-b19f-1e2f8231606a | -17.87272 | -57.28882 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 6568232c-2c92-34eb-86af-d0a91031d6eb | -17.87192 | -57.2934 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 70c72c81-2722-3f7c-b007-885086fe7b12 | -17.87111 | -57.29799 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| e2452602-2195-3ae5-957b-0659b57b1e11 | -17.87029 | -57.30257 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| d116a64d-8c54-3377-bfb3-a881ddb1bd7f | -17.86949 | -57.30714 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c451d66d-ec9d-3e0f-b309-81f5d844f97a | -17.86903 | -57.2881 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 523483f6-cc96-349f-a9d2-345996f31f4e | -17.90759 | -57.28616 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 226.3 |
| 31b90df7-d02f-33d3-9f38-d5be0e19d1f4 | -17.9047 | -57.28087 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c6fbe3db-94ab-36f4-9757-7b0cc8131e70 | -17.91419 | -57.29216 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.9 |
| 1669f017-467f-340e-8d59-6dce18584061 | -17.9073 | -57.30975 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d1baa190-578e-33b7-9642-ac2eb3464a90 | -17.906 | -57.2953 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.0 |
| c084797a-1717-323c-851b-b45c7970dc3d | -17.9052 | -57.29988 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.0 |
| 061ae5ee-8027-3813-84ba-e604273d74dd | -17.8978 | -57.29843 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.8 |
| 117eb946-e248-344e-ab4c-80f36f8324aa | -17.89411 | -57.2977 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.7 |
| 204dd833-a173-3d2f-b6d2-f1cf9cd45e99 | -17.89121 | -57.29242 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.7 |
| 0e37fe62-97c1-3ac8-907c-3f8120b2b53f | -17.88751 | -57.29169 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.3 |
| 1f14cfb5-1bd0-3145-9bd9-cfa03fea0ddb | -17.88301 | -57.29555 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.3 |
| 0d05aa8c-fca5-3cc8-89e8-30e340887ced | -17.15253 | -56.84856 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6ec18d2d-0e30-3a72-bf0b-3568eee37ecc | -17.14888 | -56.84787 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 18728db0-d66b-3e83-aa96-19dec26cc3f0 | -17.14862 | -56.87072 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 868f7de8-36b0-3f2a-b82e-23add3beba2f | -17.1481 | -56.85229 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e4a96037-bfbb-3749-9b6c-a32dbdd7e3f0 | -17.14418 | -56.87446 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 16690208-c130-3cab-9a1d-ad6a24a3811e | -17.14288 | -56.86046 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 87f4c875-6803-3331-bc2e-82908bff68fe | -17.14209 | -56.86489 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| aad433fb-17b5-30ef-9e4b-e22b05ed625a | -17.14131 | -56.86933 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a7f67315-cfd9-3787-ac20-bb2e431ffd06 | -17.1408 | -56.85782 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ce2ac5ab-02e2-3e06-9678-efb5a6a28842 | -17.14001 | -56.85534 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1cb36d43-3b4c-319e-b493-e2efe08aa898 | -17.13923 | -56.85976 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4dd8cf1f-db8b-33c9-86dc-19783e21bcfc | -17.134 | -56.86795 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ee48fa6e-a551-3f82-a57e-2cc7f68c25e9 | -17.13321 | -56.87238 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c6aec025-2348-3dad-9cad-2a11bc12910f | -17.13192 | -56.85838 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d852667c-c13d-381c-a1d1-ab4da1a01d79 | -17.1312 | -56.86976 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e091a436-8904-3c59-8a40-b70e656f954e | -17.13113 | -56.86282 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8abdd222-7734-31f8-b1fd-1be162a87b48 | -17.13034 | -56.86725 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 69cd0bc2-7d82-310b-84bf-58283e6e19f1 | -17.12908 | -56.86017 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 930537f0-1a3d-36a0-a7da-299d5492021b | -17.12389 | -56.86836 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 812bb223-f4a7-3a2e-902d-49f0de2b2a6d | -17.12312 | -56.87281 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 053dd531-08e7-3cee-8ffb-906d8a623fa5 | -17.11947 | -56.87211 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 35ee60a2-8d85-38d4-9710-7b84504982d1 | -16.86711 | -57.29781 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c06db22e-d7c1-3be4-935e-acdefb40d522 | -16.78436 | -56.70969 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 224adaaa-38af-3c97-b542-9edf13703059 | -16.77995 | -56.7134 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 62bb673f-637e-3caa-961b-55431b0df433 | -17.91948 | -57.28374 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e4cecd44-8987-39ef-9487-dcd2b6d02a11 | -17.91209 | -57.28231 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fa59f7f5-92b4-3121-9c83-0609cab5fef2 | -17.9084 | -57.28159 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2a3bdbfc-6659-3ec6-bb79-e027ada9befd | -17.9039 | -57.28544 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 200.8 |
| f7f72157-7f19-336a-9fc7-cbf86a68117d | -17.9002 | -57.28472 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 200.8 |
| 400c2b19-9ee6-3449-9724-ce5bbed833b9 | -17.88912 | -57.28257 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 4246514d-8406-3619-9739-e8b692adfc4d | -17.88623 | -57.27729 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| aaa25a67-e81f-3036-8d4f-7dc3e0b8ed8e | -17.88542 | -57.28185 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 33853f61-fcd8-3bd6-83e1-4446e2851a28 | -17.88462 | -57.28641 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| fa1d67cc-4366-37e8-9f83-f111d3337da2 | -17.87723 | -57.28497 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 9034ae6e-75ef-39c5-8fae-450984b10bb7 | -17.87353 | -57.28426 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| abfe57de-d65f-32d7-bcae-29658f49972f | -17.86983 | -57.28354 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2568973b-59dd-347d-844b-88f9419631ac | -17.86244 | -57.28212 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4f893dd7-64b2-323b-acb2-ad686c0099a3 | -17.85505 | -57.28069 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3d28a873-66cd-33c4-91a6-8bd4f3a503e6 | -17.94326 | -57.28579 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3af8784c-0aa0-375a-b082-028003a5e042 | -17.93957 | -57.28508 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 778563cd-7eab-38d6-99e2-6970da374de8 | -17.91578 | -57.28302 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ea09a6a1-7ce2-3e27-9471-56f9ae7dd262 | -17.90919 | -57.27702 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 18656fba-24b2-3784-94dc-efbeadb17e9d | -17.9055 | -57.27631 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 736c5a79-f0c5-3293-bb61-820518f10ed6 | -17.901 | -57.28016 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| eac73d6f-a048-3772-9c62-c29b061ffeb0 | -17.89811 | -57.27488 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 326bfcae-ff76-3d0c-a071-437f8adf840d | -17.89731 | -57.27944 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5927ccc2-a31c-33c6-816e-33611b5ee12d | -17.89651 | -57.28401 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| a8fbc62a-4132-3b71-9bdb-46577146c85a | -17.88173 | -57.28112 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 3da5b55c-374d-39b8-afe6-19ea31fd5b2e | -17.87803 | -57.28041 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 59f87fe9-06c5-3f0f-9687-49c66dc5350c | -17.87434 | -57.2797 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 30901e62-a7a3-39f5-be6b-1344b64a0eb0 | -17.85874 | -57.2814 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aeaecff8-ce2a-330d-8766-36b60344947d | -17.85423 | -57.28526 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 71c84b02-6a2d-3ee9-adac-af64aac3142a | -17.84314 | -57.2831 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f8fc9a98-325a-35b1-bb81-ad191951b58f | -17.7561 | -57.11847 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f47129e7-e1cd-3a6d-9d10-cbfb9281ead5 | -17.15332 | -56.84414 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 04925591-bd82-3dd5-91a1-d8828ac8b9c9 | -17.14575 | -56.86559 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ae024039-a236-356a-be50-01bf7e8a8cf7 | -17.14496 | -56.87002 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 59a7c815-f4f2-3237-96c0-cf76601d7674 | -17.14366 | -56.85603 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 168ec331-05a9-3248-9762-007d0903de24 | -17.14156 | -56.85339 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 024bc990-e053-30e4-92e8-9c153b14a328 | -17.14004 | -56.86226 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f3b8b069-b525-305e-91d8-ca2691f0cd8e | -17.13844 | -56.8642 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f2f7dee7-4f6f-3c0a-a79a-4f9928d8122c | -17.13639 | -56.86156 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d4afc951-e576-3251-9525-6b5fc57e1f70 | -17.13562 | -56.866 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ab19729f-ccfd-3d69-acb9-af0f23cd43cd | -17.13486 | -56.87045 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 778f8d8d-c443-3d31-8454-9b1cef4d8ec3 | -17.13478 | -56.86351 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README93.md)
