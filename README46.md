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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89501a73-34a0-3552-b592-7100e802e4ef | -17.2544 | -43.17403 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5614ce21-9a14-3254-aadd-a1157cd2ecb1 | -17.09443 | -43.80422 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ffc53b8-d618-3c2b-ae4f-b60a5711d219 | -16.68204 | -43.88571 | 2024-10-01 03:49:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54af914d-9a0a-37ec-bd15-7b05f64c2ef6 | -16.34994 | -43.69857 | 2024-10-01 03:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 866cdf0d-288d-36a6-9666-8cc1d35c9fd6 | -15.6389 | -45.17076 | 2024-10-01 03:49:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 723ca0c3-a176-3017-bc4a-0ccaf074d8f8 | -15.58691 | -42.07416 | 2024-10-01 03:49:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3021bae7-c02d-395e-9355-e9acb6bebfb8 | -14.55639 | -44.87037 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cb6d571-7729-3dda-949c-307fc6897b41 | -14.55588 | -44.84867 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c83f18ba-5e26-3941-a21e-4e4e6d548536 | -14.55155 | -44.84784 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd462fac-fd56-330d-82d4-f863f1218a2e | -14.50411 | -45.25465 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5d53b71-ba2c-3253-8473-fce06630c431 | -14.50326 | -45.25928 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6916dd8d-0ec1-3775-8e81-e2c549e24817 | -14.48521 | -45.23221 | 2024-10-01 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff687899-c5ee-3048-9a87-e5672e38fd84 | -14.43814 | -45.7154 | 2024-10-01 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b63c67a4-024e-3e19-9287-4da5f86aede0 | -14.43671 | -45.71738 | 2024-10-01 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1addf9f-450d-33cc-9f2a-1f9bccc1cc76 | -14.43356 | -45.71446 | 2024-10-01 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3df8810f-4b36-3c1d-acbf-bc7386863461 | -14.43305 | -45.71164 | 2024-10-01 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea85238a-2524-3367-928f-6e56e76b5652 | -14.18795 | -46.45582 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48be7c0a-5f4e-3632-8ee8-d0f07e607e97 | -14.18683 | -46.4618 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3e735e3-5485-33e7-a194-654d3ee2a7a9 | -14.18513 | -46.45634 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75821665-9513-3c8e-98f4-5c60576641f0 | -14.18399 | -46.4622 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98c38037-7c5c-390f-bd36-3209dca01aff | -14.18201 | -46.46071 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ca98df8-56a8-3bfd-97b0-b19767aa7082 | -14.17917 | -46.46112 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 544567fd-cec2-3a05-ab76-f0aa64e680bf | -14.17811 | -46.46652 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 558c7d45-0a92-3bb0-8b91-af475a7a66b2 | -14.17616 | -46.46505 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ca11f22-49e6-3cbd-81a8-40f3f8a57b7f | -14.17332 | -46.46528 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a6a9e40-2637-355e-a819-7f6fafe9edc6 | -14.17136 | -46.46383 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec0f3d0f-74b2-30b7-8ec1-1ba2dc7a96fe | -14.16761 | -46.45707 | 2024-10-01 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48d65ddc-958d-3695-8f9f-aa6ad496f671 | -13.74428 | -48.15792 | 2024-10-01 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 594b7134-93ea-3686-b93d-2f9e1981f278 | -13.72176 | -49.42201 | 2024-10-01 03:49:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbc852dc-3432-3164-8312-f307f610a517 | -13.72087 | -49.42651 | 2024-10-01 03:49:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2b4f242-29f5-3209-91c4-97598cd16107 | -13.53607 | -47.57914 | 2024-10-01 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8dc229ff-67b1-3117-8e75-41cd540c479a | -13.53148 | -47.57468 | 2024-10-01 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| df42fc04-d066-3936-b7e6-e42ba7c7ae5b | -13.51058 | -48.59138 | 2024-10-01 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b99c4c45-2598-3ae1-928b-9b3fa2e89909 | -13.50976 | -48.59548 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b124c2bd-3126-3a41-be9b-f431444a272c | -13.50584 | -48.58578 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d40c1305-88e6-3ffd-bbb8-a64fb5f0bce6 | -13.50497 | -48.59012 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0fc558bd-6e66-32a5-be67-12a00429d825 | -13.50411 | -48.59443 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7a0cafea-3c44-3e93-8f35-ec835e1e1bf9 | -13.4994 | -48.58871 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 486f2a48-86b0-3da1-9825-a7219b652eee | -13.49856 | -48.59291 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a9d6c473-c40d-30b6-8915-717a23f38386 | -13.46943 | -48.62114 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6d858c0-b5c9-3b57-97c3-9a5f27145161 | -13.4686 | -48.62523 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e18184fe-dde2-3ad2-bd60-1a33f8a08a71 | -13.46777 | -48.62935 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a886e4c9-6686-3bc7-bf71-4616a67d0389 | -13.46301 | -48.62383 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef25b35f-c294-39ba-98bf-7163e23460d2 | -13.46216 | -48.62804 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b537d38f-e336-3c49-b2aa-b7a94ad3df14 | -13.45258 | -48.61728 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 778488fb-aaf6-309d-b862-e7dcdb1968f3 | -13.45092 | -48.62548 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f3676c7-291c-3d7c-a82a-41d91cfe022f | -13.45008 | -48.62961 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a25a066e-2855-3eac-b908-019fa324e235 | -13.44935 | -48.62206 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8815ef2d-4683-3a84-ae8f-510f37bf1936 | -13.44853 | -48.62623 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90f1c218-ea4a-3a46-8e1e-115b8e056cd3 | -13.44773 | -48.63036 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aa7ae7e-9bc1-34cc-9442-22b90e345968 | -13.44608 | -48.62033 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fb19088-9ca7-3b82-84cf-b65c08dec13d | -13.44369 | -48.62096 | 2024-10-01 03:49:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bf487d6-8ea9-3bf0-bf70-b3ae35391725 | -13.2201 | -48.5842 | 2024-10-01 03:49:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41383442-b356-3098-9560-8b857e3e1113 | -13.21932 | -48.58803 | 2024-10-01 03:49:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1951779c-ec9f-34cb-bf0d-333243660fd8 | -13.21833 | -48.58275 | 2024-10-01 03:49:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dd09e9e-8b6d-3566-8daf-0ca56edfa703 | -13.21803 | -48.55431 | 2024-10-01 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39cbc719-ac11-3fac-9c36-eac4e08d60c0 | -13.21756 | -48.58664 | 2024-10-01 03:49:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc9ab28a-9d1f-38e6-826e-d19b02cd1f89 | -13.19555 | -48.51964 | 2024-10-01 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6874f72f-610c-3aee-bfcb-6e1cad2ff0f2 | -13.19486 | -48.52312 | 2024-10-01 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97ca8c23-c42f-349d-8998-f21c756e3d50 | -13.19049 | -48.5156 | 2024-10-01 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e830e2c4-96c1-3a69-8a7b-d2e40f481508 | -13.17825 | -46.32778 | 2024-10-01 03:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70709cf7-0467-3604-a215-9a2b94a84d63 | -13.17323 | -46.32749 | 2024-10-01 03:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 129c0fed-86a9-3be8-800b-d08f038f6d19 | -13.17208 | -46.33354 | 2024-10-01 03:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4bc2ae06-ea50-3113-9336-cca1a2d0b54d | -13.17099 | -46.33931 | 2024-10-01 03:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1f66dc4c-704c-32be-88c0-7e82787625c2 | -13.16991 | -46.34497 | 2024-10-01 03:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dab7f735-800d-330b-8d27-9a27984ec16d | -13.16611 | -46.33827 | 2024-10-01 03:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f74a8ea3-e1e1-3e52-a66a-a533b106fb9e | -13.16504 | -46.34388 | 2024-10-01 03:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e501a98-0372-3a6b-bf2d-0239258aa4be | -13.13025 | -46.77147 | 2024-10-01 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 254f5263-8eaf-32f4-9038-7827e8ec0e61 | -13.1297 | -46.77441 | 2024-10-01 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 14248a85-74eb-3199-9935-23e7cc37d3e2 | -13.12914 | -46.77735 | 2024-10-01 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c23abb47-eda2-3c67-8e1a-d4df2beba3a3 | -13.12467 | -46.77336 | 2024-10-01 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fd7a55a-32cc-3ffe-a7e1-fc7f76da779f | -13.12409 | -46.77641 | 2024-10-01 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b216e5f-2112-398c-b6dc-84ff00ac0baf | -13.12351 | -46.77948 | 2024-10-01 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ee7158f-5dd0-38f7-9905-01aeda1166d4 | -17.00812 | -49.7821 | 2024-10-01 03:49:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b171980f-ac9e-3ff4-a0b7-dad20baac57a | -16.6664 | -50.59794 | 2024-10-01 03:49:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2827f06d-f66e-3475-9e5a-122f7f3e6a57 | -16.66536 | -50.6028 | 2024-10-01 03:49:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97af6b82-7e79-364c-a65f-10578c7bdf3c | -16.10044 | -50.3425 | 2024-10-01 03:49:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd7488be-7645-340a-a3b8-feb2d9cc5cda | -16.09921 | -50.33937 | 2024-10-01 03:49:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58def9be-cf88-3360-b7fe-aa386376d884 | -16.09831 | -50.34367 | 2024-10-01 03:49:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29c04e81-7e49-3ea5-a153-60e407a90fa6 | -16.09806 | -50.41127 | 2024-10-01 03:49:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9865e150-d182-3f74-b38e-40fc418af25d | -16.0963 | -50.41298 | 2024-10-01 03:49:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59f21467-65e6-355a-bbeb-6a7620b5f684 | -16.09476 | -50.33986 | 2024-10-01 03:49:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0a2d2775-e352-3c48-87ef-7ce162d598e3 | -16.09347 | -50.33698 | 2024-10-01 03:49:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c8e6aa2-ade1-396b-a0b9-c23baa22ce53 | -16.09221 | -50.40928 | 2024-10-01 03:49:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf2662a2-46d5-3320-9bb9-1b311ec72061 | -16.09141 | -50.40635 | 2024-10-01 03:49:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4acbf113-d96c-31fa-9c43-2a72a5c6b146 | -16.09126 | -50.41363 | 2024-10-01 03:49:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 299fe46b-2793-378c-8e72-a859da356b0c | -16.09041 | -50.41114 | 2024-10-01 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0912d06-0472-3668-98f4-b1ef3ab603c5 | -16.08953 | -50.41532 | 2024-10-01 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d8de3b6-d323-3b20-97ea-6ffda1fa3f54 | -16.08891 | -50.33798 | 2024-10-01 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 731eb702-4daf-3bae-8330-f0a084d47262 | -16.08624 | -50.37902 | 2024-10-01 03:49:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a17b6f7-0cc1-3dbd-b346-6a3c8df654e8 | -16.08526 | -50.38351 | 2024-10-01 03:49:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d04f0c0-a95a-34ee-b6de-29677b13c110 | -15.77379 | -48.4958 | 2024-10-01 03:49:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c26d4a6e-93c8-35b6-acad-189650d45731 | -15.7731 | -48.49922 | 2024-10-01 03:49:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78f67e53-d45b-3838-b9c8-453ba16f3ea9 | -15.77242 | -48.50251 | 2024-10-01 03:49:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a212c61f-93b9-3152-8fea-979ba9976db8 | -15.76765 | -48.49847 | 2024-10-01 03:49:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c923ed2e-2af3-36fe-9d12-63e3be870981 | -15.15716 | -49.59592 | 2024-10-01 03:49:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ab5e8ff-f0c4-3883-903e-b93f0856f434 | -15.15136 | -49.59462 | 2024-10-01 03:49:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9d269e0-c37d-35e7-a538-c9b3a9d2f7b1 | -14.7882 | -48.76063 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 261f6f65-0096-3a24-8bb7-300f38e08cb2 | -14.78752 | -48.76398 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f71a7136-5b65-3188-9778-fdc85de4c16c | -14.77239 | -48.78152 | 2024-10-01 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README47.md)
