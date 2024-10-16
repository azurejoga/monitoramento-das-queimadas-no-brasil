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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d49db8b4-4ad9-3c24-904b-b7d726668feb | -3.77624 | -51.34572 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff7d62f1-0828-3f74-8f5b-703ffbf9c2e0 | -3.77548 | -51.35036 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34d87350-e4eb-3300-8b0d-d2e233070e7a | -3.77473 | -51.35499 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a8123e6-58ad-3618-a3b9-f8e2a79265c8 | -3.77244 | -51.34508 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ed2743-7710-3192-b496-14a59433517c | -3.77168 | -51.34974 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8e7ce1b-bae1-36c9-8c6c-a68935037dd6 | -3.77092 | -51.35441 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62328a2f-17ee-3b59-872f-576b01e097a6 | -3.74829 | -51.93721 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f1c9913-7502-373c-a69c-8a3e6bee102b | -3.71662 | -51.40503 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd642e58-0405-3887-90ca-abd42bc420b8 | -3.70043 | -51.0497 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bc6da5a-592d-3797-9859-a708780a6df3 | -3.61705 | -51.48615 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbd0561e-e260-36b0-9344-445ab4c2ef26 | -3.8704 | -52.27205 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a30cc309-468b-3b98-9b53-5fcee0414582 | -3.78819 | -52.23696 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aff3c4a9-3c82-3678-a46d-88e022fb02d3 | -3.78763 | -52.24044 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e85a573a-a23f-3f20-950c-23233708ae77 | -0.61073 | -52.38615 | 2024-10-16 04:29:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c22622b-30e4-3867-9315-efad63f2bb4d | -0.61009 | -52.39018 | 2024-10-16 04:29:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b5ccd20-2f3a-3618-9937-56101df6a9d7 | -0.01903 | -51.90892 | 2024-10-16 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcc540a0-00fc-3b7f-a1f6-1a0153d3da96 | -2.07859 | -52.26041 | 2024-10-16 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a214ecec-fc2a-3957-8ded-be7c770dd588 | -2.07606 | -52.26009 | 2024-10-16 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eeb316a7-7f8c-3892-9853-0ec596d80233 | -0.98244 | -52.44227 | 2024-10-16 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37d6549f-b659-3967-9a9c-e64c48f6a56c | -0.9818 | -52.44622 | 2024-10-16 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6fd0d5ad-4a03-3f16-ba19-7ff23cb8f970 | -0.97819 | -52.44159 | 2024-10-16 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81132361-5d1a-3154-a297-37979bc6c776 | -0.97755 | -52.44554 | 2024-10-16 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 932bf595-858b-3acf-ae17-c99752577e30 | -0.97691 | -52.4495 | 2024-10-16 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8fef1a2-730f-31bf-bc50-b5c8bcfdef62 | -3.33829 | -53.54208 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c5276f0-4b29-38bc-a8fe-fae6bfa031ea | -3.0507 | -53.25988 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de5df194-7073-3cce-9738-2e76073e87c5 | -3.04704 | -53.25494 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d8dd2a0-7396-3b64-a437-4501f40bfd95 | -3.04337 | -53.25013 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a13fd7d8-dc11-305e-a366-256494bf8a39 | -3.04269 | -53.25428 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2995aea7-35b5-3349-a4b3-5e12cdca92fd | -3.03901 | -53.24949 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b374701-293f-3324-af26-b7d86fbe9972 | -3.03533 | -53.24469 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46784b17-ddbc-3278-abc4-f0329adea1bc | -2.6966 | -52.44482 | 2024-10-16 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25eb0da1-18eb-3138-b9af-f4389756b644 | -2.69296 | -52.15139 | 2024-10-16 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 608c77d8-9370-35a4-a183-48e930a68d9a | -2.69245 | -52.44419 | 2024-10-16 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30c4dd41-28e6-3b34-b4ce-804f108bc7a3 | -2.32312 | -51.98674 | 2024-10-16 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cfea756-3d33-35fe-ba71-c5c0fc2a924a | -2.09332 | -53.41134 | 2024-10-16 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65c783db-54a2-399f-aa9c-10b4de89ea0a | -2.08886 | -53.41062 | 2024-10-16 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abb4948f-0613-3aac-983f-b6fca9b35c0b | -2.08816 | -53.41503 | 2024-10-16 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d41324e-3ba7-3a95-8e03-9977a35e95bf | -3.42045 | -52.77439 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 706de591-e373-33e1-a283-025016ccd524 | -3.33759 | -53.54635 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 090e1942-52cf-3422-a4ed-812defeae446 | -3.05001 | -53.26412 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cc40ad2-f1f1-3263-8a05-e30f0b84a417 | -3.04772 | -53.25079 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8e8b5b7-2d4d-32e4-8af7-fb538eead45c | -3.04634 | -53.25923 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db8ab507-289b-3b39-b47c-6654d59db614 | -3.04199 | -53.25852 | 2024-10-16 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6841dd4c-18f5-35f2-a18b-9de2a24def41 | -4.31144 | -53.71437 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ef1799f-fac1-351d-8ef6-a2de40760bf0 | -4.30705 | -53.7136 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1593785c-a148-3d0d-81a4-9fbdbb4b1993 | -4.26369 | -53.67553 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12305a90-1da4-3fb9-bf75-a015cb3eef5e | -4.01667 | -53.80291 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ead487-433d-3b75-965d-7f037b366b68 | -3.79469 | -52.2993 | 2024-10-16 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef8a3593-03f3-33ae-91a7-40d30f716dfb | -3.69201 | -53.44753 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efbf3f28-210b-317b-9432-e1efeef5878a | -1.51886 | -54.80244 | 2024-10-16 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4473598b-e3ef-3047-9fe8-b6534913f5c2 | -1.5139 | -54.80165 | 2024-10-16 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2905b953-1cee-39e5-b926-0fd5fbdeb01f | -1.51098 | -54.52069 | 2024-10-16 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc40f68c-9eb3-33f3-8334-b52c4a352c1d | -1.5032 | -54.31834 | 2024-10-16 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20577cdd-e99c-3244-902c-90a1372f3bbb | -1.24307 | -53.38031 | 2024-10-16 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a29f8b4d-3538-3e8a-bd13-6732374586f6 | -1.23854 | -53.37963 | 2024-10-16 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae230223-572f-342d-ba26-bff3f749e052 | -1.0231 | -53.73273 | 2024-10-16 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17fc3cfe-caab-3132-a73b-5182d5fde39f | -2.2049 | -53.6599 | 2024-10-16 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 30194413-6a97-35b2-aa61-2fa8e5a04dc0 | -3.15183 | -53.93609 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bae0f75e-27a3-3491-9e5b-35d231098f67 | -3.12756 | -54.28728 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b695af05-0587-3c1c-83c6-27cdcfe68695 | -3.12531 | -54.24232 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e9eedd05-cfb1-3d6d-95a5-5cd0ed1ee94b | -3.12223 | -54.23198 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7a962181-e6ef-3c82-9920-d2a1cada279e | -3.12145 | -54.23674 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| fbd32e06-33d2-33a2-a8a3-dd98843ac15d | -3.11837 | -54.22636 | 2024-10-16 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aaf29f42-b90c-3251-a478-718871f13605 | -3.11729 | -53.73982 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78e1ff36-201d-3d22-b749-7bb428b9ed67 | -3.11456 | -54.22053 | 2024-10-16 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1f738fde-91b3-3681-8103-553876766cb0 | -3.11374 | -54.2255 | 2024-10-16 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1441aeec-c211-34cd-ae9f-15344b3a4aea | -3.11353 | -53.7346 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0364cb9-85a2-3238-92fd-efef7c55c29f | -3.11216 | -54.23516 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 99c3e8be-714d-30b1-b9f6-87623f9a9d16 | -3.11135 | -53.74808 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9f0c36f-164b-3bcc-a62e-cb3072309d3f | -3.10993 | -54.21967 | 2024-10-16 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f4d95c19-93eb-305d-bfae-6cdad56b99f8 | -3.10829 | -54.22964 | 2024-10-16 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ff05eafd-2e75-3557-8e0a-626cca68e031 | -3.10382 | -53.7376 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be67e158-177e-31c0-8eb8-8d48f15bcde2 | -3.48832 | -54.45935 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3ce73c7-5b6b-357b-8486-94e08c9dcc5d | -3.26654 | -54.18386 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8ea8c8f-60f8-3467-95f0-480bfccb1d3d | -3.14728 | -53.93532 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7eb0827a-709d-3152-b58e-ba870a022e9a | -3.12067 | -54.24151 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e1bdc48d-4560-39ae-93cd-4195f2f4ca45 | -3.11758 | -54.23121 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8cf8022d-80fa-39f0-adb6-6acbcfeed57f | -3.1168 | -54.23596 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| dabac121-e54c-3ff5-aa1a-caa4213628e2 | -3.11657 | -53.74433 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0084e05c-d1e1-3d5b-b479-b3149ff16095 | -3.11602 | -54.24071 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| ba48884c-bee3-39bf-b88e-1bb2c7fc8815 | -3.11497 | -53.72562 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 177b9614-f405-3762-8d4f-bbded9f861e1 | -3.11425 | -53.73012 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71255f22-ff31-3168-a329-ebb370413399 | -3.11294 | -54.23042 | 2024-10-16 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 670a7eb1-d5de-3d52-8e0a-8ce364309822 | -3.11208 | -53.74359 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a9aae47-34d9-3ee8-bd44-67e5dc768141 | -3.10911 | -54.22466 | 2024-10-16 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| cf329468-9aa4-3d2b-9143-02ad851f3582 | -3.10904 | -53.73386 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ccb37ca-d28c-3640-8069-e05b926901f1 | -3.10831 | -53.73834 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2d5e001-ec5f-3a9c-99e1-4f0cb20fb874 | -2.93739 | -54.82369 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b82dacf-ebe6-335e-b70b-cefc8c7e1cbb | -2.9334 | -54.81754 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7030fe79-503d-3faf-b4af-3739279001ca | -2.93252 | -54.82301 | 2024-10-16 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0acc2287-5256-388a-aeb0-ccbf27710ac4 | -2.62031 | -54.33325 | 2024-10-16 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d778e5fb-a4e8-3d75-8915-15f8960f1ee4 | -2.39085 | -53.72635 | 2024-10-16 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b841496-c47f-391f-8a07-36187235bd29 | -2.38678 | -53.72791 | 2024-10-16 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6268033-0968-39b7-a901-4458cf82b161 | -2.38631 | -53.72564 | 2024-10-16 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 988db6be-eccd-3913-ad04-948a36b57f73 | -4.50676 | -54.97926 | 2024-10-16 04:29:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74ac61e7-2e51-3b1d-9955-06d3341d0dcc | -4.47576 | -55.40594 | 2024-10-16 04:29:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a177402-8589-3719-98dc-4042611c054b | -4.17798 | -54.58899 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afead96d-bc78-3af6-ba47-e3944f91950c | -4.17331 | -54.58813 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b41f145e-75d4-3f51-a33d-486ea4f19dbe | -4.139 | -53.96617 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25401c1c-3089-3904-9f91-f6a75931e495 | -4.0674 | -54.0258 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README49.md)
