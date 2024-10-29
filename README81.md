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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 454fb3ef-a044-3c46-8017-b9f24623e3a4 | -2.85554 | -53.34148 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 670a1c41-3fee-3897-9ca8-878ff35043af | -2.85498 | -53.34509 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf1e24cd-21b2-3ff7-9c80-0ad9e813f521 | -2.85384 | -53.33009 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22e4546a-0c1b-3c4f-be30-a1a25bcd99e7 | -2.85215 | -53.34095 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46af67ef-a7a3-32b4-a612-b59e852fad3a | -2.85158 | -53.34456 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40a455b0-de24-3c5c-9261-bee248200238 | -2.851 | -53.32594 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d019f27a-2d7c-3dd3-a571-2fbc8626bb16 | -2.85044 | -53.32956 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7da4790-0926-390f-a4ff-5970c4b63fe8 | -2.84875 | -53.34042 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fac3b80-712f-39b7-a4c2-a4df64eba60b | -2.84819 | -53.34403 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa5ebfea-cb35-397a-a219-3c0012a48954 | -2.84761 | -53.32541 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be11abb7-3b24-3e8c-baa5-57d63d1a05d7 | -2.84705 | -53.32904 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a85d588-2e3b-310e-b690-3a01a2842beb | -2.8448 | -53.3435 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df7f839b-89ba-3b2d-9665-2dba91584994 | -2.84424 | -53.34709 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 420a9b67-f288-3df6-8479-92fe32335f8e | -2.84365 | -53.32851 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99409dab-9575-3488-8e78-cfd32a8d7acb | -2.84166 | -52.5515 | 2024-10-29 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74fdd099-d52e-3ebe-8845-67c60342d7a6 | -2.8414 | -53.34298 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1121b0d2-6dcf-3c3c-bfbb-f750eae71f72 | -2.84082 | -53.32436 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39724afe-3b40-30ae-89a9-74e9b81eb9cd | -2.78649 | -52.48489 | 2024-10-29 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44666023-c68b-3b72-9fc5-d7e0de8937ac | -2.69627 | -52.44024 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e445799-0c27-3823-9945-119a18ae5ea3 | -2.65688 | -52.53255 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd86ee6a-4627-3d0b-9cee-9bd26db20bd2 | -2.62273 | -52.45263 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c508bf2-337f-3e13-8e5f-bfc8c5c79338 | -2.62223 | -52.44941 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 491c351d-b7f0-3979-8d0f-e0dd76ff6f65 | -2.62162 | -52.45328 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1c3b234-c255-3ab6-95d9-4e9ac678e646 | -2.61934 | -52.44501 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| dce2b1ce-9e4f-3fc4-bd7c-1ffb7b00cabf | -2.61873 | -52.44888 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 801a88b7-9a63-3b9e-ade4-5cc9d0c4670c | -2.7594 | -52.05859 | 2024-10-29 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 406f1188-8e48-312a-a758-a1ddd2cadfc5 | -3.68072 | -52.27226 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6b7907f-629e-3557-8613-4d7b331aaa0c | -3.6801 | -52.27629 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52d674d8-ebda-3fdf-9cea-0c45760962a8 | -3.67948 | -52.28032 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 663dd1c2-7f08-3a54-8cf7-62aeb71c7ae4 | -3.67716 | -52.27173 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d386ebac-cd19-369e-aa51-aab1e12b1eed | -3.67654 | -52.27575 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 047adaba-86fe-3d03-8e91-1374054c69c0 | -3.55655 | -53.00673 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad742f80-136a-370f-8144-7478337c4faa | -3.53612 | -53.5191 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aa9f390-8916-3c19-baab-40d6984f0a68 | -3.53273 | -53.51858 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c110149-bb7b-3a12-a583-f8b81a613426 | -3.47647 | -53.25252 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e12fba04-f4a0-39fc-a522-10e43fc644a7 | -3.4759 | -53.2562 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d755069b-6a4a-3562-b0e9-f4533a3c1b1c | -3.47406 | -53.24896 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bf67a5d-30cd-36bb-b4cb-056b37f8eb11 | -3.47361 | -53.24834 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad8b59ca-5645-30cc-88a3-b245db5ea85d | -3.47348 | -53.25264 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abc07c54-a05c-3176-a8e7-b42296f0b755 | -3.47305 | -53.25201 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 342bc968-2965-3254-bae2-a0248f92e694 | -3.47291 | -53.25631 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4970fb25-cb28-3008-8462-0df87438ed59 | -3.43548 | -52.48391 | 2024-10-29 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3ffd0ee-4f79-30c0-861a-deec1d9b0eca | -3.4165 | -52.83532 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44065310-52e8-3f2a-a071-a7f001945972 | -3.41303 | -52.83482 | 2024-10-29 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08654d1b-1d7b-39c6-8cae-62c87937fcc6 | -3.40121 | -53.69009 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35337e98-895e-38c6-a7c2-65bc73cefe41 | -3.39783 | -53.68958 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8589e9d-cd39-362b-ba19-375d7b936d0d | -2.76234 | -52.06317 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d18c7220-f53d-38d7-a648-5c9ae7d2ab15 | -2.75878 | -52.06261 | 2024-10-29 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f854d44-2a40-3066-bcde-09a068d7fa64 | -3.7415 | -53.41225 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2182723c-2901-3341-ba46-302a65a3a3ce | -3.73923 | -53.40445 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ce785db-a21e-3e9b-ba01-98284309298d | -3.72271 | -53.39845 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b38f5a-9cae-3bc2-a1a7-a17126639b0f | -3.59687 | -53.5355 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 39ea9378-890d-3a2c-8b5f-537ca6ccd08a | -4.30612 | -53.70985 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ce47078-2bc2-3987-8bc1-1adadcb749ca | -4.21859 | -53.51023 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64fdb49f-5caf-35da-a2c7-f5a10434bacf | -4.21172 | -53.46412 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fecd012c-aa12-3a0c-aade-a841e8456274 | -4.21116 | -53.46778 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb4ef96d-5831-3a13-909a-066bd2a5783e | -4.20798 | -53.64646 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f481bac7-b939-345e-8263-d07554c4afa0 | -4.20148 | -53.46255 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87978190-4430-3176-9f5a-cd8828b2d774 | -4.20092 | -53.46622 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ddf3fd4-cb44-3c1e-9873-2ae31226cfa1 | -4.19807 | -53.46204 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a71f87fb-1a7e-3556-b573-7fffd2eea32c | -4.19795 | -53.46246 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 114aff61-6573-330e-8287-226450407ff6 | -4.1975 | -53.4657 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7ae5479-0250-37fe-852f-43efe3b2839b | -4.19737 | -53.46612 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccdd5157-400b-3b71-aad0-9316e4851699 | -4.17054 | -53.59275 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c48e8b64-45c9-337b-ba72-8e9daa0bcefe | -4.15015 | -53.54492 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5f2ab96-ad4c-373f-888c-18e28eec34c5 | -4.14277 | -53.45771 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85e1ca2d-8ea5-36e2-8eca-ab869348566d | -4.14221 | -53.64041 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a87817ae-23e9-37d2-aa07-5aa693a06872 | -4.13938 | -53.63627 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e227695-4c00-3721-a13c-c5d24f11686d | -4.13936 | -53.45719 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1dbae50d-946d-3863-a840-de2965d7ac3b | -4.13882 | -53.63989 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75955f66-9950-3495-a2d4-3158df042c6b | -4.12573 | -53.47758 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9014366-4260-32f7-a12a-3d935649f9b5 | -4.05263 | -53.41064 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0415e12c-2e9f-3666-9db5-d239b325c6ea | -4.04978 | -53.40645 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfce23f7-2410-3d71-b8b4-4be60dd51da0 | -4.04921 | -53.41012 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ce1cd03-0284-3e0b-8474-009c5b114e1f | -4.04407 | -53.23932 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e09eb31-d4c9-30d6-947e-fed7f3b2d5ff | -4.04064 | -53.23877 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcee0fe4-2852-3fd2-b4f8-d381c539b29d | -3.99908 | -53.37234 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c37ba34b-2271-3f84-bf9b-cc651f52f379 | -3.9387 | -53.46847 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a267f5d4-ed2b-3278-9c82-0aafcbb60e56 | -3.93813 | -53.47213 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3818813b-32eb-319b-b4f5-4c29e9c74076 | -3.9353 | -53.46794 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d615955-d194-3e7d-9a20-91565eef480e | -3.91415 | -52.39627 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17a795ca-ca11-37b1-8f46-4bf8726c0deb | -3.9106 | -52.39571 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72e26d93-00c2-398b-8304-77a3b3afec6f | -3.9079 | -52.36636 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1ef5978-8b13-3ace-b38c-d6e66305171e | -3.90646 | -52.39901 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2d4604a-6236-37a0-a205-371ff0d1fb27 | -3.89632 | -53.62913 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84d02b1b-f137-3b73-a4d2-9a197094bb36 | -3.89293 | -53.6286 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad3f0250-341a-31a5-be87-6131c47ff41c | -3.88763 | -52.37978 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00e13d0b-04d2-3d6b-a168-6bea001d8f73 | -3.88703 | -52.3837 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 251f29ae-715e-3ca9-ad8a-67e249b253cb | -3.88407 | -52.37933 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5dc78d69-5fb8-3069-bb1b-d395d1908289 | -3.88392 | -52.3093 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daf7ea14-45ee-3f23-8476-e0f6c9033431 | -3.88347 | -52.3832 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e306441c-c8b8-3309-8475-b0720aa0e201 | -3.8805 | -52.37888 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 329a298d-e3d7-3931-8a7d-46a01bfd3663 | -3.87991 | -52.38271 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd28aa85-cbb6-3008-b591-3028ab462923 | -3.87933 | -52.3865 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e0109a8-30e6-35f6-8e3f-8a6869f920c9 | -3.86551 | -52.31046 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44f0ed3d-aeb8-348e-a0be-bd18c880d421 | -3.83602 | -52.40845 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e442d6fb-9882-35f6-9922-0026ad31e238 | -3.83542 | -52.41243 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74909213-8813-3bdb-ac91-9a0a9ffcac8b | -3.83483 | -52.41627 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96309a2a-e070-3ad9-91d7-0f6350a321a4 | -3.83188 | -52.4118 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4648666e-3713-3178-8ae5-f3f8610b22f7 | -3.83129 | -52.4157 | 2024-10-29 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README82.md)
