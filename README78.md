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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05814784-5c27-30de-8b1e-9b0998dd153d | -16.24465 | -44.05406 | 2025-09-30 04:42:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64672a54-df5d-34bb-99ae-f272270d7d3e | -16.74775 | -51.3554 | 2025-09-30 04:42:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a6d051d-a458-34d0-a274-e9b2f721d7ce | -19.23339 | -48.68616 | 2025-09-30 04:42:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27988f0e-58d2-3b76-9fde-538fbb6010b3 | -17.41019 | -47.14846 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab079ed6-83c6-36be-b94b-e69ea6bae502 | -17.71289 | -46.64663 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 395cd20e-c278-39af-b50a-c6086c7e4d33 | -14.65085 | -46.96568 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b0e361c-0008-3557-90ea-747aee073ebb | -15.71663 | -59.51514 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be0c2f49-bf88-3924-8375-7c43b5228fe7 | -20.61861 | -46.18747 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1a47674-dee0-3b53-a322-fe129141c8bb | -20.06394 | -46.79642 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3841723-ba8b-3c0a-b130-c812c9a2d0e7 | -14.78494 | -48.30592 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47af82b4-af61-31f3-82af-ea777ab36708 | -14.53473 | -48.24166 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 881fe1fd-0f44-372a-b251-04aca7764cf0 | -19.55379 | -44.24313 | 2025-09-30 04:42:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b37e79-c58c-3724-93d7-26356ff3acf7 | -14.5915 | -48.16544 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d82230b6-4ae8-315e-acf2-499f2a7a86fd | -15.27297 | -49.49636 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 274e603d-78a8-3ad5-9497-548724fd19f4 | -15.29184 | -46.4145 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63ed1033-3044-3797-8941-db59c32bf2c5 | -14.52823 | -48.48838 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f7b0feb4-0f05-3cf6-a141-39fc62444a0a | -14.48516 | -48.5609 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c01076a-ca53-3415-8336-d1be6ed23430 | -14.53177 | -48.48898 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 30c5e94d-d752-36f5-9b97-13537c4c2183 | -17.3998 | -47.13572 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 078c0f89-9133-3156-a5b1-9d4894bc9133 | -15.62748 | -46.25713 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ab0a566-b0a2-3d46-8846-913b553ad63f | -19.86026 | -44.55117 | 2025-09-30 04:42:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| d6fbfe64-0b4e-3dea-989c-db2103aefcf5 | -15.27061 | -49.25084 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ad8eed66-012d-3927-8f20-d3f20f67ba60 | -15.77841 | -43.67565 | 2025-09-30 04:42:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e44457c7-ff97-3e78-8d5e-9f06a486767e | -16.61683 | -49.20167 | 2025-09-30 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec7fcaee-4bf7-37ec-a30f-ec680cd25a6e | -19.94221 | -41.64214 | 2025-09-30 04:42:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a5e14a3d-8d2e-319b-b04e-e331ad3ad6cb | -17.89599 | -57.60155 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6b7403db-f833-353f-ab32-2d944632600d | -18.4803 | -44.0186 | 2025-09-30 04:42:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6248eb40-52df-3a2f-a933-e7eb4419b7b3 | -15.14676 | -46.43565 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bf1dab7-1a4c-3885-a0f3-d87a167deed7 | -18.33122 | -57.10458 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3b7f3ffc-2772-317b-be38-58a51bd9fe2e | -15.71829 | -47.58113 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40a2a2aa-ed4d-3b0a-a1a6-ded23d52dd7a | -15.84851 | -46.24709 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04aadbdc-f7a6-30ea-aa2b-6bfa88859615 | -14.70201 | -48.13977 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46a110fa-faaf-3c41-a8f0-f63a901f569e | -19.79725 | -46.51789 | 2025-09-30 04:42:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0facdfeb-e456-3afc-a753-d0110def5042 | -17.41624 | -47.13326 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9372182-1de8-397d-862e-06b5f3e4ac51 | -15.21126 | -50.10306 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64fe0f4c-8d80-32ba-a2be-1d6815115b9d | -14.56432 | -48.46261 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9eb44e0-d040-3e63-a232-134552315dc7 | -15.93194 | -46.20898 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2ac7be03-67e7-3034-ad9d-d318d59691c7 | -13.73607 | -52.59921 | 2025-09-30 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d32cc9b7-e6a1-38b7-8a48-6875364778b9 | -15.52163 | -50.0451 | 2025-09-30 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a29de668-e0aa-3d9b-94c7-0ad75a4ce88a | -15.25289 | -56.83279 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d8bb349-457e-34a4-aa92-e7153bad268a | -16.41633 | -53.54094 | 2025-09-30 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cca3bd34-8a36-35d9-897c-f8844aec3fc1 | -14.27058 | -52.93964 | 2025-09-30 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f818a10-cce0-3441-8cc6-33859e02423d | -17.3927 | -47.12838 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96bff7ae-55ea-3016-9463-b5b4c5968ace | -14.70908 | -48.23046 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac339aae-a9d7-3ec7-aef6-2831294d23a7 | -19.86061 | -42.59196 | 2025-09-30 04:42:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| cad579fc-3f52-333e-b9e9-28d75ddfcbd1 | -16.07268 | -51.03463 | 2025-09-30 04:42:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0d79dca-7b86-3024-a06d-ebb35854e192 | -15.68909 | -46.263 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee6f00e7-d172-314c-88ac-eedab3e52bcf | -15.16123 | -52.84447 | 2025-09-30 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 67a9cdc5-6312-3fd8-837d-800fdff69108 | -15.91288 | -59.49938 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78541907-de7d-323b-ad67-aee1eb617ea3 | -15.2694 | -47.85727 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32eb8d55-2146-3f64-b328-c0271901ada8 | -14.68771 | -48.13666 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| aed190b4-99c7-332e-a102-0149a41b1de3 | -19.87164 | -42.59301 | 2025-09-30 04:42:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 34e3030b-1e90-3922-86ad-58b2201a171d | -14.58978 | -48.28246 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60c77037-f693-3ff1-bec7-7142b3e54db9 | -14.58619 | -48.28196 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23fbfd58-99a6-3250-a128-a4c7a2338c43 | -15.42345 | -48.24521 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0713cce-71a1-3364-8a3b-249be65e3006 | -15.55347 | -44.33617 | 2025-09-30 04:42:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c7ac8d2a-21d5-345b-b76b-e62cbccaa7df | -15.9327 | -46.21053 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4e43bd4-90ce-3db9-b5f9-877e009abd48 | -17.09713 | -48.56303 | 2025-09-30 04:42:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d7a33fe-c3d5-330b-a3f1-209bccc6ec90 | -15.20961 | -50.1141 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbf1da15-7858-39d5-8521-8bfa348a9fd7 | -20.53308 | -43.13457 | 2025-09-30 04:42:00 | NOAA-21 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 864857b5-5c67-3a8e-9b06-0bcfcbc95e5f | -14.53948 | -48.25964 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 06b363ca-9242-3383-be5a-f5f9bac8ac41 | -18.12359 | -42.19176 | 2025-09-30 04:42:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| bd8be519-041b-353b-a23b-1a1fe341c440 | -15.87876 | -46.20693 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d966b75-cccc-32fa-9024-61d58f8c4a89 | -15.90579 | -46.22413 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25a0a057-1fb6-3b38-afa4-e4e0242b1262 | -15.07452 | -45.06247 | 2025-09-30 04:42:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed11b78d-aed3-3c21-b28c-1a51239eddc3 | -14.54007 | -48.25549 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e6be4c4-40d4-3985-9580-4399784d6bf8 | -14.54602 | -48.26508 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0ca35998-54ed-3009-841b-4dab66a9c3a4 | -15.17541 | -52.82051 | 2025-09-30 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72a14d04-4202-3487-9905-1f51e8c8d975 | -14.52007 | -48.44476 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 22f67f17-03b7-3304-b372-3623527733b0 | -14.57845 | -48.28498 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bd62cfc-979e-3ae7-854d-4be76d8dc78b | -19.33199 | -43.80042 | 2025-09-30 04:42:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0623f2c-3c62-3928-afc8-6ca42b16e5e7 | -16.06273 | -51.03299 | 2025-09-30 04:42:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e9d182b-636b-318e-b144-3f8e7f0f28bc | -16.16658 | -51.94129 | 2025-09-30 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5493b2f-8d5d-30c1-a16a-f07523fcf678 | -14.51474 | -48.4565 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cdf15038-e9e2-3960-a83e-0b67dd768498 | -15.67685 | -46.26116 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82a1ccbf-48f5-39fb-b5b8-48d1a11d2aeb | -14.54013 | -48.22953 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 593ad824-dc4e-3cc4-aaca-d4ef99170f8a | -15.23979 | -50.09655 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 093b2186-18bb-3405-b49d-c8761b91f3c2 | -14.5183 | -48.43188 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6afa0f7-41c8-3d4d-979c-5ba18bb92732 | -14.58216 | -48.21805 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52ae075e-2472-3051-9c9a-4a719193d979 | -14.51354 | -48.4397 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cb488d04-ce2b-3ee8-85c8-207979259ad4 | -16.20975 | -52.8242 | 2025-09-30 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2642bf8e-1372-38fe-b2f0-20fabe33851a | -18.05745 | -43.65533 | 2025-09-30 04:42:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bab909a-e7e9-3702-8f96-9a595163e804 | -15.05201 | -46.98033 | 2025-09-30 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52cfbd0a-707f-3214-bdc2-32b5760bd9dd | -15.6025 | -47.82672 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 616c4a34-0537-3109-974d-dcd728cb4a3c | -14.5508 | -48.25732 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 563bf13e-a7ce-3050-8da2-0f3eafcfa6da | -18.32733 | -57.10381 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 85a18b2f-8986-3bfd-8237-28671a6ee479 | -14.16475 | -52.85671 | 2025-09-30 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f927d58-6813-3b42-a0ed-d610882c22d0 | -14.51597 | -48.42289 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98381ef4-9f79-340d-a1e0-db22d6b15343 | -14.52066 | -48.44065 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57323d39-c21d-32eb-af68-440ead133dc6 | -15.06685 | -45.05266 | 2025-09-30 04:42:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7857e761-085c-313f-8adc-cf8fded7ae73 | -16.5789 | -45.10669 | 2025-09-30 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87bcd3a2-2265-3533-abcc-f468c8a0277f | -17.70269 | -46.66083 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d66d1fa0-dded-3d9f-951f-e3ee5bc1795f | -20.23298 | -41.34145 | 2025-09-30 04:42:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66268bea-8e9d-3ff6-9025-284d4ef4670e | -15.2774 | -47.85395 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcebb580-0183-38dd-8536-23133679e8fb | -16.29266 | -44.926 | 2025-09-30 04:42:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 739e7d51-fcee-362a-9e85-a5c3f9d8c08f | -15.08204 | -48.33354 | 2025-09-30 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59699195-e555-3b5f-bb9a-5ca724c8fe58 | -16.67945 | -44.55786 | 2025-09-30 04:42:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d72583cb-b4f2-3913-b412-f266f3114f6b | -15.30126 | -46.40527 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fe5b531-23b5-3d37-83e3-7fae74ef1beb | -15.2624 | -51.47979 | 2025-09-30 04:42:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 719fcf7c-d3ee-33d6-a6f6-9bf1979a5f56 | -15.55729 | -47.87947 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README79.md)
