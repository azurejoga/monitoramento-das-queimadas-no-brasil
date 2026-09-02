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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11ca9cd8-bef3-3fb7-8908-15f63f8000ca | -8.9135 | -62.367901 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 862d3ee7-8d97-3372-9f4e-01693a49b783 | -7.3501 | -60.581402 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ea131ec-689a-35e3-9e4f-90d8af63f554 | -7.7703 | -61.195702 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e20f807-0208-3d01-b30f-456555e868aa | -6.8788 | -59.3992 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2c40e43-90e7-3ff3-84fc-c5590e3fcf80 | -7.4609 | -61.376099 | 2026-09-02 01:33:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a24a09a2-d1ee-3580-abcb-9f14fbebdf0d | -9.0032 | -65.420799 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d220530a-cf1d-38c8-b84e-cfc655372703 | -4.2434 | -62.232601 | 2026-09-02 01:33:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1424deab-86ae-3588-a208-91b4779df9a0 | -7.2034 | -60.660702 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 529c40c3-5383-308e-b05c-7c9d572c8362 | -11.3424 | -50.603298 | 2026-09-02 01:33:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f99b75e0-45bf-3cd7-8bd5-dda38eedf5c2 | -8.4279 | -54.693401 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdfe21a1-aaf6-36ef-bb82-e937c180403f | -5.5547 | -60.225498 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a12e6fb0-174c-33a7-a28f-e8a7c1e0f985 | -3.0952 | -61.186298 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51937c47-4509-32b4-8f61-5d3f3eabbb1b | -11.3395 | -50.631001 | 2026-09-02 01:33:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdb1e6f4-534f-33f9-9e34-0816db2ab3dc | -7.3599 | -60.579201 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a303d80f-1acf-3124-a43b-b81392cb8e8c | -14.4968 | -59.844898 | 2026-09-02 01:33:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 320b2faa-a87a-398b-94dd-60a08902da0b | -7.7301 | -60.9758 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d113dad-2367-3a75-8c76-92081b0c3b0b | -8.403 | -62.708099 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5a5e4010-5ce7-3a62-9fb4-83ab5f742053 | -11.6621 | -50.1833 | 2026-09-02 01:33:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23d5afd7-d01a-347c-849b-82661ce935f3 | -8.6898 | -62.930199 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ce15bd52-40ad-3bf4-9e7d-751b25a11b22 | -7.2148 | -60.6656 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0734e3-4e72-3ffb-973a-755fc18c0e31 | -3.2379 | -61.223801 | 2026-09-02 01:33:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96fc7dc9-ccd6-3d64-a35d-45479a35b8a7 | -7.205 | -60.6679 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6142f75-359e-3272-b2ee-520c71c2fc1f | -8.9331 | -62.363499 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e6bd6628-884a-3323-a585-efad2be82889 | -9.9285 | -60.485901 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb47613-0a60-31ff-9945-a3db18d4018a | -1.4911 | -54.236698 | 2026-09-02 01:33:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1dc740-c30a-386c-b373-a5de4dfadda7 | -7.2182 | -60.68 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39c15bff-cc52-30a9-9f0d-ca59d9ff722a | -9.0206 | -65.453598 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2157a3e0-f7ef-31a3-8184-423291d97bfa | -9.0876 | -65.384399 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 418f83e1-f0b0-391a-8835-1eb534521bef | -9.4445 | -64.573196 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 988aba81-86ed-322c-98c6-fbaee0718bd6 | -9.447 | -67.445801 | 2026-09-02 01:33:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b8016ca-238b-3c42-b7bf-32adc3886c96 | -6.8262 | -58.867699 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99ce9c18-d107-37b4-81e5-91e083ab8c37 | -3.6244 | -60.5756 | 2026-09-02 01:33:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c21af490-2b0c-31c8-9a83-dd82b4313765 | -14.004 | -58.691299 | 2026-09-02 01:33:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3bda6de-2f95-30b8-94e2-24bce94070fe | -7.682 | -67.126297 | 2026-09-02 01:33:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b63b0dc-c748-324e-8fbf-9d21a58ac0e5 | -3.7534 | -59.311199 | 2026-09-02 01:33:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4adefe32-eef9-3511-91b4-611da10e9acf | -11.3557 | -50.653198 | 2026-09-02 01:33:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efb88610-47ec-3649-95d7-85449bcdc170 | -9.0908 | -65.493599 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94c612c3-0991-3685-bf09-1e003b8351ec | -6.8282 | -58.876202 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba5c6e96-e3f4-335f-ba10-b9f5c7d8baae | -8.4376 | -54.691002 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d48b95-6996-330f-bc69-656ca7f9eac0 | -6.8885 | -59.3969 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec729857-53bc-386a-9808-2fb2e79ffb52 | -8.7721 | -62.8382 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1607d601-e27e-3cf1-a7fb-0180195f197f | -7.7621 | -61.204899 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 454115d6-4181-3a0b-be57-bf996541137a | -6.8164 | -58.8699 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edd96b88-265f-392b-bf59-a9d3c66aac67 | -7.3552 | -60.6031 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e168b17-4661-3c51-945f-cfe3c8affbb1 | -8.4741 | -54.7132 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afcc9493-5979-3a8d-92d5-8e35c4cc1681 | -8.2688 | -62.752701 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc26500-2dbd-3b42-b341-d912a192df11 | -9.872 | -64.9814 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c52d8e5-f3bc-3b70-b0f7-83033dced726 | -6.8075 | -59.0952 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e637438-40a0-31b1-a6c6-44f6069b0f65 | -6.6998 | -58.769501 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 291fafc5-4ac7-3305-b565-bfbc3986cfb5 | -8.5623 | -63.1884 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff54478f-a63f-31d0-939a-0e6fd5e7a450 | -7.2084 | -60.682301 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e6657a9-7a06-3ddf-8d7d-afb6ea91dbd1 | -3.6387 | -60.5481 | 2026-09-02 01:33:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21b6e223-ee87-3959-9b2f-0a2a36a513cd | -9.8701 | -64.9729 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e19dff9c-82a6-3f0b-ac85-585e20af5b13 | -7.4493 | -61.415298 | 2026-09-02 01:33:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1abbb323-1001-3370-8c14-9af8bd0a66be | -11.7876 | -50.534 | 2026-09-02 01:33:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5664cd19-9ecf-33c3-a720-a85cfabf16f0 | -3.2362 | -61.216499 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 027b26e1-17b6-3e9b-90ab-9b99fcf9b758 | -8.451 | -54.7033 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffadbe9f-df90-3e4f-8472-f3e06c2ee64d | -11.8938 | -63.183399 | 2026-09-02 01:33:00 | METOP-C | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7c0b7d9-589a-3144-a3d2-03d4d31ee341 | -5.977 | -53.5658 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1f10ac-9880-3b81-81e3-fb301635dc48 | -9.0092 | -65.401299 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a318e6cb-679c-35c3-a526-a7eb00470830 | -10.5005 | -59.612099 | 2026-09-02 01:33:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9a38f43-4c24-34be-81e6-f0bac949c3d6 | -6.7749 | -59.440201 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98400af2-a1fb-3f47-bb78-cc71ece9f596 | -7.4379 | -61.410599 | 2026-09-02 01:33:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8d4311c-8d41-3797-a71e-92314dab0841 | -7.7605 | -61.197899 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e023f05d-1f18-386e-b454-a85e36019561 | -9.4397 | -67.459602 | 2026-09-02 01:33:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa7feb52-9cca-3944-8bff-7b5df01fce6e | -9.0051 | -65.429497 | 2026-09-02 01:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5bdfdc-8102-302d-88a6-65364b189c77 | -8.1181 | -54.940601 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e23157d-d803-3340-a9d5-5a973df2b851 | -7.1969 | -60.677299 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb3969b-34d2-3ee3-bb12-0724f155a297 | -8.4777 | -54.727901 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd280d95-635e-3776-82d5-b77b552d840f | -6.6051 | -58.587002 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f30921c-0f08-354a-a87c-d7e27f6d4a80 | -13.5555 | -59.744099 | 2026-09-02 01:33:00 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72e04c93-5754-33ad-a4d2-0aff5d8dee10 | -8.4583 | -54.7327 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9527b840-488d-384c-a945-8106b2eb066b | -4.1299 | -51.032902 | 2026-09-02 01:33:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e80adf4a-0348-35e4-9aa7-32f59e109412 | -6.5576 | -58.560501 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b270074-f3b8-3087-8266-462d5dc52e2b | -8.9022 | -62.363201 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d4c70321-c919-3ab9-ba7e-22f856e36e11 | -5.3417 | -60.1525 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb9ea0ce-0b5f-3454-add1-2858036a765d | -9.8683 | -64.964401 | 2026-09-02 01:33:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b4e3546e-a7ff-3c0a-94fe-5197b4dc2ffa | -8.912 | -62.361 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a8b3480b-947a-3c5b-870d-9a9cc005481f | -5.5903 | -60.201099 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84ccf36f-57dc-3bc1-8851-8fc64aaddf05 | -7.4558 | -59.925098 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a25ec50a-2f74-3081-b361-44233dabf83b | -7.5354 | -60.713402 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d454ffd-cbdb-37a1-91db-8be2a78a937e | -7.3568 | -60.610298 | 2026-09-02 01:33:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e444fdf7-5c56-30a0-a522-fb175897eddb | -8.4353 | -54.7229 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94ce7720-5a9f-3b2f-ba17-ac359f2b9014 | -8.1119 | -54.957298 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e09a7c95-7a9d-3ad6-a9e1-598c078f0490 | -11.3586 | -50.625702 | 2026-09-02 01:33:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0076aad-bc14-3271-b7e7-6d6339c4fd69 | -10.4898 | -64.328796 | 2026-09-02 01:33:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab8088da-44f5-31a2-a0f9-2e76e43df372 | -8.1019 | -58.282299 | 2026-09-02 01:33:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae05ed91-7ec0-3410-b65f-f75d692309e1 | -6.6977 | -58.760799 | 2026-09-02 01:33:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59e8ee96-23ba-3e0a-8a84-c662cea439f1 | -3.2145 | -61.167198 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b727785-f10f-3e30-8d1b-31fcbb5d18f7 | -3.2128 | -61.159801 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6dc05f65-7a31-3971-8084-fbc50eca156f | -8.1278 | -54.938202 | 2026-09-02 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b06c747-69e7-33d0-8112-3f1b1855d33b | -9.1845 | -59.459 | 2026-09-02 01:33:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 853cb5a3-9afd-3aaa-9a99-7ac840ead4fe | -8.7852 | -62.484001 | 2026-09-02 01:33:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd15459-b313-360b-a89d-0e9cee198378 | -4.1882 | -63.164398 | 2026-09-02 01:33:00 | METOP-C | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3771139-2558-325d-b0c7-aab2e5891041 | -7.4737 | -63.751999 | 2026-09-02 01:33:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7787a4e6-2722-3249-af67-58b1e1b34695 | -5.5769 | -60.188099 | 2026-09-02 01:33:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0219fa1-1e2f-36ca-8886-219d22c2842a | -4.1478 | -60.697498 | 2026-09-02 01:33:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9323dafa-6dcd-3de1-bbc9-baf56f55143a | -3.1152 | -61.228298 | 2026-09-02 01:33:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47eadfc6-a713-3f27-9fe3-3bb5d7d42427 | -11.3328 | -50.605999 | 2026-09-02 01:33:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2afd7f97-870f-352b-add8-bff31537117d | -8.5737 | -63.193298 | 2026-09-02 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
