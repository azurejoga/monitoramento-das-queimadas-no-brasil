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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5f7901a-d143-3a58-bd60-0de719eec8bf | -4.60452 | -44.30894 | 2024-10-31 04:23:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 644af241-271a-3d12-9975-09384c4cbdee | -4.6017 | -44.3048 | 2024-10-31 04:23:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0c1a6eb-9516-3b27-9e6a-3a249a01ff71 | -4.60114 | -44.30841 | 2024-10-31 04:23:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 537be115-8585-3ca1-831e-8f9ff1c13dab | -4.59831 | -44.30426 | 2024-10-31 04:23:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cc2133a-814c-3c45-8f72-f9e756d45098 | -4.59775 | -44.30788 | 2024-10-31 04:23:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76f845e5-3592-31ff-bc1f-c234cac9f96c | -4.94802 | -43.98338 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee62e6e6-03b6-3e85-a3c8-3dff555efa59 | -4.94745 | -43.98709 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee81ba69-415a-39ec-837f-059cb2318f49 | -3.61127 | -44.4784 | 2024-10-31 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4185582c-52eb-3aad-a801-8d6b69f2cedd | -3.60792 | -44.47788 | 2024-10-31 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580b0feb-119b-345a-b2e4-1f6b147c5bdd | -3.60456 | -44.47736 | 2024-10-31 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80a166ca-d738-311c-b6e8-7a218370ad65 | -1.56978 | -45.47439 | 2024-10-31 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fc122d5-f8c5-353a-8625-c6eab0ef6062 | -1.56923 | -45.47784 | 2024-10-31 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53c5b9d3-1641-3e89-a1d1-c70aaed806cb | -3.39687 | -45.24103 | 2024-10-31 04:23:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e5dbb4e-e443-3700-a433-1bce90840061 | -3.28745 | -45.63389 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1925915-e6fe-32b2-8cf1-b83f8d3da2b6 | -3.26113 | -45.97326 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e9a3dc6-60c2-3318-84c5-f3ccc6e63ec1 | -3.2578 | -45.97275 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 311ce1c4-8657-3b3c-87f4-f0e4b2f47065 | -3.24643 | -45.82913 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a721135-117d-3c2c-906b-7ce10b0ee470 | -3.24365 | -45.82516 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b08ce0c1-6d42-311f-adb0-8116cce4347e | -3.24311 | -45.82861 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20e93abb-91d6-3691-973a-016407f3072e | -3.24033 | -45.82464 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f28fd03-1a43-3a46-b03b-b6ed8cf7a7cf | -3.23701 | -45.82412 | 2024-10-31 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4902f60c-2822-3bfd-ba38-c32761c525f9 | -3.13291 | -44.48402 | 2024-10-31 04:23:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85b175e5-0bae-3e82-a2da-045b878c2531 | -3.12956 | -44.48351 | 2024-10-31 04:23:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc6dacbf-b634-32e3-8158-3e577beab188 | -3.12676 | -44.47947 | 2024-10-31 04:23:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14b84543-f510-3c6b-86be-6cdbe15517e4 | -3.12622 | -44.48299 | 2024-10-31 04:23:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99366640-0f8f-3be7-b66f-a3cdd5e48bb4 | -3.12396 | -44.47544 | 2024-10-31 04:23:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d33beeab-d82f-3be1-83bd-af600fce888b | -3.12341 | -44.47895 | 2024-10-31 04:23:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b72778e-b0f3-3d7e-85ab-3993bd815a4f | -3.10068 | -45.50953 | 2024-10-31 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7abcfea0-ef15-37c7-af06-3ff94eb3be21 | -2.92043 | -45.66821 | 2024-10-31 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a20c6a2-d516-3356-b584-ca52305a9796 | -2.91711 | -45.66769 | 2024-10-31 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e61782a9-29b0-3a5c-a1d0-1241b6ce45e7 | -2.87546 | -45.82407 | 2024-10-31 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 849bc18c-2bd8-32ca-822a-2e6aca09349e | -2.87492 | -45.82753 | 2024-10-31 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f807d642-abed-3208-a452-94b3ffde22ec | -2.87214 | -45.82355 | 2024-10-31 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebbe7846-b438-3eb5-bbc1-6f85fdc14087 | -2.87159 | -45.82701 | 2024-10-31 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f495570a-9543-3398-bcc6-6d5182c3ba55 | -2.81496 | -45.47878 | 2024-10-31 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73d1482-7a01-32e4-963b-3ede0df71a97 | -4.46175 | -44.84041 | 2024-10-31 04:23:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0668486-3474-3bf7-8efc-e3edb9156511 | -4.44046 | -45.62008 | 2024-10-31 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d589886-bf5d-3eac-9c19-150f54c092db | -4.40574 | -45.86235 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be6d3029-9dbc-3550-9dbf-4231d2fa23a0 | -4.40519 | -45.8658 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20ed6546-3846-34ce-9a2d-a5f94363eed6 | -4.40465 | -45.86926 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ee7db68-c42b-3182-936a-7a5341558675 | -4.40187 | -45.86528 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 320acb0b-e08e-38fd-ab86-7bae0537ca81 | -4.40133 | -45.86873 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77d83940-63e4-38ec-8f43-ac66e13eb33d | -4.38456 | -45.80241 | 2024-10-31 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bd56caf-a0d0-3d73-8a85-42a818718286 | -4.37438 | -45.7159 | 2024-10-31 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65c02e41-cd65-329a-bcea-ab51f4d35488 | -4.37384 | -45.71936 | 2024-10-31 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0384a9e1-30ff-35bd-a61b-ec906e32936a | -4.35975 | -45.83038 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2d981c6-84bf-301d-9b1d-58999f487883 | -4.35921 | -45.83384 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 853f642c-b538-33aa-b464-763c16cf3d4c | -4.32545 | -44.68966 | 2024-10-31 04:23:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af853ff8-7db9-35a8-b581-f82dfeeb5474 | -4.30428 | -45.98803 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 088055a1-b41f-380d-8392-ae31ed2e555e | -4.30096 | -45.98751 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64c650fe-dad8-3e2a-917f-696d0f5cbaa4 | -4.27723 | -45.71145 | 2024-10-31 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 421c5f81-d7cd-32b3-a775-1cc48cf5994e | -4.27336 | -45.71438 | 2024-10-31 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53e34002-66ad-3b55-8209-f5e01e5ad29f | -4.11278 | -45.66116 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7c002e9-91b3-3913-81f8-c3dd09ace4c9 | -4.10946 | -45.66064 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d20af18-ae08-350a-8cdd-3b3c09615c83 | -4.05229 | -46.00207 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd07643a-e79f-3a3a-9865-5f97334d8fe2 | -4.02131 | -44.82247 | 2024-10-31 04:23:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e63b6c0-397d-30ca-82b7-8b8f6108f3fe | -4.02076 | -44.82597 | 2024-10-31 04:23:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 4829a9f9-2463-349d-a19c-de05bf027ae4 | -4.01797 | -44.82195 | 2024-10-31 04:23:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b73a61c-8c0a-3433-8b62-c78fd65b7930 | -4.01742 | -44.82545 | 2024-10-31 04:23:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 30010900-45a4-31e2-bb34-8cdf93c4f934 | -3.96983 | -45.7938 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e499a366-8d81-3336-8928-2bf7ea88efcc | -3.96929 | -45.79725 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79472afb-5789-36da-a5b6-8d8b4bcccb92 | -3.96597 | -45.79673 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed57e6a1-64b9-32be-ad12-e9cdca6847cc | -3.96542 | -45.80019 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad7284b0-ff91-3db9-9620-f7c9c7e70b82 | -3.9621 | -45.79967 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19c06cf4-7150-318d-9744-f156568c6318 | -3.9249 | -44.93625 | 2024-10-31 04:23:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4d4fea3-a402-3822-b7c2-a980fa896a03 | -3.92042 | -45.26971 | 2024-10-31 04:23:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7d9b5e9-949b-3620-b8f7-53f7dd356eb7 | -3.89952 | -44.92877 | 2024-10-31 04:23:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c89d637-e2be-3b89-b324-47193af6ce8c | -3.72095 | -44.62131 | 2024-10-31 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2080e078-508e-37f8-ac27-1405b7623b9c | -4.68563 | -46.08382 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf553286-b5a3-3ec1-9f21-7637d572d521 | -4.60375 | -46.08515 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e8a67ee-c87a-3f50-b1b8-f9fbb61b88cb | -4.49258 | -46.04298 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f55b3b67-2f14-3f86-a524-a70314334db1 | -4.1636 | -46.108 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d074b7b-4fd4-3c6b-94b0-10ee368897d0 | -4.79406 | -45.26435 | 2024-10-31 04:23:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4ec7d27-0f46-3441-a30e-e0db62deaa4d | -4.69968 | -45.73552 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41fe274e-a4f5-3833-9e9c-51b9b47dbcdd | -4.69913 | -45.73898 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7c2aab3-aadb-3f67-9c19-b255950d55d0 | -4.69744 | -45.7281 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9ded8ad-53e0-3201-b525-2a487b020e2b | -4.6969 | -45.73155 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f32114a5-1725-3a73-b87d-1ce62a86c8db | -4.69636 | -45.735 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdbed53f-101f-3ffa-b7a4-eb244ada4089 | -4.69358 | -45.73103 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88fc97de-f51b-3e42-90a8-2db794604f95 | -4.69304 | -45.73449 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a768ddce-2d16-3a86-b7c1-7956e12411d8 | -4.68386 | -45.81446 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 229d2881-fa09-36b3-b3ba-4108aef91f1d | -4.67355 | -45.68542 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ba84176-2070-3ee3-85d5-3caff2a41217 | -4.67023 | -45.68491 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f2bf55cd-aed5-3895-b022-aaae8975ab4d | -4.61319 | -45.53079 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66bdf7a4-dd4c-3ed3-a5b0-ac7425aaf1a4 | -4.58051 | -45.9115 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc53f09c-b683-3c5f-9658-de96cd22b7a1 | -4.57996 | -45.91496 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a31440b-b4c0-3f16-90bf-729cb995ada1 | -4.57664 | -45.91444 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0496e612-bf75-31e4-b354-78a0b9c63ddd | -4.57185 | -45.77211 | 2024-10-31 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d7e578f-0695-3171-aa3d-86df5162fbfe | -4.56239 | -45.96173 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8334d75-46e9-3423-8a89-f05511ffda27 | -4.55874 | -45.55783 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa936199-72ca-3976-93db-7080fb7fdfbe | -4.55819 | -45.56128 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8879255-d6b4-3add-b77c-70013831e689 | -4.55765 | -45.56473 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6769341b-5b86-3947-b1be-d172d854a8ec | -4.5565 | -45.5504 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52713009-7b48-3bdd-8817-3d19f8e55e03 | -4.55596 | -45.55386 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1404341c-d8b2-30e2-bfb5-c162918be976 | -4.55542 | -45.55731 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 693e65b4-d481-3efa-b06e-10aac935c407 | -4.55488 | -45.56076 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08529c6c-97cc-32d5-8f07-6653117e6cfd | -4.55434 | -45.56421 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 081ef866-96df-3d3f-9162-741d6d64fe15 | -4.55264 | -45.55334 | 2024-10-31 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61694bdd-6399-38fc-9105-c23aa762c359 | -4.55113 | -45.88212 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc27adba-f4ee-3838-9599-95542846260e | -4.53534 | -45.98227 | 2024-10-31 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README18.md)
