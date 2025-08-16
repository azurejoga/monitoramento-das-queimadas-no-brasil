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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a7b0d3c-7e5b-356a-871d-dfeafaf0acb9 | -7.28043 | -57.65955 | 2025-08-16 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a9063b9-44fb-34c3-bd28-68cd1f7565bf | -6.93231 | -59.64857 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a7375c8-80e1-3408-a507-7eb068870893 | -6.95706 | -59.53197 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e81b288b-e607-3244-acb0-37fa33f443a0 | -6.94581 | -59.51559 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02cf8835-63f8-32ae-ad96-c70b860b46e7 | -7.43545 | -60.02332 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 650cca69-926d-3cec-833e-a84564ecb05f | -7.52288 | -61.31911 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56620dc4-08a4-303f-8cea-a889aee29b08 | -8.99244 | -60.55069 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d80fe287-7808-375c-90d6-5e714c36b377 | -8.80803 | -52.03619 | 2025-08-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| beac7e12-0dbb-3181-905e-719c91fdf151 | -7.81729 | -61.32702 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5300ba5-aefb-3f45-b9a4-6e76ef10f0fa | -9.39363 | -60.54891 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2336d44a-3a64-32c9-bba1-3732303dde4a | -7.30499 | -60.6245 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212812b5-5dd6-3f69-8ff8-790fb0b76463 | -3.38118 | -52.71246 | 2025-08-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98fe4e59-a2d1-3715-a044-369c102bac7e | -2.38566 | -47.66819 | 2025-08-16 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c16f841d-8462-3205-89d5-8627c40db241 | -7.81013 | -61.32945 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08b6c3e7-8585-3c4d-b83f-2b5357b046e8 | -7.08026 | -59.23266 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3ae9523-cf8c-3d19-9218-1f81c4b9b3a1 | -7.90803 | -61.74513 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8c8aa90-cf07-37df-b873-cb222ec63ce6 | -8.45811 | -64.05067 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9d6e4d9-e527-3f60-9391-9cb942b17493 | -7.92961 | -61.73778 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 347a2f54-c031-3430-bcf1-826e2abf24a0 | -10.3947 | -53.46699 | 2025-08-16 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88abbe67-a008-3ee1-b7cc-895328d784fa | -8.59175 | -63.8748 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f833d0dd-9a91-37fc-bf61-8dbfa2f2d0e5 | -9.21825 | -59.64921 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a19f2784-86a8-3de7-b495-31b0ebd28f28 | -7.87313 | -61.81498 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8271c31-430f-34a5-a219-90240aadfb0e | -6.9334 | -59.64146 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4f16c5-49c4-3e01-be1b-24bd8343ab99 | -9.20299 | -59.65817 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cfefca5-cc81-30df-92fc-302c94d4adcd | -6.94589 | -59.53759 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23919d6d-d0d1-377d-a801-cdc984af1c23 | -7.83746 | -62.99823 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72eb153b-16d6-3992-9770-5b83803c4f81 | -7.95673 | -61.76001 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63ed4ccc-f2f6-3dc0-a343-2b99de94f269 | -7.92629 | -61.73726 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8244c27e-78b4-3d71-b34c-a259df1a2cf3 | -8.98634 | -60.54613 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5d7c5c3e-64d3-36a1-afaa-ab9f9b99129c | -8.09372 | -54.988 | 2025-08-16 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e0e11fa-ef31-3578-a85f-de699791f3aa | -6.93246 | -59.53549 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22f202a6-3990-3aa9-8934-e774d418e4b7 | -7.41546 | -60.02021 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 268a53b8-1d88-3066-8946-3a60e30b1874 | -7.9191 | -61.73971 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 397768b1-9336-329f-b2d6-f90b9c463e19 | -7.53393 | -61.33508 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13cd81a9-2f98-357e-9651-21a5456a0fa5 | -8.98674 | -60.49934 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ae897035-640b-38f9-9fd8-8a97259bc63d | -9.17329 | -59.6422 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 673f7372-af4e-312c-a7de-9dae715e47aa | -7.95009 | -61.75896 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27d4a63a-e3bb-30b2-8982-86d4eac0d48e | -8.14791 | -62.77474 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 844a983d-0b3a-333b-8e13-0149463554e3 | -9.20355 | -59.6545 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1936a6fd-8cf2-3f51-919e-e2b8eba11f99 | -8.4145 | -67.74194 | 2025-08-16 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e53e8d-d0c7-36cc-8996-c4a8f6c78ab8 | -6.90714 | -59.63377 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0c8a4a7-a72c-32f6-83a3-44572ced6b3b | -7.46335 | -60.41498 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2a1d367-6ba6-3dfe-b5e4-1de9ed3da1b6 | -8.99346 | -60.52205 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8713fd3e-d92f-3864-a274-84881afc3b50 | -8.66517 | -62.4608 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ab51aa-ac28-3003-b24e-0112b5685f2c | -7.82802 | -61.32528 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 996bd737-d118-3ce5-9eb1-7fd4db040eba | -6.9476 | -59.54883 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 10d6973c-840d-36a0-a902-00391ae3a619 | -6.79388 | -59.81912 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f732f81-0b91-364e-8a71-c51e21cbe17b | -7.67134 | -63.30947 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56d57820-c1c1-3743-bfa6-b2899044a00e | -9.50808 | -60.55577 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c2c386ed-cab0-30a0-9e6a-5c2afec07250 | -9.51358 | -60.54216 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 199590f7-3786-3c65-9bb8-99062a402633 | -7.29122 | -60.6259 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f37f97a0-0c84-323e-8b8b-84556ae04979 | -6.93527 | -59.53959 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec0f2cb2-d33f-3930-a6dd-a9dd6b302def | -3.43518 | -49.04697 | 2025-08-16 05:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ccbb53a-2f2b-3514-b9b2-43f49f82eac6 | -8.91235 | -60.73916 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5aeb637-dfd6-3afe-8f5b-420fa9ae2ad1 | -8.91011 | -60.73164 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a9e397e-1e9b-3031-95ca-a8b6b1c5eb89 | -7.43382 | -60.03385 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca335f2e-9f2d-39ad-965b-fec18d7024bc | -9.39751 | -60.5459 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb49125d-0b64-32c8-bcf2-41fd0d7f118b | -9.17409 | -59.64237 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4fb0828-5a39-3b67-861c-88597b4b2b4b | -7.83403 | -62.99768 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e3a33cc-93a1-33ba-b7f6-278feb7ea6c4 | -9.39139 | -60.54132 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c51ee4ea-e2b8-3f08-abe2-f42679ec36f3 | -7.61714 | -63.33622 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d73a4882-2874-3aff-8eb4-9792150a6517 | -8.66852 | -62.46134 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| deb1b766-72e0-3bf7-8021-2b1af6b6e679 | -7.07293 | -59.23524 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cae6eb07-3126-378f-be40-ce557936d0b0 | -7.52683 | -61.38023 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b817a080-daa5-3732-b1a0-0948a9b2b5f2 | -9.53332 | -63.7158 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67d97ba7-38c9-38dd-b891-f11d892971bb | -8.11773 | -61.19025 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 829f6bb9-da19-34d9-8148-6929dca7a999 | -7.04169 | -59.62161 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15faa9df-200a-36c7-b10f-50ba77f2023b | -9.39472 | -60.54184 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae5eec42-f978-392e-be39-1b54978b4988 | -9.0406 | -67.42426 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 552dbc30-ebfe-3d4b-b16c-a4881da280ed | -7.07632 | -59.23577 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80de4362-b1f0-347a-9afa-662bea622e96 | -7.30115 | -60.62745 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b25652f-60aa-3cc4-aae4-e1e6a21a0023 | -6.95206 | -59.54215 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df5c6660-f60e-3991-85db-d37ebcbc8048 | -8.93887 | -62.23878 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0bde981-0906-37ca-b621-32efcaf7b291 | -7.81675 | -61.33049 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 745fbf5a-3d95-3ebf-a062-2800d45d29ec | -9.17273 | -59.64589 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c67c567f-06b9-3168-90c5-aca791ef46a9 | -6.80055 | -59.82016 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e0bc9be-a565-331e-bbb4-d0bfc5744293 | -7.07687 | -59.23214 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee7cb320-0069-36b5-a303-fc53256c58a7 | -6.95316 | -59.535 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d64a4de0-d590-389a-bda9-7e2d4bd530f5 | -6.63252 | -60.00612 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6db1e266-0416-344d-954d-0f2f6f9863cf | -7.07266 | -59.71015 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bd9fbc4-4b70-3da8-8e8f-1ffe7051e89a | -6.94363 | -59.52989 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c644ca1-1c49-35ea-95bc-788b06814305 | -9.508 | -60.53405 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7142449f-f6f1-3657-ab1f-7aaca7a62c9b | -9.1676 | -61.50033 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebb59515-0d72-355b-b494-e0c3052c766e | -7.2846 | -60.62487 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a53b274-501a-35a6-801b-f9d5bf3fcdd1 | -9.00234 | -60.53065 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33938390-3d5d-31a8-a504-595ce1ebe0d9 | -8.9995 | -60.50495 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c700d560-2656-3a61-a02f-657a57af5f9c | -8.99407 | -60.54015 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90373acf-5bcb-3f45-ad47-a2914136d8dc | -7.60262 | -61.2215 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f38483cf-922d-3200-a40d-6cbe40c7b33a | -9.5035 | -60.51886 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27e54258-1b5f-39a4-a9e4-5b7266b6a269 | -9.16877 | -59.64905 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f396833b-8ced-3627-86cf-008cdda0f1e1 | -7.62408 | -63.33734 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59697d1d-cc2e-368d-9e5d-8c6a510ee05c | -10.04687 | -59.12127 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 324aac92-f6e9-329a-ba6c-f235a356c53c | -7.43987 | -60.01679 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10438d07-833f-33e3-ad62-8dd3b26a932a | -6.93862 | -59.54011 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f564d7ae-f368-3391-ae21-3aa7b3763e13 | -9.1682 | -59.65273 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 348ef3b5-5856-3a2c-be89-21c7d21c91f4 | -9.04921 | -67.42575 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e17c64f-a378-3f5a-985b-ec8069be6069 | -9.34326 | -62.58492 | 2025-08-16 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7439842b-213e-3b6e-8ab2-a9a61ee55ff2 | -7.43932 | -60.02032 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6fa0eca-c2ae-3b4c-b5cc-dd5392d1b3fa | -9.16537 | -59.64854 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42a7d50c-ba05-3e89-836e-20ce759881af | -7.61998 | -63.34063 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
