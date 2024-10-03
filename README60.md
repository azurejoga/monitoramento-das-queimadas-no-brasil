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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a081d326-9fc2-396b-a47a-117af34a4775 | -20.85121 | -42.23421 | 2024-10-03 03:15:00 | NPP-375D | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2a7ef83b-7173-3432-8d18-3c03dcbe5713 | -20.84967 | -42.23274 | 2024-10-03 03:15:00 | NPP-375D | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5c20a51b-eefd-37dd-97ab-aa64c141c147 | -20.22022 | -42.47948 | 2024-10-03 03:15:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe2c9c97-1361-3359-8896-6ef5e2ae3678 | -20.21906 | -42.48452 | 2024-10-03 03:15:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26a7478c-b396-3aa6-9905-620af8775523 | -20.21543 | -42.47232 | 2024-10-03 03:15:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d1efbac6-4a58-30ee-903c-629179172509 | -20.21429 | -42.47731 | 2024-10-03 03:15:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a44eaa67-0b84-34fc-b14e-94aced07112e | -20.20936 | -42.47078 | 2024-10-03 03:15:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3917df67-2752-3129-a47d-3c90e0273fad | -20.20817 | -42.47597 | 2024-10-03 03:15:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 954b7693-62a1-3a1b-8f13-2c32cccad1c0 | -20.20575 | -42.48655 | 2024-10-03 03:15:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 127ee393-f0bd-3b6c-b4e7-157b048d3210 | -19.89043 | -42.1124 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed9fed66-fc4a-3c92-824e-e1176fad73f0 | -19.88865 | -42.11484 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 00d91f62-a611-3d4e-b062-4136845a6d8d | -19.88458 | -42.11035 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 585d0961-43d2-3edb-9a21-f587ecc1296b | -19.88411 | -42.10688 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c5759a79-252d-3ff0-b40a-697e47a57583 | -19.88311 | -42.11667 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 933e10cd-022f-3c30-9d77-a993b76af649 | -19.88263 | -42.11348 | 2024-10-03 03:15:00 | NPP-375D | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cf324e76-26d8-3b5a-b54b-32d30d7c0d92 | -19.69091 | -42.03635 | 2024-10-03 03:15:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e6e78f95-f6da-3712-a189-ba7944aa55a4 | -19.68911 | -42.0388 | 2024-10-03 03:15:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 104df4df-96d5-3ad7-a8d8-a4fb699ee50a | -19.6848 | -42.0354 | 2024-10-03 03:15:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 0cf4d25f-5e72-3e93-b8e9-b3419c06aa58 | -19.68409 | -42.03302 | 2024-10-03 03:15:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 69c85d7d-4a28-35b7-a45a-712e66169c3c | -19.68304 | -42.0377 | 2024-10-03 03:15:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 61b6f5fa-8f06-32dc-9cf3-4f1fb49b303f | -22.15749 | -42.54375 | 2024-10-03 03:15:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8e355459-a5c9-3cae-bd20-16aae16a23b9 | -22.1564 | -42.5485 | 2024-10-03 03:15:00 | NPP-375D | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4471233b-32a0-3cbd-ad9e-416b9320e6c4 | -22.15023 | -42.54829 | 2024-10-03 03:15:00 | NPP-375D | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 04ea1307-1e00-362a-858d-21175362048f | -22.14901 | -42.55357 | 2024-10-03 03:15:00 | NPP-375D | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00f21ef9-8b21-35d6-9267-62730f78cf6d | -21.79498 | -42.49139 | 2024-10-03 03:15:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c3388eb0-d35d-3a88-a4f4-d6294d361c84 | -21.79399 | -42.49563 | 2024-10-03 03:15:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a7dcd609-0ad2-3176-b567-7efe66a4adfa | -21.79013 | -42.48543 | 2024-10-03 03:15:00 | NPP-375D | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2dc498df-d9d0-35a0-9aef-94f4033f76b4 | -22.05866 | -42.96884 | 2024-10-03 03:15:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ae73be10-44d0-30b3-8121-fd0d61e1bf75 | -22.05726 | -42.97482 | 2024-10-03 03:15:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| eb7301b1-ef34-37ab-90c8-418cec5be953 | -21.63154 | -42.80664 | 2024-10-03 03:15:00 | NPP-375D | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 34af4727-e4c8-3ebd-95c9-c62bbfd02254 | -21.63023 | -42.81223 | 2024-10-03 03:15:00 | NPP-375D | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0c59be2d-6254-3a34-a98f-6299a7e490d8 | -3.4042 | -42.2621 | 2024-10-03 03:15:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 0e0002b8-31bf-31d0-a916-b6ec0241d360 | -3.3855 | -42.263 | 2024-10-03 03:15:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 7f7bec97-9fa3-3028-a23e-c1d9741bb64c | -4.1134 | -48.4886 | 2024-10-03 03:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 29321580-309a-337b-9711-558175210a35 | -4.095 | -48.4679 | 2024-10-03 03:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| dbab6edf-539a-3df8-983d-9fb85d00ac1a | -4.0949 | -48.4894 | 2024-10-03 03:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 320e6494-9dfb-3f20-8e77-6c0119813c72 | -4.5375 | -43.304 | 2024-10-03 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 313985c6-f32e-3db0-bdfc-29038ea7b328 | -4.5373 | -43.3273 | 2024-10-03 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| a78b32f9-5a48-3917-9177-67c7488f902c | -4.9264 | -43.79 | 2024-10-03 03:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7f3856f4-fdc6-3502-9265-2b0c61442a14 | -7.0752 | -48.028 | 2024-10-03 03:15:46 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 81bec951-8d7a-3cf7-8d18-fbbd51d4251d | -8.8506 | -45.5086 | 2024-10-03 03:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5b96923a-5824-3bd4-a48d-c71db9d6316c | -8.8926 | -62.3348 | 2024-10-03 03:15:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.5 |
| c7e5982b-5377-332e-83b1-cc71c2c60254 | -9.1566 | -61.6758 | 2024-10-03 03:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ea7f5682-b9b2-314c-a4bb-29a064ad0ce7 | -9.0515 | -67.871 | 2024-10-03 03:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| faf01c8c-3291-373d-9b80-4952e0867411 | -9.0149 | -67.7423 | 2024-10-03 03:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 6a5af5dd-0dd4-3730-8f80-849042bd920c | -8.9976 | -67.4094 | 2024-10-03 03:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 368f6227-441a-35b2-b4f2-06226b565738 | -8.9791 | -67.4099 | 2024-10-03 03:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| eab23ad0-add5-3e3e-983f-2e4af01682ad | -9.4866 | -62.3849 | 2024-10-03 03:16:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 17621911-21bf-3d4f-aa80-017f98503934 | -10.8942 | -63.8971 | 2024-10-03 03:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d3bfe528-fae2-3627-8278-1c39567f8008 | -11.6931 | -64.9974 | 2024-10-03 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 79dc0709-5339-371b-b4b9-7ffccd64d0ab | -11.6743 | -64.9983 | 2024-10-03 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ab4e1844-501d-347f-98a8-dcaca2dd920f | -11.6932 | -64.9785 | 2024-10-03 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 107.8 |
| da35c96b-f95c-355b-8869-1b57d6f40e7c | -12.4038 | -63.0009 | 2024-10-03 03:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 2c5a9159-f8c1-3e02-bf20-9d2e19f8f763 | -12.404 | -62.9817 | 2024-10-03 03:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1274d3eb-cf07-3120-a75f-739147487405 | -12.6484 | -63.1214 | 2024-10-03 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| cfe60d2b-94d7-3141-8891-75a0f3644b13 | -12.6486 | -63.1022 | 2024-10-03 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 81863999-9aee-312c-b77d-091b23d93544 | -12.8808 | -62.4731 | 2024-10-03 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5bf2185a-bf7c-3835-bfd0-74633b4552ca | -12.881 | -62.4538 | 2024-10-03 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 836a77ca-43eb-3499-8031-6fd2b8bf7cf7 | -12.8996 | -62.4913 | 2024-10-03 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 124.5 |
| e219d2d8-0129-308c-9e2c-1bd3ff8c5b06 | -12.8998 | -62.472 | 2024-10-03 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 831951c5-d979-3976-ad7f-9833cbd35a7b | -12.8999 | -62.4527 | 2024-10-03 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2d8c07d7-ed8e-3159-b00a-603fe7d20796 | -13.0402 | -51.1432 | 2024-10-03 03:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 3bbd192b-a76e-3c47-a603-801a7d73a0b6 | -13.0594 | -51.1409 | 2024-10-03 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e338dcbd-0487-3da6-9d84-bc20c57c72e7 | -13.0783 | -51.1599 | 2024-10-03 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| f9b7eae5-c03b-3c23-a538-44f460573b70 | -13.0971 | -51.1789 | 2024-10-03 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 602cf810-ffe7-3ae3-ad46-baa76679ef8a | -13.0975 | -51.1575 | 2024-10-03 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 3cd107ed-ff29-3598-8f74-dea2a8302455 | -13.1351 | -51.1955 | 2024-10-03 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7ec6f666-523c-3b35-85c8-20aab6b96dcf | -16.539 | -58.2225 | 2024-10-03 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 87adb042-db6f-3260-abe8-7a8f0f1dc11f | -16.5582 | -58.2407 | 2024-10-03 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| b5f85f5b-8330-37d2-b43c-c2ef69653223 | -16.5585 | -58.2204 | 2024-10-03 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.2 |
| 1ec75d3c-3ce9-348b-9c96-bb2fe2c60e63 | -16.5588 | -58.2001 | 2024-10-03 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.3 |
| c3843d7c-a21e-328e-ba65-66c73ec6a23d | -16.578 | -58.2183 | 2024-10-03 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 31e594b6-1a9b-3ec1-99c4-ad68ab490ef7 | -16.5783 | -58.198 | 2024-10-03 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 216cc45d-529d-343b-a051-a3cddd5aa9bc | -16.779 | -57.8306 | 2024-10-03 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 877e1ffb-05f2-3e7b-bf37-68b7a0730153 | -16.8983 | -57.6949 | 2024-10-03 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| d64b4b15-1e41-3880-9f0e-41a77f6b8241 | -16.9176 | -57.7131 | 2024-10-03 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| f09291b4-762d-39bb-b7ae-8b44dd96ba5a | -16.9179 | -57.6926 | 2024-10-03 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 28d34c1e-628f-3c41-8a71-125084d745f5 | -19.0344 | -43.1944 | 2024-10-03 03:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 79f8afeb-9e36-32b8-b1cb-20ad0609dcc9 | -3.3854 | -42.2866 | 2024-10-03 03:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d3a6b312-d8d9-35b8-b3c1-051e6980d10b | -3.3855 | -42.263 | 2024-10-03 03:25:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3db3359f-dac1-3885-8030-11648c4e9ff2 | -3.4039 | -42.3094 | 2024-10-03 03:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 26761fab-1713-3ca0-92cb-daf6c559288d | -3.404 | -42.2858 | 2024-10-03 03:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 318.8 |
| 6b4afd0e-118f-30f0-bd0a-45744337b8df | -3.4042 | -42.2621 | 2024-10-03 03:25:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 273.1 |
| e4469055-3791-37a5-a289-6301938321a5 | -3.4227 | -42.2849 | 2024-10-03 03:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 40d5fd09-0fbf-3230-ab02-c028e3ae847f | -3.4229 | -42.2612 | 2024-10-03 03:25:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| fbbfb309-7293-3fa3-b2e1-f8f408c693ae | -4.0949 | -48.4894 | 2024-10-03 03:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d43c7d98-e8e5-3f0d-8a3e-a84e4de2e471 | -4.095 | -48.4679 | 2024-10-03 03:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 419159f0-6ac4-38fd-9a40-efcbbf33188a | -4.1134 | -48.4886 | 2024-10-03 03:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a22427d3-ccd7-3700-b983-5346657f9b10 | -4.4844 | -42.8866 | 2024-10-03 03:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| d1ed2b12-8364-3e82-95d2-5ee595fdea7c | -4.4845 | -42.8631 | 2024-10-03 03:25:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| dfa0ef02-ffb8-36ac-a843-be6dd959456b | -4.5375 | -43.304 | 2024-10-03 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b278cc21-f8a0-305c-aa4a-2fb1458ea1e5 | -4.9264 | -43.79 | 2024-10-03 03:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9d160c25-15f4-3009-9ca1-1b56aa6e2893 | -4.9265 | -43.7669 | 2024-10-03 03:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| f82ba441-b257-33bc-b14d-24faa5127faf | -8.8506 | -45.5086 | 2024-10-03 03:25:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e3b85044-a4d9-389f-b100-915e1745bfea | -8.8926 | -62.3348 | 2024-10-03 03:25:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 75d1e4e5-49a2-3f9f-b337-0f567548697e | -8.9791 | -67.4099 | 2024-10-03 03:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 05945359-ee28-3a98-82d6-877cadda057a | -8.9976 | -67.4094 | 2024-10-03 03:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| f288d298-2feb-3837-9726-478c11ad6c03 | -9.0149 | -67.7423 | 2024-10-03 03:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 084fa891-8c09-3dd6-9f32-4745d7bbb3d1 | -9.0515 | -67.871 | 2024-10-03 03:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 36fe5e85-c4b4-3744-b8cc-b23667e658db | -9.1752 | -61.6749 | 2024-10-03 03:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |


[Clique aqui para ver as próximas entradas](README61.md)
