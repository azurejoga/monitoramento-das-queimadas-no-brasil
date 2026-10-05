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
| 86af30b9-45a4-3407-b789-fdc1ca33f2cf | -9.15263 | -68.23869 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8104e775-ee5d-38ea-bb55-49b693893e10 | -8.59402 | -66.81367 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce0973c2-3a40-3d26-afbf-de5f9d308aec | -9.16574 | -68.25486 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9f8350a-e2a9-3b8f-b6b6-15c3e50d81fd | -8.34307 | -62.82566 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0645fe7b-fdb1-3ce5-a3d6-d587548c2e01 | -8.69995 | -69.28296 | 2026-10-05 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb4595e-2152-3d93-bcd5-2a240d38fa8e | -8.04867 | -72.43769 | 2026-10-05 06:20:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33e83d5e-447b-32f1-b015-72bbcaf995e1 | -9.03268 | -67.47303 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43535e30-1488-3993-a2f1-372dad52aa72 | -8.45087 | -62.73218 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e27a85-eda4-358a-b586-807608cc6e09 | -8.62638 | -69.50547 | 2026-10-05 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb6dbb05-01fe-3498-b5eb-63e1dab569bd | -7.44176 | -63.56461 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76ff1177-0c6d-3781-8413-a8baccffdb7d | -9.02892 | -67.55527 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9871e4b8-97aa-327c-b6ba-f9253fd11580 | -9.10972 | -65.36126 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15c67097-638e-3732-8a5a-69a53ba3384b | -9.1212 | -68.21495 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94407506-4aa3-308c-84b2-a1cc93191c80 | -10.87971 | -61.40581 | 2026-10-05 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe4f7cab-3b35-392d-b7fe-90a4e234b48c | -8.64636 | -62.5264 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89d9d7ee-f072-3571-a773-d7c5356af260 | -9.16128 | -68.25888 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41850b6d-4ace-3698-803b-a6a1f5db16b7 | -8.66362 | -70.04104 | 2026-10-05 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfbf220a-7710-3758-8599-a6346cb511a9 | -9.23016 | -67.89745 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b706368-5025-33d8-9259-bc1eb30c0406 | -9.50309 | -68.49906 | 2026-10-05 06:20:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2198a874-9f89-37ab-8ef0-cc928b4945b5 | -10.62196 | -67.92285 | 2026-10-05 06:20:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cd9a1ee-794d-34cc-b993-2b4775e5c143 | -9.08506 | -72.24205 | 2026-10-05 06:20:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aedfbb0a-f35f-3d20-940a-21a1fb257abe | -8.66707 | -70.04158 | 2026-10-05 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cf24ce9-a21b-32fe-8b14-3d58a7a5bf5b | -9.17127 | -68.26981 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c48cbeb-0e47-3e49-9bde-50d9b1b8a0ea | -8.74196 | -69.45268 | 2026-10-05 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35fbd120-b5e5-3ced-856b-613f08d0346b | -8.08981 | -70.23849 | 2026-10-05 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7a1bd32-ebe2-3c66-aba6-54f2ff168703 | -8.51664 | -67.00612 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c52d133-8c8f-3dae-9ae2-9d997a4c1431 | -7.43779 | -63.56815 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29846dfe-55da-37d3-b6e5-61d9d553fdd3 | -9.12334 | -72.23745 | 2026-10-05 06:20:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f639613e-007e-3ae1-8c17-6d253a049c72 | -8.052 | -72.43822 | 2026-10-05 06:20:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74a8ef6-936e-3611-a48a-ffd1a87bf857 | -7.43359 | -63.56163 | 2026-10-05 06:20:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a781ac56-b9e8-3e37-a0a9-3a86e91f0d1e | -9.13275 | -65.90929 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61e32bbd-d53a-391f-8a39-7e5b98f2219c | -7.67791 | -72.45368 | 2026-10-05 06:20:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8dc763da-7962-3adc-8b04-3ede07fe2683 | -9.11104 | -64.36216 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5ec1934-f8ba-3b47-a6c5-8dcc8eec814c | -8.28449 | -71.07515 | 2026-10-05 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e174b8bb-e9c2-39f1-a1c2-9942e958023a | -9.10515 | -65.36058 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05d6dfe6-66da-3d7a-9a48-8aee31f4f8ef | -9.12187 | -68.21031 | 2026-10-05 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c197cd5-e67a-36a0-ab50-579485a5e33e | -8.62404 | -69.49699 | 2026-10-05 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cdd6ba3-6ea8-3d23-b5f5-895147713217 | -8.65185 | -62.52729 | 2026-10-05 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea730b1d-3424-39a0-b7c9-c35a0a4c223b | -8.05257 | -72.43472 | 2026-10-05 06:20:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 809d8ad2-e128-3236-b951-b7b8b089e549 | -8.87943 | -66.64763 | 2026-10-05 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 122ebf0b-d6c8-3148-b667-39627073c62b | -9.50348 | -68.49738 | 2026-10-05 06:20:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 655c9ba6-77c7-3e61-a57c-6e7a51e7f6ff | -12.88386 | -61.71357 | 2026-10-05 06:22:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d65048ec-c952-3230-8dca-03299801263f | -10.60737 | -68.68215 | 2026-10-05 06:22:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f614b761-d863-3d97-a674-754134fe55da | -10.64285 | -68.59799 | 2026-10-05 06:22:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6c2b036-5a1a-3115-8900-7c2ded2f5454 | -12.87718 | -61.71752 | 2026-10-05 06:22:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f267b64a-83c8-3102-95fb-c5f7f6786a6e | -10.44655 | -69.49825 | 2026-10-05 06:22:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45bdeab4-5279-3889-9277-fd083db0469a | -12.88332 | -61.71828 | 2026-10-05 06:22:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8846e302-9191-360a-87c5-c5511f333795 | -12.87654 | -61.72351 | 2026-10-05 06:22:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f1a6412-d3e3-3098-be94-f5ef6cc412c3 | -10.86008 | -68.69152 | 2026-10-05 06:22:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb82ef72-1aec-37be-90d9-062b31b5f6e3 | -10.63805 | -69.28472 | 2026-10-05 06:22:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 039e6643-c9df-3fbf-8245-0cdad0c15b9b | -11.97751 | -63.61062 | 2026-10-05 06:22:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c3d5068-3fa3-3c7f-aae1-3d33d076160a | -10.86454 | -68.68747 | 2026-10-05 06:22:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d27012cf-fdac-3cbe-a701-81077464573f | -12.87664 | -61.72226 | 2026-10-05 06:22:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d59d6f0-9eb8-30e9-a84f-f12b82de0e3c | -10.63741 | -69.28899 | 2026-10-05 06:22:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82e16d7f-7302-380f-aafc-aec8eaa7b218 | -11.97214 | -63.60989 | 2026-10-05 06:22:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 22733748-6c25-330a-b0d9-8e54b548ac3a | -10.86076 | -68.68694 | 2026-10-05 06:22:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6f3a33a-9506-3bdf-906e-6bfdfca44f69 | -12.87711 | -61.71878 | 2026-10-05 06:22:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1bba135-ae02-3d24-9ac5-fe9f2362e277 | -12.87768 | -61.71407 | 2026-10-05 06:22:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a68bb983-17b6-3d8b-bc30-8b6a3958d7cc | -8.66687 | -70.04461 | 2026-10-05 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b85883d-09ed-3662-9a2a-1875ed4cc6fa | -8.77189 | -69.53377 | 2026-10-05 06:40:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a62bf378-e0b0-3205-bffc-6e474d0bfdce | -9.12198 | -68.21941 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56bdf437-f14a-35c5-8fc9-9ec92f899f25 | -8.74518 | -72.82816 | 2026-10-05 06:40:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83a2e05d-5750-39e8-bec2-29cd4d91117a | -9.02922 | -67.55428 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a666cab6-5770-326a-a88f-ccd9cec5b568 | -8.66728 | -70.04153 | 2026-10-05 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a5d5cfc-0629-337f-ab1d-8a5e8cae9dfc | -8.6651 | -70.04375 | 2026-10-05 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4652f251-d5b7-3ca7-8690-aced404fe03f | -9.49905 | -68.49709 | 2026-10-05 06:40:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b67e6a-05ab-33a2-98f4-9b0005a84962 | -10.85687 | -68.69134 | 2026-10-05 06:40:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1973f5d7-9a3e-37aa-a59c-a8665b731992 | -8.05074 | -72.43702 | 2026-10-05 06:40:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34150060-9949-3908-bb2b-6a9b94e33af1 | -8.2854 | -71.07568 | 2026-10-05 06:40:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d438b9b2-519e-3741-bc48-b7756cb526ee | -9.15035 | -68.26853 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce2d2841-8f6b-36e5-a351-969469a70c2a | -9.39801 | -65.89931 | 2026-10-05 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebebd0a0-747d-3d95-a5f8-36dc833d9134 | -9.40306 | -65.89954 | 2026-10-05 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 490cdda3-0694-32eb-a4c3-5ad7da38296a | -8.87165 | -66.65155 | 2026-10-05 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60d55143-febb-3534-8fe8-e8d59395af64 | -9.15725 | -68.26107 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85de9298-c19c-34bc-8c11-d7219c370aa0 | -10.6397 | -69.28858 | 2026-10-05 06:40:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4dc8fc2-d861-3772-b796-9d43dbdd1a91 | -8.87941 | -66.64814 | 2026-10-05 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8c3a363-a642-3b05-9c8f-e1f5276abdd8 | -8.67068 | -70.04143 | 2026-10-05 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b749ace8-202b-31e9-9383-4b80812450aa | -10.63411 | -69.28794 | 2026-10-05 06:40:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88099430-91a6-3759-bcb2-a0403cb89aec | -9.02863 | -67.55897 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94b25792-574a-3342-bfb6-dd51d5beb493 | -9.15089 | -68.26438 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| decbf453-97da-3da3-996e-82cccf84a06d | -9.40384 | -65.89337 | 2026-10-05 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8e3d86a-91be-32bb-a538-7b47cc07273d | -9.16362 | -68.25776 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3008d03-ca38-36f8-b8a8-0d7643e7994a | -10.86269 | -68.69198 | 2026-10-05 06:40:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bae56a10-98de-3b9c-9c50-cd16c93e680e | -7.36157 | -72.61219 | 2026-10-05 06:40:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3d849995-5821-30fa-bcdb-c718384391e0 | -7.66425 | -72.43264 | 2026-10-05 06:40:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19167fbb-334e-3588-a04d-9f97602941cc | -9.22263 | -68.17129 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 356d89f9-de9c-3bc3-8999-6b76afbcc461 | -9.16202 | -68.27015 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a8c4133-34f2-3a3d-b7b1-0ee81cea3325 | -8.66553 | -70.0407 | 2026-10-05 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eaaaf42-0c7c-388f-9978-8969e029d38e | -9.49986 | -68.49366 | 2026-10-05 06:40:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 119e182a-7da9-3804-b3e0-d5a9e0952ac4 | -7.75189 | -72.86953 | 2026-10-05 06:40:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75bfc1c4-a286-34f6-936a-2dd83aa32b0a | -9.49935 | -68.49776 | 2026-10-05 06:40:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 528bf522-716a-3dd3-ae60-9a607b42355e | -9.12254 | -68.21519 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3af3b56-cd91-3a2d-afab-78b388f904f3 | -10.85666 | -68.69198 | 2026-10-05 06:40:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a11a671d-f5e3-3516-888d-352aab31d015 | -7.36213 | -72.60824 | 2026-10-05 06:40:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90053509-0682-38b7-b56d-0dc91bf1d2dd | -7.34518 | -72.60578 | 2026-10-05 06:40:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5debb9cc-5629-3840-a76b-61ed2725d6e4 | -9.12114 | -68.21766 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccf5c43b-dc6e-3885-a045-97dc210e9d5d | -9.16148 | -68.27433 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0835114b-a108-381e-a895-993ac4a91431 | -9.21674 | -68.17055 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2a82ad9-c881-3d65-83ea-2c4722a5c1ff | -7.34511 | -72.60725 | 2026-10-05 06:40:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87e6d137-7093-31f7-837e-45a9dc3bafd5 | -9.03532 | -67.55514 | 2026-10-05 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README61.md)
