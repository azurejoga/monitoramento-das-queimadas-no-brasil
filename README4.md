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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4966b829-27e9-3389-97c4-395956f0cedc | -22.73505 | -49.9091 | 2025-09-14 01:26:00 | TERRA_M-M | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 01efe5db-56f4-3c28-be69-e7056e2e18e1 | -21.65283 | -50.17885 | 2025-09-14 01:26:00 | TERRA_M-M | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.8 |
| 8eb9ebc5-aef0-3c87-9eec-d7e1529aa035 | -12.94159 | -54.75335 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| c700ccc8-3c74-3076-acb1-fd4d0a567cff | -15.19608 | -52.49687 | 2025-09-14 01:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 42addb84-84f4-3422-a87b-4dabf560bfd5 | -12.66629 | -54.67992 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 46b2b0c6-6ae2-3f14-9317-13a10e5fc327 | -14.63746 | -52.13338 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 315f0bb4-fc90-3f6b-95fe-15bf10dfbe5f | -12.65964 | -54.68715 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 95090107-e12a-384f-8832-3fb8a43c916b | -15.80259 | -52.20227 | 2025-09-14 01:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 03f32b49-24a7-3f30-a834-735dccf5331f | -12.65573 | -54.66344 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 54499602-3977-3031-8299-d128b1170c70 | -12.93764 | -54.73051 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 04cc3126-87fa-34e6-b503-24ec66f74b61 | -16.49738 | -55.13076 | 2025-09-14 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 4cb12f2f-ea79-3a89-bb9d-c75e2373ea73 | -14.47497 | -55.95431 | 2025-09-14 01:28:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 0027809b-6e6a-305b-8eef-1ed9831ba974 | -16.48528 | -55.13343 | 2025-09-14 01:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 946b7db4-fc0d-33f4-8ddc-10ac02822fda | -12.94357 | -54.7359 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c1b52b5d-e143-3081-bdb1-e90ff42790e4 | -14.72383 | -59.73223 | 2025-09-14 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1d844491-c220-3c15-90b3-93b6005c265f | -12.45172 | -57.78865 | 2025-09-14 01:28:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| daded0ac-6d61-3372-877e-3ca751f79370 | -14.47782 | -55.97159 | 2025-09-14 01:28:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e048c68d-4736-32e1-836b-54826b9bf06b | -12.91668 | -54.74107 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| fd4dd80e-eb72-3cee-bc6d-43704f228093 | -12.93013 | -54.73853 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| bea69ed7-8b97-33b9-a7d3-3d63f60319c2 | -12.68387 | -54.70083 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6a6508ed-ee5f-3532-818a-d150f42bc2b6 | -14.46312 | -55.95654 | 2025-09-14 01:28:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| db1e00de-2c2a-3596-a370-19f34cbaed90 | -12.67034 | -54.70349 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 72f175cd-3c9f-391b-b52f-bf8922e9bb83 | -12.67707 | -54.70815 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 899c6651-9a34-3426-97b6-05f0702c9a99 | -14.39925 | -60.29334 | 2025-09-14 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4393e0aa-6ff2-3bfb-abf7-ee4f9fe25312 | -12.6732 | -54.6845 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 179.8 |
| 0ecd19da-aef6-3e34-97e2-e9c44a8fd912 | -12.92047 | -54.76371 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5dc26fd8-c377-36c1-96fe-61cd6de5126c | -12.66934 | -54.66091 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 516601d1-3343-35d8-84b4-af802cb125ec | -12.92419 | -54.73304 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| aff65faa-c59f-3f81-bd42-aaf7f415fd95 | -12.67984 | -54.67725 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6467e248-eec8-3f6e-b7d2-07a89c39ed9d | -14.7224 | -59.72247 | 2025-09-14 01:28:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 30b96b39-7535-3ebd-85a7-d5229c5c3783 | -14.46598 | -55.97379 | 2025-09-14 01:28:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| e229b5ea-0e13-3155-826e-2c9031063092 | -15.79791 | -52.19616 | 2025-09-14 01:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 2373012b-3139-3c3d-8a74-5d40c52d18b3 | -14.63161 | -52.10157 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| f42db5d3-3f55-3acf-9b27-f764c885e5d1 | -12.92817 | -54.75587 | 2025-09-14 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 94df26dc-b29e-399a-871c-524cfbc7fb36 | -12.9294 | -54.7333 | 2025-09-14 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 2ed96d15-d605-3112-8039-e7f78e674b54 | -12.7867 | -47.9986 | 2025-09-14 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 65fa5129-d3ae-3e76-b79d-55cff36bc6af | -3.581 | -47.5149 | 2025-09-14 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| cb281a5d-706c-3aef-b877-4d2302de0b00 | -3.5994 | -47.5359 | 2025-09-14 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a5651c9d-39d5-3edf-b6d3-edf9db5f6abc | -13.9478 | -44.8306 | 2025-09-14 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| eb102318-0226-3fa2-8940-8cb7ce43ef41 | -10.7579 | -44.7721 | 2025-09-14 01:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e5889ed0-2fc2-3054-914f-8bfc6983e63c | -12.6826 | -54.6763 | 2025-09-14 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 174.3 |
| e6962e9e-4c44-3093-9483-9c6697800267 | -10.7816 | -48.1256 | 2025-09-14 01:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d7267a12-1e86-3de1-96c6-5c6e830d5edc | -11.3491 | -50.8507 | 2025-09-14 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 584b6ecc-b11f-37a3-9d14-d6a052aadb05 | -22.7492 | -49.8817 | 2025-09-14 01:30:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 92a415f6-c0b7-3186-b89c-89ccfa9b1b64 | -12.6824 | -54.6968 | 2025-09-14 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 233.3 |
| 594008b2-f426-3d43-ab4a-c155fd98296e | -3.5996 | -47.4923 | 2025-09-14 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| acd3167b-058c-3a69-9754-b2776acda98b | -12.6633 | -54.6988 | 2025-09-14 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 249.6 |
| cfa5d0eb-921f-3123-b652-7bde14ed170b | -12.7859 | -48.0432 | 2025-09-14 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 43d8ff7c-7668-3f7a-b837-c7ce92df6e27 | -22.7275 | -49.9098 | 2025-09-14 01:30:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ecd6f16d-b391-3291-a774-7c0f81247b62 | -15.4512 | -47.3519 | 2025-09-14 01:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 4bc33d55-dff3-34dd-83d4-36dafb8de6f1 | -22.7282 | -49.8866 | 2025-09-14 01:30:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 13722634-54ef-3e90-b2bc-92e99147a0b6 | -15.9235 | -49.9744 | 2025-09-14 01:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 33b5846f-a55d-349d-b88e-ad9aba0e35b6 | -3.5995 | -47.5142 | 2025-09-14 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 177.6 |
| d4ca2740-e718-304d-b97d-36965fc4dfe7 | -13.9283 | -44.8341 | 2025-09-14 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 35e1f51c-16c1-3a4a-a5f7-32e39ea2ee62 | -22.7485 | -49.9049 | 2025-09-14 01:30:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 68f0f052-bcb7-3d58-b296-53be47d1a7ba | -12.7863 | -48.0209 | 2025-09-14 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 494484b9-c813-3cae-a5a7-e6723fec868d | -11.7011 | -59.3061 | 2025-09-14 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3b43f9f2-caf8-33b1-be86-7c7eeac5e1c2 | -11.3301 | -50.8528 | 2025-09-14 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 80a361d4-546e-3e9f-88e1-887b127c2e12 | -12.6636 | -54.6782 | 2025-09-14 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 253.7 |
| bd94e8f2-af19-3048-b9b4-896c51e79a35 | -11.70152 | -59.31738 | 2025-09-14 01:30:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ab21c66a-23f9-3fcf-b0b5-174f0b9901ee | -11.77676 | -64.94504 | 2025-09-14 01:30:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4344db9f-483f-3ba6-8093-5c8660ed9846 | -12.86089 | -62.13495 | 2025-09-14 01:30:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 35805526-3946-39fe-b66f-ca8d519562e9 | -11.69986 | -59.30624 | 2025-09-14 01:30:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a052fbf5-ba76-33ef-95a9-bb579a223326 | -12.86213 | -62.14395 | 2025-09-14 01:30:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1c5ebc85-5d41-3036-9b7d-8c91a0aa8bc8 | -12.87468 | -62.16964 | 2025-09-14 01:30:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d11b5d6c-8200-3536-9a4c-d545b16e640f | -11.71126 | -59.31586 | 2025-09-14 01:30:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0df8ea64-0ae3-374a-a6cd-27f93b72ac89 | -12.88737 | -62.11599 | 2025-09-14 01:30:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b30b8be5-2699-3fec-91a9-854db88d8203 | -12.32267 | -64.08443 | 2025-09-14 01:30:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 08e9668b-22b6-3cc6-bc10-eed34e0dcf17 | -3.59505 | -58.6066 | 2025-09-14 01:32:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9d285653-2787-3393-a125-453b8bc27722 | -3.59271 | -58.59026 | 2025-09-14 01:32:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 808a6eb2-4c21-36b5-bf02-7fcab4fa1332 | -10.7579 | -44.7721 | 2025-09-14 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 938a4f51-8033-3d41-8723-72076b3300c3 | -11.3301 | -50.8528 | 2025-09-14 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 337f1b84-327c-3824-bd6b-05b2233d3936 | -12.9294 | -54.7333 | 2025-09-14 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 42abea65-6f00-3a66-af63-2b8fd99436ad | -11.3491 | -50.8507 | 2025-09-14 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 051391ba-1ddd-3f66-ad0f-130b273eefe3 | -11.4453 | -50.7549 | 2025-09-14 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a13e5a45-fb59-30c8-a823-049062dee913 | -3.5994 | -47.5359 | 2025-09-14 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 56b8586e-4d86-319b-8aa6-9e119cd5a2b9 | -14.6394 | -52.1094 | 2025-09-14 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 32d04781-2a2d-3b0f-bc8a-f86c282c704d | -11.4827 | -50.7934 | 2025-09-14 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f06c5e66-4cc1-3fa1-8bf4-5eea48ce6019 | -11.7011 | -59.3061 | 2025-09-14 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ba78e0a6-b6e7-3fd3-8e90-83dce0a156d9 | -8.9427 | -48.6491 | 2025-09-14 01:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 9f1ceb1b-7328-32b9-8bb9-a65e8aa6bf56 | -12.6824 | -54.6968 | 2025-09-14 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 329.6 |
| 5050e32a-fbfa-36a9-9e47-9b3c01c02349 | -11.2924 | -50.8356 | 2025-09-14 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| ae537cfe-8da7-337f-8611-182b56d54c62 | -12.7863 | -48.0209 | 2025-09-14 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 48361f08-f85d-3c07-9e1e-44cdb92733da | -22.7282 | -49.8866 | 2025-09-14 01:40:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7ff2049e-01d7-3cae-836d-e74a596503e4 | -12.6826 | -54.6763 | 2025-09-14 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 631cec22-3bdb-3614-9107-14bec81817c6 | -12.6633 | -54.6988 | 2025-09-14 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 227.8 |
| 82753c4a-4321-3ae8-b97a-e02a7bf86e07 | -11.445 | -50.7762 | 2025-09-14 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| f549ce9d-5d4c-3b29-9dee-5e6bd9b7e6df | -12.6821 | -54.7174 | 2025-09-14 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 8473f485-a52d-314e-ac6c-d3bf6c62f5bb | -18.0065 | -46.9499 | 2025-09-14 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| dcd12d93-f179-3481-9851-6cbb163fe188 | -12.7867 | -47.9986 | 2025-09-14 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0eb44a11-9d66-35ff-a119-acbf8f615159 | -3.5995 | -47.5142 | 2025-09-14 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 227.4 |
| 1eb74f56-2f50-3911-bdfa-55fd75d82cf1 | -11.4637 | -50.7955 | 2025-09-14 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 57b518a4-936b-3f9c-b8b4-0c47208cfe4e | -11.464 | -50.7741 | 2025-09-14 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 7ccb15f7-d850-3af1-9f38-404d7f2cb0df | -11.4569 | -48.7026 | 2025-09-14 01:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2a7ddaef-130e-39a5-bdd8-e975c7b4fc4e | -22.7492 | -49.8817 | 2025-09-14 01:40:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7f56af7a-b4c0-366d-aece-271351a902f4 | -12.6636 | -54.6782 | 2025-09-14 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 38db6e8e-9659-32dc-9210-0451a929a7ba | -3.581 | -47.5149 | 2025-09-14 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 325596af-ecdf-33b6-8a48-fb5c9c57b6f2 | -12.6636 | -54.6782 | 2025-09-14 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 2fbfb76f-a082-3b46-a34c-001a70cdd6e9 | -22.7275 | -49.9098 | 2025-09-14 01:50:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 91c44cd9-0ca9-32cd-b483-28a3f674e71d | -3.5995 | -47.5142 | 2025-09-14 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |


[Clique aqui para ver as próximas entradas](README5.md)
