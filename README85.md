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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e3d4f9-e5e8-3c87-ab2b-346c2ae62c3c | -9.0543 | -53.24765 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6656da08-f5d6-3cec-8e02-38146f814183 | -9.05087 | -52.99913 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d789bd0e-46ae-31c6-bb1b-6ba6792b4acf | -9.04787 | -52.99429 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34fdd8be-f183-3135-96d0-14dcd6941c08 | -9.04721 | -52.99868 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd5067e0-b7d5-3f4a-bb0f-d485595014a7 | -9.04423 | -52.99372 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd28452e-ce97-3a68-b0fc-d0a084d8fe44 | -9.04358 | -52.99812 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23ba6ba0-72b9-37fd-900a-ced4d76c0f25 | -9.04124 | -52.98876 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbdb124b-7f31-3eca-83c2-8687c06fe72b | -9.0406 | -52.9931 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35cafd3f-f5a9-3eee-a761-f84cd457b538 | -9.03995 | -52.99746 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5763283f-c306-3f56-89b7-3cf1ad1f31d4 | -9.0372 | -52.94032 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34559499-2b6e-3ef8-b2cd-24d025da0808 | -9.03656 | -52.94473 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d71b8669-8c40-3afe-b6ff-4eb11baf406a | -9.03594 | -52.9489 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b32b5524-daf4-3a8d-93ff-6d5867d3c3f6 | -9.03292 | -52.94408 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64cc894f-0c87-3cbf-abf6-8d64cf59d149 | -9.0323 | -52.94831 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 292830a7-faff-366b-9d88-46d53e5a5f75 | -8.9918 | -52.7989 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 594e4768-cc61-316f-81a5-37bec9261bee | -8.85491 | -53.01598 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38c97ffb-22eb-3297-b4e3-8b7d11a027c4 | -8.85428 | -53.02021 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7dec7781-f6ca-3553-9039-ee7519c2e4c0 | -8.85193 | -53.01113 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f6b17c0-45f4-39bb-81aa-d2b156ccabed | -8.65444 | -53.06151 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4ce5b60-317d-319d-b034-f816736130c2 | -8.65148 | -53.05667 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b6be41a-c9be-3f1c-8ad3-b8e0f4da7dd4 | -8.65084 | -53.06091 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaf2d4ac-d668-3ce0-bd68-d363687c7d77 | -10.87539 | -52.36706 | 2024-10-13 05:04:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a55991c5-0e69-3f84-b356-83a442a79844 | -10.87083 | -52.37139 | 2024-10-13 05:04:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbd208ef-d1ea-37b7-a483-140c30346cef | -10.22124 | -52.68972 | 2024-10-13 05:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a81b65d-5784-32c9-bbe4-e90a62da486f | -10.21352 | -52.68629 | 2024-10-13 05:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eea57b48-20c9-313f-b6f9-09f00a500de0 | -10.20976 | -52.68572 | 2024-10-13 05:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d96159fd-a310-3ca9-a13e-a6422553f98d | -10.2091 | -52.69024 | 2024-10-13 05:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a408bd6c-4ae1-36bd-80a3-cbe9c90493a5 | -9.73149 | -52.82446 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6740de2-82bf-3086-852e-ebee335aff72 | -9.73127 | -52.85159 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00e1766e-673d-3023-9415-74caf14746ef | -9.73084 | -52.82886 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e84d13ac-4122-33d4-a296-58447ef2b205 | -9.73019 | -52.83328 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b200521b-8e48-3ae7-955a-f7b0a5d40535 | -9.72822 | -52.84661 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb989178-efec-3827-9923-82a8445282c2 | -9.72778 | -52.82394 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c38b9f7-ad69-30fa-a84b-5f58fbe56ecf | -9.72757 | -52.851 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e005a467-475c-3990-836d-7a42c54b5771 | -9.72536 | -52.81465 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c751eb00-eddf-3f0f-8ae4-dcc631f2047d | -9.72518 | -52.8416 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 005a5dc5-10c6-39a4-89f4-e937a4515cfa | -9.72471 | -52.81905 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab90d719-7460-3c53-a833-178895774a89 | -9.72453 | -52.84599 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a5c852a-b7d2-3be5-94ef-0d1a03ed8f64 | -9.72389 | -52.85035 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0aba7ae-6a6e-3f5c-8883-03fef89bc92c | -9.72099 | -52.81857 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee5de9b1-5c72-3562-9a5f-baf94a7b508b | -9.71955 | -52.85413 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a67dd083-4bce-3c83-a811-9aa0d42646f5 | -9.71727 | -52.81817 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 794d12e5-5145-37fa-aeb6-2d472af83544 | -9.71583 | -52.85373 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 970bbe15-5f41-3a53-8b1d-16bd4f67304d | -9.71354 | -52.81778 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4821059d-d20e-34cb-a2bd-cf851e898204 | -9.71289 | -52.82223 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcd73af6-d83c-3469-8f43-60cddd124c31 | -9.71275 | -52.84898 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ea5838f8-c277-387a-a298-9e2ff50a2c0f | -9.71212 | -52.85325 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b76cde92-d95b-3c49-94f1-292e89260892 | -9.7097 | -52.84398 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c202122-0c2e-3a3d-ae33-bda00786c6ce | -9.7092 | -52.82156 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa6b0d36-1412-3038-affd-80b1ef12e54f | -9.70907 | -52.84827 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 89578710-9de2-3f8f-a96d-70fa1d03e704 | -9.70856 | -52.82593 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c10d635-e934-3576-8e78-effe5c3c6da6 | -9.70845 | -52.85255 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9ecafa69-3d40-320e-a4f7-7e0619ac91d7 | -9.70604 | -52.84318 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4b45e04-d0c2-3a0f-8491-9408ef098764 | -9.70541 | -52.84748 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2232fe1-604e-375f-88b6-810cecd135b7 | -9.70488 | -52.82522 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0474903c-9e35-38e7-8f7a-2b38609e36af | -9.70424 | -52.82957 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bf03f24-a0ab-3138-826c-a358ae970cd2 | -9.70362 | -52.83385 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a391315f-8e3e-30c2-995b-53812b82f8c0 | -9.69993 | -52.83318 | 2024-10-13 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 308ad614-fdd7-3fbc-9016-b7a289bc7ec6 | -9.57668 | -52.1694 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fa1262b-c0df-362b-8870-b881c74bd00b | -9.57284 | -52.16882 | 2024-10-13 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bbf5f69-09a3-3288-9524-0ef598553356 | -9.57065 | -53.25883 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 469100d1-1bb9-3b4d-98c0-b4afd72e69fb | -9.56941 | -53.26712 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8696932c-110c-3da5-923f-b0110e19b708 | -9.56703 | -53.25827 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb8e90d0-f026-33b5-bff5-195c7b134c2a | -9.56642 | -53.26241 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44a130ec-7ac9-3be7-b573-fbf994fadc00 | -9.43044 | -53.2007 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f20eaaf-01c7-3e62-82e5-44c9f5a2d795 | -9.01141 | -54.50963 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6059abc5-94b0-32a9-912b-295b7ba4afa8 | -9.01085 | -54.51334 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84032ce6-5644-3a31-ac8f-7183bb1e89f8 | -9.008 | -54.5091 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb27ece1-5cd1-362e-bca4-e1eba07d6a37 | -9.00743 | -54.5128 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9db87c69-73d9-3992-8867-1724b4c4ff6b | -8.90034 | -54.57639 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce1fa0c9-4a70-3875-a106-24956df7106b | -8.63671 | -53.65289 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80671ea9-90de-3296-b4aa-852b09cbb495 | -8.63379 | -53.64841 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 797cbaf2-34e4-3e7b-84f8-bdab494c6561 | -8.63319 | -53.65236 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a38bce9-504e-3ed6-a26a-9f78475cd671 | -11.28262 | -54.58771 | 2024-10-13 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f28a5cab-78ab-3684-aa6f-b04754d0ff6d | -11.27915 | -54.58718 | 2024-10-13 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cc54372-547e-39d8-a7d3-9d834805268f | -6.22888 | -55.51576 | 2024-10-13 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c13a53b-dab3-38fe-8c8e-3a861ee3f03e | -6.16934 | -55.51011 | 2024-10-13 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bf4b88a-622c-3677-99d9-53f0f948750b | -7.86965 | -54.69847 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 32321ecf-8e19-3e95-b492-9cd2cfb98d57 | -7.86908 | -54.70208 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 65a85fda-c745-3e65-a434-0535ff2659f7 | -7.8689 | -54.70901 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdaaaff2-79a7-381f-8580-31b9bee5f1e8 | -7.86796 | -54.7093 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b933b400-67ff-3ae8-a90e-6b03d52e73cb | -7.8674 | -54.69074 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11c04f58-9e11-30b7-a175-9ca8aa36fbe6 | -7.86627 | -54.69796 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 022c0dc1-200b-3575-9bba-094f3745d42b | -7.86346 | -54.69382 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e219c523-ebde-389f-abd1-a118195d47c3 | -7.8629 | -54.69744 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db73a725-f1f4-3f11-8bb5-65cacc3dbc77 | -7.86176 | -54.70472 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 99f10a81-4f12-3ddd-80ac-875050ec00e4 | -7.86009 | -54.69329 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9d2c9254-da9b-35aa-b6f3-4184bfc15c6f | -7.85953 | -54.6969 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e77a7ec2-a3e0-3d56-ab8b-4bc077105141 | -7.85896 | -54.70053 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c94f2a1-19fd-3e82-8a0e-c5160933b248 | -7.8584 | -54.70415 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e8f26347-210d-3af7-affa-f9e7c342049c | -7.85828 | -54.89046 | 2024-10-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eee8edfe-34f6-35b8-91bd-8a95c1074e10 | -11.8999 | -56.21304 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5301fee2-088c-3232-b655-fd67bde9221e | -11.89935 | -56.2166 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 861da2b9-396a-3f35-bfef-fbff9409798f | -11.89656 | -56.21251 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa621003-5f38-322e-b292-28a327224c12 | -11.89601 | -56.21607 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d79ee5f8-a1dc-3f8e-b1e8-f4c5bfcfbe9b | -11.89546 | -56.21962 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5b78b1-5359-3a7b-8ee0-6148eb321408 | -11.89323 | -56.21198 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37508a39-4154-3fef-b9e4-7c74fa6f5bd9 | -11.89268 | -56.21553 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f654dde-84bf-30a9-8f3c-9b59cf248f95 | -11.89213 | -56.21909 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3c9bc95-28ae-3c1a-a330-a5c22d336a3d | -11.89158 | -56.22265 | 2024-10-13 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README86.md)
