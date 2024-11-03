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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ea927e8-15f1-39e3-9ba5-5ea9895da85e | -1.25029 | -54.51313 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7b9b943-c695-38a4-89f0-95120762eacf | -1.24991 | -54.76023 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 091fe1b8-f0a5-3231-9e40-ad1f0d0d1ac7 | -1.24935 | -54.76377 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f7411a09-11ef-34a4-bafe-37e78bd0e501 | -1.24923 | -54.44996 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af4e12c2-df12-3676-ba25-14ac1bd8e928 | -1.24865 | -54.4536 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac6d65b3-b9cc-33db-937a-71b7251cfc9e | -1.24764 | -54.75263 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26a9b30c-b56a-3802-abe2-d4897fb8ba37 | -1.24514 | -54.49776 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b073dd4-3cbf-30bd-b821-f2ab635c4310 | -1.24482 | -54.74857 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55c3f31e-4048-3c43-a0fb-b70537d4acf4 | -1.24427 | -54.7521 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaa345e8-b3be-32b0-857f-0f071c437ff9 | -1.23663 | -54.50758 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c194c693-aa5b-3062-91c5-ddb7de2710a9 | -1.23323 | -54.50704 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ccce90-ba9d-3823-ba97-71bd7078ecaf | -2.2235 | -53.8131 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bdc19c6-4d8a-3aeb-83ce-d72c7e130d77 | -2.19533 | -53.66851 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fad4b2f-07d7-339f-a734-a874148c864d | -2.18811 | -53.69162 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4021eb61-623c-3cc8-8839-e8c96fe82415 | -2.1858 | -53.68321 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68a628d3-6c82-39f0-95d9-a700b2ee6fda | -2.18519 | -53.68715 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ae214a3-d77d-35f9-8d6e-3358d3523baf | -2.15209 | -53.71409 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca5f815c-8107-3595-9313-58e6b66dca66 | -2.14314 | -53.88834 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 687c1e6e-4f0f-364d-a404-d2982353cc48 | -2.11929 | -53.74229 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fd46d3cc-4415-303d-a5d8-a3d83c025352 | -2.11576 | -53.74174 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 23ea5893-b8d1-33b9-9bf1-d22c2a423fe4 | -2.10245 | -53.71158 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b818f197-712e-3f84-b79b-a1313888211b | -2.10077 | -53.69925 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4abe00c6-6f2f-3a56-bad3-7f5d5441741b | -2.10016 | -53.70318 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a19dc7de-badf-3f75-bb7d-fb8913e0a194 | -2.09954 | -53.70711 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f06894a9-4bcb-3260-9bd9-e001ba4c3426 | -2.09786 | -53.69478 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8af6fbb-1aa8-355b-b4f4-29d381f822a7 | -2.09724 | -53.69871 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6677891-f3a0-3c1a-a94c-cf612b123c11 | -2.09663 | -53.70264 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a337772-4f8c-3724-b619-294f2057d535 | -2.02 | -53.54608 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3814f62-63d6-3b3c-8268-b53430dad880 | -2.01276 | -53.63835 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b874da8-3a13-325b-90b8-b48970ecd8cc | -2.00984 | -53.63386 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 78826657-342a-39e4-8fb0-73ae5b5291f3 | -2.00947 | -53.68219 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 365bc347-4911-3223-b46a-e815986734d7 | -2.00922 | -53.6378 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 41253616-5f23-3a52-aea4-044f657ee38e | -2.00886 | -53.68612 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 800708b6-bb4e-3c07-8be1-f8ff58204472 | -2.00879 | -53.61751 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3d54fd4-f1cd-3377-970a-d39f9ba286bf | -2.0086 | -53.64175 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c95292f8-6877-3f83-8ba5-cbd8adc1f6bb | -2.00816 | -53.62146 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bfa2de1-678e-373e-a414-76f2ea8c68e0 | -2.00798 | -53.64569 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ae72f64-2cdc-3a80-93d4-e028b31a8d34 | -2.0063 | -53.63332 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838a90e6-f91e-3af7-868d-3a5781b35a9b | -2.00568 | -53.63726 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 45d07dfb-4273-35a7-8848-864cee4dc677 | -2.00507 | -53.6412 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b0b0ae2a-48c1-3c3b-87eb-eb033eba3129 | -2.00463 | -53.62092 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eb0691a-5404-373d-beb3-f66a62bf5c08 | -2.00445 | -53.64514 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f2a531c1-39b1-31e5-a50c-c42d264c8cf5 | -2.00383 | -53.64908 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c1314d2-5299-3d91-979f-dae278d45db8 | -2.00321 | -53.65302 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad5be666-c0b3-3946-a7c1-18fe6a7483c9 | -2.00277 | -53.63277 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 008be20a-5188-30d2-bcde-5a11ce890c7e | -2.00215 | -53.63672 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 199b8d5b-7621-34c1-b719-3ef8b23acce1 | -2.00153 | -53.64066 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 29e3d901-f864-381a-8010-af3ede532f3d | -2.00091 | -53.6446 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 28063d06-35ff-3248-92b4-055795ae6c52 | -1.99968 | -53.65248 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2c2ef65-5222-30e7-98e5-c1f43849ea8d | -1.99923 | -53.63223 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00dd0cf6-0a33-38e5-9575-3463ef2e3948 | -1.99906 | -53.65641 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fb829e0-2e86-3635-b8fc-fd5abd06d01e | -1.99844 | -53.66036 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2f9f7be-535b-315b-91f5-aef831759a76 | -1.99738 | -53.64406 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44d31ea4-466b-3ab9-a501-ae238f6952db | -2.08884 | -54.46324 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cfb8fc22-ac14-3d2f-ba08-a2dace7d9c09 | -1.99044 | -54.60248 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afb37536-1c98-3ee5-b3c8-53f0d1df3410 | -1.99028 | -54.60191 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 078112f6-8902-31c1-898b-be7d8860ee17 | -1.86149 | -54.89307 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d102cca3-4c24-3277-b52b-5a3e4e51be64 | -1.73905 | -54.60202 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc97cd89-c002-3414-9d2e-96d435c994e0 | -1.69656 | -54.65114 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1da19a4-fa66-3bfd-a791-d358fd678ff0 | -1.39547 | -54.16709 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ddf88263-4d87-3721-98d3-9a62dd0614bf | -1.36536 | -54.24644 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5cf91d9-d9f0-36fb-b11b-c71f8c0f5724 | -1.3414 | -54.75547 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cfb9749-00c0-3622-9eb4-a62166348359 | -1.33391 | -54.24545 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a87ca0b3-5225-3936-b8a7-9771cea210b1 | -1.32703 | -54.24454 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5a21929-4672-3e3f-ac09-c5621dbb0d58 | -1.31164 | -54.20802 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e97e3a7e-7364-3ff5-96fa-e9ba012a7c08 | -3.57973 | -54.70638 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaca747f-5fd8-30df-8455-447812838f4e | -3.56345 | -54.02792 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3bda191f-fea9-3f2b-9036-0e8b62d94271 | -3.47325 | -55.23122 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4020d068-6dcf-385b-a8c2-89507ccbc3b5 | -3.45677 | -53.92365 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8ff5d80-fd30-39d3-a9a9-00f6908f464b | -3.43133 | -54.69517 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53e083f6-ec70-323f-89d6-93b186268f08 | -3.41596 | -54.5205 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f1e9539-b5f0-33eb-a981-41f3027f7423 | -3.41251 | -54.51997 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba7bd515-ff70-38eb-b6e2-6483fe4f71f5 | -3.39373 | -54.60218 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4713fc42-d1ad-317a-8ccc-fc123cf7aae6 | -3.39315 | -54.60592 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ac6f35c-9b31-3db9-b7c8-3b4177a12b1d | -3.39044 | -54.55573 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7961a00c-bf39-339d-98da-ebf601c63ee4 | -3.39029 | -54.60163 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03a47a42-1e75-342b-80d7-b859664597b3 | -3.38971 | -54.60537 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ba2e0fc-bc0e-3e71-9a47-290b69388ce0 | -3.37951 | -54.55787 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78f3efb6-7e96-3dc9-9e9b-7245c8be879c | -3.16895 | -53.76037 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 264ee38a-d236-3e82-82f3-c30bcde4f830 | -3.16539 | -53.75982 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2108d150-6978-3505-9fa3-5b72fba722bb | -3.16501 | -54.13354 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3118a2d-6bd2-35f2-8e6d-859d24b96a3f | -3.16442 | -54.13738 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e25baac-9d81-32a6-be34-938b53fa0b18 | -3.1637 | -53.74725 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1054de6f-fe8c-322a-b687-99aa6cee80db | -3.16308 | -53.75126 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7d22915-8517-33fa-8772-7adcdd79cb03 | -3.16014 | -53.7467 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99a6cf31-caa1-3b15-8f80-0b51e9d15336 | -3.15952 | -53.75071 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f13c3b96-667d-3096-b498-004558b80951 | -3.1589 | -53.75472 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 737ec52f-1826-3b63-b3b1-8723e5fb08a1 | -2.95795 | -54.21292 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8405e714-97ca-3ad6-85fc-7d0248109be4 | -2.95737 | -54.21666 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bc7be39-2ef0-34d0-8086-3e146098ef0e | -2.95679 | -54.2204 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 969065c6-c7c4-3328-ba9c-ef2f2688b89e | -2.95446 | -54.21239 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c1b8ce3-e970-34c9-ad37-82ced8d82054 | -2.95388 | -54.21615 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30dd2201-dd28-390c-9a54-31948ab40ce9 | -2.9533 | -54.2199 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a62d34ce-4c38-3fbf-a839-784578e2cd4d | -2.95272 | -54.22369 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7560ea8-e168-30d6-99e4-661ed007501d | -2.95213 | -54.22749 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30ac2952-198c-38d4-8f36-746e3138c45f | -2.95098 | -54.21187 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25f0aca0-6699-34dc-8d2f-823d41632765 | -2.9504 | -54.21564 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bcb78fed-5f7e-3c4f-8e93-451e2fb5c7b4 | -2.9503 | -54.26232 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ccc11a9-8522-3c64-be8c-47a272bf6143 | -2.94981 | -54.21941 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 312c96cf-b0a3-3792-8a95-981b6782619a | -2.94923 | -54.2232 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README69.md)
