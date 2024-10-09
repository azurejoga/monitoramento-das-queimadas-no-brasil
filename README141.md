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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7dd202b-0f0a-3ac6-a546-47c95ec4759f | -15.67423 | -52.50959 | 2024-10-09 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60a08f0c-df3c-3103-9d57-e283567d8287 | -15.67389 | -59.40987 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1acc55d-5d89-3eca-b68d-2397b227e680 | -15.67363 | -52.51327 | 2024-10-09 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6fa0db46-de24-3295-8cc8-396b694e1d96 | -15.67245 | -52.52061 | 2024-10-09 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ba2744c-ef8d-3817-849b-095f3247ba01 | -15.67146 | -52.50535 | 2024-10-09 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97cb7593-79fb-3516-a3d5-970b270aba9d | -15.67087 | -52.50903 | 2024-10-09 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6e89788-78fc-3dd3-b683-5bff389f0468 | -15.67028 | -52.5127 | 2024-10-09 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd2cb0cb-e268-383c-9d32-2a206490006e | -15.66968 | -52.51637 | 2024-10-09 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9bd8f1ac-6e4b-31aa-8a1b-4077409cc75e | -15.66905 | -59.40899 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89af3908-7c47-361f-8d79-b7b050fc341d | -15.66803 | -59.41415 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64b60bf7-4ddd-32cb-b1f7-8c946e2241b7 | -15.66679 | -57.38935 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 137b5148-6f06-3b7f-ab19-5cfcc29bf628 | -15.66428 | -59.40771 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdd38282-6ef5-33a8-bc19-35c94ceab530 | -15.66325 | -59.41293 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7015f79-4763-3c2e-a4b9-5bb562577ec6 | -15.66261 | -57.38825 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9e8d091-24ad-3d26-a742-2f52a82aa157 | -15.66148 | -59.40556 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 958d3f76-7fd8-3982-86e3-f0cf734e34a7 | -15.66048 | -59.41084 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 755d7a16-dabb-30cd-8ba4-822552ef5150 | -15.65947 | -59.40668 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9be412c2-e661-3e9a-87d3-302c474a9a60 | -15.65908 | -57.38362 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac4b8bd5-38b5-3d62-ac41-11631f1697a2 | -15.65844 | -57.3871 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f907d144-119f-3e53-bbba-72934b745fd9 | -15.65843 | -59.41196 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f293e74-2765-3902-97b2-110a1371cd2a | -15.65738 | -59.41725 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6530c62b-74aa-312d-b900-451fd751a3b0 | -15.65633 | -59.42257 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdcf567b-df69-3a0b-9041-1fcb537ed9b7 | -15.65564 | -59.40994 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bff6fb91-acd3-3a4b-9a8d-35b60f2d9940 | -15.65526 | -59.42795 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f590a41-553d-3c74-8fba-e1438a21c27c | -15.65489 | -57.3826 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2d19764-5046-38ea-ba05-ea80e636cad7 | -15.65463 | -59.41523 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a30d3e3-a5ba-3c5a-9797-5b8a19437200 | -15.65417 | -59.43349 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c290e62-9e99-3ddc-8603-a4d3678da674 | -15.65404 | -59.44477 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9b455b8-00d2-39b1-b05e-b1af65a57477 | -15.65361 | -59.42056 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a98cc9cd-88d8-3950-b63e-44008e81f2bc | -15.65299 | -59.43945 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 890e23f6-bb5a-3950-a565-a81374a27642 | -15.65258 | -59.42596 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4fdefe15-5bb5-3fe0-88d7-710eede4c93d | -15.65253 | -59.41637 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65cc8387-af13-396f-9440-c046fceb117e | -15.6517 | -59.44594 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83a46514-375e-3792-a2be-c7c7c6a05234 | -15.65154 | -59.43148 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0974a1bd-faa8-3833-8eee-84b8c04b9395 | -15.65147 | -59.42173 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 662c6f3a-cece-32a3-b8a7-35697bf63284 | -15.65067 | -57.38166 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7891d1f6-be0a-3a13-b87b-5d6d1a9a78d1 | -15.65046 | -59.43713 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ccc1aad-b988-3040-8460-ca5171f7e1c0 | -15.65002 | -57.38519 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b501ec95-eb4d-3992-a01c-de061d518d39 | -15.6493 | -59.43269 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da3f72de-0ede-3e01-861e-c485b4be9a18 | -15.64922 | -59.44366 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dfa5540-7034-353e-8846-5c3b03f708e7 | -15.64816 | -59.43842 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f01e19f5-0026-32e6-8f30-d2efd654e876 | -15.64647 | -57.38067 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f127c81-6b6c-34f0-b512-361062206b30 | -15.64579 | -57.38437 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a72fe9e3-0d01-386e-bd87-f021dd4ecbd5 | -15.62681 | -57.36858 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff35d8ab-f5be-3d4f-b10e-a98b05052efc | -15.62261 | -57.36756 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aaaf3b1-4654-3486-8d0e-0cddea89129e | -15.61904 | -57.36324 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c122e4b3-08ad-39b8-a74b-986e3fa10af7 | -15.61418 | -57.36582 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2e9bb6e-c10f-3a83-96ed-f94345029348 | -15.60995 | -57.36496 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d5f101e-532c-380e-8326-f9c60bf4f14a | -15.60639 | -57.36545 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a8b3ad7-4c20-335e-9738-7299f7da0dca | -15.60574 | -57.36404 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b1263b2-57b0-35e1-acd3-dfb419b92af7 | -15.60492 | -57.36838 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 344e3226-9c03-30a0-a925-85ed6a896d9e | -15.60216 | -57.36464 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 557fa5e4-e96c-3f9e-9f8a-8176bb1c1b04 | -15.60151 | -57.36325 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbe0b726-9bbb-3468-8d4d-8ffcf28087b8 | -15.60134 | -57.36921 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 353381b3-ed34-3f4f-b3bb-f50e91b20015 | -15.60066 | -57.36775 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecd254eb-7a34-31a5-8777-09c2ae49a333 | -15.60053 | -57.37366 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0d7a69f-da93-3397-a60b-c08b248f26d1 | -15.5998 | -57.37228 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| edf6cfff-05e8-3825-bbf9-77b0fe1aedad | -15.59742 | -57.43158 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcb7e265-d74e-39d8-be94-f681dad9a913 | -15.59707 | -57.36858 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79d00231-8f3a-31ec-bd2d-93a0ea45fc79 | -15.59665 | -57.43567 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdb2438e-aaec-3f14-bbda-7311de0e06dc | -15.59639 | -57.36711 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b7b375f-9df4-3c14-b34f-eb2e859b568c | -15.59282 | -57.36786 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65941249-be0a-36f3-aaae-38639167ee76 | -15.58857 | -57.36716 | 2024-10-09 04:40:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0e4dd32-cb82-30fe-8048-67dd639e0c5d | -15.5542 | -55.98868 | 2024-10-09 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76222069-ab67-3f24-a8a2-1672f87bfb70 | -15.55194 | -56.64581 | 2024-10-09 04:40:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e008d148-8ce9-3156-b8b1-fd62a77d5a20 | -15.54988 | -59.34577 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a2fa5dc-c3dd-3909-bc13-9efceed1f2e6 | -15.5479 | -56.64498 | 2024-10-09 04:40:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e756072-31b7-306f-b961-1804c680e48e | -15.54778 | -59.34602 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bc6e199-b157-3927-8c7b-ad3522f2156c | -15.54454 | -56.64048 | 2024-10-09 04:40:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87380164-7f39-3ddf-bf3d-00bcccbc92a2 | -15.54405 | -59.35007 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a892953-e90d-3518-b6ea-3fd5cc21b25d | -15.53981 | -56.6434 | 2024-10-09 04:40:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 012f9ae5-7390-3d0f-b081-cea605d02fd4 | -15.53913 | -56.64711 | 2024-10-09 04:40:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c14cc5fb-2346-3085-95fb-e6d451cc4ae0 | -15.52715 | -56.89724 | 2024-10-09 04:40:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0097f734-9f4e-3584-8ff0-73a4ee3d343b | -15.42118 | -60.01589 | 2024-10-09 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b6490c9-d67d-3462-93b0-fb7177d7e760 | -15.42059 | -60.01891 | 2024-10-09 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 636619f7-8f8b-37d3-97d2-2a9d70ba82f6 | -15.41907 | -60.01545 | 2024-10-09 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1921402-acf9-3554-a95f-fa6cb70b4e45 | -15.41846 | -60.01847 | 2024-10-09 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 922d8669-e261-3ea8-9dfc-9f4f8316654e | -15.41614 | -60.01481 | 2024-10-09 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6576322-186a-3beb-9a7b-3ae1407eba51 | -15.41555 | -60.01783 | 2024-10-09 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f686a073-923d-3d25-8aac-7779179086cc | -15.41342 | -60.0174 | 2024-10-09 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ffade1e-d996-375c-aabe-53913111a832 | -15.39368 | -55.87553 | 2024-10-09 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bebf8e32-59d7-39ab-aef0-3a8c48aff194 | -15.39076 | -55.8694 | 2024-10-09 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23775019-de13-3b38-9e43-4e02af61ec37 | -15.38984 | -55.87457 | 2024-10-09 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a51d5d1a-dcfd-306a-82fc-171032173f59 | -15.386 | -55.87368 | 2024-10-09 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 115913ff-f5ba-3489-aa6c-1ab317346c7d | -15.38212 | -55.87296 | 2024-10-09 04:40:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8afe0a6-3790-3fb4-80ac-235a808c71b7 | -15.26519 | -53.77215 | 2024-10-09 04:40:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05437c65-5f89-30d3-afb1-78190e52f3ca | -15.12347 | -59.02621 | 2024-10-09 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70bb48a7-f3f5-3b1a-95f2-bbc211916111 | -15.10392 | -58.36249 | 2024-10-09 04:40:00 | NPP-375D | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51487b2e-d7ce-31a4-adaf-185c6c3ec624 | -14.79701 | -53.93468 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c4bef4e-8ab9-3113-b427-d6903ed8699e | -14.79633 | -53.93308 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d279f365-3aae-36f8-a9b5-8df2c5a86003 | -14.79347 | -53.93407 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20d58742-f893-3d62-a4e8-a6b7a1975a43 | -14.78725 | -55.98692 | 2024-10-09 04:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 158cfaad-b28d-3358-8917-822dca39bedb | -14.78218 | -53.93633 | 2024-10-09 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0e0edb1-4edb-32b3-b454-37759e3c45b6 | -14.77797 | -55.93021 | 2024-10-09 04:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd0747d4-b51d-3905-a9e8-f940df0e9c90 | -14.77689 | -55.93193 | 2024-10-09 04:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 179b0e45-b3e0-368a-90cc-d2bd13615c37 | -14.77405 | -55.92946 | 2024-10-09 04:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 548e08cb-5e0b-328c-997b-475aaa8d0636 | -14.77297 | -55.93118 | 2024-10-09 04:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca10dd8c-4e5b-3da3-b9e9-41f8210a0a6d | -14.77103 | -55.92357 | 2024-10-09 04:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d7d0f45-8773-3dd7-80fb-11af5f99239d | -14.76998 | -55.9253 | 2024-10-09 04:40:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5c8e38d-155c-3179-88d4-e91629600235 | -14.33923 | -57.58736 | 2024-10-09 04:40:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README142.md)
