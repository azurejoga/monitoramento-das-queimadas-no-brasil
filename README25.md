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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dae45ac7-82f6-31e7-a97d-e78d160a89a2 | -12.47801 | -58.46761 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e8d2229-892e-349c-9d72-8877e19e76b8 | -18.66109 | -55.7529 | 2025-06-19 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c8403ed3-e8d4-3c19-bbc7-761f96257fe0 | -13.58066 | -59.20487 | 2025-06-19 05:40:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ac410d5-1e90-344b-bb39-6d6d1ae2a3ba | -12.23799 | -63.60041 | 2025-06-19 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebccf5b1-eccd-3d74-9ea8-dfca8b81204b | -18.65524 | -55.75222 | 2025-06-19 05:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 080225ee-e288-3838-91d2-6472261619b7 | -14.02882 | -55.1237 | 2025-06-19 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28ed922d-bf2b-39b4-90ed-a245dc78c784 | -13.72203 | -58.68505 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63b77866-8f33-3876-909e-3750035b68bb | -14.07554 | -53.38602 | 2025-06-19 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b09ca87-7df0-33a3-b406-da57f7f20431 | -12.4735 | -58.46698 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ef6b291-41bb-3a51-86a9-fbf388786edf | -14.30825 | -59.89444 | 2025-06-19 05:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb3e324b-67b8-36b6-8aa3-f5a5adb0b573 | -12.4684 | -58.47102 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6693b53-1abd-3795-8b05-110aa9a72e8b | -18.99533 | -52.08419 | 2025-06-19 05:40:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 817ae340-2b17-3b82-b7d4-a01d998a2a75 | -12.49149 | -58.46968 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cafcb252-30e2-3e9a-ae08-cf53fec5dcd1 | -14.02868 | -55.12359 | 2025-06-19 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e3de345-e716-36d9-9cf8-93c40144be35 | -13.28932 | -57.07224 | 2025-06-19 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4e090b8-bd49-319b-be1e-0817c12d6028 | -12.58002 | -56.98347 | 2025-06-19 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9d95442-bebd-3c70-8b41-7769606f2d93 | -12.23403 | -63.60357 | 2025-06-19 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca6d7bf2-cafe-36c1-be78-b7945b99021b | -13.72387 | -58.68276 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfe26b0f-409b-3d32-944c-a46a3b12d1a6 | -12.53431 | -57.72226 | 2025-06-19 05:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de4bbd02-9ceb-3239-94f2-2573fffa86b1 | -16.30212 | -58.25593 | 2025-06-19 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| e80f7dc7-b277-3c81-982e-414369d4314a | -16.30759 | -58.25126 | 2025-06-19 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 27fc91f0-bb40-3742-a00a-aa9983aa479c | -12.469 | -58.46637 | 2025-06-19 05:40:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96b055f3-7e92-34d8-8499-301d503750d1 | -16.31241 | -58.25196 | 2025-06-19 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 961142fa-0b7b-3230-8a98-e040980020b3 | -13.28968 | -57.07123 | 2025-06-19 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 850cfa15-42a4-303e-968c-5ef2109d39a7 | -14.06741 | -53.40118 | 2025-06-19 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2be98efe-5fa6-3dca-81fd-512910733d26 | -13.58009 | -59.20922 | 2025-06-19 05:40:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8cee0b6-18c0-3d35-8631-9bdfa7d9d91a | -16.32079 | -53.79819 | 2025-06-19 05:40:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f1f1f0b-f07c-34e4-a5df-786848624c3e | -12.50594 | -58.35928 | 2025-06-19 05:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e25914b1-3f86-343b-9ed6-ac6728564dec | -14.30876 | -59.89052 | 2025-06-19 05:40:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b2556e9-f369-3e52-bb95-60bcc91c1251 | -14.02819 | -55.12775 | 2025-06-19 05:40:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 769eacf4-08c7-37f4-bf33-520fd708b0f0 | -16.31175 | -58.25727 | 2025-06-19 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f6f268d3-588e-3aa5-ace8-365cd31f6bb1 | -21.7859 | -52.7635 | 2025-06-19 05:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57e4bc1f-d97d-34d5-b3e0-3129733834e7 | -11.9709 | -58.7362 | 2025-06-19 05:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9eeb8843-ab15-335b-a3fb-7b679e44130d | -11.9518 | -58.7574 | 2025-06-19 05:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 64300c48-d358-3116-be04-315a2db0b218 | -8.0703 | -43.0981 | 2025-06-19 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| c2fe7330-7a73-309e-9055-41aae5c246db | -11.9707 | -58.756 | 2025-06-19 05:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 24107906-7edc-3ec3-a019-d2ac9a2a0836 | -11.952 | -58.7376 | 2025-06-19 05:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| eef53d11-d519-3ca9-833f-8ee688cf0f92 | -8.07 | -43.1216 | 2025-06-19 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 3a649403-766a-3d6f-8cf9-93f959c1e82a | -9.00391 | -61.52641 | 2025-06-19 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efc0a6c0-75d2-3d89-82d1-ea05b4955f74 | -9.96768 | -64.95669 | 2025-06-19 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2125f85c-dec6-33f2-9bfb-27617dffeb49 | -9.71421 | -64.54109 | 2025-06-19 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 058b006b-edab-350a-9f20-654f0f0a17a4 | -9.39182 | -63.26508 | 2025-06-19 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b565d7c2-a0bf-3d28-8ae4-c5984ac45ca1 | -8.72391 | -64.17644 | 2025-06-19 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 154935b8-552d-373b-ba3e-eeb824e88145 | -9.39656 | -63.26574 | 2025-06-19 05:59:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d55fdb8-478d-3065-bc9f-bda8fd9c8ed7 | -9.00435 | -61.52313 | 2025-06-19 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38054a21-78c8-3f40-ba58-c38c44372ac7 | -10.28177 | -60.54153 | 2025-06-19 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9175fad6-819d-3a58-b610-fa6003695d01 | -9.39805 | -65.51438 | 2025-06-19 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b736ae51-5a48-35f9-8023-3fc7febbb48a | -10.28229 | -60.53741 | 2025-06-19 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6dc2610-4e02-3429-b39d-2cb810e9bd9d | -11.9518 | -58.7574 | 2025-06-19 06:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 936b9920-a724-3727-903c-b096d1ff93ff | -11.9707 | -58.756 | 2025-06-19 06:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 849b2616-ce04-3b8b-85c3-6b153bc67b2c | -11.9709 | -58.7362 | 2025-06-19 06:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 84c2ea8c-dd7e-33ed-b452-82a09eee203b | -11.952 | -58.7376 | 2025-06-19 06:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 97284cec-cbd4-3e54-a38d-fe37e68f206e | -8.07 | -43.1216 | 2025-06-19 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 47d4557b-cdd3-3e95-881c-d35da8c9c3a3 | -8.0703 | -43.0981 | 2025-06-19 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 7f9f110b-a0b7-39b8-bbb8-9db1294995cc | -12.47755 | -58.46938 | 2025-06-19 06:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1c68e73-16ea-350c-91e5-c3f41f01aedd | -11.95213 | -58.73713 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e4796eaf-ae80-3594-bb30-e57a9ff9b9d4 | -16.3012 | -58.26418 | 2025-06-19 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 960de055-b58c-37ea-956d-6ed86d04d9ba | -11.95147 | -58.74305 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c5107cda-35a8-3e7b-adf5-0ccfbac67f40 | -11.95405 | -58.73656 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4a7ef1f8-f7fd-3183-ab35-a922af098a6a | -12.47338 | -58.47093 | 2025-06-19 06:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b917aef8-3798-3e00-a510-b37eae222bb9 | -11.96405 | -58.75011 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5f87474-f874-374c-b666-77b91ff27a34 | -11.93756 | -58.76306 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb078145-c823-3a6f-b7ac-1228aa808783 | -11.94473 | -58.75886 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e9248a5-049d-3b23-ae67-dbdd02983624 | -16.30898 | -58.25787 | 2025-06-19 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a717fae0-a2f6-34e3-9432-19e1feb79bf4 | -11.96064 | -58.73742 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2a95c317-e17c-397a-bc03-52d570bcaf35 | -16.30651 | -58.25168 | 2025-06-19 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 559a8cff-cf76-3b59-906a-c53c06c7b472 | -11.94541 | -58.7531 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| adaa5cf6-2267-3c8e-ad71-9e691b35f0b0 | -16.30188 | -58.2571 | 2025-06-19 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| ba239500-eab3-3b13-8c0d-397f62eafb90 | -16.30525 | -58.26564 | 2025-06-19 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| f34c856b-d89a-3e13-b11e-ab44faf11ed5 | -12.23285 | -63.6005 | 2025-06-19 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7da14f17-d1a2-3430-ba26-02e7f455f86d | -11.96005 | -58.72613 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3918c436-fa57-32c6-9ba1-b437a831811e | -11.95279 | -58.73116 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 138f7cea-0489-34b2-becd-c1afdb3d5d48 | -11.95927 | -58.74896 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 4137582c-392c-3002-b882-8a82e0a1449b | -11.95615 | -58.76095 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d4a7244f-1887-3ab9-be69-93619730cce6 | -16.29877 | -58.25795 | 2025-06-19 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| a4a39ac2-5399-3533-90c5-9ff27b43f199 | -11.94297 | -58.75937 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d17604a-316d-3207-8b48-1bb34cd43b95 | -11.95806 | -58.74391 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 48e06d5e-0709-3395-bd25-513d35debf01 | -11.95996 | -58.74323 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c4a18558-6359-35ae-9131-101b249666cd | -11.95938 | -58.73215 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d545feb-c002-38b6-82a1-06392004c1b3 | -12.4708 | -58.46861 | 2025-06-19 06:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51bdfbc3-111e-3403-a6a6-10915606c51a | -16.30588 | -58.25864 | 2025-06-19 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 3426b402-13cf-3806-baf5-b1c1524d2ea8 | -11.95795 | -58.76007 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ee437b3-578e-3b25-8afd-fab18a4a700a | -11.94954 | -58.76042 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6a7f112a-4f3d-34d6-89e4-bbf7a3b8140f | -11.95131 | -58.75978 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1e6b7ab6-1d4a-38d4-9ff1-3afa6b4667a9 | -11.9586 | -58.7546 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5ed2e5f4-9f5f-3742-b612-ea52cc6fb2bc | -12.23768 | -63.60119 | 2025-06-19 06:01:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99de1a65-8950-3b43-a411-cfb5bba8df52 | -13.57844 | -59.21127 | 2025-06-19 06:01:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94e4d7c7-fbb4-3a5f-9de4-8bab89e636d3 | -11.94424 | -58.74792 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f1c1c05-7f6d-3120-8516-57c40c92bb56 | -13.57999 | -59.20428 | 2025-06-19 06:01:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75165ba0-901b-3fd5-9ab9-e6eea881313a | -11.95476 | -58.73059 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5f645cf-f556-370c-8a53-5a4ec25a0e37 | -11.95335 | -58.74247 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6338489a-3886-3f67-8b07-ffb2e0eee119 | -11.95018 | -58.75468 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d98fe736-5886-360b-9e5d-cf7cc3ecfa98 | -13.57932 | -59.21028 | 2025-06-19 06:01:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26aacd09-713e-3510-be6e-3cd68a4fa05f | -11.94409 | -58.76433 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31254555-e73f-33a2-88bb-0eeee044ca7d | -11.62182 | -58.29239 | 2025-06-19 06:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb1d5c71-c557-3390-b599-e02415e14b37 | -12.46662 | -58.47025 | 2025-06-19 06:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e77befa-80bd-3b2e-ad5d-2f57f9fdadb5 | -11.96135 | -58.73152 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0a74b99-df41-357d-b31f-6408e344706a | -11.94609 | -58.74732 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5256ea96-f7c0-30cf-80c9-15f8da252452 | -11.95198 | -58.75411 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 0bf2eab7-891f-3b6e-a7aa-46e46ab361d3 | -11.95741 | -58.74969 | 2025-06-19 06:01:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |


[Clique aqui para ver as próximas entradas](README26.md)
