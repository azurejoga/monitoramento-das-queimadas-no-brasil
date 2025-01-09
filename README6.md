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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e227ac38-c355-3bfc-a3ae-5bfa28a532aa | 1.94258 | -60.86776 | 2025-01-09 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b84ef57-74c9-3033-9e34-1cae4d83224e | 2.56969 | -60.69054 | 2025-01-09 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 536fc73c-7b25-35c3-adde-cc93e8e10eb0 | 4.1367 | -60.61391 | 2025-01-09 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 391e2acf-b6b3-34e1-91c6-3fa3e691c20e | 2.92311 | -61.11152 | 2025-01-09 05:52:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58cd76b6-6db0-3a53-8686-f3b5388559c9 | 2.56474 | -60.68722 | 2025-01-09 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f92948b5-c291-343d-abf2-23c9c7a584d0 | 4.18178 | -60.51852 | 2025-01-09 05:52:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6ace128-51d3-3908-8081-02024fd87da7 | 4.09299 | -60.61193 | 2025-01-09 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0834a2b7-1b38-3bff-83c8-3635e1cdb87a | 1.34514 | -60.03339 | 2025-01-09 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f4e2731-2744-3127-88dc-a2e54c6ff202 | 3.52952 | -61.3657 | 2025-01-09 05:52:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1ce5001-696f-3af4-9435-d89c8fd6314d | 3.53009 | -61.36925 | 2025-01-09 05:52:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79666b54-8fa8-39d1-afc2-ac14aca2334e | 4.09721 | -60.61125 | 2025-01-09 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ebba8b4-f68a-3fbe-a40e-2835177d84b1 | 4.18117 | -60.5148 | 2025-01-09 05:52:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e24746a-2fa3-379b-93c4-666e8ba8ca3d | 4.17753 | -60.51915 | 2025-01-09 05:52:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f07644b-df48-3c91-b0ec-c00a187d7d09 | 2.92372 | -61.11525 | 2025-01-09 05:52:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b10a96f-19e0-3a80-bf3a-f519e454d9fd | 1.34971 | -60.03258 | 2025-01-09 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1cd62ce-0cb7-3330-a34f-8aeeafb794d7 | 1.94323 | -60.87179 | 2025-01-09 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b52502e7-0d03-372a-ae98-d48e37216f07 | 4.08999 | -60.61518 | 2025-01-09 06:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4af7000-0e0a-3b5e-af83-82dbc9451875 | 3.18682 | -60.41912 | 2025-01-09 06:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeaee2e5-ce62-3719-a764-44282b33b273 | 4.09633 | -60.61414 | 2025-01-09 06:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda8b78f-4f98-3129-9334-f5815587073a | 4.09427 | -60.61634 | 2025-01-09 06:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43dc6224-889e-3f57-a3b6-13451764f50f | 4.09091 | -60.62035 | 2025-01-09 06:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a0b3f7a-ef91-384f-b927-2c39bcdb0915 | 3.53027 | -61.37135 | 2025-01-09 06:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52fde751-e3fe-31ae-bac8-7623a5009d1c | 4.18636 | -60.63266 | 2025-01-09 06:33:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 97ee038b-4b18-3207-b6d6-e8ede8a7c54c | 4.09085 | -60.60824 | 2025-01-09 06:33:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 595d0207-cd6e-3e7b-a1b3-090eb6dd0217 | 4.09217 | -60.61705 | 2025-01-09 06:33:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 08811bc9-bdd3-31a6-9b85-e8912254d72a | -10.4781 | -36.8588 | 2025-01-09 06:40:00 | GOES-16 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 94.6 |
| 7d9a4c61-c89e-3bcf-a236-2ff0cdb2184a | -10.4776 | -36.8855 | 2025-01-09 06:50:00 | GOES-16 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 115.0 |
| 8d3064e4-743c-3eff-a48f-005d8abd771c | -10.4781 | -36.8588 | 2025-01-09 06:50:00 | GOES-16 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 129.1 |
| f4f55c1a-b6d8-334e-aea6-671a80adae43 | -4.7686 | -39.59135 | 2025-01-09 12:38:00 | TERRA_M-T | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 280ce263-762b-3405-b01a-424b52737aad | -18.41919 | -51.95579 | 2025-01-09 12:40:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| acb41c78-4813-324a-a2fd-df30374658e5 | -19.76768 | -47.40041 | 2025-01-09 12:40:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 82ba72a3-3b9f-3f2d-8572-950d9f3e55bc | -20.00789 | -47.55342 | 2025-01-09 12:40:00 | TERRA_M-T | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fde8a73a-8649-3e1e-a67d-9b72768cc3e2 | -18.58618 | -52.13081 | 2025-01-09 12:40:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a49696c6-8c27-3292-8a90-022f8a6e4de7 | -19.16266 | -50.53823 | 2025-01-09 12:40:00 | TERRA_M-T | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| e1b3a7a0-5e46-355d-b333-ed085a47e5d4 | -20.81074 | -47.66094 | 2025-01-09 12:42:00 | TERRA_M-T | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7ed185cd-af8f-3794-a89c-7a094db84408 | -20.88296 | -49.86787 | 2025-01-09 12:42:00 | TERRA_M-T | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| a96ffca6-8ef8-357c-ab98-b7e5258c5c39 | -22.36604 | -47.55115 | 2025-01-09 12:42:00 | TERRA_M-T | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 1e626dfe-e3c7-33c3-b207-d3df34c60e14 | -20.78007 | -47.60201 | 2025-01-09 12:42:00 | TERRA_M-T | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ec64b051-f9dc-31e4-a2c5-f9b4df24b38b | -23.04564 | -46.67389 | 2025-01-09 12:42:00 | TERRA_M-T | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| cd0318b2-39d1-3c5d-ad2f-9a1d30fe1418 | -21.01022 | -47.61425 | 2025-01-09 12:42:00 | TERRA_M-T | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d93b6ef4-ccb6-3383-b2dd-f5fd79ff8d41 | -20.42048 | -50.07742 | 2025-01-09 12:42:00 | TERRA_M-T | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 179fe5a1-ae06-354e-8586-b01ff4cc47b9 | -21.0209 | -49.74766 | 2025-01-09 12:42:00 | TERRA_M-T | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 92a72e33-2338-364b-a8f7-f5bdae69b38f | -30.97868 | -53.4341 | 2025-01-09 12:44:00 | TERRA_M-T | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 6.2 |
| 3deb29d0-35b3-33ff-90a5-f150d2f048b4 | -31.75545 | -53.24025 | 2025-01-09 12:44:00 | TERRA_M-T | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 5.4 |
| 0f40185a-c06f-3ae9-90a3-2c1ef2e55967 | -29.02273 | -52.51439 | 2025-01-09 12:44:00 | TERRA_M-T | BARROS CASSAL | RIO GRANDE DO SUL | Brasil | 4302006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1b0edf33-d6fa-33d6-b7d5-44d053275b97 | -30.27759 | -53.61275 | 2025-01-09 12:44:00 | TERRA_M-T | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 7.4 |
| b5a9cfa9-96ab-3664-be73-d0adc48ad1e4 | -29.46199 | -54.04228 | 2025-01-09 12:44:00 | TERRA_M-T | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Pampa | 10.4 |
| e7958ddd-7e67-3865-80a5-de4dd9d9946e | -21.1985 | -53.1747 | 2025-01-09 13:30:00 | GOES-16 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 4d885ad5-f5fd-3fa0-909a-64154f3f25fb | -21.1985 | -53.1747 | 2025-01-09 13:40:00 | GOES-16 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 70e6988e-8b9d-308d-91bd-63cc3c0e59eb | -21.1985 | -53.1747 | 2025-01-09 13:50:00 | GOES-16 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 8c65893f-f9dd-3e9e-8e2d-c3ab4d631792 | -21.219 | -53.1708 | 2025-01-09 14:00:00 | GOES-16 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 58581931-5069-3209-866d-a3b2c815ba25 | -21.1985 | -53.1747 | 2025-01-09 14:00:00 | GOES-16 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e0ac5a38-5924-395c-9ce0-f71ded43b602 | -21.1985 | -53.1747 | 2025-01-09 14:10:00 | GOES-16 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 8712aed5-55f7-3788-82c5-330f3611139f | -21.219 | -53.1708 | 2025-01-09 14:10:00 | GOES-16 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7ef1273a-5cca-3d27-a2fc-66a68112e663 | -21.1985 | -53.1747 | 2025-01-09 14:30:00 | GOES-16 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 91.4 |


