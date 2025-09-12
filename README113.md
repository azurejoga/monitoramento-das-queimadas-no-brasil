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
| b213b5f2-a7ca-3a29-888f-ee27fb8a7460 | -14.55688 | -54.52158 | 2025-09-12 05:46:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cf64314-6446-30b7-85fc-4b0adc85150c | -14.50739 | -53.91746 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6a2ced2-164c-3a42-9fcc-da01c5ff190c | -10.36042 | -57.48843 | 2025-09-12 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 868da9bd-f1ec-360b-84fa-1f12b659149a | -11.64525 | -61.86679 | 2025-09-12 05:46:00 | NPP-375D | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ea00258-5336-36c9-8ed6-4812f643ccf7 | -9.42656 | -58.99038 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb99ba2d-03de-3db3-a6e6-b0c99e7ad336 | -9.22087 | -59.39604 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1b57791-70f9-337a-9174-bf43174d9f80 | -9.33401 | -65.72811 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d6577a3-b08b-3c1c-83aa-2b53ddbe9b10 | -11.19332 | -55.07675 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7467f7ba-ce27-3676-aff9-3e2612914a8e | -11.1856 | -55.08157 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6445105f-c055-38f3-b144-b437844397d0 | -9.50616 | -65.58302 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f275f02e-5fb6-3040-9013-eba75e85a542 | -9.21446 | -59.37685 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bf73868-6126-350a-8bd8-191b5c49d31b | -11.18717 | -55.07607 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e37ecb7-b225-3ca9-9202-219397a98cb4 | -14.50867 | -53.90481 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d9651da-ec22-33d9-8aff-b30a69ef966e | -14.33187 | -54.12259 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c0d28970-426a-3c34-8c7a-0e3cc9c0d8f0 | -11.18489 | -55.09438 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bde004b-0458-3e1f-ac12-5590a81a4cc4 | -9.89878 | -51.88304 | 2025-09-12 05:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dcee2124-71d6-3e54-95da-89e6182f98d3 | -9.29889 | -65.6041 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3870a2ad-e9d5-3c06-82e0-a4cf36d2501a | -9.83194 | -54.53524 | 2025-09-12 05:46:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36702966-95fd-32a1-82ce-d0a0b3e99249 | -9.15245 | -65.39722 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf0e347b-cf67-3bfc-9c8e-3e9ea31ca70d | -9.2421 | -65.79907 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a9d283c-66a0-3262-98bc-a3616c4fdb19 | -9.34692 | -65.44987 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2139a70b-9195-3d80-a56d-933af33f4c2d | -11.1867 | -55.07222 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9812eeb-f436-34ec-92ff-598449d1b96d | -12.83255 | -61.94967 | 2025-09-12 05:46:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a871afcc-e5ba-39b9-b454-7662ef7b16db | -12.41783 | -63.88949 | 2025-09-12 05:46:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 451d6642-3e72-3cfc-844d-8d98beb9eeed | -12.91731 | -54.77115 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 118b79a6-cb8f-361e-ab23-469964064481 | -9.03705 | -65.40082 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd3f4d21-43de-3a90-81b3-f9ba19909241 | -9.22278 | -59.38259 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73974f36-b42d-374b-8c32-05e4d3e95345 | -9.70171 | -64.93494 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3017a8cc-9d3c-37d9-8b10-b4d1cbb4fa49 | -11.87296 | -58.81142 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37ca98e7-5713-3e8f-94ca-7771c6bade51 | -12.91624 | -54.77061 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e325da49-10bc-381e-8765-737189a002ec | -12.76989 | -61.4504 | 2025-09-12 05:46:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a21c08b9-2dd7-306e-adbd-07df1c18918f | -7.56425 | -61.31298 | 2025-09-12 05:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c36a6671-2502-3c00-83e6-6ea9af51516a | -9.02641 | -64.297 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca788d1d-0ea7-31f3-ad36-f019000d7608 | -11.77561 | -64.92233 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d3ba4d0-d3be-3eed-b1f9-d196452edd3e | -10.72713 | -68.87975 | 2025-09-12 05:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b2d26e2-fce7-3510-8e35-ba6f73c2943e | -14.32716 | -54.12804 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 151cd711-6fd8-3597-925f-4905fac3e623 | -11.79395 | -62.73458 | 2025-09-12 05:46:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ef31abd-c98f-39f4-88a6-a7612b4fb5a6 | -8.6417 | -55.24879 | 2025-09-12 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96ddec1e-0439-363d-8c69-fe718200712a | -11.20461 | -55.0789 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 158ab5d0-2b00-3e1b-9869-dcb46868c5be | -14.74811 | -59.68999 | 2025-09-12 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b502ed52-51aa-3433-835c-6f5c9b7dcdf0 | -14.4268 | -52.93162 | 2025-09-12 05:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d03066f-34ee-333b-8544-2323b63342bb | -12.92662 | -54.80403 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67d6df05-a41c-33ab-ac7e-55c4d8d083d2 | -9.32958 | -65.73459 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cfe4986-cc86-36e3-b7f2-c50638901d7f | -10.67487 | -68.87131 | 2025-09-12 05:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c6081be-af81-3280-9848-4c8fa26c1ad1 | -9.69832 | -64.91238 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb283fb0-36e1-384a-b3e1-4dc00df0c927 | -9.51493 | -65.58418 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 157f9451-febc-31c0-b78d-91b81584ee06 | -14.40514 | -52.92885 | 2025-09-12 05:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5b031bd-2a12-3640-b475-c2a85f2c922b | -12.92443 | -54.75606 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62280b64-ca37-35ab-8016-c5e78d4e4d38 | -9.49198 | -55.97183 | 2025-09-12 05:46:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bd1d4b1-c708-35c7-b1dc-6ec8d067822a | -11.18546 | -55.08979 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84fd14e9-db13-323d-90a4-828b5b0168c0 | -9.33624 | -65.73565 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c089117-b1b2-3aa4-aa65-0ba7baa19d72 | -9.12096 | -65.48934 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1a91762-a616-3e82-845f-4dae6d895946 | -9.33346 | -65.73161 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55cc2820-cf3c-3e97-a1e2-51410c574848 | -11.87227 | -58.81688 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7353821d-870a-3731-b3b7-08315451c220 | -9.24155 | -65.80257 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5931084e-6ad4-3982-b68d-edd39d20b26c | -12.92776 | -54.79374 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4763965-3053-3def-b3b2-d3611da37245 | -9.48707 | -55.98862 | 2025-09-12 05:46:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f04c74d8-cccf-3328-b2bb-147a032edfeb | -9.21766 | -59.38647 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd1efc5a-94f0-3b98-828a-fb794270b622 | -9.12484 | -65.48637 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62a7c263-4cec-330c-94b5-ac8723733943 | -11.77538 | -64.92225 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d01ac1b-9a05-344c-8a24-4d662872d09b | -14.33121 | -54.12873 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 235582b4-748e-3692-bb80-54aeadb12e39 | -12.92535 | -54.80337 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ab158f-8e3a-3f9f-9b3d-3dfd60b5b1c1 | -11.17669 | -55.05995 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e48dd45b-cdec-31b8-b2f8-41737acd9faf | -9.33068 | -65.72758 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd94881-c993-32a8-9254-0534a4386b84 | -11.18453 | -55.0907 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac3982cd-03db-39db-849f-7bb802ca3685 | -9.03983 | -65.40485 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fa19e54-c983-3c04-a34e-637757df4dea | -12.93879 | -54.75267 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20b81812-05b7-3f1e-8411-9301ce1eb66a | -9.33528 | -65.45883 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98a4ea46-1790-38df-81ee-ce86829c9766 | -10.35692 | -57.48478 | 2025-09-12 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3184595-f6be-3db4-bba9-a0b1dd159754 | -9.49148 | -55.97582 | 2025-09-12 05:46:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7f345cb-9b78-347d-b60e-cc3604dad2e0 | -12.93144 | -54.75154 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c69d5292-0dff-3167-99b5-1bd0a5213ad9 | -12.35044 | -63.64117 | 2025-09-12 05:46:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be52546e-7041-3d9f-80c3-3fd7c959782b | -9.22214 | -59.3871 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08c01595-64f4-3400-9ebd-234161050cae | -8.81263 | -64.07625 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08e7383c-2ee5-343a-a616-c67a97d1d89c | -9.70169 | -64.91292 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34aa5f22-205d-31ee-98dd-095d42c678ca | -12.86298 | -62.12313 | 2025-09-12 05:46:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3841b153-ba41-33e9-879d-ad4344962758 | -11.22644 | -55.00015 | 2025-09-12 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6951b592-6c9d-30b3-ba33-d06e6e5e1f7b | -9.50841 | -65.66942 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2e24c91-fe03-3d61-9ea7-a114101b0c30 | -14.55625 | -54.5276 | 2025-09-12 05:46:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 788be25e-27aa-3fe2-8b42-460c31c3c434 | -12.91844 | -54.76085 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 25883ad2-f530-34f2-9d85-f37ad5cf6dd0 | -9.0898 | -65.39119 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95d46863-be63-31a3-bb87-08571d300cf8 | -14.33052 | -54.13522 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12fcb3ef-1335-393f-87bf-c687057dc045 | -12.93242 | -54.80996 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 846bc72f-ac8a-34c9-b000-410835ac1674 | -11.19174 | -55.08234 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f93246ec-f1b8-3270-9d43-52047d5fcb86 | -9.29124 | -65.59527 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2e0e02ff-e848-333b-9994-43521fe2c4bc | -12.97082 | -54.7562 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87853418-e53c-36bc-8e63-c4fd4f65f902 | -11.87439 | -58.8104 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2beddc4c-72b1-3d89-92a8-f007fb1523b5 | -9.52196 | -54.63612 | 2025-09-12 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ce18d05c-4d35-3968-a28b-c45ca358bb2e | -9.33582 | -65.45531 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af765f2a-de47-3c03-91f5-a4dacc483bb0 | -9.51577 | -54.63543 | 2025-09-12 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d14406bb-6de8-368f-95b8-a275a4b70e26 | -12.92504 | -54.75085 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15463bea-f3ca-3ec1-b990-572535470431 | -9.89833 | -51.88773 | 2025-09-12 05:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 31f347dd-5ab8-3dec-a2b2-5330d9f06317 | -9.33916 | -65.45585 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cdd225c-3b85-322e-9d0e-6c3f307b340f | -9.33473 | -65.46235 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11bc8bbe-94db-3be6-ad24-2f7f847cdefb | -11.65927 | -60.59924 | 2025-09-12 05:46:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adde1acb-6065-3ec1-8e57-74b51f09e67d | -11.191 | -55.09534 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d7393c1-93d5-39f5-a747-855edd821c95 | -11.19845 | -55.07831 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a2cd49c-e7ad-3378-908c-a70db374dd95 | -11.18614 | -55.07696 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 492511d4-e487-3099-8e46-7ff01e1b9653 | -14.41959 | -52.93066 | 2025-09-12 05:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fea1b12-af3d-3154-8ffb-c42c9070cf89 | -11.18603 | -55.08522 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README114.md)
