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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3ec724d-a78b-3252-8f6d-383389dbab16 | -2.2906 | -50.66816 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f495dfe-82a6-3760-a642-3fbe006f5c66 | -2.28998 | -50.67229 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9b1b7e9d-02b5-3626-b51f-caec04a8cfde | -2.28278 | -51.92357 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d7a73e6-ebec-3fc2-aa5a-8c29fd7d2fb1 | -2.28039 | -51.9234 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf02aa2f-0937-314e-8df6-7659bb10fb64 | -2.27738 | -51.9228 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29ed9a01-f648-3e35-b99a-69aa8341bca4 | -2.27689 | -51.92617 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45d9549a-c037-39e0-913a-48cd2f82ce64 | -2.275 | -51.92258 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60256e33-3ecc-3b06-b2af-fb8f9f4bc7b2 | -2.27448 | -51.92595 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e8189311-791b-32c6-8426-89d01ab3705e | -2.272 | -51.92196 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08a0319a-d213-32fe-9a1f-c575b9fce825 | -2.2715 | -51.92532 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04776dfb-7fbe-3e6d-98b9-dcd0c371512e | -3.02553 | -51.37585 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c59b02-d8a1-3faf-9c7a-374a666c3c81 | -3.02045 | -51.37112 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 056a580e-894c-31cc-8bde-55f8e060c520 | -3.01989 | -51.37495 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9d1c4ce-b683-3e96-ad97-b9279558217e | -3.00751 | -51.57639 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74398059-ec89-3c84-911a-fd4bbd805806 | -3.00695 | -51.58016 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 417afa97-a567-3004-8cf6-5c1877ad27d0 | -3.0064 | -51.58386 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 84e48b55-5ce4-3373-b950-5b6a483ee1f5 | -3.00193 | -51.57557 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 321da52e-ef15-3860-bca0-edc57aa1c665 | -3.00137 | -51.57935 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38d05e7c-71bb-35dc-87c3-0e748ef2dd3b | -3.00083 | -51.583 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eedf8c82-5dcc-35da-9c5e-7b3215fbb15f | -2.99582 | -51.57835 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 64798b6c-5d8c-367e-8a83-93c4b6aafefb | -2.97378 | -51.43096 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f705f61b-7c11-361f-88bc-676273febca8 | -2.96873 | -51.42629 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02726e2f-320b-3caa-8507-cc4995240fe5 | -2.96815 | -51.43014 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d2b387a-dfb1-3e5d-8e16-497d221810f2 | -2.95941 | -51.05807 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6863725-cd11-3701-8f16-bcdb56923b7a | -2.95906 | -51.06021 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3b43aa1-6502-3f6a-ae75-4b2bd33fb86e | -2.95879 | -51.06214 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80c14d95-64e2-3687-af88-1644bcc66f53 | -2.95427 | -51.05315 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7f50e3a-6a99-30bd-bb06-09cc37a55d66 | -2.95389 | -51.05521 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f2c01ee-0c85-3dfe-b954-3997666d8c29 | -2.95365 | -51.05719 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f81b5f4-f0ad-3d20-ba26-815fe11069b7 | -2.95329 | -51.05931 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0613dbd4-5d86-372b-b5d4-15dae4cefdd0 | -2.95303 | -51.06126 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcfcabb0-5748-3912-836e-003462f6294f | -2.9165 | -51.46834 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c9607ed-2a00-3ff1-baf6-336696de9f2d | -2.91594 | -51.47212 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7a8b74d-70f9-3a26-b746-19aa0b45f52d | -2.90253 | -51.4854 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa9608d2-023e-382d-b8d6-15a5a8c35f65 | -2.89927 | -51.77457 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae136498-e8b1-31c1-9bf8-18422b601b90 | -2.89873 | -51.77816 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c57a4af0-2bbc-30ab-8333-ad2fa77e843a | -2.89694 | -51.48448 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 850bbeca-f1d4-3140-8ebc-8ec41db75ade | -2.88819 | -51.65976 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 966d751e-d487-3775-8da1-b083b3a5e819 | -2.88765 | -51.66338 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d281dc38-87bb-37fc-9d21-2dedb7a862ea | -2.88581 | -51.31057 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 085b0299-fc55-3ad5-9665-e1216eea8b53 | -2.88523 | -51.31441 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb783589-0d05-3d4f-9909-1ef2ffb8904f | -2.88321 | -51.65519 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4238463f-9d6c-3bcb-89ca-7bf99c5da8ea | -2.88267 | -51.65882 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b604b038-e0a0-3460-b0bf-e92b2b781645 | -2.88073 | -51.30589 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8746171d-e7e7-3d7f-ba46-7b0d966c16a0 | -2.88015 | -51.3097 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db009d59-d9bb-313d-845e-1a87d9e83e7f | -2.87957 | -51.31351 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee109d73-37cd-34f8-8bf1-be64aad0386c | -2.87506 | -51.30505 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11a808e8-8335-3b44-aab9-e1ef170ad20d | -2.87449 | -51.30885 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56aaa6a0-c098-3936-992b-bdf152af41a9 | -2.87391 | -51.31264 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4e6fd89-d4c7-33ee-badc-8dfea785c06a | -2.84511 | -51.80023 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe6d847-7b51-34e7-89d2-73ec80985ee9 | -2.84459 | -51.80286 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8f2c355-72c0-3a6d-9c8d-1649f0e45336 | -2.84457 | -51.80375 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 799dd760-7db8-3fa4-85b1-f57dc6125ee5 | -2.8386 | -51.80553 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 542a8a0e-d5ee-36c2-8de2-e6dd51dbbefc | -2.83855 | -51.80645 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ca58ee2-e083-3d0f-a21a-cb9a0164d834 | -2.83808 | -51.80907 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 869a5880-b4a5-3c20-bc28-3b2855e424f2 | -2.83801 | -51.80997 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aef96d6d-157a-3fca-9067-194ea0f6c003 | -2.83363 | -51.80202 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2221e1b-d08c-3cac-bd02-b5a6f02692cb | -2.83313 | -51.80463 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f71b84f2-31d3-3664-8d54-43106acde6a9 | -2.83308 | -51.80557 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74df4478-9065-3cd3-bacb-26bb818abef4 | -2.83262 | -51.80818 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f111ce4b-ceb6-3ef1-9946-3923935c5c37 | -2.83254 | -51.80912 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab999edc-3bc8-3bfe-a6f1-ad019d465d6b | -2.82816 | -51.80116 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99cce9c9-3a26-3d4f-8974-49365ee46581 | -2.82766 | -51.80378 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9514e2f8-d9cb-3a6c-bf73-6195d63d1e8d | -2.82761 | -51.80472 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbebda23-301e-3cf4-8ede-499d29715f04 | -2.82715 | -51.80732 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0642499-c7c4-3756-8713-52eaafa2c20a | -2.82707 | -51.80827 | 2024-11-02 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 901694f1-0115-369b-aa3a-60a0ce558024 | -2.81171 | -51.34216 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce82a247-1cc2-3eeb-b6e0-763fad0ec323 | -2.81115 | -51.34595 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 984b22ab-0b2d-3f72-bab7-59ee20b5e9dc | -2.80887 | -51.34098 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 034439fe-a999-3906-91d1-546350ef6040 | -2.80829 | -51.34475 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0ba8b55-adac-3cbe-b778-b755e2703366 | -2.80717 | -51.75476 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a9c5c45-6119-3383-a800-039a3b89bf2b | -2.80663 | -51.75829 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4fe42e5-df5b-3f35-bc08-fe53b5930231 | -2.80552 | -51.34504 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f108ef7c-0ac3-33a9-a417-e9fab094f7c4 | -2.80221 | -51.75036 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1929b1f-56c1-35bf-bb7a-7b6ed9ba3c40 | -2.80176 | -51.60279 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c6c7ed9-8d2e-3c11-9172-1f69ab0b0686 | -2.80168 | -51.75391 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6bc4805b-f7ba-3c07-9919-294108f1ee9a | -2.80121 | -51.60648 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3124803-33b0-3b81-b219-1fe9a0ac6751 | -2.80115 | -51.75742 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f33262b5-9acb-3805-ba4a-e1a4d6ac02da | -2.79675 | -51.5983 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6f8a52a-5fda-3955-9d7c-4ed78e9c0e6a | -2.79621 | -51.60198 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 86490cec-f2e7-3515-a70b-a1961c6ee5e7 | -2.79566 | -51.60564 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c27d9d12-a46d-34e0-9c29-e02abeccd921 | -2.79512 | -51.60927 | 2024-11-02 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 93844014-32ef-3692-910b-8c1eabe5396a | -2.76888 | -51.67183 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33216ba9-1c57-33b2-bf2f-86496c885cdf | -2.7639 | -51.66735 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07a489ee-fd0b-3a46-addd-ed6d384e43bd | -2.76337 | -51.67095 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b90051fb-16ac-3f6e-8d34-a552180a965d | -2.74784 | -51.73828 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d20fe2b-4e3b-32b7-8065-d6859ae24b0d | -2.74769 | -51.73718 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9001fd12-1a4a-3280-8535-48484ffee879 | -2.74287 | -51.73388 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f146d0c9-efdf-3f01-9035-70c44686b88f | -2.74275 | -51.73278 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23f33700-c1a8-3915-9daf-4ada4e63d1da | -2.74234 | -51.73748 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ef3c9c4-6d43-3dfd-9d3e-f9b6bef9e545 | -2.74219 | -51.73638 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84f0e138-2b53-3f94-bdf8-00abc6d2e893 | -2.74181 | -51.74105 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 593b3685-6cc9-3f25-995e-db201c2399d5 | -2.74164 | -51.73997 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a39ca24-573f-388c-aab8-80ee398d5f4b | -2.73735 | -51.73315 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c01eed55-4abd-39d6-ad71-1f9bb904f89f | -2.73724 | -51.73209 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5147e694-c0ca-3043-b2cd-0bee83c9943c | -2.73683 | -51.73671 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86545585-04d4-3bcf-8b27-65cde7c2229d | -2.73669 | -51.73565 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2fb7d46-e3b3-35a5-aa3f-782ec0997160 | -2.73614 | -51.7392 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62f89b79-b940-3d5a-9ae6-73c79fcc1464 | -2.73239 | -51.72869 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c3391cd-f864-34a0-804e-e99cc91f28f6 | -2.7323 | -51.72765 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README94.md)
