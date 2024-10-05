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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcebab51-5f08-3453-83ef-d19639950d55 | -17.11634 | -57.38488 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a53e0c3d-4b55-366d-8890-e457c64dc179 | -17.11615 | -56.77385 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 98d7fb11-3a5b-3ae6-9732-cb3c95decea2 | -17.11606 | -56.7457 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1c47ebc9-c53a-3e31-84fd-dfe3a7608f72 | -17.11603 | -57.41577 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 9ebaabbe-9f1c-3848-9b2d-fc482d8fb1a9 | -17.11518 | -56.77832 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9ac9279f-f29e-320e-a01c-605398f2d136 | -17.11422 | -56.78279 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c6349696-6296-3fe8-a6af-481054508563 | -17.11228 | -56.79172 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a3867a8e-9d60-38df-9487-3481d5bb1cb1 | -17.11132 | -56.79619 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4a190b08-88dc-3ccc-a3c0-68f5160d91cb | -17.11123 | -56.76797 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ee12fd72-7a26-3e0f-9f81-9e1379fc1b30 | -17.11034 | -56.8007 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 6f8bfdbb-0ff0-3fe2-8a91-65b3da36075c | -17.1093 | -56.77689 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8bbdd1d5-e9c5-3672-86eb-212e0964b59c | -17.10639 | -56.7903 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1d92fb62-fad1-388e-8178-caf4e734278b | -17.10543 | -56.79474 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a970034d-2a9e-3c68-863a-1404c0cc6cdc | -17.09953 | -56.79335 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 641f5714-e93d-3421-9721-5cd771da6852 | -17.09855 | -56.79784 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0c411b52-f4c1-35b0-9fd1-1e44bb0fd7c0 | -17.09363 | -56.79194 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0c7a847b-5fc0-3b41-b9d9-b61025c5f574 | -17.08774 | -56.79052 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ecc6814c-c64c-3918-b677-ff846d7c0024 | -17.08676 | -56.795 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 323f89b7-d593-36e7-8f2a-48471ef30bc2 | -17.08574 | -56.77124 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f8f9fee0-b0d9-3f20-8a51-cc5c9639dad5 | -17.08477 | -56.77571 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8132b06b-a472-3b6f-b047-83bf665ab108 | -17.08379 | -56.78019 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4fa4a67c-96a0-3df9-84f2-bfb3576a37d5 | -17.08353 | -56.67971 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 257cfa4d-f7b6-3084-9e85-fb82b9646166 | -17.08282 | -56.78465 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 870f0a2c-abc9-37c1-88d3-549295389365 | -17.08235 | -56.77277 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 1332622f-583d-3331-8475-eb3663aa0045 | -17.08184 | -56.78913 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5c343a96-381f-3558-8946-5b32ad6cf2ef | -17.08162 | -56.67715 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bc7bfe24-b3c3-3a84-b714-f7e636877ef4 | -17.0814 | -56.77727 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 46bc59c3-77e7-3282-bec9-e0430dac7b1f | -17.08086 | -56.79361 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 53862f5a-0809-3e87-93cd-17d23480ce76 | -17.08065 | -56.68155 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e42de0b4-ab14-387f-b147-c72cb2de1181 | -17.08045 | -56.78176 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e283d19a-9793-3b58-80b1-d404f3cca981 | -17.07988 | -56.7981 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 747854ab-33a3-36af-979f-3632ae83f6e7 | -17.07986 | -56.76981 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4bd613cd-c66d-3886-8d65-20ac2d2a87d1 | -17.0795 | -56.78624 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 66b71a5c-6351-3a92-9407-d6b358c7d78b | -17.07888 | -56.7743 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f6e1316d-3e37-3981-9293-8e7b896a320a | -17.07855 | -56.79073 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 176b1f32-ed52-3d15-99e6-3edea24863e2 | -17.07767 | -56.6783 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 69a1ccab-95d0-3dac-b0bd-b99c6f3df514 | -17.0776 | -56.79523 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 06bea48c-b6ae-3afc-90ea-2c31a1cf5f31 | -17.07692 | -56.78326 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3295849b-d750-3705-9746-7ea83a7e205c | -17.07665 | -56.79974 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 09f581fb-9be1-3387-994e-778fcf761ce2 | -17.07576 | -56.67576 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bebf0fa4-7ace-3580-85fe-138864f70f9e | -17.07551 | -56.77585 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ed74fe25-43ed-39a4-9729-b7fe7dfde1d3 | -17.07397 | -56.79671 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 75508d9e-9076-34fc-bd83-44a01ec4c266 | -17.07299 | -56.8012 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ec19b58c-91e4-33d5-ba4f-6a65e66db4e4 | -17.07088 | -56.68129 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 49841022-f474-35cc-9b4d-b60d6de21aae | -17.06894 | -56.67876 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c25634a5-4bdc-33b6-bd63-f0a7a33804ac | -17.06797 | -56.68316 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f86fb17d-fc9e-3b50-9e21-98ce2e3d3eec | -17.0661 | -56.80428 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b33c91f1-7d38-359c-ac27-7e29e71015de | -17.0602 | -56.80286 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3dc8c62e-3882-3b7e-b987-00f0ae5da3d5 | -17.05758 | -56.06527 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 70155f11-3721-324e-a902-41a4c07739d8 | -17.05673 | -56.06932 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e0780e87-f138-3fe3-a3c6-38bb47a7b006 | -17.05046 | -56.69031 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| af1092d4-a301-34bd-a4b6-b7c55e73bbf8 | -17.04952 | -56.69472 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 18fd40ca-20e2-331a-8153-aa46655f3496 | -17.04939 | -56.79552 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7f2a90a5-69a3-305b-8497-b73940001734 | -17.0446 | -56.6889 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| dab0d82f-2d06-3e80-b91b-0f2869244f07 | -17.04365 | -56.69332 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4d8d4cee-6c4f-3ca6-ae73-7ca730640ee0 | -17.0427 | -56.69773 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d4bb524b-e8ae-3d75-bb1b-f23bf001ee3d | -17.04029 | -56.79567 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d58cf32a-9389-3e17-a41a-dde7ac1a2bfc | -17.03968 | -56.68308 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 11ee7b1f-0f3e-3a52-94da-e54e887f278f | -17.03874 | -56.68748 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| fcaa349b-269e-3089-b974-94e95790860f | -17.03779 | -56.69189 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 040b4dc6-3b84-3f90-bfb1-5b782599e17e | -17.03684 | -56.69632 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 981ba7dd-1936-3015-817b-1de83e014957 | -17.03589 | -56.70071 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 05daf7f1-3888-3477-822f-8afc097ac7ce | -17.03494 | -56.70513 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e91097be-85d8-3599-b715-4fc25bfd4d01 | -17.03439 | -56.79425 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0d5d3f98-ab92-3d9e-a1a3-3bf11e0cb4c5 | -17.03413 | -56.73767 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| bcc55289-9a50-388e-90cb-fccf575f0e53 | -17.03399 | -56.70957 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0828691c-3b61-322c-a803-f0bfdd7995ac | -17.03342 | -56.79875 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f8915350-ebd4-3a72-b2e7-9314f9e57f52 | -17.03287 | -56.68606 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 0d0b2314-b4b7-3d41-98dd-718fadcb8b82 | -17.03192 | -56.69048 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 958d19f9-2e4e-3931-af78-00d00a467dfb | -17.03097 | -56.6949 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 16697547-809c-3129-9046-50e440ad2829 | -17.03002 | -56.6993 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| dce26ade-e8b5-3bfd-950e-b036e52a4615 | -17.02945 | -56.78835 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 1dbf7b6c-8491-30aa-859f-f9d6077be6fa | -17.02921 | -56.73179 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 42d32d68-fe33-35ee-8f07-cdcc1731d83f | -17.02907 | -56.70371 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b4383aed-757d-3d3d-9c7b-e235830a99d2 | -17.02848 | -56.79284 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| d427c6ce-d197-3f8d-aa90-65b9ef28de79 | -17.02812 | -56.70815 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5626ba4c-26fd-3689-946d-1936b0c135ab | -17.02752 | -56.79733 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| f6b63801-b11f-340d-9de1-5ceb56fd0cdf | -17.02729 | -56.74073 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f4a186db-8904-3a68-902f-a2856d05ca65 | -17.02701 | -56.68465 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| be4c3f7a-5fbe-3c21-96d8-df38636b9b3e | -17.02633 | -56.7452 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1ab15bab-6fca-3256-a44d-09a4169a5c48 | -17.02606 | -56.68907 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 20cd0233-3746-38ec-b2f0-f086ee0ec0a5 | -17.0251 | -56.69348 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| fa4e5656-dc11-3ef1-996f-00732ac29252 | -17.02415 | -56.69789 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 594f2165-0d3d-3e58-b302-e017bacc4f1a | -17.0232 | -56.70231 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b66012b0-b200-30f6-9714-69e679a928bd | -17.02258 | -56.79141 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 2f8d8e31-3961-3b5a-943b-ca65dc08f418 | -17.02162 | -56.79591 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| a2155603-a545-3a23-9636-a890569cc5e6 | -17.0214 | -56.73932 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0d9b3b0c-36b7-3b06-9d39-e20bb2a060a0 | -17.02065 | -56.80042 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| f402baba-cf90-3321-b31b-d0a90ecd0562 | -17.02044 | -56.74379 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fc46f82a-705d-3161-a5d6-ec4003efde1c | -17.02019 | -56.68767 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 7a6f8908-50f7-3151-aac3-beb8f3607bcc | -17.01924 | -56.69207 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 0a18152e-2319-3db1-aaa6-1b745b263f7a | -17.01828 | -56.69648 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| bd827f28-b4d6-3e89-8bc0-97b9e1836166 | -17.01732 | -56.70092 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 99107058-5603-3978-8856-3450e3d7c210 | -17.01668 | -56.79 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| bff87460-ea37-3fe0-af19-6c793083414f | -17.01648 | -56.73345 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2cbef28a-cf9c-3760-8aa6-c15b434c6f40 | -17.01571 | -56.79449 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 15dbc459-1aa6-3b5d-9de3-fd9e8a2ba191 | -17.01552 | -56.7379 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 62d75e2d-b5c7-31a4-b7dd-26d376925403 | -17.01474 | -56.79899 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 47843456-60c7-30ba-b625-38464f422821 | -17.01432 | -56.68625 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 0d38f3d7-672e-3765-bd4f-949e53a1a896 | -17.01337 | -56.69067 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |


[Clique aqui para ver as próximas entradas](README83.md)
