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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a6e8226-c6cb-3812-aa38-ca0f6eb16187 | -7.00996 | -49.33851 | 2024-10-23 05:16:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 311713fb-a9c9-35f1-8616-19ce58568df2 | -7.00945 | -49.3422 | 2024-10-23 05:16:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a436eda-e3cb-33e0-a373-b93acc9bd5f7 | -8.73875 | -50.05658 | 2024-10-23 05:16:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1f4cdeb-9ae4-3b24-bd66-e5023e61796b | -8.7383 | -50.06005 | 2024-10-23 05:16:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c3dbc56-a10e-3329-bd15-bc9f91e7eff5 | -8.73657 | -50.05859 | 2024-10-23 05:16:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c938256-43f7-397d-893e-8e63a98920e3 | -8.73288 | -50.05929 | 2024-10-23 05:16:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff47467-73fd-3493-ba09-c635757acb50 | -8.1791 | -49.75567 | 2024-10-23 05:16:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 227abb74-7c4c-3eb9-b409-c80fb7bd6f1e | -7.97583 | -49.68563 | 2024-10-23 05:16:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43bb01d3-8666-3c40-b48b-244b5bdef530 | -4.42578 | -49.8028 | 2024-10-23 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6f22716-6419-3bce-866b-b8bf6c05bf9b | -4.42059 | -49.8021 | 2024-10-23 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad59271c-be07-3b43-a2a2-e6cd7d03b052 | -4.42015 | -49.80519 | 2024-10-23 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c2a921d-74be-3046-a6e7-a4303dd80479 | -4.38446 | -49.75546 | 2024-10-23 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7f47c22-d82d-30cb-9095-9fd34ea4ea24 | -4.38402 | -49.75848 | 2024-10-23 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf35a876-73b7-3a67-bece-bfd687d25872 | -4.38046 | -49.4155 | 2024-10-23 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e02b534-2a98-3a8a-91a7-353384f7b926 | -4.37928 | -49.75467 | 2024-10-23 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85bae5c2-9a93-3e31-9251-6f7f3a887268 | -4.37883 | -49.75771 | 2024-10-23 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07ecaf52-3b70-34d5-8211-bece6b116c38 | -4.37516 | -49.41463 | 2024-10-23 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a196a417-a7df-3b0f-bbe3-aebe113ecbee | -6.44842 | -49.91454 | 2024-10-23 05:16:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf9f947a-d051-3535-a0b4-2ae49d33d426 | -6.44798 | -49.91769 | 2024-10-23 05:16:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 863799a7-39d6-32b8-8201-b02787d6901f | -6.1019 | -50.97018 | 2024-10-23 05:16:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d068ada8-1389-3ac1-8253-dafba4bcce2e | -5.85337 | -50.05085 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baa50fef-7706-3b1c-9d80-7813206504dd | -5.85315 | -50.05083 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d00593-8976-3592-b6bd-839cf2fa4353 | -5.755 | -50.2209 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e97f565e-7a7a-349c-8798-3a3900e753ab | -5.75458 | -50.2239 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae302cc1-fcfe-33c5-a8aa-cd0826fe6cdc | -5.75416 | -50.22686 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79db6485-3f8a-389f-a3e1-cbec737c1d00 | -5.74988 | -50.22008 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f18d8c9-8b05-39e0-b8ba-268366dab257 | -5.61334 | -50.01146 | 2024-10-23 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75598857-301f-3c2a-82f5-3da9a52aaf04 | -5.24354 | -50.88198 | 2024-10-23 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b02795a7-54e4-3347-aa86-dcc3afdf7603 | -5.23712 | -50.89206 | 2024-10-23 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff0129b3-873d-3ee4-9d55-66c53e864a88 | -7.98029 | -50.15938 | 2024-10-23 05:16:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6db2b95c-c9df-3f0e-b004-2f15ecb987a7 | -7.97985 | -50.1627 | 2024-10-23 05:16:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa1a41bc-b56c-3062-8954-22e6ee4c3511 | -7.98547 | -50.67334 | 2024-10-23 05:16:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27604266-14d1-3cf8-8820-3577fe6b91c3 | -7.98504 | -50.67642 | 2024-10-23 05:16:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52737975-3863-3573-a432-c6c1f54acdda | -7.98032 | -50.67265 | 2024-10-23 05:16:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5236a24-da63-3761-93ae-04942e0a52c2 | -7.9799 | -50.67573 | 2024-10-23 05:16:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91aac24c-c975-3b01-b5ef-e24e50ebe0ad | -7.97947 | -50.67881 | 2024-10-23 05:16:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bb0dfba-9063-3dba-9113-d6c0f84e78ba | -4.63572 | -50.91413 | 2024-10-23 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ee65a63-82bd-3fd9-a03e-e6f2c4b11f3a | -4.61087 | -50.91599 | 2024-10-23 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 555565ca-506b-3efe-a798-af2a56d7a225 | -4.61012 | -50.92109 | 2024-10-23 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74706e35-43fb-3e42-9a31-2a311ed7159e | -3.8902 | -52.12541 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6534e79-c156-37b2-b799-4f7a6eeef11c | -3.88202 | -52.15025 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77dfc8ad-5a31-31c2-aca3-c5e8a89f5a8f | -3.84899 | -52.13213 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b4fe3b7-f634-31bf-85ce-aa41a1d10e36 | -3.84867 | -52.13387 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b536d579-3910-3f55-87b0-579f863a1290 | -3.84838 | -52.13631 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4194d718-bd4d-3f1a-af85-569a212e5b8a | -3.82342 | -51.3844 | 2024-10-23 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55630a8d-5db5-3c65-809e-31d627e8644e | -3.822 | -51.8947 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1f8ee00-79e7-3eb5-b1c0-5d7fe690cefe | -3.78443 | -52.17505 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 635fcf09-1657-3e9d-88f7-e02fcb43848e | -3.78381 | -52.17919 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 967ec565-5517-3acd-8bfc-70eaf0501b4c | -3.6802 | -52.09167 | 2024-10-23 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07ac2a25-4b88-33dc-8f5d-2568420afb7e | -11.60205 | -54.49967 | 2024-10-23 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0c935bc-c424-322b-97bb-0726364f653a | -11.5124 | -54.33739 | 2024-10-23 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4435f0a-a0cd-37ab-8485-bb6cf00f98eb | -11.41482 | -55.07478 | 2024-10-23 05:18:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0322453c-91b7-3798-9ce1-0b61e1eb4ed3 | -11.33424 | -54.3531 | 2024-10-23 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 48e1be74-a194-39b8-9b91-d6cd5319aa0f | -11.33003 | -54.35255 | 2024-10-23 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d0c9edc-897e-3985-bbf9-bde2335b265a | -12.50435 | -54.43118 | 2024-10-23 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64ba411c-6052-3ff3-89eb-f94f816a56c4 | -12.5038 | -54.43517 | 2024-10-23 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d77b31ca-38e8-3de4-ad8c-d0d1b9e405e9 | -12.49956 | -54.43457 | 2024-10-23 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03e4feb7-952e-30bf-8837-1962a81dfa0c | -11.88226 | -56.4133 | 2024-10-23 05:18:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ab28a0d-a664-322c-88f3-bb5c89f63a34 | -11.87789 | -56.41726 | 2024-10-23 05:18:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a320d6b-24b1-3b02-ade5-e69318768203 | -11.87416 | -56.41672 | 2024-10-23 05:18:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3139e929-4fe1-3ed0-b301-4135c467bbec | -10.94765 | -55.45198 | 2024-10-23 05:18:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 758d595c-de54-3e18-96a6-996a588fdcd4 | -13.06419 | -57.26178 | 2024-10-23 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6d66eb9-bcf2-317f-af47-342ac53d1471 | -13.06058 | -57.26124 | 2024-10-23 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 617fc9f2-75da-3810-8b2d-6e08f70f5c9d | -14.85055 | -56.44941 | 2024-10-23 05:18:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d2bee29-f012-3b74-9783-5d483626a78b | -16.96124 | -56.79447 | 2024-10-23 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c1b144da-e9a6-397c-85e1-f471a56a3538 | -11.808 | -57.36501 | 2024-10-23 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af6aba64-379a-38bc-a6db-83a0b9cc3cd2 | -11.44892 | -57.77392 | 2024-10-23 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f482b77f-77d3-3ce8-94cd-363a4ea1c6a4 | -11.44603 | -57.76951 | 2024-10-23 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1618208b-fdf2-323d-aea9-04c3839a1f9c | -10.48111 | -59.2734 | 2024-10-23 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c12d74d1-2837-30e4-a3d5-7a2d54dc401c | -10.4357 | -58.82349 | 2024-10-23 05:18:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ef28355-665c-3c75-bca9-134d4bf3644f | -10.99135 | -58.65951 | 2024-10-23 05:18:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aebc1af4-1bb4-3f3d-82bd-6145add82f52 | -16.09538 | -60.12862 | 2024-10-23 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bb08b97-7390-3bb1-b015-59278d30647a | -16.09202 | -60.12807 | 2024-10-23 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5f26d66-2df6-35a1-b5c5-36664a5f893f | -16.09146 | -60.13172 | 2024-10-23 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ee7f1a0-2deb-3292-8ad4-9d5e9f2df6e2 | -16.08867 | -60.12751 | 2024-10-23 05:18:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80414ec1-8411-3e9e-97df-576225b10149 | -12.06266 | -61.063 | 2024-10-23 05:18:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a37658a8-7d77-3639-ba2d-f03a8d29f206 | -11.51218 | -60.73482 | 2024-10-23 05:18:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 77135c19-d534-3b03-b45c-e96fb104215f | -11.37502 | -61.27565 | 2024-10-23 05:18:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 192cdc89-42a3-350a-a123-8a7bb0750d49 | -11.21465 | -61.33967 | 2024-10-23 05:18:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 253594cb-ffd9-37d9-9323-8e6bea79c759 | -11.11342 | -61.31578 | 2024-10-23 05:18:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4df24cd5-3139-395e-9a1e-d5f7e92d9698 | -13.36553 | -61.34924 | 2024-10-23 05:18:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab017f7e-2dbe-3ae5-b505-71ee7b07b45c | -10.16384 | -61.95276 | 2024-10-23 05:18:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a237f79b-1417-3e84-85a8-48d9cb8ae321 | -12.80404 | -47.8945 | 2024-10-23 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee1a6464-e3be-30a1-b6c5-12d60f795a13 | -12.80339 | -47.89172 | 2024-10-23 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3114d02f-fe3a-3fc9-abac-117442c78b70 | -12.19809 | -50.36532 | 2024-10-23 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75d021bd-5983-3f62-b3d0-6100e1eb8c1e | -12.19762 | -50.36904 | 2024-10-23 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d8935ad-44f5-3137-b3ad-eaddabcfe00b | -12.19635 | -50.36398 | 2024-10-23 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0f553ce-522a-322c-90f7-4abe7fe05bb5 | -12.19591 | -50.36771 | 2024-10-23 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 50db361c-6c2b-3c4c-a654-c7415d9fdd82 | -12.19252 | -50.3646 | 2024-10-23 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6cd032d-de6e-353c-83f4-3741609a7c3a | -15.90659 | -51.74425 | 2024-10-23 05:18:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0b10130-5de8-3c4e-92df-d1268a6efe6e | -15.9062 | -51.74767 | 2024-10-23 05:18:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e73963d-87df-30df-af3d-b7979ce10b96 | -15.90581 | -51.75105 | 2024-10-23 05:18:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24a61c08-1610-313b-b958-091f575f9dc6 | -15.90125 | -51.74356 | 2024-10-23 05:18:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8096c08-756e-3813-a3db-c0fac22068ae | -16.23836 | -52.60172 | 2024-10-23 05:18:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abc061e4-0bd2-3b53-a75b-bbf5ef849ed8 | -16.23783 | -52.60622 | 2024-10-23 05:18:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d5f7c6c-12fe-344a-893a-21a7251f8567 | -18.3142 | -56.21793 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5c0ca8db-f201-38e3-a12a-707b9a091119 | -18.31372 | -56.22173 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 03dce042-a0af-3d64-b5cf-cf9d7d20485a | -18.31106 | -56.20974 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 916bcc1b-05cd-3968-b284-35cd91ef211c | -18.31058 | -56.21354 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5de57e35-b5ce-39ad-84e7-4bd0584a58a2 | -18.3101 | -56.21734 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |


[Clique aqui para ver as próximas entradas](README57.md)
