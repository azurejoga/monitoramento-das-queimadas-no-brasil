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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b410f98-ea16-3859-b929-ae0f8a25885a | -16.68433 | -57.19316 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 10c1cfe7-7cd8-39ec-ac2d-0a6fd8c8f718 | -16.68198 | -57.18454 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 469fae78-9509-38a0-9c63-9fafbab10112 | -16.6814 | -57.18858 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0105ae1c-14a0-3a45-8c47-ef30674e90dd | -16.68082 | -57.19261 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| e7d4f89d-24d7-3ea5-9faf-3af108142d7a | -16.67029 | -57.19096 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1f2e0be4-7c65-3320-84c7-8c7392891016 | -16.66504 | -57.20251 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 98b60d33-1516-3ae9-9045-eb24cad7f1aa | -16.66212 | -57.19793 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2a131d7a-aa4f-310d-9f5d-30208c5f85d9 | -16.66154 | -57.20196 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5450cae0-1872-3a40-b995-9b7b591be64f | -16.65861 | -57.19738 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ddc5e06e-e4fa-35df-a2e6-922977c8ffe7 | -16.65803 | -57.20141 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 47a36a05-fd89-32da-acf8-c40788a57d5b | -16.65745 | -57.20543 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 344cf760-af21-3294-8a85-1de3e49ed593 | -16.65394 | -57.20489 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a217a812-0be8-3a63-8eae-9edf8c8f62d7 | -16.65337 | -57.20891 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 85c18ef4-7426-305a-bc36-033d79b7be20 | -16.64986 | -57.20836 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 91a0f068-9142-37e0-8736-6aef20916277 | -16.64612 | -57.20919 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a07f563c-c4c1-36fd-9f4f-8738412d2276 | -16.64578 | -57.21183 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f33ca610-d1a9-3fad-85fd-844291b1c1f0 | -16.6417 | -57.21531 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 103f3677-6f7c-3c72-9579-1fbb6cd5db84 | -16.64143 | -57.21668 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 02256fc6-930f-38d2-bbdf-71cbfe3b841e | -16.82786 | -57.47123 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5ae9e486-a8af-39cc-a4d9-feb86b2e2176 | -16.82615 | -57.4831 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cb88dc92-a21d-357c-81ae-c40513d5bff0 | -16.82438 | -57.47068 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 74d5cbc0-1bad-34e2-95b0-01d47fec2bfb | -16.82318 | -57.47176 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2f5bac81-7775-3c0a-9c84-0a024877b4be | -16.82034 | -57.47408 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 53e70530-8a79-3821-95d9-37faaf255e80 | -16.81977 | -57.47803 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 760b3cbb-fb62-349b-9548-6087d3eb02cc | -16.8197 | -57.47121 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 375b1823-3228-3c39-9c8e-4679588d430c | -16.8192 | -57.48199 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8bd9db77-b5e9-37f7-94be-13dbbd0bc3a0 | -16.81911 | -57.47516 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1579e883-88f8-3f3e-bc9f-67e83135142b | -16.81853 | -57.47911 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 677e9d10-a596-30a4-94ed-d27f5dd9ce47 | -16.81821 | -57.56246 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8c8c21f7-1f97-3bdc-b709-2cd59eb2d0d2 | -16.81564 | -57.47461 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bd16bbca-6703-33a3-a129-62f0bf438eca | -16.81506 | -57.47856 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7d4f8fdb-7db0-3794-99af-637071ea5cf4 | -16.81475 | -57.56191 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3d5a67b7-647c-3671-9919-2d1cae7055dc | -16.81128 | -57.56136 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9505915a-2818-398f-8c69-2f835572c405 | -16.80972 | -57.56234 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 385bd0ca-9d1e-3b2b-90de-fb023a6900f1 | -16.80782 | -57.56081 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| afb92d2a-bf51-3bc3-8279-fd54aca8f84b | -16.80725 | -57.56474 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3d5ef2cf-d2cd-3a53-b4a7-2bedefb98a38 | -16.80626 | -57.56179 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| aeb77188-bd44-32c6-b20f-a6ae12f440e4 | -16.80174 | -57.47242 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b2da8dd1-756f-3017-b868-cc6c7a09041f | -16.80163 | -57.56909 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 00b652c4-0487-3efd-86f0-97656e05a3e2 | -16.80116 | -57.47637 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8a6b92f5-bd7d-349c-953b-ad0adc47fe9a | -16.79817 | -57.56854 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5bab8a7e-e718-3323-8743-894210ae0b9a | -16.78782 | -57.49446 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6e2c25d5-3f3f-3ef7-a0b1-f99f277b32c7 | -16.78725 | -57.49841 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5fe72a44-4fb9-3689-a0a6-445c544aa9c8 | -16.78551 | -57.48603 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3e58e2cb-00a4-32a2-b99e-b744bee06184 | -16.78493 | -57.48997 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cd05f1ef-236a-31bd-9398-73686dd996f9 | -16.75602 | -57.54179 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8f565ccb-ecbe-3cc2-9854-234ca57af7b3 | -16.75425 | -57.48109 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 3eb2547a-f3de-3dee-b583-7549d63f5dbc | -16.75368 | -57.48504 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| c012e76e-e4a0-37e9-9eb3-52144d83fc10 | -16.75078 | -57.48055 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 78218e1c-0fe1-33f9-8a07-8f8e09ffcada | -16.75021 | -57.4845 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 63f3047f-3035-3db3-822c-403be95403aa | -16.74963 | -57.48844 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 53af17cb-bbf0-3ad2-9b8f-1df4f530f6f1 | -16.74731 | -57.48 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 4b01283b-f153-398e-be1e-c683f68b8c76 | -16.74673 | -57.48394 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| a10f3aa8-6b63-3775-bf04-60b6f0550d46 | -16.74616 | -57.48789 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| dd98dc53-6909-3f9a-9464-cbbefd0b356c | -16.74383 | -57.47945 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2337327c-fce7-3042-85de-fbac1970c136 | -16.74326 | -57.4834 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b09b0b2-3113-3bd0-ba1e-7fc0bac6dce4 | -16.74036 | -57.4789 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 033e9783-209c-3655-8ac4-6cadebaa5f66 | -16.73399 | -57.47386 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 76cc3798-f8fc-3455-a40a-388a16d07612 | -16.73341 | -57.4778 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bb125edf-6458-398e-bb2c-f256bf64189e | -16.73051 | -57.4733 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 48a965db-dc78-3b32-9ef6-3239ef40c01f | -16.72994 | -57.47725 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8a385fbb-1224-3c90-ba17-2b47d384a018 | -16.72941 | -57.5054 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 53fb8262-84ff-3e74-a842-b623e0a1cca2 | -16.72937 | -57.4812 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b0c75d1b-675a-3458-95de-6fd178c60a54 | -16.72822 | -57.48909 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8d01393a-2907-3808-91fd-f8e3691ef2a3 | -16.72765 | -57.49303 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| baf81be9-0780-3c4b-a00c-742dbb282c3d | -16.72356 | -57.4722 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 795182f3-7ff5-3609-8450-7532f33c3463 | -16.72027 | -57.56824 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b4205c10-120c-3090-a26d-f70c087afb54 | -16.72009 | -57.47166 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3a8ec883-3cf4-3c43-a02c-338fea4c9548 | -16.7168 | -57.5677 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f4abe309-cf53-3db6-9217-34f3d8c32ab2 | -16.71662 | -57.47111 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3a39f341-afdb-3e8e-944f-fe7911993936 | -16.71605 | -57.47506 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ac1973d5-1ea5-302f-9352-b98372f40167 | -16.71444 | -57.47516 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 306391ca-a3b2-3d1f-aa7c-82602bd6ef4b | -16.71155 | -57.47067 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 790b8cf2-1656-3154-96f2-85e3f3182c1a | -16.69707 | -57.47243 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 2cf3107b-2d39-3004-8998-760e7f53fa0b | -16.6965 | -57.47636 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| df8dc475-a84d-32a6-93bb-45fbca76d07f | -16.6936 | -57.47188 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 43e51e67-aa6b-37d2-a6e9-63522a0ad96a | -16.69302 | -57.47581 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 04728cb4-ff40-3485-97f3-8247d31d4023 | -16.69244 | -57.47976 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6fd972e5-d0c0-330f-b7bb-5d4d2b14cb60 | -16.68955 | -57.47527 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 86b28d33-d6b3-3e80-b6f8-d745189ab75d | -16.68897 | -57.47921 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c560329b-4106-33e7-9d38-47a9df8fa1b4 | -16.91217 | -57.70847 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 5ac5cba4-073f-3de4-ab0f-7934efd88d81 | -16.90929 | -57.70403 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 96359ced-81f5-384c-a059-b9526e4160c8 | -16.90872 | -57.70792 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 6822e357-e3a1-3d31-8a40-dba6713ac935 | -16.90815 | -57.71182 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 166fe184-1186-3ea3-b25f-1195d7057c40 | -16.90584 | -57.70348 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| f4806ee5-808d-3b1a-a730-b4c3793eb46c | -16.90527 | -57.70737 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| c4ce49f4-5950-30d2-b68f-a57c9834790b | -16.9047 | -57.71127 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 7f72485f-bf55-3021-8bd5-beaebd88fdd4 | -16.90414 | -57.71516 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| af0dac61-fffe-3398-8c7a-4ea5bf217fa3 | -16.90295 | -57.69904 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 43a9daa6-6bce-3c41-b0d8-5e145d0d904f | -16.90239 | -57.70293 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| dafa9f4a-6bb0-3e2d-9380-7b71fd36192e | -16.90182 | -57.70683 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 1bc5d914-a498-3ca1-9fe8-493366bfb2bd | -16.90125 | -57.71072 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 6eaf1933-9b78-3467-bea9-0494035a46d7 | -16.9012 | -57.68679 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 357795e9-7593-3196-9224-c1a43c7acf6a | -16.90068 | -57.71461 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 3ca3bd38-82c3-3359-9918-609cfdd425d0 | -16.90007 | -57.69458 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 715b4dd8-d9b8-3276-a1e5-052c9602dbc7 | -16.89952 | -57.68346 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| ebe58e2d-358f-3b8c-beee-9fa7befbf200 | -16.8995 | -57.69848 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f20b3c20-3a47-3fe3-8111-4f6999ffcb71 | -16.89894 | -57.70238 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 21586edf-3a1e-3900-b2d2-a145afc77d0b | -16.89894 | -57.68736 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 4d84c7fd-5e7d-306b-a77d-79c25706d8bb | -16.89837 | -57.70627 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |


[Clique aqui para ver as próximas entradas](README151.md)
