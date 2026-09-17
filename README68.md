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
| 96d0ff62-979d-3f7a-9c66-2cee98ae7aeb | -12.11161 | -57.19599 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f5c5536-a632-3e82-90ff-507bf8b4813f | -10.3864 | -58.31024 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2802f85e-a162-336e-a3d1-904dbacfe138 | -9.10607 | -60.95316 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 565debf7-5e69-3d89-b1aa-cbfa1c146fd0 | -9.09208 | -60.96294 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d022059-6a25-3307-9802-bc28ada45b4c | -10.14962 | -61.17955 | 2026-09-17 05:18:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 370ca445-1824-34a1-9864-998010587b1a | -10.91334 | -46.30418 | 2026-09-17 05:18:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88e053ff-faa6-378c-a278-7655bb8506e0 | -12.45798 | -50.78036 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| edd77402-cddb-3aac-b6bc-5b9cbf3408ec | -12.44621 | -50.80096 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 58fed85c-0cf7-3073-847c-4fa1051bfa5e | -12.40599 | -48.48205 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 705c316d-a044-3768-861f-c8b18aa59bdc | -12.44887 | -50.81464 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| edfa958d-ae0f-33a1-99a6-64cb3c34501b | -13.38295 | -57.02822 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7b69a45-1597-3b19-b4dd-407fa4a0f8ee | -14.3978 | -47.27666 | 2026-09-17 05:18:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0447908d-eedf-307a-a208-e5b125a5ebba | -11.52633 | -46.86412 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ebaf2de-d889-36bd-b57a-13c5e6683b99 | -12.43597 | -50.84378 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8b972087-9611-3b0d-827c-3eea91e1a2a8 | -9.1005 | -60.96236 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a78afbae-4afb-39fd-8ec2-5d9280471131 | -11.55802 | -46.88858 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9adcde9-7d35-3d3e-9690-1ae8a8901aed | -12.11718 | -57.18241 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fefdfe1-e2c7-342e-b0d8-df1dfaa91ee8 | -10.87795 | -61.39566 | 2026-09-17 05:18:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cad2ad21-6489-3208-8179-1ddc205a961f | -12.43237 | -50.80344 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb99d87c-d532-3d08-8f38-7cc8ceea5ae1 | -11.53673 | -46.86188 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 018fdacd-9fa4-32cc-bd89-60ab2461c992 | -12.45211 | -50.82395 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fca78894-f3ce-3ce2-9540-2b572d110296 | -12.4624 | -50.8475 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18ddea4e-999b-3c41-8444-eb49676e0599 | -11.80652 | -58.17287 | 2026-09-17 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 43a4b924-46fd-302f-b21c-e6bf0a165064 | -8.76043 | -66.56769 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55dda209-eb32-3793-87f9-a7995a36a1f5 | -7.80134 | -66.91855 | 2026-09-17 05:18:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b27c725-63a5-348a-9d67-0523c122e723 | -11.04377 | -48.27727 | 2026-09-17 05:18:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1aad480d-c964-3e39-8f0c-e3101e72391e | -13.37794 | -57.03836 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 117a0ca6-4d43-3a58-b2e1-fe6c46cbc626 | -9.09716 | -60.98231 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5f2efd8-abcc-322c-a070-fe7cd6201865 | -13.38074 | -57.02055 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85116faa-d109-3fbc-a7cd-5b623c97ca06 | -15.4735 | -53.78027 | 2026-09-17 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c18052dd-e4d0-30f9-9c43-879be55118a1 | -14.84288 | -59.54001 | 2026-09-17 05:18:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c73f8274-b16d-354b-a5cf-440e80c90a93 | -11.89067 | -47.58404 | 2026-09-17 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34825dd3-15c1-3e65-b94d-2c8f09f6b0de | -12.14688 | -48.25978 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76073018-248a-34db-8fec-6b1425e6bce4 | -7.60768 | -67.32317 | 2026-09-17 05:18:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10768528-e076-39f8-84bf-6923e6b2499f | -14.96249 | -47.5295 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8b585a4-5418-3f1f-ac5f-f43c1ba43b03 | -12.37684 | -48.46248 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b4e0188-004e-3a14-b9b5-84fea955e63c | -11.89657 | -47.58113 | 2026-09-17 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f024633d-1086-38a9-b04d-86fb11ae2e42 | -9.74424 | -62.36551 | 2026-09-17 05:18:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ee75f7-7fc6-3634-b885-b59f9c19a2ec | -12.43621 | -50.80842 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59801959-bebb-3edd-83d3-0ae3c510db72 | -12.45622 | -50.79348 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27a468b5-8b08-3c00-a681-a324cda14d9f | -11.55848 | -46.88482 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| af4b058f-2f56-3254-bae1-cf8c010b6bfd | -9.10133 | -60.9574 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c5767a7-041c-37fc-a74f-08658f97c63f | -11.52952 | -46.87302 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a88ca499-6f6b-3caa-8135-14fe77ab6b21 | -13.7482 | -48.80772 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb8386b0-1a80-3988-a25c-d61b6af77da2 | -11.31851 | -46.7839 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ba31ed6-70a7-31d2-b0c2-b3c6d52ec54f | -12.45976 | -50.83388 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8e4c929-ccb7-38c7-96b3-3ac524652c6a | -13.67807 | -48.59361 | 2026-09-17 05:18:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 44283e4e-e890-33c8-a680-68b1b2195744 | -9.76716 | -60.4642 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6fad03ad-6bef-3322-9611-ba83dd3c2957 | -11.32549 | -46.77415 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 658de60d-67e1-37a1-a144-722c2c803b2e | -12.43183 | -48.48569 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 265a78e5-9118-380f-88ab-c1606e282f40 | -12.42796 | -50.80282 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| afb5f27f-43f1-3980-8dbd-ed36a67ff557 | -12.14164 | -48.25915 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a867e85-4537-3793-8f1f-2be611b038bc | -12.45387 | -50.81091 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77ff3287-f242-3549-8716-73ea875d3962 | -11.31708 | -46.78556 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8224d7f0-57f7-3fde-8cc6-8e0ced828f5c | -12.44271 | -50.82706 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf24a4aa-dad1-363f-8321-aeaacf73f0a1 | -9.05784 | -65.91859 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c59ab2be-ef45-3e72-acdc-0b76a4d6ffaf | -8.6474 | -66.5959 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47fae018-d6fd-3e50-a053-e85a7c542c34 | -11.49223 | -45.73871 | 2026-09-17 05:18:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9b975c0-31ac-372a-b7d0-4af8c7fc5139 | -15.4874 | -53.79212 | 2026-09-17 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73077bae-c28b-3b48-84b8-03d870d46a52 | -10.39321 | -58.31137 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4a5d720-bb74-390d-b91e-8b436836c569 | -13.43743 | -43.81778 | 2026-09-17 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 26f9f51d-2fd9-345d-b140-cc52833c8e94 | -12.10571 | -57.1952 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5a53250-9d67-3bf4-aafd-629135c4580b | -12.11606 | -57.18948 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1875c7e4-c386-3486-9655-532adcc9483e | -10.27705 | -60.53765 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86c9b6f3-0518-3dc2-b526-0ea0301f0fa4 | -12.41682 | -50.81897 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67238ff1-502c-3dc9-8d1e-c40fc979f8c9 | -12.42564 | -50.82022 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7ef4e2c1-5456-348b-bb84-ffa8bd1ba5ab | -8.91711 | -62.39974 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eacf597-8eb8-3c33-83ce-dfbf0959cb08 | -10.79145 | -46.19077 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d254408-4b55-304b-ab13-e11060d19544 | -12.11273 | -57.18893 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3943ef2f-c18e-3e2b-a3bf-f284b6ce1cff | -12.45415 | -50.77537 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8452468c-cfdb-3a02-84d3-68179d02f61b | -12.44977 | -50.84131 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4107a3b4-7a08-38a3-96f6-789facbb7b46 | -12.45563 | -50.79784 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 204020d3-ac6d-36aa-b49b-46b28d753af2 | -11.88934 | -43.82535 | 2026-09-17 05:18:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 848f1e77-46ec-301b-8e49-d430052b0328 | -9.40645 | -62.71637 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d06d178f-ad71-368a-9855-b990537fb250 | -12.46358 | -50.83884 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec20150f-ec32-3dba-a50e-86161a3284ec | -13.58139 | -45.47609 | 2026-09-17 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f95b64c5-347f-330e-af34-beecfe2f87aa | -9.10122 | -60.97987 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 021e2fca-141b-310b-bbfe-ebc06ef164a3 | -9.51464 | -61.02499 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1257b189-6356-3117-a984-5bc1db23c214 | -12.43563 | -50.81277 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 961d89a4-02b5-3493-aa6a-45db40f5f646 | -12.32334 | -47.9586 | 2026-09-17 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c67f7e5-98a3-3f5f-b0ae-fea12d0b23d3 | -11.56465 | -46.88165 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96723491-57bd-3c1e-8cdf-0b1726c78008 | -12.43063 | -50.8165 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e759996-a336-33af-8b6f-6aba7586f005 | -12.43946 | -50.81775 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 7b3a5b52-f9ff-3f36-a9fa-f1778b076af5 | -12.43655 | -50.83945 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| afc59fda-77c5-333a-91ab-6cf3b9e1755e | -12.43888 | -50.82209 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b53a4295-494e-3114-b807-8ec14ff2a390 | -12.43179 | -50.8078 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b976f268-0eb3-396d-993b-98626bad1629 | -14.22482 | -48.50941 | 2026-09-17 05:18:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6504dc04-4dac-3d04-a0fa-646e4b4b9090 | -13.58318 | -45.47134 | 2026-09-17 05:18:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fa19ae0-7645-33ff-8be1-5aee16147bdf | -10.24141 | -54.26437 | 2026-09-17 05:18:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22f0145c-82b3-3c9f-97b5-a1379d5116bd | -12.45474 | -50.77099 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db78a97a-752f-3ad5-8e06-ea0a5d112da2 | -10.57802 | -57.69017 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7c9881a-8d78-36b3-b4f8-1ebe1ff5d023 | -11.80871 | -58.18066 | 2026-09-17 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cf280c0e-c442-301c-92d9-7db1a2c0b1af | -12.45125 | -50.86357 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0466fe82-dba5-3356-97f3-c80ce01f630b | -13.74986 | -48.7941 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8740dc6-6712-3fa1-9942-373f1c5558c9 | -11.31937 | -46.77675 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11e1c7d8-0a23-3ae8-a257-5bf617597533 | -11.16713 | -42.79404 | 2026-09-17 05:18:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 92352188-c42c-3bb1-ba5a-1a912b3e7257 | -12.86499 | -60.02647 | 2026-09-17 05:18:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2abda96f-0313-31b6-bd53-af12c5d609c8 | -12.44712 | -50.82768 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ac785108-c66e-36ac-96e5-941e376ea7ef | -10.39501 | -58.30027 | 2026-09-17 05:18:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dbcb160-906c-3bfb-b0ab-0a427f29d3be | -9.09268 | -60.96101 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README69.md)
