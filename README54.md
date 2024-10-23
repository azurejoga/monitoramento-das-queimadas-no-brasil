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
| 5c96c4d7-78a5-36ef-8c3c-ecde69bc537e | -3.58478 | -53.78294 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4af4428-965e-39dd-bd96-60669e689276 | -3.58439 | -53.78468 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6ff15f2-eab5-3e1d-8e78-ece65ca636d5 | -3.5809 | -53.78221 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 288850fd-4809-3772-a2b7-7602e87d0bea | -3.54365 | -54.7394 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 888003b4-c3d7-38d2-b20f-a3b4c170abd3 | -3.54298 | -54.7437 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 030b878a-dffd-3e50-98a7-c565738d9e39 | -3.53996 | -54.73886 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e2e01370-5cc7-3863-b07d-00911d8076b9 | -3.53929 | -54.74318 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b8fb0eb-011b-3874-85a8-bfad445dce39 | -3.53627 | -54.73833 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1e02a16-5bb8-35e1-ba87-c89a0850fed3 | -3.48836 | -54.15226 | 2024-10-23 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1380767d-4de3-31fc-8215-5c149b84b156 | -4.31005 | -54.75703 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a0ffe7-a0a6-31f5-8453-95d3eedeed62 | -4.30863 | -54.75836 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bda76781-abcd-311b-953a-d9799b494db3 | -4.12971 | -54.89722 | 2024-10-23 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2163080-9a38-309a-80f1-29b80d5ca2fc | -4.11543 | -54.41298 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4c18b42-ecc2-381f-97bc-af9aaa54f24f | -3.90186 | -54.14315 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f2fbed1-625a-3edf-8af8-ce12a8159442 | -3.89803 | -54.14254 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8dcb2fb3-2d18-3639-91c9-02e7a8d1a1b1 | -3.89037 | -54.14136 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bcf2ecc-3dcb-38c6-ab1d-564bf8d12bf3 | -3.88966 | -54.14605 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06cb6127-c7d6-301e-951a-26cc1cbf74be | -3.88654 | -54.14077 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc5c8824-e5c7-3939-8036-fa148c05b501 | -3.88583 | -54.14547 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8686a9f4-bb6a-3fce-9939-d576d889fc83 | -3.84922 | -54.76348 | 2024-10-23 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b99737be-c7c0-3988-a570-fc4a31fe9683 | -3.84856 | -54.76775 | 2024-10-23 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eda5d76-0ec9-3ecb-9c88-3d592caf0fd7 | -3.79799 | -54.44452 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bf03e0e-c08c-3439-b974-598532a399ad | -3.78447 | -54.38224 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33b5e1e4-b4dd-36f6-9602-4ad011ed48cf | -3.67735 | -54.55205 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2fa0a542-95b2-3c78-a6c3-93b0772e2179 | -3.6623 | -54.4262 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a2b89a96-c390-3bb2-ad0d-275e8aac1808 | -3.65038 | -54.79802 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d705ce9d-8594-37cc-8344-64bf65721b1b | -3.64928 | -54.79599 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7021d7e8-e0e8-31bf-8132-10954d900eb3 | -3.64735 | -54.79329 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22f1087a-459d-3b8b-8105-fe9af3f4a97d | -3.64669 | -54.79753 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9045d65-e921-30a1-97b4-30baedc95611 | -3.64367 | -54.79274 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14999b40-5a15-300c-86c0-461e0d6f2b2d | -3.63833 | -54.68116 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43581e53-93a1-381f-b1c3-bd49552e8f04 | -3.63765 | -54.68556 | 2024-10-23 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6206b5b4-caa6-3803-baec-34c65e79a8fa | -10.79651 | -55.48153 | 2024-10-23 05:16:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ece808f-2474-3e0c-a598-22dbbf641af9 | -10.66377 | -56.64211 | 2024-10-23 05:16:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa1aa7b-441c-3351-bc28-101a463edee9 | -10.66314 | -56.64635 | 2024-10-23 05:16:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c35f7a8d-81a5-353f-8907-9b8aa0411a76 | -10.48379 | -55.60213 | 2024-10-23 05:16:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24c49f84-8540-3109-a283-7b82512027c3 | -3.56632 | -55.51426 | 2024-10-23 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 270f8e17-306a-34a1-88d8-26bf7882f6c2 | -3.56571 | -55.51824 | 2024-10-23 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2f5db9c-df3f-3b23-8d95-13ca2eb26237 | -4.87888 | -55.83697 | 2024-10-23 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bf7b77c-4a57-363d-950c-08d11a7f1ae9 | -4.11903 | -55.57695 | 2024-10-23 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4c13a93-93df-3654-864f-1baba7b1a637 | -3.90463 | -55.39872 | 2024-10-23 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e88a2a3e-3b2e-33d7-90df-c379cc2a3417 | -3.90105 | -55.39815 | 2024-10-23 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b614ee29-e2da-3e39-8d58-a4f90146d555 | -3.86116 | -55.58892 | 2024-10-23 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c0fb8f-5e8d-33ba-b5b9-c673a99be293 | -9.35652 | -57.60265 | 2024-10-23 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92fd73d9-52a9-3790-a01c-ae25a294d9d6 | -9.35309 | -57.60211 | 2024-10-23 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a061b0-b998-3f43-a3b5-26f1a581ba04 | -9.35251 | -57.60588 | 2024-10-23 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29d2be23-2db2-3d51-927b-932bbebf55d0 | -9.22368 | -57.65179 | 2024-10-23 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d47dd2ee-d589-3f26-b1a6-97a0287fcfd9 | -9.22311 | -57.65553 | 2024-10-23 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b85a7bd-78ba-3959-b52c-335f81b6abc0 | -10.58471 | -57.80033 | 2024-10-23 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 151bf7d2-988a-3ca9-aa33-806410c0cf90 | -10.48473 | -58.02662 | 2024-10-23 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35f8df02-4acf-3cd3-a129-c5946ac3c291 | -10.46137 | -57.46817 | 2024-10-23 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cd233fc-7c3d-3ccb-b262-b9954dd04262 | -10.45788 | -57.46763 | 2024-10-23 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3425c759-9e73-30fc-8835-3575d9319772 | -10.27202 | -57.70315 | 2024-10-23 05:16:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6592b971-f1ae-3f84-b02f-eae95bfd5308 | -10.18397 | -57.91716 | 2024-10-23 05:16:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a654976c-cec4-3c83-bd0c-a7361758227d | -10.43235 | -58.82295 | 2024-10-23 05:16:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74817db0-aa48-3455-b118-05a637964aba | -10.4318 | -58.82653 | 2024-10-23 05:16:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c3f2e54-ede7-3134-81df-9184c078f542 | -10.43125 | -58.8301 | 2024-10-23 05:16:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b1cb9dd-e25b-3fa3-a426-7683f105488f | -10.429 | -58.82241 | 2024-10-23 05:16:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb696c40-26ca-3714-98cd-e6e443e28de1 | -10.42845 | -58.826 | 2024-10-23 05:16:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9a4c2b4-44e4-355d-b03e-79b124bdf2a2 | -10.4279 | -58.82957 | 2024-10-23 05:16:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 927574ad-da0a-3f46-ad94-33b99c88d170 | -10.20632 | -59.15021 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70cca768-75b4-31e2-9cfa-c208b59fc501 | -10.20577 | -59.15374 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6407c4fd-cab3-3842-8c01-398f9356216d | -9.97765 | -58.78838 | 2024-10-23 05:16:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e5a7892-60a0-3a4c-a2fb-cac1a13cf808 | -9.73972 | -59.32114 | 2024-10-23 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30fb1b72-ebfe-304f-89a9-ef711e281971 | -9.56547 | -58.9196 | 2024-10-23 05:16:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3735111-0050-3438-a8a1-26588feb2ca9 | -9.56493 | -58.92312 | 2024-10-23 05:16:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22b0ff64-0e7d-31c2-a9ac-f5984d99b7ea | -9.56159 | -58.92259 | 2024-10-23 05:16:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a8c86b4-0af5-3507-b77a-a2e3f90784e8 | -10.13235 | -58.99778 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0b4215b-e22c-3c3c-a51c-abf3e395f38d | -10.1318 | -59.00132 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf307e11-0a86-38f2-a8c1-53f600eed255 | -10.05907 | -59.3577 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4028f6c1-a8d6-3d3a-9d7c-d5e277518665 | -6.5032 | -60.02116 | 2024-10-23 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9a32868-9e84-3a14-9604-7ccdc47ad796 | -6.49984 | -60.02063 | 2024-10-23 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 175462b0-fc92-3bd8-9cca-4963fe4bbb47 | -9.98532 | -59.99934 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66f0ac61-bcd3-31a9-a3ef-dc01537188a2 | -9.982 | -59.99881 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d76827d2-19b2-3cd1-ae09-8f9c8be2f4a5 | -9.98145 | -60.00231 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f234ae6f-274c-3171-98ce-e8d0948b7373 | -9.97978 | -60.01284 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1af40866-7d77-3a27-b8f6-44bb165528ae | -9.97867 | -59.99827 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecaf5c95-73df-3fdc-9654-f95902f62257 | -9.97812 | -60.00178 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f87f0349-f7b6-3434-9284-1ae85a331912 | -9.97535 | -59.99773 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47de5c0e-93d5-3737-bc28-51741ca3ec6a | -9.97258 | -59.99369 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0054063-79da-3492-8b56-36f94c6c5302 | -9.97203 | -59.9972 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 568bbfb4-f877-3cd4-8e43-89d53cded72e | -9.94932 | -59.8606 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 379bb9b5-f5b7-3d34-8c26-2dae528c449a | -9.94655 | -59.85657 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9df9f7b3-3253-300a-94e5-6b0799b2fc6e | -9.946 | -59.86007 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb28e4a0-ee7f-34eb-a8d6-9b004e5e57c8 | -9.94544 | -59.86356 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 519df074-94d9-35ee-a8c7-61d6feaec4a8 | -9.8723 | -59.98484 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53fca175-d885-33f6-a9d4-c9dcbaec30ec | -9.87174 | -59.98836 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 178b0399-9dae-353a-9d52-46b60059d212 | -9.86897 | -59.98431 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f917ba1-054a-3d8c-a8ce-fa6a6ebad97f | -9.86842 | -59.98782 | 2024-10-23 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 413cba14-5dcf-35f6-8208-c12e46b55dbe | -9.42042 | -61.08965 | 2024-10-23 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82b927d3-96fb-348b-8116-3c5bec700d5a | -2.95556 | -60.01404 | 2024-10-23 05:16:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75f00670-d20d-3ced-9703-2ede9e921a7a | -7.82338 | -61.69349 | 2024-10-23 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48f233ff-bd6a-31f4-8d21-122cab60654d | -9.18688 | -62.03331 | 2024-10-23 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee61a0e3-ac7e-3601-98d3-4b3c07ea5db5 | -9.18401 | -62.02878 | 2024-10-23 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28d14ff5-74e0-39a5-9ea5-776b1ba79397 | -9.18336 | -62.03273 | 2024-10-23 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53f4a64f-f31d-3bf8-aad0-d73290f7532d | -6.83488 | -63.07528 | 2024-10-23 05:16:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6a5f087-cf78-355f-88a9-e8b9219a9529 | -7.89329 | -63.71907 | 2024-10-23 05:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97380628-8195-3c1e-9179-96007987c55f | -5.62272 | -44.83216 | 2024-10-23 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e0c6410-2951-3d64-a3f4-6bb0e81ea9b8 | -5.61553 | -44.83104 | 2024-10-23 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5597209-8c11-3240-8c00-e9097ad81668 | -5.58419 | -44.8801 | 2024-10-23 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README55.md)
