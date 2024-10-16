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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6111783-600f-39a2-9baf-06b1ebc4b549 | -6.89968 | -45.96108 | 2024-10-16 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9faf9b09-c4f6-343e-91c5-12e5a088739a | -6.83924 | -46.05751 | 2024-10-16 04:06:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 194c8d65-d1d4-3f59-9941-2eaad188b393 | -6.79447 | -46.44192 | 2024-10-16 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb42d044-7c1a-3278-bacd-510e60884a7f | -3.57352 | -46.12385 | 2024-10-16 04:06:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d415113-c46f-3068-a42c-95ed4f612169 | -3.47115 | -47.46846 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0e345ef-1a8d-3cd8-85ee-d1c03a6e5e71 | -3.47052 | -47.47123 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe7def78-cc53-3479-938e-b9a8f6419430 | -3.46657 | -47.46788 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4523fb49-e3dc-3064-af9f-a3da2ca52c0a | -3.46594 | -47.47064 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13c4060f-8715-3d53-85a4-311daedeb97e | -3.29789 | -46.55464 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 210a37fc-fc76-324c-9829-476077d61962 | -3.29616 | -46.55437 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a61e4d31-e667-3cf2-ad7e-12b7993fc533 | -3.2936 | -46.55399 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57fc9ea8-9391-300e-a323-6d0358718dc7 | -3.29187 | -46.55374 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ead6e7ab-eaab-3b96-af57-c549be44a12f | -3.28931 | -46.55336 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75613b31-0d83-3ceb-9f2a-a9974cff6b06 | -3.28867 | -46.55736 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e326d99-2d5b-3f8c-8fd1-2e7205b553fb | -3.28787 | -47.1241 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b39baddc-f114-337f-956f-60d1fa9a33e7 | -3.28715 | -47.1286 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 43675668-0e3a-34bc-9bf7-67583aa76225 | -3.28691 | -46.55709 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 394a796e-0765-36d2-804d-90d7b546cd57 | -3.28588 | -46.5199 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0631111d-c5c5-38f1-85f5-6ae60b6de85a | -3.28523 | -46.52393 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05a8f104-9f0b-36da-aba1-9ead2c3c48eb | -3.28343 | -47.12331 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c67920f2-6543-3094-8b1a-4064a3739f18 | -3.28271 | -47.1278 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8a5d30ff-ca06-3a57-b83b-1891fd195a00 | -3.2816 | -46.51925 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9271095b-67c4-3f48-953b-8e821299afb8 | -3.25444 | -46.88512 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a310246-45af-3868-942b-d7271a816180 | -3.24938 | -46.88847 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db3ce2c2-e76f-3549-ae11-8263dccee2ab | -3.2457 | -46.88353 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b556c43e-b57a-34be-afc7-065aba4d02c2 | -3.24558 | -46.88386 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 615add9f-01f5-39e1-9852-4256a367fcbb | -3.07747 | -45.94534 | 2024-10-16 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070b6068-788d-3ec8-8c2a-fec561243c70 | -3.07686 | -45.94902 | 2024-10-16 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af6796ca-1a50-3150-860f-18b9be3cc35c | -3.07212 | -45.95202 | 2024-10-16 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8b81f13-73f4-34e9-b11d-393bf9167080 | -3.06738 | -45.95507 | 2024-10-16 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 405c3089-e34f-3c41-bf71-598523536a1c | -3.06552 | -45.95566 | 2024-10-16 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 214cf064-e9ff-3488-8856-e34c6116c5b2 | -2.66002 | -47.07861 | 2024-10-16 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4fac8de-12ee-3782-bcd8-cca84c0d83e8 | -2.53692 | -47.22736 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 45ad0e92-8f5e-3a03-9ab0-f8472489a1aa | -2.53652 | -47.22497 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e61a74d3-2baf-30f8-a01a-b49f39c0f074 | -2.53616 | -47.23192 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ce3f32cd-34e9-37a8-9c6b-8580e8ede398 | -2.5358 | -47.2295 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1fac70ec-d3a0-31b9-81f0-288c39c30f63 | -2.53314 | -47.22208 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0951f46-6520-39f7-b965-faaad26b619c | -2.53238 | -47.22661 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c9a19b1f-2a1a-31ac-93fb-1e7e36bd0062 | -2.53198 | -47.22421 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70f593e0-31f0-3f57-87c2-166bbfd7c28c | -2.53162 | -47.23117 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 779b0b30-37c1-338c-85df-b32e1beaf6ad | -2.53126 | -47.22876 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 20ba1899-3afb-33e2-b615-5994d0d4a78e | -2.51699 | -47.34708 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbe9899b-b52f-39a2-b229-063c0fe5bdf1 | -2.34443 | -47.25788 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27128176-67db-3b6b-80d9-09a8a5a4e426 | -2.34095 | -46.48395 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faf77c5d-ab3d-37e0-b422-23f019fe7a44 | -2.33987 | -47.25715 | 2024-10-16 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf1d8e17-e1d9-39d0-b847-4bb74dfb6463 | -2.33984 | -46.48426 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dae5e9db-7533-36da-8680-af84a265e028 | -2.33663 | -46.48323 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53494555-27b6-391d-b4ed-f25fb199a654 | -2.33552 | -46.48355 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938ffcdc-7070-3b50-85d9-5004086154d9 | -2.33488 | -46.48764 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 833ee527-bdec-3037-9de0-69080b76ba24 | -2.33298 | -46.47846 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7cfb52b-e8f4-3915-8ade-703115169790 | -2.33231 | -46.48254 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b37684d4-b8bf-3d5a-953d-ef3b1fae751d | -2.33184 | -46.47877 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05b2af3d-fcb4-32fe-9e40-daf1b63d0ff0 | -2.33164 | -46.4866 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 64155a1c-ed06-375f-b198-f2227e296073 | -2.33119 | -46.48285 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a6d1483-5393-394c-861c-0b5be34fb43a | -2.33096 | -46.49071 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1326071f-3755-3b2c-b8b9-05d60d56ca99 | -2.33055 | -46.48692 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a359447-5f64-317a-bf8f-59824fbb14c8 | -2.3299 | -46.49105 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c563b2ef-fce8-3f2f-98e1-4aada3e23309 | -2.32731 | -46.48589 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5511c15c-500f-3756-a949-9e227668dc9c | -2.32706 | -46.45292 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb7116b-a0e0-3376-a5bc-61a24c9107f8 | -2.32663 | -46.48999 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c441094e-c553-3684-9cb2-b8283d5a4ffc | -2.32622 | -46.48622 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9ca306c-96e8-33ae-8180-c242694f3978 | -2.32557 | -46.49033 | 2024-10-16 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d1c05e1a-b142-3dce-ad81-ddacfdd04217 | -2.29917 | -46.60072 | 2024-10-16 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bb656a1-fe51-314d-aef8-41edf0814841 | -2.2873 | -45.88599 | 2024-10-16 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df055978-8c60-3d13-8b9e-829449988a52 | -2.2867 | -45.88973 | 2024-10-16 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93bd554c-28b3-33ad-ac5c-7732c1adac4f | -2.28314 | -45.88532 | 2024-10-16 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a4b419a-0dfe-3c97-83c5-b50df3f09cae | -2.20831 | -46.29824 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4343dfa3-4267-3d21-8847-cc913864244c | -4.06804 | -47.1291 | 2024-10-16 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1eb0867c-0847-39dd-a7c8-c494b5d940e9 | -4.06726 | -47.13166 | 2024-10-16 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61b2cc13-06f9-30d3-ab01-3d2c08efaeb4 | -3.95964 | -46.43517 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 22b192ed-1571-35f8-bb88-7342e7fd8d87 | -3.95933 | -46.43591 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d358028a-6d1d-33c2-959c-764eb7e3db71 | -3.95899 | -46.43903 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 01bb37bc-b2a9-39fd-aa59-3ae2d05ab11b | -3.9587 | -46.43982 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ab407ee2-e11f-34a2-a6be-8d5635d718ab | -3.95575 | -46.4313 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a110dd11-09ba-3820-870b-38e7bb54d5df | -3.95547 | -46.4343 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| d19b4a64-ab79-3092-9eda-0d29d9a1041e | -3.95516 | -46.43501 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ce511bd8-7df9-3513-88f5-16ca85c8fd2e | -3.95484 | -46.43805 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 96372f94-ecec-3017-859c-8318308c127b | -3.95454 | -46.43882 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 60e74758-b044-3851-bd6b-f2aba80ff7b6 | -3.95097 | -46.43422 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1bbe6dd2-d4a8-34cb-9582-4309f080c6d5 | -3.95036 | -46.43799 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1537426b-36ff-34df-9ef1-8ac014896f1f | -3.93361 | -46.40825 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b86868ae-4476-3f71-ae20-78127ae0cbc6 | -3.933 | -46.41196 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 03907165-50c6-3b5c-bce7-fa1bbe8f5199 | -3.91486 | -46.44389 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c843cdf1-b5c1-3052-ab8a-176f6d702c25 | -3.91423 | -46.44775 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abe29ea2-4ac0-3fec-8c92-1bde0067b710 | -3.86764 | -46.46796 | 2024-10-16 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2d3cec8-8730-36b6-82a5-8ccfcd994856 | -3.83397 | -46.91167 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fba3e523-faed-30e0-bc7a-592fc8ca3176 | -3.82961 | -46.91107 | 2024-10-16 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8647697f-c277-3ebe-9245-1b754c3db256 | -4.96551 | -46.77715 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a33909c1-e815-3d6f-8aae-5705d0242774 | -4.74187 | -46.61332 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34a88548-cba2-33a6-80f7-9cdb06d2a2a1 | -4.73969 | -46.65271 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f81ab2e5-4973-32dc-8cea-656d9f01dd90 | -4.73832 | -46.60873 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1b21a08-e730-3eb7-b30e-04521ee8effd | -4.73767 | -46.61264 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06854cff-9598-3ac8-8191-2a625ec04f4a | -4.7341 | -46.60811 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5172ef64-6967-30a7-be20-fdd5c80b0556 | -4.73217 | -46.54204 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1cbf8f1f-823c-3f9b-97ad-7a5f40b8c672 | -4.73157 | -46.54567 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b8d7c9c-835c-3ede-858a-d925a511f86a | -4.73095 | -46.54938 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 04f05791-fdd7-3229-8ae0-fd5fc4033d20 | -4.72799 | -46.54132 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4c8b9aa9-3a97-32d4-a338-ae6045948307 | -4.72738 | -46.54501 | 2024-10-16 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6711470d-f8fb-3e99-ab4f-244fdf46cc6a | -4.47586 | -47.73755 | 2024-10-16 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff988bbf-afde-3bf4-86ad-d6fbe725e275 | -4.47131 | -47.73675 | 2024-10-16 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README34.md)
