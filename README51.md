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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7986a898-fc32-3d61-953f-25d2d4b73c1f | -3.05028 | -54.40122 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94a57b14-0b73-3386-a3fb-6886b1b77f47 | -2.2383 | -53.61471 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f3b0d87-9ce9-3693-9151-362f71cc5163 | -2.94233 | -54.8 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 676aeb00-296b-3730-8bbd-627e3a8116ae | -2.97487 | -49.29003 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 119c3689-238f-3553-82b1-26fb0d9c150d | -1.47126 | -51.1158 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e302e3f2-73cb-305b-9330-30ace006a6a8 | -6.48097 | -47.49618 | 2024-11-20 04:50:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 265bbf3a-1aab-3838-b69d-22371f85a50b | -2.68557 | -51.80712 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f6f70ad-221d-384f-a15c-61e5ec77a40d | -1.11176 | -52.39188 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9acdfc5-26eb-3425-8855-10cd4743df80 | -2.71033 | -49.86927 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cb810ec-e874-3133-875a-faa26064da09 | -4.1144 | -43.58562 | 2024-11-20 04:50:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ce59783-2709-3161-9ce1-35890a244557 | -1.10724 | -51.75482 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9c69fa8-8b20-3e3b-b599-1934e6cdd153 | -2.44906 | -49.14583 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ab9783a-8d66-3925-ac86-b718078e7d22 | -3.29452 | -53.84871 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22bc11da-a497-307f-80a3-87403727cb6c | -2.27735 | -53.63634 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cff2925-bd13-340e-b82d-7be546d628f2 | -1.62925 | -52.6758 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3f800b0-9129-3f3e-ba0f-07d2e4d8e19d | -1.37383 | -52.08038 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aeb5f25-e060-3e6a-83c9-bca16dd8fb23 | -1.61758 | -53.28294 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba6fb466-f62c-3d94-986f-9ccb275832bb | -1.45837 | -51.99382 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c533ed87-80b9-3ef1-af3d-c3f1741a8d61 | -2.60966 | -49.25168 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c216250-ad5a-317a-8fb7-aa7d8ea190fa | -5.45 | -44.82335 | 2024-11-20 04:50:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d1f8646-0609-3dd7-b17a-615ecae87c7f | -1.29618 | -52.24726 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5d7486f-842f-395a-882f-779c1333e25e | -0.92861 | -51.63795 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 248d9d88-06dd-3ce1-9aa8-cf5edea43dbb | -2.61842 | -49.24121 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86cffd35-be8c-3e84-a43e-22e368844fff | -2.68692 | -46.0835 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0910c3ff-a2d5-356f-ac0d-f133cd550ab3 | -1.74446 | -50.3499 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2dcb5a6-e57f-34a0-8f7c-7876533fd485 | -3.30621 | -50.36771 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a6e23f0-84b3-3350-9d50-35ca52f2eac8 | -4.13596 | -53.61113 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ed89712-a83f-3da6-ae23-7edf1c922d9e | -6.24903 | -47.26955 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a908bf7-3c64-3d39-a737-d99e21eeac59 | -2.56426 | -54.0749 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1735dd69-fa87-351a-b1ef-50b76c31b2ad | -2.91668 | -53.06208 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 35d8a44e-114e-364c-9d03-9e28951b5cf7 | -3.97669 | -49.91893 | 2024-11-20 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66b66183-4dee-334e-bde9-587625e0aeb8 | -1.61768 | -52.22597 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28414df0-3853-3959-8494-93a3a88b8861 | -1.68768 | -50.19645 | 2024-11-20 04:50:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f3ea34a-4449-3d78-982a-706218463a23 | -1.93564 | -52.99516 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 040b1034-ef3a-30b1-8b46-c697d8efc927 | -3.87843 | -47.07975 | 2024-11-20 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5771e15-1ebe-3c26-85f5-1aab86512696 | -4.16943 | -46.83027 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 427c934c-2ce9-3f1f-8287-ac313edb12da | -2.91049 | -53.05745 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 056eef4d-a733-3a67-8f2d-9287e9b0af2e | -2.9223 | -53.07031 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| a471e88c-b5b8-3030-a604-f0ac5b78c10b | -3.0461 | -54.40464 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa9576ea-0d06-3fe7-88b8-194cfcf394e2 | -3.50909 | -53.80107 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4dfb0cc1-ff2d-3e54-85b5-34ba773c2ef6 | -3.24055 | -54.16077 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e6ccb16-5dc4-344a-bf03-1f3ba7794209 | -1.66495 | -52.80554 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d21411e-fd7b-34bc-ac0e-371b40deb8f9 | -7.21123 | -55.00177 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1dd34ec-0f0a-32e0-87be-ffa1ef531724 | -1.53841 | -54.89821 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 913e7570-7958-314c-a51c-9c8d8b9c95fb | -3.50968 | -53.79732 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49938570-5fe7-3e5e-910f-e4c4baa5444c | -5.97814 | -45.36171 | 2024-11-20 04:50:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f5790f0-9e14-3a3d-871d-ad277bdafc74 | -1.45316 | -52.66673 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b25257a-4ab6-3c1a-83c2-93ef5374cece | -2.85593 | -51.58657 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e7cabc2-f3ee-3edb-a649-95cc36e297c8 | -4.44138 | -50.13616 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e71b2ea3-208b-32b9-aa89-8fcce2925741 | -9.17383 | -44.71819 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e487cdf-ac43-3d0e-b895-2c7fe405fb14 | -2.76963 | -52.60283 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1538a03e-01e3-3574-93a2-3e36b7d5b7c5 | -2.74847 | -54.11837 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 443fbd2d-7d9f-338a-aad9-cbca27bffe54 | -2.74661 | -51.82729 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 16e3cef3-3ba7-3c7f-ae90-d55a8450bbc0 | -2.41876 | -46.51427 | 2024-11-20 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4bd978a-4d6b-3a27-b74d-b029c2f8fce3 | -0.95649 | -51.72016 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02ca766e-327f-37ac-a32c-4471b1f25983 | -1.44585 | -52.66924 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af444112-a555-3ce9-90b7-62c9af4d04b7 | -4.45054 | -50.09954 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c73f10c-26cc-38e2-829c-91e851fc9714 | -1.39013 | -55.17585 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3660f079-058f-3296-8919-fc3eb6f5f25b | -2.73795 | -54.11668 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cb499aa-6948-388a-b2d4-813499836385 | -0.91285 | -51.78075 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 618275ca-d8ea-3e56-8d37-75c573fcff9e | -2.68845 | -46.2418 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2a80568-4fb5-3200-875e-0a3faf8f03fa | -2.00328 | -49.13929 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1097f25-82d5-3d22-b11f-39dce9dd6bf1 | -2.63435 | -46.56795 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d8bfe3f-7a51-3089-bebb-bf3de1c1f95a | -2.65132 | -46.1452 | 2024-11-20 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bce8689d-4373-3174-86a6-aeb85ee89960 | -1.44642 | -52.66565 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b14fc8c-e1d0-3b60-92c1-839920744e00 | -3.10666 | -53.97913 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d7ee01-ac07-330e-a73f-ad2ea196adc4 | -3.76735 | -52.13927 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3453d7c5-4726-3f37-907c-c14d475b918d | -1.437 | -53.38522 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d5a6b65-90ca-3e30-ae9a-d58d8ba57c70 | -2.57355 | -54.08437 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f44fe370-621d-3b5f-b3ae-45160cdf958c | -1.52098 | -55.48938 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 086263f7-ee27-3443-80dc-a1640f4430e7 | -2.71043 | -51.99485 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29dd0562-1d99-3955-b8fb-b6254b2e5214 | -1.98332 | -48.71263 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c033cf8e-c4ca-3ea5-b2de-cfc57adb9b18 | -3.80861 | -47.80637 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 92a50641-66fb-3f7d-af6b-8163ea3c9e06 | -1.39547 | -52.43558 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d74d15f0-c84c-3af8-9519-497bdfb5a138 | -1.66854 | -53.83294 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dc82bb8-da97-3a8f-a393-e35514bb7490 | -2.55785 | -54.06992 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6baa27bc-b210-3d4c-97b1-0efdd3eec9d3 | -2.62216 | -51.80444 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0b49a95-9ce7-37fb-ba86-c9742c7f1c96 | -2.34411 | -54.78232 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c56ddd01-93cc-313d-b1cb-e08d9fa0402c | -3.50832 | -53.80041 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a906888-5439-382a-9d8b-3edc4fd76172 | -0.9742 | -51.71583 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79e8d294-c002-35c3-a8f2-9cab58073286 | -2.93852 | -48.32225 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4af8c150-2174-3ee8-8f01-f1c899d58324 | -0.92716 | -51.73332 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 803bb6a9-2ec1-3553-b07e-41be8adfb3c6 | -1.49915 | -55.16844 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1ef3ed0-35b4-3e05-9b93-22b0ec5ff68b | -3.08746 | -54.6621 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6428c26d-5e71-37cd-95e8-5d9e591f19bf | -1.14791 | -53.51857 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d868ed6-2bfd-31cc-9d7a-189022035e5e | -3.00182 | -46.95845 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2610ed3e-08f7-3973-9950-2b40a0db6191 | -1.46461 | -55.45897 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfc3fb6f-90b1-3672-88d2-6b3b3d063808 | -7.15299 | -48.31918 | 2024-11-20 04:50:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2e53b93-58f7-3cb3-a059-8bc8defa5cb9 | -2.7234 | -47.97367 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a17a5ca-38f6-34fe-8e97-b08810ee72eb | -2.28401 | -48.40737 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11700ad7-9c37-31aa-83e7-fe5e5fe5aa31 | -1.22718 | -51.78751 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62e3e85a-6f75-3e17-81d7-d6b2e578898c | -1.9983 | -46.60424 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41606b74-5978-30fb-bbf0-e18a554326a4 | -4.99314 | -46.92092 | 2024-11-20 04:50:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce4a39b5-7f91-31cb-b313-0888b4c84f5e | -1.58742 | -50.44082 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5dcced55-4598-34c2-acc8-4c550d7eaba9 | -3.58964 | -43.62629 | 2024-11-20 04:50:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d1f2abe-f8ab-3d7d-ae6b-6435f0d91773 | -4.74452 | -45.41414 | 2024-11-20 04:50:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82d4c88e-3196-3216-b0ca-1738912678a9 | -1.38818 | -52.41644 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1e316c1-11a5-33ae-adcd-f2ae386efe4f | -2.56958 | -53.99599 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7caef3f6-6001-3062-8a4c-f73cf66950d0 | -3.01122 | -51.00473 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac6fbac7-403b-37b2-9fc0-f4feb1c645a2 | -3.97867 | -54.34799 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README52.md)
