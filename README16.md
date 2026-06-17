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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 981bc9a5-d4d2-317b-bdea-a8eee1e373e0 | -13.60219 | -56.59891 | 2026-06-17 05:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d1dbc0a-4922-31e1-92ef-be438428162b | -12.7663 | -59.00827 | 2026-06-17 05:42:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66fc385a-aa31-39e0-adf5-1acad95bc7ae | -14.09654 | -59.45785 | 2026-06-17 05:42:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4a0703c-1794-3935-af6e-371b5c20a9ff | -14.0933 | -59.45223 | 2026-06-17 05:42:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f9f48af-7f12-33d0-bc05-12f3ecda94e8 | -15.06953 | -55.81339 | 2026-06-17 05:42:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea31a9dc-ab7a-309b-9fbc-b6eca31c204d | -13.94387 | -53.56577 | 2026-06-17 05:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5042c0d8-a74a-3422-b66d-b26f95775131 | -12.43054 | -58.40232 | 2026-06-17 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 063feec4-8e57-37a6-9bd4-2ea1fc0cac66 | -12.15372 | -63.04168 | 2026-06-17 05:42:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 502369cb-d660-3f19-8878-e4d137ffb00c | -13.94339 | -53.56999 | 2026-06-17 05:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebea4757-438a-34ea-b83c-e002b47cd431 | -12.77028 | -59.00886 | 2026-06-17 05:42:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cec9cfce-411e-393f-ba8c-4665d673c867 | -14.09583 | -59.46291 | 2026-06-17 05:42:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b321772-a07f-39a1-a6be-57ef70e1d452 | -12.15316 | -63.04523 | 2026-06-17 05:42:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e2a7409-d6a1-3730-81ff-b27716a54fcf | -12.43002 | -58.40602 | 2026-06-17 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b3d1c75-b89f-3d52-b2ca-1e62c1268af7 | -12.14982 | -63.04471 | 2026-06-17 05:42:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0877fa91-2249-3ad8-bd6c-ae71f5143b7b | -15.06913 | -55.8167 | 2026-06-17 05:42:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f2e9067-392f-3ef5-af9f-e07e9b32b5ce | -12.8354 | -44.3657 | 2026-06-17 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| f0b590e4-f3dd-33ac-81b0-cc63fd35bb83 | -12.8548 | -44.3625 | 2026-06-17 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 37ca0abe-4b41-3623-ac0c-083519a6da85 | -12.1952 | -52.7821 | 2026-06-17 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 182.2 |
| 7d348c35-8492-33fd-b8e5-43f9311c3c30 | -12.214 | -52.801 | 2026-06-17 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 314.9 |
| 4947a1e3-ab05-33dc-ae72-d54a320575cb | -12.2143 | -52.7801 | 2026-06-17 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 411.6 |
| 8bc0c1d9-9ec5-3635-b5d2-15d27fafc79d | -12.233 | -52.799 | 2026-06-17 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 69d1a6b1-2edd-3528-9c9d-d49ecf99f812 | -12.8354 | -44.3657 | 2026-06-17 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 9be9e7b5-e27d-372c-8e1e-05827e04866f | -12.8548 | -44.3625 | 2026-06-17 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 4c966102-ea35-3d51-a9e6-97ef842dc859 | -12.2333 | -52.778 | 2026-06-17 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8a14efd4-53bf-36d2-a27d-98162ee6a9be | -12.1949 | -52.803 | 2026-06-17 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| e13e0d30-1eea-3170-9cfc-50aed7525996 | -12.2143 | -52.7801 | 2026-06-17 06:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 174.7 |
| 79d039f2-0dd8-3f2b-be38-1fe542b1f864 | -12.2333 | -52.778 | 2026-06-17 06:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 772679d3-f838-3809-b780-5dd5ff4880d1 | -12.8548 | -44.3625 | 2026-06-17 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| fc01acd1-2244-3599-9e63-71b077c1ae85 | -12.8354 | -44.3657 | 2026-06-17 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| e92d1ab5-0223-34d0-8551-1ee895485032 | -12.1952 | -52.7821 | 2026-06-17 06:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| ff9da98b-9622-366e-b8f5-f4ddba3494d2 | -12.1949 | -52.803 | 2026-06-17 06:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 480a92e6-057c-36bf-8ac4-3fde42da9581 | -12.214 | -52.801 | 2026-06-17 06:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| a9e567df-06c5-32e6-b080-f9bd0e29c79a | -12.1949 | -52.803 | 2026-06-17 06:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 59ce9040-52bb-39f8-ada8-55542b638628 | -12.2143 | -52.7801 | 2026-06-17 06:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| bea64c6f-ab35-3da6-8f23-a34f412b67d8 | -12.2333 | -52.778 | 2026-06-17 06:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 992f0be1-d2e9-3e55-82cf-bb754b866607 | -12.1952 | -52.7821 | 2026-06-17 06:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 87b02ee5-a8c4-3e42-837b-a32272aa9eb1 | -12.214 | -52.801 | 2026-06-17 06:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| bc6347d9-5af2-3ba7-b195-053583114823 | -12.8548 | -44.3625 | 2026-06-17 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 36be0040-e71c-3522-943c-ec583448e853 | -12.8548 | -44.3625 | 2026-06-17 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e89b2cc9-23a6-3534-a0ce-7e74439e6561 | -3.508 | -48.02853 | 2026-06-17 06:46:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d0095668-b82d-3161-be39-a042887d000b | -5.79268 | -45.08692 | 2026-06-17 06:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7d0b92c9-7321-3d48-b293-3fee88dbf210 | -4.34977 | -47.75583 | 2026-06-17 06:46:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a1422982-59bf-3ed9-a957-fdab81e8009f | -5.79949 | -45.07742 | 2026-06-17 06:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 577ca5ef-a2b0-3053-90f2-631d87e53c69 | -3.50651 | -48.03854 | 2026-06-17 06:46:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8d27bbf6-23b9-3ec0-96e2-c6efca952c15 | -5.79514 | -45.06973 | 2026-06-17 06:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 16e9db65-84e7-3a18-8afc-512649d8fdcc | -10.12231 | -52.17692 | 2026-06-17 06:48:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6374e60f-aee0-3e62-b69e-96492225680f | -12.23164 | -52.78016 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08a23d92-0428-303d-98c0-dda93a20022c | -12.21403 | -52.77742 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 0c674182-b9ae-343c-a959-de7763577433 | -12.91405 | -54.22242 | 2026-06-17 06:48:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c2dfe126-2a2c-3159-bb3d-412282e46877 | -12.19641 | -52.77468 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 6af60081-4810-3e24-9fff-a3c86e7d2bfa | -11.53902 | -52.77668 | 2026-06-17 06:48:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 0d2d2fc5-9472-3a12-a1cc-05813b3b1c84 | -12.23026 | -52.78916 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 93ab8ab7-c5e0-36ff-8ca3-d68bee4d8c5b | -8.98375 | -46.99192 | 2026-06-17 06:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e8299c8e-a0fb-3b00-8ad4-e03001de181e | -12.22145 | -52.78779 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| dff4feee-6183-37a5-bf1f-db974ad2dd64 | -10.98059 | -46.48084 | 2026-06-17 06:48:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| f6e7d0e1-84d5-30b9-a785-4f307ad58f0f | -11.54041 | -52.76767 | 2026-06-17 06:48:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bb8511cf-270d-36eb-9fe2-6a026938837c | -12.07424 | -54.60468 | 2026-06-17 06:48:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 05fc7e4b-7522-3ccf-ac9a-55601f86662d | -9.33305 | -45.4864 | 2026-06-17 06:48:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| c67cf9d4-3d75-3aa9-89bd-cc5bccc90d86 | -12.20246 | -52.79404 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 405.4 |
| d4d92900-c9fa-3bcd-9179-02eb2e6533d9 | -13.94217 | -53.56652 | 2026-06-17 06:48:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 975b022b-25bb-3e0e-91b2-a1e0295578f6 | -12.19503 | -52.78367 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a5366162-0da2-3a16-a014-61441148f729 | -8.97096 | -47.00435 | 2026-06-17 06:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 929b91bc-56dc-3904-ab9e-6b8fe85649bd | -12.18622 | -52.7823 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 8ddbfc62-b723-3f1b-a981-928653866777 | -12.84356 | -44.37539 | 2026-06-17 06:48:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 231849ab-2505-3c52-aaa9-b70b3dac6fc0 | -12.21127 | -52.79541 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| fd4002fa-b78f-3fe0-b710-a7d8e13bebe8 | -12.84586 | -44.38299 | 2026-06-17 06:48:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| bb3b6cab-1abb-37ba-b7a8-ab6f1fec0acb | -12.20384 | -52.78505 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1202.3 |
| 15f2ded6-49bb-3b72-908e-b8054b64d7a2 | -11.54924 | -52.76904 | 2026-06-17 06:48:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ec69ce49-d2e1-3c3a-bc67-795778cb50e1 | -12.22007 | -52.79679 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| aa4bde10-98bd-31c0-8549-58f676d56964 | -9.33547 | -45.46772 | 2026-06-17 06:48:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.4 |
| bf513ab3-a3db-3e5c-8822-02c7fbf8f32d | -8.98566 | -46.97803 | 2026-06-17 06:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e47956e3-bcad-3b95-abb6-a6fef113741b | -9.33232 | -45.46214 | 2026-06-17 06:48:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 16801ce7-011b-3f6a-9f3e-25b41b932f12 | -12.1876 | -52.77331 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8b53b0d4-11cb-3f44-9435-2a8f9cb64d9e | -12.19226 | -52.80167 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 865342e3-dbe8-3b56-874d-d2735da67a5f | -12.07591 | -54.59437 | 2026-06-17 06:48:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 55032eed-0f02-3f93-8d1d-55295738a14a | -12.19365 | -52.79267 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5baa399f-d110-31ac-aaa8-b4221d01feb4 | -10.98272 | -46.46467 | 2026-06-17 06:48:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| b9e29cc2-d4d1-334f-8df2-5e3580cff2d6 | -12.19779 | -52.76569 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 87918157-ec8b-33fe-8a46-2f36ca36eb9c | -12.84676 | -44.34935 | 2026-06-17 06:48:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 6193e1ce-c318-3bd2-ae7c-6771eb928d92 | -11.54785 | -52.77805 | 2026-06-17 06:48:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f19bd490-f81e-3133-ade5-d670b46821c6 | -12.22283 | -52.77879 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 51c6d9b9-fc3a-34bd-9984-38ce2acff7d4 | -12.08367 | -54.60617 | 2026-06-17 06:48:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 85d8ade9-265e-3911-9fee-a129d8d21a8b | -12.84887 | -44.35694 | 2026-06-17 06:48:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9ce33b35-b823-3b6a-b3b2-cfb31d79ea78 | -12.83452 | -44.35509 | 2026-06-17 06:48:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 0d99b6b7-4f82-34ac-a583-38ed55c04364 | -12.08198 | -54.61659 | 2026-06-17 06:48:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b900197a-a320-32b9-9839-078587971479 | -12.20522 | -52.77605 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 6b3e4af1-3cbc-3c13-ab84-c9caabbc55c3 | -12.21265 | -52.78642 | 2026-06-17 06:48:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 287.6 |
| d5e06bc6-e311-3ceb-94ad-33d566370459 | -9.32977 | -45.4808 | 2026-06-17 06:48:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| e4b59385-cee0-39f1-91a4-01c903ec017c | -18.98745 | -52.4566 | 2026-06-17 06:52:00 | AQUA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 86cb580d-7d02-3c63-bb01-6f93c0b439dc | -12.8354 | -44.3657 | 2026-06-17 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 55d465e4-586c-36af-9ed3-33656a57db9c | -12.8548 | -44.3625 | 2026-06-17 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| b1791c1b-087d-3e79-a357-5fb1cd718706 | -12.8354 | -44.3657 | 2026-06-17 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| b11569f4-2ce1-3a37-9b75-d556f838af3d | -12.8548 | -44.3625 | 2026-06-17 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 2616a945-e889-378c-9408-d927f68da9dd | -12.214 | -52.801 | 2026-06-17 07:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 346.2 |
| 7a72a42c-fa20-363d-9a26-bba0e9c190dc | -12.2143 | -52.7801 | 2026-06-17 07:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 638.4 |
| edeaede1-7c5a-39bc-bac0-683ce6589291 | -12.1952 | -52.7821 | 2026-06-17 07:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 354.8 |
| 5b0f5f7c-ef04-39fd-833a-74f79324db09 | -12.2333 | -52.778 | 2026-06-17 07:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ca7c5207-9291-3106-a981-4e29b490952e | -12.1949 | -52.803 | 2026-06-17 07:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 164931b9-40fa-3c1a-8a0c-e5bd2d2c99f0 | -12.8354 | -44.3657 | 2026-06-17 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| ab5fd9e7-98c6-39a1-841e-591147a87ca5 | -10.978 | -46.4766 | 2026-06-17 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |


[Clique aqui para ver as próximas entradas](README17.md)
