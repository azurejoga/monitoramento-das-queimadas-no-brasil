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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebad46b6-308c-37bf-9cf1-1aae7b10263b | -17.66224 | -53.04482 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5732abd6-cbeb-3def-9d68-32ab163c3ba6 | -17.66198 | -53.09319 | 2024-10-07 05:18:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33b538fd-0988-356d-821a-6bf2dc293301 | -17.66157 | -53.05161 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efdd5b5b-02ae-3c84-b724-42723474c7c4 | -17.66151 | -53.05094 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad0c1439-b667-3d6e-8e12-ba5316e582c6 | -17.65724 | -53.04488 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51281c12-afa6-3aba-ac97-49a3c43eef1a | -17.65723 | -53.04424 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2e76ce9-36da-3476-bd23-094bf23f3f41 | -17.65657 | -53.05096 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91ff242a-fa76-3964-b508-120d8f630a70 | -17.65651 | -53.05031 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dc50dc10-7182-3cf5-bb93-846e83f5d7b6 | -17.65156 | -53.05037 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5c26380-5460-3d93-8851-864921cf1146 | -17.65089 | -53.05643 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5398d5c-1b23-34e8-901d-997a8bfa7672 | -17.65078 | -53.0558 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fca9cd4-2845-33db-ad09-3babbedc50f4 | -17.64577 | -53.05522 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f703955-9ae6-3f80-b467-7ed4b4daeb7a | -17.63696 | -53.09076 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ae36f2f-d20c-3172-aa7e-751f8f26cb75 | -17.63659 | -53.0901 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb1fd767-a835-3907-8ab6-b05df2e648b0 | -17.63198 | -53.09004 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a77ba288-8864-3747-9ef3-4ddcdfc14586 | -17.63161 | -53.08939 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6749c04-3d67-3079-b889-0a46c49ddde4 | -17.63008 | -53.10726 | 2024-10-07 05:18:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f5465737-289e-350c-a390-82778e2f6175 | -17.62959 | -53.10657 | 2024-10-07 05:18:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b087c2b-3004-3480-9f6d-08c9a09fb9df | -17.62943 | -53.11312 | 2024-10-07 05:18:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5de2e475-80d6-3404-88ae-d97983685cca | -17.6289 | -53.11243 | 2024-10-07 05:18:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13705ec5-5966-335c-a3b7-8eaee0b7dfa0 | -17.59821 | -52.51103 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12c4b0e4-d4c6-334f-9883-4815fda147b0 | -17.59785 | -52.51407 | 2024-10-07 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e7df5ba-f95b-39e1-9347-676764b5ef1c | -17.78405 | -53.76023 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13763e10-c019-3c4c-96c8-9167b664052a | -17.7834 | -53.76556 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b567c624-6636-323f-a676-7b271ee28416 | -17.77929 | -53.75944 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb9e573a-081b-393d-9811-866a6fb823d4 | -17.77867 | -53.76461 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4845d609-9d7f-3857-b01f-ce07702fe89e | -17.77451 | -53.75883 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 689837fd-b5a0-3d44-8bbf-21955e8c0f06 | -14.8163 | -53.89297 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 469274bd-3dac-30ab-8e03-61165121040f | -14.81117 | -53.89692 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a78574b1-5eaf-363d-bb5c-2e300bbcb4f9 | -14.7935 | -53.92739 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b84852a6-0042-3e6f-ad82-ef7f38425a08 | -14.78445 | -53.92599 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4248bbc0-bf9f-3859-84fc-0e6413e439ba | -16.4927 | -53.95544 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a172f8e-82ff-3203-9eaf-db761b2fe6f4 | -16.48685 | -53.96505 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94ff17da-af05-34ba-8653-d911c91ade6b | -16.48493 | -53.9531 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39a574aa-75b5-3a69-9004-46915fe03f6b | -16.48428 | -53.95819 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b80c340-3110-313f-a821-c28cd14b87e3 | -16.48339 | -53.95459 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6174b076-2c64-3fd8-aadd-2c1ddc5989ed | -16.48279 | -53.95964 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| baf0b813-5026-3ea3-a502-18d284342314 | -16.4822 | -53.96458 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2052258b-73c4-3ed8-9ec0-f958bd625d2b | -16.46775 | -53.96735 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aea2bf14-8e68-37bd-821b-2b44c9781b9f | -16.4651 | -53.96093 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e38a7be-c29a-3ef0-9542-c74e1f70f106 | -16.46365 | -53.96235 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cff5ccf3-99f7-302a-8277-7f30e57475af | -16.46255 | -53.97163 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 238bfabb-9aa5-3005-9e8d-8cbbe943d42d | -16.45988 | -53.96502 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9893583a-f797-3ac6-b913-338945d45a8b | -16.45531 | -53.96402 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c39c1d2d-2847-3a01-9587-b5ae46fefe75 | -16.49209 | -53.96057 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d97c6c3-4b2f-3e21-9882-bf27e370f12c | -16.48805 | -53.95497 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 628cef49-300f-3dce-aed3-b9e1d0f00be1 | -16.48744 | -53.9601 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79c2c913-9bdc-3447-82f4-301060c2bce8 | -16.48365 | -53.96319 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 139a9b4a-9a46-316e-8679-80ebf889c49d | -16.47994 | -53.94399 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f1d29ed-3826-3d94-b278-a8fe08d203f8 | -16.47963 | -53.95775 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e0c24bd-8b17-3ef4-8a24-5cf387886029 | -16.46917 | -53.96598 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e1d9861-dd7c-33c2-9b05-8763e642343d | -16.46857 | -53.97079 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 968622a9-e504-3e95-950b-f6cafdfc86e5 | -16.4645 | -53.96569 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58fe0243-c9ba-3b81-b846-c1dae1fee98d | -16.46392 | -53.97033 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f3f7b35-717e-3303-9fef-7def5d8c02b1 | -16.46048 | -53.96024 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 082a87ae-d587-3d11-a7eb-e20a314aac3d | -16.46012 | -53.92544 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8abcb921-a070-3a37-bfd7-3bf63e4fcf46 | -16.45931 | -53.96963 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9ea1a67-ad84-31d8-b411-538acaeba66e | -16.45488 | -53.92972 | 2024-10-07 05:18:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b319d19-1103-3be2-b633-82923ca38eb2 | -17.77966 | -53.79624 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9152399-651c-3974-b4ab-522082b8353c | -17.77906 | -53.80119 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eba7b61e-3cce-3770-97e0-42ea34b1aedd | -17.77846 | -53.80615 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 10e5232c-9ba8-325e-bebe-21d72088525e | -17.77786 | -53.81107 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c12cb485-00f9-3816-8b59-e534b5a96e60 | -17.77724 | -53.81618 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 852c202e-9ed5-372e-8ba5-ca7554d451a0 | -17.77677 | -53.7802 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 272787c2-45c8-369f-ae94-e2cce3445304 | -17.77613 | -53.78545 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08904958-a55f-3997-8a05-fd8eace7b395 | -17.77552 | -53.79053 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ebfc547e-3453-3fcf-b46c-4d2279896719 | -17.7749 | -53.79556 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fdd8e9ec-a40f-3d67-8fbf-ab398ab5d8c1 | -17.77431 | -53.80048 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59ed06e6-25f1-3772-886a-11940b3adb57 | -17.77204 | -53.77931 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf91b51f-7e28-30f1-be44-69e9e7698b83 | -17.77141 | -53.78448 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55a8474d-335b-3122-af57-41e5f38e5afb | -17.77078 | -53.7897 | 2024-10-07 05:18:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f031d88a-68b9-3df6-ac5a-5b2d04ae070c | -17.3259 | -55.03887 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ddff0639-e57a-32cd-abd5-c49279f1d61e | -17.32154 | -55.03826 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a2381f03-1d84-31e3-84b5-e49884486e00 | -17.17896 | -53.92231 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb531ee4-3591-386e-87aa-0cb4c5082ac0 | -17.17835 | -53.92736 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e2ebb63-4465-3691-8020-280222b92a44 | -17.16782 | -53.9358 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fd79e80-8007-3539-9757-3490237fcfe2 | -17.16722 | -53.94078 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c0eb75a-386a-34a3-b143-e826fbf6c88f | -17.16314 | -53.93512 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cb41394-6d4b-3539-88be-d46bb10acd11 | -17.02777 | -55.07324 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b0f3ba2d-690b-388f-beef-c664beaeef36 | -17.02397 | -55.0684 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 226a4f04-d83f-3b46-91a5-b65168a47363 | -17.02343 | -55.07265 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9bd90316-80bd-3c92-9118-8eded27c1eee | -17.0229 | -55.0769 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 10ae58d0-9e99-30c9-872f-67a21e85d48a | -17.0207 | -55.0593 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9412be67-dfb8-359a-9ddc-7bf307fb6699 | -17.02017 | -55.06355 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7efd63f5-8bbe-33f4-b06c-5ddda7c191f0 | -17.01643 | -55.09328 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 22f777ce-dbd4-38cc-b08e-f313f2c4d8a1 | -17.01256 | -55.05384 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8469f833-cdb4-3f5b-9973-efb1c9c95c4c | -17.01211 | -55.09269 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 07d1dd2c-b7a6-363e-95fc-70ab89d8c188 | -17.00653 | -55.03133 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8abffa05-829f-3a1e-8ef8-3e54514ef368 | -17.00219 | -55.03073 | 2024-10-07 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ce39b82-613e-3491-94bd-b4bb5c8e5b9d | -16.90351 | -54.54024 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03b6ce5e-1d52-3f2d-a116-9d853820c8aa | -16.90233 | -54.5497 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b70c5f8e-6a35-3a70-86da-b446c8150c9d | -16.90113 | -54.55923 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ce1c8f4-58ac-3bd5-883e-a1edcc02fdfe | -16.89904 | -54.53959 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f3999ad-c0a0-3c4f-8528-ff7d3bf9570d | -16.88673 | -54.52866 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fcd50e0-6a0f-32f7-9e81-208c05d9642f | -16.8828 | -54.52361 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08b83568-856c-3142-bec5-920c3c21eb40 | -16.88225 | -54.52803 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bea18470-55fe-3147-90cd-d0f07c0afa7c | -16.8031 | -54.11068 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71593578-f8e1-35e5-a828-aecec7dadaf6 | -16.79849 | -54.11005 | 2024-10-07 05:18:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40b96425-db03-3600-9f83-fc0c775aa579 | -17.32537 | -55.04319 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a2e81356-a275-3597-9d43-6ddae00101ec | -17.32207 | -55.03394 | 2024-10-07 05:18:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |


[Clique aqui para ver as próximas entradas](README114.md)
