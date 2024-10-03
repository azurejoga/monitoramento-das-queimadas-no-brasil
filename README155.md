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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74fbd898-8289-3357-981e-823f425360c8 | -8.75605 | -67.70106 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 496100dd-245c-35ab-a2b7-844a5a78b59d | -8.75552 | -67.70395 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b2fa2d3-a379-345d-aeef-5b6b5b6ee13c | -8.755 | -67.70685 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01d81592-57ff-32b4-a5a2-7e3c7634b1e0 | -8.74743 | -68.69631 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f267714b-fd33-3ee6-af43-c59b1575a5f7 | -8.74209 | -68.6953 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86f7ee00-99f3-3f43-b54f-57d2007d2280 | -9.39734 | -68.11839 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2711b07-8293-38b5-8791-4dce06a09a3c | -9.36512 | -68.20937 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd4e9243-526a-33cb-8605-7a6dfa98b122 | -9.35945 | -68.21145 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 079d8af2-e9a2-3484-b8a6-f3b80406b1f6 | -9.356 | -68.20136 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eab23b6-ff0f-3e44-92ab-5828d03769cb | -9.35434 | -68.2105 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85b13c34-aeaa-3de5-b9c6-cfcac84f6ea7 | -9.27725 | -68.36937 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff81a38e-0f6f-36ca-85a1-00f91cbdd505 | -9.2164 | -68.17027 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aa3f800-6561-303c-9da8-9edfa0920bf0 | -10.63781 | -69.05238 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fc21098-d8c8-39bd-b791-9f102cfbcbec | -10.63719 | -69.05573 | 2024-10-03 05:16:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdb667af-1053-33b4-a834-d2f753eec356 | -10.62751 | -68.7306 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 690fcff2-f5d1-3321-91c6-f7ec6893ffc4 | -10.62692 | -68.73373 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b941620-5801-3083-8444-53a0bf8c244d | -10.62354 | -68.72324 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c31aa9a-ef71-3f2a-9d52-dc7168d4ab59 | -10.62295 | -68.72636 | 2024-10-03 05:16:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27b03b7b-2c3d-306a-aa5f-c08823c51102 | -9.401 | -68.15656 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6933d188-1b23-331c-b052-1a57cfef27ad | -9.39775 | -68.2633 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 995cc7b8-4a32-3486-ada2-db0c637d2989 | -9.39724 | -68.3055 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6659572e-d867-31c0-a2a7-1ee10535a611 | -9.39568 | -68.30473 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac747634-67a5-3779-9488-d4e8b8904c1c | -9.39564 | -68.25706 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3289dc47-5c5b-3560-86f8-79d536a7683f | -9.39152 | -68.30766 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73efff4f-21ce-3fe3-b1a5-722736aad323 | -9.39091 | -68.33958 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e6e334c-58da-33c8-ab80-a15722397f18 | -9.3905 | -68.25615 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a75d4e3-a417-30b6-82aa-717c3ccc26dc | -9.38993 | -68.25922 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cabfc895-6139-3fba-b67e-429fcc3340e0 | -9.3896 | -68.33886 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ec5e48d-eaec-3740-9e5d-d5cd21ad0b97 | -9.38904 | -68.34196 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c232be63-8595-3245-960b-64e36293f2be | -9.3839 | -68.3409 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cedafefb-f3f0-362b-bb29-6a8e7a36ec5a | -9.38063 | -68.33751 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9744e88d-cd50-3257-9fbc-450c6dfbff7b | -9.37987 | -68.33369 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10a517b7-ff32-3d8d-938a-bb24d4d994f3 | -9.37932 | -68.33677 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 576af697-2922-3fb7-9c40-aa2ac6acb702 | -9.37876 | -68.33986 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f3a216f-a8be-3c09-8fbe-8acf8664fce9 | -9.36591 | -68.79786 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d14d7357-cec3-3643-8f33-99e0d71ee0e0 | -9.3653 | -68.80119 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3a0b9fa-bc26-3c68-bf34-d0e480ab277e | -9.35528 | -68.79587 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29fb7d49-893a-35f3-85cf-7d91609f6fcb | -9.35071 | -68.911 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7a8aa90-b310-3dd4-a4ae-46c5e1df63c8 | -9.84723 | -68.79794 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed9523f6-07e8-3839-98fe-ca6fb9337838 | -9.84682 | -68.79547 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b7df071-3302-3c06-a0f1-32b4e3458955 | -9.84618 | -68.79887 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8317733-c968-304b-bbcc-8f3b2a910310 | -9.84198 | -68.79676 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b56c39cf-769c-3e0f-910b-5e2a53d8860d | -9.84157 | -68.79435 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad9d8ef6-a2f1-3417-afe8-2dd48a0d8434 | -9.82952 | -68.9164 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed5b0e97-fbd5-31ae-a6b9-381c75144eaf | -9.82672 | -68.91141 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5cc9e26-d2ed-3cbe-8417-4652367f6895 | -9.82611 | -68.91476 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c03c9a-58c2-3172-a964-fb70c50c0d5b | -9.82484 | -68.91203 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9170c84-2275-31de-80cb-8adacf63265f | -9.74826 | -68.42261 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a57ba0cc-0a1b-39b4-a34d-50c391cb8d0e | -9.74312 | -68.42162 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb710fb9-66b2-3d37-8bcd-cf5fa5ef688a | -9.74255 | -68.4247 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8122b02f-cf4a-33aa-8178-efe01e72371e | -9.74198 | -68.4278 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42945a2f-35b9-35c2-aa26-97622be6927a | -9.73741 | -68.4237 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f803875a-2b59-31f4-a82d-88c7697da6bc | -9.73683 | -68.42681 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9c65b5f-8b85-3ddf-8556-a380bf9d69ae | -9.73626 | -68.42992 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de220d41-3aff-36d6-abae-185e1f254834 | -9.73511 | -68.43618 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0902dcd6-caad-312f-b8e6-831ce7d4ca0b | -9.73453 | -68.43934 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63bda8c5-4477-3ac9-b619-b5d844cf9cee | -9.72995 | -68.43523 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 771dffbc-01d1-3c7c-af24-f20b0d6b03a2 | -9.72937 | -68.43837 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5a57ba7-0b16-3459-aa4c-f6283ea0a9b6 | -9.7289 | -68.3833 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3c053f8-7670-327a-87f1-a8de180e59b7 | -9.72376 | -68.38235 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c92aec67-872c-3b21-b086-b4d4312ba28e | -9.68637 | -68.8186 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7419bb2-5b5e-3bce-8fdb-7a234e1581a3 | -9.68107 | -68.81762 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7d0ee95-e23a-35b7-aafd-60c152c343ba | -9.677 | -68.81001 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 494e5fa2-7ddc-379b-95aa-5623a172c495 | -9.67171 | -68.80901 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e16522b0-d584-399b-96db-12954bfcd523 | -9.67109 | -68.81235 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bbf3dfc-26d4-37ab-8e8a-570b13ac3177 | -9.64346 | -68.63949 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5485b1ee-f75d-3b4f-9780-964b1c6d49b5 | -9.63733 | -68.64382 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12867d8b-3fd3-3bb3-bab6-6c7013955e52 | -9.63673 | -68.64708 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1b5c20a-c823-33e0-8395-cfa0eed845d6 | -9.63328 | -68.63627 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b26fe02-57fa-343d-a0d5-3d94828a2218 | -9.63268 | -68.63956 | 2024-10-03 05:16:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 386451f5-5ec0-3b4a-87ab-bcadc48e67f9 | -9.36059 | -68.79688 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b65f53a-b85e-33b0-9304-04f3beae9730 | -9.35997 | -68.80023 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cf1dd07-429f-3191-9fe9-30011897fecb | -9.35465 | -68.79926 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32a32332-04e8-3614-825d-7187895d5b57 | -9.35133 | -68.90762 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0a148c1-53eb-3b3a-8e08-d415c25047c4 | -9.54973 | -68.26743 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6dd84a6f-7673-3d19-a35e-c2f02108354a | -9.54916 | -68.27053 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db7f3ef4-a486-3de6-93f5-f86e04c05479 | -9.51373 | -68.43441 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2ba8d8c-0bf0-3ad1-98ed-9376b2a2ad51 | -9.50911 | -68.45949 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a872db8-c721-3646-9709-06c849bf32ad | -9.50627 | -68.44581 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11855618-c995-3bd2-8448-6c10a7276fdb | -9.50569 | -68.44895 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ddd2ed2-ba15-3325-9022-11034738f55e | -9.50511 | -68.4521 | 2024-10-03 05:16:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86ccee46-4b01-3ef2-a63f-47ba322aabf3 | -9.50065 | -68.05769 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0f756d4-fa73-3688-8201-0995c5e91538 | -9.50011 | -68.06065 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81f018f9-6b97-3077-860a-595697be34d3 | -9.4956 | -68.05672 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 955f99ad-64d3-395b-a6d3-647c4a1d3c9f | -9.49507 | -68.05968 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c36062a5-1b86-3696-9c67-7869dda666a2 | -9.49001 | -68.05875 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de0551da-669a-3b39-9d04-467fcbca5bfd | -9.47295 | -68.26888 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea1a8caf-a671-3be9-9a26-b5143ec41786 | -9.39592 | -68.15556 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d281bc2-eae7-35c6-a143-99b0b69cafc7 | -9.39512 | -68.30785 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f88b3753-d0ac-3f10-84d5-93ff974850b4 | -9.39506 | -68.26015 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba946485-b0f5-318b-b045-07d1bdf5b8af | -9.39448 | -68.26324 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b33d9db-b138-346a-8554-7368cb4b4d99 | -9.39319 | -68.25922 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7d05c22-2247-32dd-b83f-986ce4ece445 | -9.39263 | -68.26231 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69814620-a4ab-3f3e-a84e-c440543f3775 | -9.3921 | -68.30457 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b020837-8301-3d2b-9e75-b795c1b43ada | -9.38178 | -68.33137 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2c43e13a-1ed9-3a88-be87-34c7eb4650d3 | -9.3812 | -68.33443 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e881884e-fbfa-3ea9-8d3e-f5f980e99b2f | -9.38042 | -68.3306 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 61d8d041-475e-3455-8bab-41269ebf5323 | -9.38005 | -68.3406 | 2024-10-03 05:16:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 195a648c-c2ac-31c2-b18c-f815a33322fa | -9.51446 | -67.43584 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeb79fa4-1b25-3ad5-a19c-2b757ef46a21 | -9.63145 | -67.47052 | 2024-10-03 05:16:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README156.md)
