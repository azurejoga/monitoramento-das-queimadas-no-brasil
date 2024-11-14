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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0348220e-8b1a-3fc7-867c-88614cc16bfb | -17.29324 | -57.47135 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 324aa408-cbbe-356b-bef1-60881cf8d470 | -17.82047 | -57.38025 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b3456ecf-3e06-3fdc-a39e-47a0ef38ffbc | -17.6293 | -57.5528 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f5211c5b-c6d7-3278-8996-451bfca6b7e3 | -17.60981 | -57.54579 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 26aa2f34-3d8e-3758-8969-49ddc0afe9a2 | -17.58207 | -57.43601 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bc17b77b-7e6c-3b45-b9db-0575d4c86f63 | -16.07513 | -59.715 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f3a3eb8-4785-3002-950c-7adc149b111d | -17.61315 | -57.54635 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 357e8fe0-473c-3502-bbe1-ec91a66a6371 | -15.90522 | -59.28203 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9707bbfc-a41d-3ba0-aef1-73e9dc95b9d0 | -17.25203 | -57.47197 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 9d22e5ca-af7f-35f0-9de8-850790e14492 | -17.63824 | -57.53929 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ce97af61-7cb7-3dfe-a160-e86908ce7978 | -16.94991 | -57.63866 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 739335e8-1904-33c6-89dc-609571b905e9 | -17.58934 | -57.41088 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2c5fba1e-e35e-3f1d-a974-fda3bea3b4fe | -17.58982 | -57.49743 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c5899e91-5fee-3e05-bdf9-d7c4467fe7c6 | -17.70511 | -57.53859 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 604df955-d6ad-3c1d-a9c2-ed9836395c14 | -17.63489 | -57.53873 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4b89ed7e-e213-36a5-909d-b4c5859786c5 | -17.58196 | -57.54863 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c4483179-c423-3dbc-805a-ef26a68ffbea | -17.67393 | -57.51835 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 719011fc-c0e7-3616-947f-a50589ae5bcc | -17.56694 | -57.53489 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 39d3b4c2-53b6-33cc-af87-1d9b3f593181 | -16.00442 | -59.40263 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| faec787a-29ab-3973-8c54-b91a75908ba0 | -17.60647 | -57.54523 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6ac94349-6e08-3f46-9f8b-b887fe427084 | -17.23923 | -57.46609 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 10b01656-53b3-347b-9ffd-c2991669ec35 | -17.24647 | -57.46356 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| f3ca07f9-e4a5-3b05-a44c-be080f05e063 | -17.25703 | -57.48403 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 438c2dd2-0826-3423-9740-35faba920e9b | -17.6021 | -57.48446 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 60ac9b36-5120-35d3-8b86-b7e9c6151f54 | -17.23532 | -57.49162 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d88cd7be-ec6b-374a-a47c-39388265ca0f | -17.64158 | -57.53984 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b8cb23b2-ea62-331e-801f-5e0f31617ee2 | -17.63264 | -57.55336 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8fbe803e-0b72-37c0-a3fc-cff55f713992 | -17.5915 | -57.48645 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d17ecee1-06c2-3bc6-802c-3108866cea16 | -17.24981 | -57.46412 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.2 |
| b1f14195-ec29-3aa2-8ce1-f683717c4fd1 | -17.601 | -57.46925 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7041b0f8-b6a7-3c68-9bef-22c5f165c0e0 | -17.26371 | -57.48514 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6dbb9ab2-f7f8-38f1-818d-516fc638d889 | -17.70233 | -57.53436 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d67e5c5a-6cb9-378e-ba3b-0ad0d20ea0ed | -17.59484 | -57.487 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8654c76a-a17e-32c6-a936-8c79ff66f838 | -17.70845 | -57.53915 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 12e7f8cc-1c0b-3264-9513-3a7c2a9d066b | -17.82103 | -57.37656 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1827109d-72b9-357a-bc75-423e051fdb41 | -17.58084 | -57.55595 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| b6cfbb71-c1db-34e5-a2cd-870af68300ae | -17.57752 | -57.53289 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d4f20cac-7c3e-3f15-8003-d0d6955cf3fa | -17.27039 | -57.48625 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 65d4d33e-822f-3dea-8d43-b0759b31ebe9 | -17.23533 | -57.46918 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9042c23e-026d-3ee1-8890-f143bc52affe | -17.70958 | -57.53182 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 82667976-b7ff-3c59-92ad-57fc487f3699 | -16.94879 | -57.6459 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 521f8ac5-1492-3ae7-afce-148cbc3e85bd | -17.5814 | -57.55229 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 56ddf812-2997-3c87-a0cb-d615a8bf4a7d | -17.76625 | -57.5107 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d4cce15e-974d-344a-aff8-51803322bea4 | -17.25369 | -57.48347 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bb8576a4-6423-3458-8d56-23b04b5c448d | -15.40935 | -58.60952 | 2024-11-14 05:05:00 | NPP-375D | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f8894c-bcfd-3265-bd4d-80cd9f136634 | -17.26539 | -57.4742 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8bf56eb3-b282-36a6-888e-4d20148d9234 | -17.23979 | -57.46245 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bb022756-f4aa-3554-b45a-53a6a1c4f5b8 | -17.58308 | -57.54132 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6e102cae-9a9b-3c3a-ab75-35e9ffaa9d73 | -17.5926 | -57.50166 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 528f1787-01dd-3309-8878-1dfe0b8bab67 | -17.61649 | -57.54691 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 4e845dac-8926-3c7d-8697-29f2d1668444 | -17.59589 | -57.54721 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6afa177d-490f-3248-8751-8ef50fae3b6d | -15.89108 | -59.28345 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b583b52-131d-3c2f-944e-cbda5a46e1df | -16.01028 | -59.38817 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57970962-695e-3a37-b797-54a6f0e2ea07 | -17.57196 | -57.52447 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 5003c7ab-fe11-34e5-8897-0d4c42724e77 | -17.57974 | -57.54076 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| dc28ccd2-2fdd-323f-94ce-ef1401e2ccef | -15.48512 | -58.19979 | 2024-11-14 05:05:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ec2caf9-e64b-3a2c-b95c-8acded68456b | -15.89965 | -59.31593 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c383d9b2-1e51-3b9e-9ed8-5c4bfa6c4ad5 | -17.58586 | -57.54555 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 85946a84-ca84-3dd6-be4f-cd31e2c98eb6 | -17.58542 | -57.43657 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e1e6ab37-bb58-3158-aa89-44e9f9c41944 | -17.58816 | -57.48589 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 396afc18-e712-384f-bdf4-9f194576f9cf | -17.58643 | -57.54188 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 33057fae-22d0-3591-a5e5-4e6a5648da0d | -17.60713 | -57.47403 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e9678246-afbf-3175-bde0-d8f0a49d129e | -17.59994 | -57.40888 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 6df0dd40-a963-3bba-afca-15bd7adb1c59 | -17.71179 | -57.53971 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 32e0749f-17d3-3d5e-b78c-087c61b65647 | -17.5675 | -57.53122 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 57598292-d9e6-3c27-b93b-f3b669671b20 | -16.24311 | -58.9306 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 14e1dba6-3b63-3bf4-9adb-928da73da6d0 | -17.63042 | -57.54548 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 52ad2a1a-8524-3287-bb32-c2c0394204c0 | -17.27208 | -57.47531 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4893e53e-7ca1-3060-96a2-9ac0d777da68 | -17.27151 | -57.47896 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| abeab83f-8abd-3be7-869e-91e641e36993 | -16.00505 | -59.3988 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36fc24c3-c0ce-3b77-a249-9edee9bdfcce | -17.25147 | -57.47562 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b1970295-f526-3660-b281-2cfe4bdbcc11 | -17.57362 | -57.53599 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 597dc1b9-6a8b-3d01-b18a-2eaa6beffe22 | -17.27264 | -57.47166 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2b332d52-31d9-304d-a18f-e7eacb85f1dc | -17.25537 | -57.47252 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7ae700fc-ba2d-3000-a320-fb85919cbd9a | -15.8877 | -59.28289 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8968667e-9b4f-377f-960d-d7097917263d | -17.61603 | -57.48302 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bff0e05f-bf9d-311f-bcf0-0eb654a451b1 | -17.70901 | -57.53548 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| e89848d3-56dd-3584-b9f7-4bdaf9c453e0 | -15.31481 | -56.51707 | 2024-11-14 05:05:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fea463da-cf9a-3dea-9e6d-517bc04396be | -17.57084 | -57.53178 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 274b1a55-e9c3-33a8-995f-106c9dfff1c5 | -17.59541 | -57.48335 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 33cebf45-a33e-39f7-82b8-2558903b42ce | -17.5764 | -57.5402 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e589c7ed-68b7-3e49-9047-c5cfd2670c0a | -17.5892 | -57.54609 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 12451cec-655c-3e88-88d2-4c11a2cd9f31 | -16.95268 | -57.64283 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3c0f5d9c-4a52-3520-8f82-1393000eaca3 | -17.58252 | -57.54498 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3a5a4d48-1ae4-3190-8119-2e0e9b30bf2d | -16.1031 | -60.09331 | 2024-11-14 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86d17ade-dbd9-359b-8f42-7d43d2db2935 | -17.57306 | -57.53965 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 87d4815c-d611-37bb-976a-6fa575a3a8b5 | -15.48569 | -58.19622 | 2024-11-14 05:05:00 | NPP-375D | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73cc712f-4a2a-3794-84f3-70765f9011a3 | -17.60329 | -57.40944 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c85b671a-ecfa-36da-ad50-9bd32a57e3d1 | -17.63561 | -57.44492 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a65f66ea-2e80-3522-adb0-e2ae4367cf17 | -17.21601 | -57.22637 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 11141daf-39b4-304c-8c4f-d848e23546fd | -17.62708 | -57.54493 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8c53e0d7-13a2-3055-a558-7cf0eebf4523 | -17.70567 | -57.53492 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| da0d7471-6c9a-3958-9fea-3ff9714e90e6 | -17.23589 | -57.46555 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d2484d1a-dc8c-30fa-bb8f-da4d4ecc8abb | -17.58474 | -57.55285 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 80e1b042-0b0e-3ff5-8ae6-4504dcd997eb | -17.23867 | -57.46974 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 829d8784-a2f8-3564-a732-6c7d32d196c9 | -17.5904 | -57.47124 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b8a390c1-b06a-3061-8842-23b8285a0610 | -17.63377 | -57.54604 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c2cec6ea-cfea-38fb-9d45-e1bb04f22209 | -17.25815 | -57.47673 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 12374d59-3e68-3999-b20e-02d6ff082da9 | -17.58752 | -57.55706 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 825928ae-2dbd-3fb8-aaed-8b03994865c7 | -17.60925 | -57.54945 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |


[Clique aqui para ver as próximas entradas](README51.md)
