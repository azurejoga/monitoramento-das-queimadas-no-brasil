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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bde5403-2300-3c62-8bae-32a60a0be0b9 | -3.5995 | -47.5142 | 2025-08-24 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 9c4c7925-facb-30ff-b7a5-74cf04bab18e | -8.7582 | -49.978 | 2025-08-24 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 4e88042e-8fde-308e-900a-ec4b39842f96 | -20.339 | -51.7062 | 2025-08-24 00:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 86.3 |
| afe0d9ac-a1cd-393a-bc89-4c764bddb88f | -10.6131 | -44.3051 | 2025-08-24 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| fe9c0f24-6563-3ca1-a772-317bf8ed91d2 | -8.6856 | -62.874 | 2025-08-24 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ccad16f0-8f31-32b8-ba55-3c801fc7ccf5 | -11.5239 | -51.9106 | 2025-08-24 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| dfd52dae-6ee7-3fb4-885a-93470e921b7f | -22.8253 | -53.9872 | 2025-08-24 00:10:00 | GOES-19 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| a886a698-3ab4-357b-afe5-0ed49dc5b1ad | -5.4365 | -60.1588 | 2025-08-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 6d443629-7300-3de8-ad43-da45d71e6676 | -9.0231 | -65.7169 | 2025-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 222.8 |
| 39859e4a-88d2-361a-9b27-e1c5500d9cfd | -5.4213 | -44.9939 | 2025-08-24 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 96a1fe20-ecff-3c9f-aa9a-fb13cd6a19f9 | -9.0232 | -65.6982 | 2025-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 159.7 |
| da9d8736-8059-3595-811c-aa966d225ad5 | -20.3599 | -51.68 | 2025-08-24 00:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 254.3 |
| 6b3842b5-bdc0-3b77-baa1-a95e1afd48f3 | -18.7575 | -45.0866 | 2025-08-24 00:10:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 42.5 |
| d935be68-098d-3df9-b24a-379caea4ce6c | -9.0046 | -65.6988 | 2025-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 83064926-c2d8-3518-8cab-b5841abd5d18 | -2.9279 | -53.7078 | 2025-08-24 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b9f5d8de-d049-3122-abdf-8521e99ac7e8 | -8.6314 | -62.63 | 2025-08-24 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ac779552-3beb-3335-8dba-7d461031dee2 | -9.0416 | -65.7163 | 2025-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 604ad023-68f6-35d2-94a9-8b7fbd72b9ae | -9.1998 | -60.793 | 2025-08-24 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| ff0b4934-49ae-3140-9074-11a5b17bf849 | -8.7591 | -46.7547 | 2025-08-24 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 161afe84-a2c8-33bb-acc4-34e5835f21e4 | -11.5429 | -51.9086 | 2025-08-24 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 02af532e-e5b3-3dcd-a2dc-3781127d0e10 | -17.4045 | -42.6186 | 2025-08-24 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 645d7acc-4a96-3f4e-b3de-e0128f0ee4f0 | -12.0055 | -61.0201 | 2025-08-24 00:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| c87056ac-e2dc-3eaf-9c3c-724ed5c00c95 | -17.3844 | -42.6235 | 2025-08-24 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b3c0e5aa-7e91-332e-babb-cb8b388a25bb | -14.7984 | -59.6145 | 2025-08-24 00:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 87c10868-4a8d-3fc5-aa06-ba00ad3dfd92 | -4.5568 | -43.2096 | 2025-08-24 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| e1f006b8-7a0e-3cd4-ae0d-e7491a72c141 | -10.6128 | -44.3284 | 2025-08-24 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| f1879648-e921-3949-b954-99496a101b4d | -14.8174 | -59.6326 | 2025-08-24 00:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9fb3cd3a-ba2c-3ca9-b6b9-c5d58e2d5d7b | -9.0246 | -65.3807 | 2025-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4f129200-c1a3-3931-b434-7e3bed1ded36 | -9.023 | -65.7355 | 2025-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 80cb7ac1-4f47-3ef2-bd0d-60fb9a0d367d | -4.5567 | -43.2329 | 2025-08-24 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8b9f54df-a32e-3240-971f-4b42496dabd2 | -5.4548 | -60.1773 | 2025-08-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 50a7e672-dece-3b01-8993-d19673fa6e75 | -8.9106 | -62.4289 | 2025-08-24 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7ea34d31-8a3e-3252-b0e6-16a5e5bcfc09 | -14.8178 | -59.5929 | 2025-08-24 00:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4a4ad2ed-241f-390b-aa29-30eb68997879 | -5.4547 | -60.1964 | 2025-08-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| dd8cb563-7d19-39d3-a63c-c793f100c1e3 | -5.4364 | -60.1779 | 2025-08-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 4aad3238-eab7-388f-a099-66e81e0248ab | -4.9421 | -55.8233 | 2025-08-24 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 5f3fe3ea-9be3-3430-b8e1-73d075552e0e | -17.6183 | -44.2738 | 2025-08-24 00:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7aa01c13-913b-322b-96f2-93970890ca1d | -22.1058 | -53.8165 | 2025-08-24 00:10:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 150.1 |
| 2e22b510-edd1-3cd0-8d92-dbc40ff8310b | -3.5994 | -47.5359 | 2025-08-24 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 20583daf-cc8c-33ae-97fc-cc6ed0e33169 | -11.5245 | -51.8685 | 2025-08-24 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ea5e0d24-004d-334e-8a55-478714969c96 | -8.7579 | -49.9993 | 2025-08-24 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 064599b7-064f-3802-bf16-54acb503e7f9 | -17.6176 | -44.298 | 2025-08-24 00:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 7b4231ab-dc7f-3cd1-95bb-f41b66ca8fc1 | -11.5236 | -51.9317 | 2025-08-24 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e064eb61-cd71-32e9-868f-19209c4d60ab | -14.8176 | -59.6128 | 2025-08-24 00:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| acbf89bb-1af3-31f3-94b0-80f9288c285e | -4.9605 | -55.8226 | 2025-08-24 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 357a84fa-933b-38d6-b7e4-04ac05588020 | -20.3594 | -51.7023 | 2025-08-24 00:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 14a5fb62-c5d6-3b61-8c23-49e4171e4d88 | -14.7984 | -59.6145 | 2025-08-24 00:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1b23b6cb-9cda-378d-8acb-cdfd20000b1a | -22.1058 | -53.8165 | 2025-08-24 00:20:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 104.0 |
| 3d78c736-8390-3cd5-869f-8c3b9ad81e4e | -11.5245 | -51.8685 | 2025-08-24 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 49cb673c-9063-3dfb-8522-b9be7bde4a4e | -9.0061 | -65.3813 | 2025-08-24 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 06f97489-2083-3f05-a3ac-a9924e66bf74 | -5.4365 | -60.1588 | 2025-08-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 493a7bf2-8fa8-3c3d-8cfc-318a2f5c260c | -9.1998 | -60.793 | 2025-08-24 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 13b60781-6dc5-3c07-896a-0de73b0e57d7 | -5.4213 | -44.9939 | 2025-08-24 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ccd0d98b-70e6-324a-a1ce-b39c032f653f | -5.4364 | -60.1779 | 2025-08-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.0 |
| fc8275de-3952-3635-b586-fdbbadea7d00 | -4.9421 | -55.8233 | 2025-08-24 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 97f8eda6-16f1-327b-b632-56bc080989e9 | -17.5975 | -44.3027 | 2025-08-24 00:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 19a1fd3f-b493-31d6-b097-3046c45aceb5 | -5.4181 | -60.1784 | 2025-08-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 272.7 |
| affad0e5-f503-384a-be2b-3c5c26a831e6 | -8.7582 | -49.978 | 2025-08-24 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 9aa9768a-f6c9-38bc-bacc-d80cb66a813d | -12.0055 | -61.0201 | 2025-08-24 00:20:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 094cfec7-f411-3e8d-9153-f83a790a7988 | -7.5534 | -63.8556 | 2025-08-24 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 318a8cc4-33d1-3c25-8fdd-9f513782b6b6 | -17.4045 | -42.6186 | 2025-08-24 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 529f2bc0-17a3-3262-92a4-6c7e107032c9 | -11.5426 | -51.9297 | 2025-08-24 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f5e5be55-cdcb-3adf-b659-3c58be79b035 | -5.4026 | -44.9952 | 2025-08-24 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 5ebfc46b-84ee-3a4a-9884-bf64210d8769 | -9.236 | -60.9256 | 2025-08-24 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a57c50cd-de14-360b-b1d8-78b1732028be | -8.9106 | -62.4289 | 2025-08-24 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5dd81cd7-74b6-3ca5-937a-1659435f00c7 | -17.6176 | -44.298 | 2025-08-24 00:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 91a48ad4-9540-333f-9bee-1b164fecb2c5 | -11.5239 | -51.9106 | 2025-08-24 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 615061e4-b6df-3a46-a7c2-7c32fb81b428 | -20.3701 | -46.7433 | 2025-08-24 00:20:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9a30efbc-e87a-3c09-8d70-cd280cc953e6 | -11.5429 | -51.9086 | 2025-08-24 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| b85bcf85-35a7-3f8b-8f64-53a7b8e07c07 | -20.3594 | -51.7023 | 2025-08-24 00:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 93e17053-17f3-39f9-9bd3-d30b9345b1f4 | -20.3599 | -51.68 | 2025-08-24 00:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 225.9 |
| a4becce5-5a9f-3771-9962-3d221b89f4dc | -8.6131 | -62.5929 | 2025-08-24 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 8c156fc0-2c7d-3b84-8b58-29ab8d9aadef | -14.8089 | -55.9678 | 2025-08-24 00:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| a4214587-e935-3251-aa54-5322b2b0d65c | -4.9605 | -55.8226 | 2025-08-24 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 2cfefce0-eca7-30ec-ae8c-6464afe8fd3e | -9.0246 | -65.3807 | 2025-08-24 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6110a045-6cbb-3d2d-993b-4bf4ae5aedfa | -3.5994 | -47.5359 | 2025-08-24 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| c4760ec4-b522-3f4d-93f8-82d1dc3b4ec4 | -11.9867 | -61.0214 | 2025-08-24 00:20:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c38d46ec-a789-3114-86f4-224768268372 | -5.4547 | -60.1964 | 2025-08-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| cdc82993-baea-3c14-ae94-be116a632bb9 | -11.5236 | -51.9317 | 2025-08-24 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| acb844c4-fe0e-304f-8347-69cf9fc55d60 | -20.3708 | -46.7195 | 2025-08-24 00:20:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 29d47eed-26d0-37c6-b070-23bd06bc0fdd | -16.797 | -51.3419 | 2025-08-24 00:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 8eff20e9-7ab1-32b1-bf24-eb03a08f104d | -16.7965 | -51.3637 | 2025-08-24 00:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 315c5665-9399-31c4-ab9a-97b17990a51e | -4.9606 | -55.8028 | 2025-08-24 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 3d493203-c104-3e13-a950-5333ecbca750 | -5.4548 | -60.1773 | 2025-08-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f61a9176-3baf-3d7f-8976-ae5b6077c358 | -8.7591 | -46.7547 | 2025-08-24 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 0c6536c7-c147-3dbb-a32c-a718ff687099 | -9.1441 | -60.7765 | 2025-08-24 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ea92ef2c-ad69-39fd-bbee-66edd63ecfe2 | -14.8176 | -59.6128 | 2025-08-24 00:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f920ac64-f37c-385d-bf44-6b4f2dbd44f4 | -18.7575 | -45.0866 | 2025-08-24 00:20:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 48.1 |
| e1a39ffa-26ea-36e7-b499-43d9cb2c0924 | -17.6183 | -44.2738 | 2025-08-24 00:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 74e6b7ed-a5a8-3c5e-a56e-e057ccc41e18 | -17.3844 | -42.6235 | 2025-08-24 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 6a509edb-08f3-303d-9507-413cc24e5b94 | -3.5083 | -47.212 | 2025-08-24 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9b0466bf-1157-3538-ab7f-67d6baf6c301 | -22.0851 | -53.8204 | 2025-08-24 00:20:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 170.3 |
| cdf8d7fc-a59c-37ad-86a0-70cafaed5606 | -14.8174 | -59.6326 | 2025-08-24 00:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 700d9e42-df83-333e-8183-7abde3173b8c | -14.8282 | -55.9657 | 2025-08-24 00:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 4af0a7f9-1455-3cfb-92b4-a1fa12ea0f2c | -5.4182 | -60.1593 | 2025-08-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 8b0a9093-9acd-3f59-aca1-1dd8feec544b | -10.6128 | -44.3284 | 2025-08-24 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7dfd5390-3f39-3ec6-b54b-8b3352e91d54 | -20.339 | -51.7062 | 2025-08-24 00:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 92.7 |
| da54a431-bc59-33dd-b1c6-52f3051db1cf | -3.5995 | -47.5142 | 2025-08-24 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 4f34077c-2a1d-36e6-b8f7-2d5e8d63a12c | -18.7569 | -45.1107 | 2025-08-24 00:20:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 43.8 |
| a965a96b-b390-3ac9-9d13-e4e6968d84ab | -8.6314 | -62.63 | 2025-08-24 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README3.md)
