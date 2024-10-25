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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d74f2aa-c2f2-37f8-bb06-462232c66503 | -5.83164 | -47.18412 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa73d5c8-4200-341f-b54c-fe8aecf4f101 | -5.83106 | -47.18787 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f1a12d8-a40f-3006-9c9f-4accebb9ee70 | -5.71409 | -47.10868 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c8c461-a49f-3530-9b70-1c9e188f2bd8 | -5.71351 | -47.11245 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 790a21a1-a8e4-34a8-be7b-054099292e19 | -5.70547 | -47.34803 | 2024-10-25 04:38:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13d36789-ec6e-33e1-ba38-a1ac7ce3d9f8 | -5.70204 | -47.3475 | 2024-10-25 04:38:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2120b89-666f-3ab3-8ced-c3e8b370f92c | -5.69861 | -47.34698 | 2024-10-25 04:38:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a87ee66-3b4f-36dd-9ad4-2cee42a49df5 | -5.69519 | -47.34645 | 2024-10-25 04:38:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0afd4cd3-0482-3b3e-be66-a1dd750a81c5 | -5.65247 | -47.91273 | 2024-10-25 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb559793-b09f-3445-8b7c-c29aa0b0ba0a | -5.64872 | -46.96764 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2997d2c-5725-3239-8e59-5b44b87c392a | -5.64864 | -47.51251 | 2024-10-25 04:38:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6e4a741-4c92-326d-b206-b166262b8089 | -5.64813 | -46.97146 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87a9c98f-c798-3d1b-99c7-ab0e19e5d782 | -5.64798 | -47.91935 | 2024-10-25 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2bbff55-9cb6-3012-b60d-483a6326782e | -5.64462 | -47.91882 | 2024-10-25 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f92e8104-79bd-3d9f-b614-131c9e705057 | -5.6383 | -46.96603 | 2024-10-25 04:38:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c14c6d56-366a-33b4-8276-752d600e6ed9 | -5.63772 | -46.96984 | 2024-10-25 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0bfa8e6-be4f-3fa8-b4ba-547e575f34dc | -5.63483 | -46.9655 | 2024-10-25 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cf5d101f-bd01-36e5-9ebc-2c7009d35435 | -5.63425 | -46.96931 | 2024-10-25 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db5a8c81-3616-3fd3-a70c-211aa062e9e1 | -5.61675 | -47.26676 | 2024-10-25 04:38:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4c6d72c-8c7f-3046-8f0f-4b2f0da103ba | -5.58929 | -47.2625 | 2024-10-25 04:38:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22e79739-dfe3-37d8-a4a8-b4e96cd52481 | -5.58872 | -47.26624 | 2024-10-25 04:38:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0314f2d6-3dbf-30fb-930e-8159bff36d72 | -5.4449 | -47.67915 | 2024-10-25 04:38:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c538a021-03a6-340a-ab08-436582b819cc | -5.43442 | -46.5578 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68e0011f-487c-3a7d-94c6-6cfe40d9322c | -5.43212 | -46.54938 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11802f83-1178-3e88-8453-579e5c65a091 | -5.4286 | -46.54883 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04fb1159-3a84-32f8-a393-d8790fc5cdd0 | -5.42677 | -46.56062 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8393f71c-5ecc-3374-a747-33a60e429ce4 | -5.42386 | -46.55613 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dc7c5a9-3057-3ae2-a6e6-426c12cd0204 | -5.42325 | -46.56007 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b01a110-1d91-3502-ba6e-b0370378d4cf | -5.4156 | -46.56293 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b052ba44-3e9e-352d-beeb-43eac6dfde40 | -5.41499 | -46.56688 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b344d8a2-fdf4-3b6f-999c-880c7af9d17c | -5.41438 | -46.57082 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66d2793c-90ba-3a32-8312-b59c67a624d5 | -5.36742 | -46.57162 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11f0f3fc-7a56-37e4-a3e7-96d38e6f47f7 | -5.3639 | -46.57109 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71885dab-402a-3ce7-9326-5947c0bd6549 | -5.3633 | -46.57504 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d510bdd-2838-3b7d-99c6-94c9103a8291 | -5.27795 | -46.70605 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f4802e-e69c-3945-bd67-42b403a14c98 | -5.27736 | -46.7099 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccb95edd-360b-3d5e-815f-0d1b540df53a | -5.27446 | -46.7055 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5eb8665-7008-3eef-81a2-60577c9b5b5a | -5.24765 | -46.69363 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18fbb784-eeed-387d-b12e-ad497661a934 | -5.24706 | -46.6975 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c206cdc5-b472-3b97-b840-b129a0684e87 | -5.24475 | -46.68917 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 463d6b03-34be-3453-a1c4-50e736d32a70 | -5.24416 | -46.69308 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90d164b8-e05a-3366-87ee-43746e498921 | -5.24244 | -46.6809 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3da8677-6cd5-347c-9048-599e2daa6671 | -5.23544 | -46.67981 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eddcbb09-ea95-307d-9472-5e4142277a4a | -5.23194 | -46.67929 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59126adf-00d1-3e7d-affb-9d178ce915d8 | -5.23136 | -46.68314 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50aabfbc-b689-3c9c-a563-39f449a16099 | -5.21328 | -47.19181 | 2024-10-25 04:38:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 846e23df-2735-38d4-84a1-24e74fa1dd66 | -5.20277 | -46.75359 | 2024-10-25 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb365f67-fdd9-3ec5-acb5-4ce09d32f345 | -5.15406 | -47.70497 | 2024-10-25 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a0f6cbd-5434-3e5f-9ca1-c0baaf933773 | -5.14449 | -47.69984 | 2024-10-25 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c869e92d-655d-3b97-8c32-200e5b7cc5b2 | -5.13819 | -46.8891 | 2024-10-25 04:38:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a5ea05d-d450-326f-a813-05ff15b66c6c | -6.52583 | -47.27062 | 2024-10-25 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5bb4306-259b-3ab1-b685-2481dd8ad2ee | -6.52237 | -47.27011 | 2024-10-25 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f16cf090-d1ff-3e93-9f58-bc6f3c292899 | -6.52074 | -47.26668 | 2024-10-25 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 629bfdc7-05c0-3e29-a480-1ec50848540b | -6.51948 | -47.26581 | 2024-10-25 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba992a3a-113b-333b-8231-1f7b252ca798 | -6.51728 | -47.26616 | 2024-10-25 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8851eb5c-bf11-329d-8490-4f54345b4b5c | -6.42889 | -46.90874 | 2024-10-25 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6685749-d8f0-359b-8668-81dcbb1ef5b5 | -7.65668 | -47.52239 | 2024-10-25 04:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e40e73c4-752f-33a8-8b09-1b68709f8928 | -7.6561 | -47.5262 | 2024-10-25 04:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 789d6add-9971-34e5-b71f-f0c7a00712be | -7.65264 | -47.52566 | 2024-10-25 04:38:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dc70de1-2ae7-3de3-b41f-51dafa7a3be5 | -7.63035 | -47.82494 | 2024-10-25 04:38:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fe613a3-6f90-385e-904a-63b320d8d170 | -7.62979 | -47.82866 | 2024-10-25 04:38:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8da92271-3873-39df-addc-799932e77f01 | -7.60881 | -47.71891 | 2024-10-25 04:38:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b6afbc6-edbf-3721-90b8-5b62c0c1a132 | -7.60538 | -47.71837 | 2024-10-25 04:38:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13fe1184-f867-3fcc-bea2-859c356f2963 | -7.56257 | -47.81453 | 2024-10-25 04:38:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d529cbde-383c-3559-840a-694966a66b21 | -7.54263 | -48.30413 | 2024-10-25 04:38:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30144973-3398-3426-bdf7-9c87e87d08e0 | -7.53926 | -48.30362 | 2024-10-25 04:38:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46966cf2-a369-3116-8c0d-7583f263ac29 | -7.27602 | -47.63532 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a560a5d-ae5b-3da9-acff-794e171cc319 | -7.27258 | -47.6348 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaad1ea9-3cd5-3a99-89a3-e482d741a03b | -7.27201 | -47.63852 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e93d6976-e1fe-3fdf-93a6-7559001e9c96 | -7.25049 | -47.91503 | 2024-10-25 04:38:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b471aff-110b-3166-922d-a573dd14528b | -6.89414 | -47.69231 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba8db78e-2edf-3596-b264-12cd0ec93242 | -6.73242 | -48.17672 | 2024-10-25 04:38:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a71ec124-aa38-3b1a-a91f-321525aed9b0 | -6.64752 | -47.86924 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c862810-57aa-35fa-9c82-8f1bd8e54a75 | -6.64696 | -47.87288 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea473c02-c056-390e-99d9-13a8e1e3ddab | -6.64524 | -47.86143 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 452e4fda-0f8d-3949-960d-20ee26e578ed | -6.64468 | -47.86507 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 158ad2a4-530d-3f04-9b4f-53681eb1194a | -6.64459 | -47.86115 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84cd42e7-7905-3dc1-ad91-ab4a41c1a1ac | -6.64412 | -47.86872 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbeb820a-15af-33e5-bc19-d0c7de97d93d | -6.64402 | -47.86479 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5faa3676-892f-3a9a-8182-efa2c29e7601 | -6.64357 | -47.87237 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a31adc5d-d411-3cdf-a6ed-2a609a20c0fb | -6.64345 | -47.86844 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec4b83b4-b157-3849-9908-ff28944ffdbf | -6.64119 | -47.86064 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33bcd98e-345e-370d-86df-18647ca1fcba | -6.6378 | -47.86013 | 2024-10-25 04:38:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d34c6477-490d-31c0-8a1e-43719b06df65 | -6.5383 | -48.0551 | 2024-10-25 04:38:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 256cb2cf-0ae6-3550-9a9b-61890569ef22 | -7.89923 | -47.35111 | 2024-10-25 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b464649-9e8b-3989-871a-01bc27a25827 | -7.89864 | -47.35498 | 2024-10-25 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8455fa4e-4740-3dc1-ab6f-4701242c695f | -7.75864 | -47.13928 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e25946f6-8bb4-38e4-be4a-b51d41f803a8 | -7.75513 | -47.13876 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57255326-2164-334d-9cfb-8a1ae6eaf714 | -7.59421 | -47.08352 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb8177fd-7b24-3eef-9b78-86f1f261cf7d | -7.54341 | -47.41619 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8050b0d6-b14a-3380-b9af-c3de621f4676 | -7.53993 | -47.41566 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9329e074-b274-3975-924d-846a0ed285d1 | -7.49271 | -46.89935 | 2024-10-25 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beef3123-6e1e-33c5-b495-4d5cc662a7fd | -7.47728 | -47.1669 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b31d859b-7af6-3b12-b1bd-71a1ecffe58d | -7.47574 | -47.39412 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eaa77c1-3ad0-3211-89e8-86f5eac955f5 | -7.47434 | -47.39486 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecfbae9d-853a-3a0c-9c50-bdab844b236c | -7.47227 | -47.39359 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9ad33c2-06c0-37a4-8348-8a7f2b6758c5 | -7.46849 | -47.17747 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d4cc435-ad83-3246-9b50-23d30d428017 | -7.46276 | -47.40087 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a15991f4-56eb-30da-b88b-60e8cdd55cb5 | -7.42887 | -47.1076 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d022ce5-8d4d-3d11-b257-73e02f49b023 | -7.42536 | -47.10707 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
