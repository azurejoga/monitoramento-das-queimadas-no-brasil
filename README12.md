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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dbb1333-a373-3e6a-b67a-d2aa62a4399c | -13.05994 | -52.03548 | 2024-12-14 05:20:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed61929c-431d-3330-b3a4-6e67e1207c0d | -11.83374 | -57.82138 | 2024-12-14 05:20:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 52d06f55-621f-3841-b9bf-88590a309f3e | -14.10629 | -59.93712 | 2024-12-14 05:20:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d50d7e7f-d87b-3f94-8bd0-427538f9879f | -12.56587 | -57.76001 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b561e62c-9d93-357e-8b42-11030bcf59d8 | -13.66185 | -55.2495 | 2024-12-14 05:20:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2067320-f32b-35a9-96d1-0d0443c7424d | -12.56173 | -57.76356 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e504704f-f9e3-3986-9b39-cc36087339e4 | -13.54915 | -55.38139 | 2024-12-14 05:20:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7dbefeb-9bc3-3483-b097-3fa9a042d8ad | -13.06253 | -52.03713 | 2024-12-14 05:20:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1609be9-3c17-34a2-aa81-cc59a8ebf45c | -9.15644 | -62.50662 | 2024-12-14 05:20:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1237150-13de-3d30-9382-f396617e2d07 | -12.54752 | -57.71117 | 2024-12-14 05:20:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8f67604a-709e-3ad8-92de-09433604ef07 | 3.22062 | -61.19601 | 2024-12-14 05:40:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6eaa9c78-7389-3e03-a4dd-a81e2d7153b3 | -1.72288 | -52.55575 | 2024-12-14 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f35b090b-e4d7-3163-94c0-94dcd41b7b20 | 2.74236 | -60.37943 | 2024-12-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 797b77e6-cd24-3511-8c9c-34971b0ac7e5 | -3.18315 | -52.88282 | 2024-12-14 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68f59807-d5b8-3ca4-8168-1bdc0200bce1 | -1.74433 | -52.02239 | 2024-12-14 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a69c3bf3-52f2-3400-a06e-f3a71f504528 | -4.0868 | -53.96221 | 2024-12-14 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b617d989-d005-3247-8bad-3df8d767d8a7 | 2.52704 | -60.64836 | 2024-12-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b5111ed-2370-3bb0-a416-8061c33c6bcb | -1.74803 | -52.81566 | 2024-12-14 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ee34290-9fa4-3b35-9c56-4e71a519df9c | 2.74059 | -60.37833 | 2024-12-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88ae6e82-9f7a-3e63-947f-5a2f8c0472be | -3.96586 | -53.8431 | 2024-12-14 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13a851d7-7e2e-382e-89d0-962fbef7b6eb | 2.74528 | -60.37481 | 2024-12-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e93eab7c-a87d-39eb-bd27-bb4751f4b9b8 | 3.22691 | -61.1912 | 2024-12-14 05:40:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b45500cf-04bf-302a-870a-280d0fe7fcf6 | -1.74349 | -52.02795 | 2024-12-14 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0446c7a6-3d87-36f2-9971-84478263ae63 | -1.72212 | -52.56085 | 2024-12-14 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6bd2f247-2ef7-35a9-bddc-f0d329ceae9d | -1.715 | -52.56497 | 2024-12-14 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db2ac401-6a7a-39f9-9374-21b27e8fc447 | 2.74123 | -60.38238 | 2024-12-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dee89915-b7f2-392f-a47c-ae3788ad09cd | 2.6239 | -60.41673 | 2024-12-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 89f1ffb7-06b3-3bdc-9587-cfd29e1c0108 | -1.72121 | -52.5574 | 2024-12-14 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7d063b4b-d63e-3bb4-a7e1-5708aee057ba | 3.22406 | -61.19548 | 2024-12-14 05:40:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d4c8083-ca69-3bcc-91f4-e2cdf4029f58 | -9.15596 | -62.50655 | 2024-12-14 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c32107e-8e56-3e25-b36e-204c4bec24a5 | -9.15533 | -62.51092 | 2024-12-14 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12ccf7b7-607f-3ad2-a38c-ad0943b08aab | -12.55273 | -57.7107 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2b6c1f12-a3f8-374a-8343-b7c7e1fa2832 | -12.56845 | -57.75634 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4612ba34-b05e-35a6-85e3-5df45e5f965d | -12.56317 | -57.75571 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 630ab766-aaa7-3dcf-961b-47f8a1b7db1f | -12.78631 | -61.5034 | 2024-12-14 05:44:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06b9e3d3-89e7-3153-bc7c-bfaec78a2b97 | -12.56807 | -57.75531 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 426a0be2-6bce-3d24-bb6f-e37aa1b5d877 | -12.55315 | -57.70737 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6cb3b7aa-41bc-3829-853d-2aa9023b74dd | -11.83248 | -57.81684 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1285d08-dd7b-3c4c-9b80-820fbaa2d08b | -16.10732 | -60.07095 | 2024-12-14 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e58371c-368a-3861-a35b-807a31c02dba | -16.07353 | -60.07167 | 2024-12-14 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35fba9a8-39dd-3fbe-bc9c-de86fe2f09ed | -12.54786 | -57.70662 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 558ab233-3755-3484-a5cd-2b86c00f4940 | -12.7894 | -61.51141 | 2024-12-14 05:44:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eae1460-8ffc-35f6-b50a-bea9a9c6ff0e | -12.56887 | -57.75302 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e848b879-f2da-36ba-a988-595ae59b4d8b | -9.65066 | -66.56274 | 2024-12-14 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e197061b-3c4a-33ca-a597-0c08f3889340 | -9.51269 | -65.59261 | 2024-12-14 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 925ecf5b-34aa-31d6-b154-e092c240aac1 | -11.83247 | -57.82069 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 807f8eef-569b-3fdd-8609-c1372e50a850 | -11.83286 | -57.81754 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41898931-b4d2-3db3-b950-ac65503b6199 | -12.55886 | -57.70474 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9773964a-50a2-33c7-9d4c-5dd1537bc1b0 | -9.65399 | -66.56328 | 2024-12-14 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a8caf38-0b55-3c81-a238-c85069dd9624 | -12.7858 | -61.50712 | 2024-12-14 05:44:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9705e281-baf7-3673-823b-422929141ff7 | -9.65343 | -66.5668 | 2024-12-14 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e0f0ecc-57ae-39bb-b153-12a94bf49ae8 | -16.10668 | -60.07606 | 2024-12-14 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecc73198-7b9c-3ad3-95ed-e88f0edaf52c | -12.53604 | -57.71519 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20733730-cf56-3d31-b588-81febb700188 | -12.55357 | -57.70403 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6e600b9-a13a-3c74-b435-eb9b4a7682cd | -9.6501 | -66.56627 | 2024-12-14 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdaad4d5-75f4-3976-80f7-8e9c1b3ed737 | -12.56846 | -57.752 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e693dcb3-bf40-38aa-82ee-3f7eacbd4bc6 | -11.83207 | -57.82 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 409a3df0-d7eb-3ec6-bfcd-1e66f3468b67 | -16.07765 | -60.07737 | 2024-12-14 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40eb7632-bab2-3f11-98b0-42cb6bb49638 | -11.82687 | -57.81928 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2543f81b-fce6-3c4c-94c9-04c34efe831a | -12.54134 | -57.71582 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1375193-a9e2-3713-9645-d78c7c76c94a | -12.78991 | -61.5077 | 2024-12-14 05:44:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 708ac503-eca1-3aee-872e-cc516267640e | -12.55801 | -57.71148 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8711fde5-a9cc-3754-9b25-bf21619a5508 | -12.56275 | -57.75902 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 495930cc-6cf5-3f76-b1d5-454299795950 | -11.83325 | -57.81438 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e6265bf-1ff0-304a-bf46-a16b37090ff2 | -11.82646 | -57.82244 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbee2f8d-6a88-36f9-9735-cf5afe8fc11d | -11.82728 | -57.81998 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ffe8829-6ebf-34c0-8bee-dabdb20fd67b | -16.07828 | -60.07224 | 2024-12-14 05:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b2f5898-8b53-3354-a9c3-577044b35700 | -12.55843 | -57.70811 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8dbdbacb-e983-3965-ba09-ac3417ad0311 | -12.55398 | -57.70074 | 2024-12-14 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 573e7723-a88c-3490-955f-d943ec399065 | -12.79042 | -61.50397 | 2024-12-14 05:44:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81e22a41-3f99-3234-877f-f165fbd07952 | -11.82767 | -57.81679 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 541f2efb-0850-36ab-9f1f-dceae318af46 | -11.82729 | -57.8161 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24203645-8b88-3b93-aa95-10b831498218 | -11.82806 | -57.81359 | 2024-12-14 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 508550b5-2580-3fa8-89b7-d8afb84aad47 | -1.71499 | -52.55958 | 2024-12-14 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 41ef40b8-6088-3a32-adbd-037850b1aafe | -1.71636 | -52.55038 | 2024-12-14 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b57ed606-5304-394f-9dd8-c47a82f22cb9 | -2.78655 | -53.22883 | 2024-12-14 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 07f824f0-58e5-36f0-b782-68be1ab6dc38 | -1.72393 | -52.55816 | 2024-12-14 05:48:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4d7ac152-f51f-315b-961e-5dcca8f758b4 | -12.55091 | -57.7026 | 2024-12-14 05:52:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| ee188285-c4b3-3c2f-8724-928b38d41005 | -14.69367 | -52.62465 | 2024-12-14 05:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 624c7a3f-838a-3231-a428-01369d252f17 | -11.82438 | -57.81973 | 2024-12-14 05:52:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 198cd718-26a0-3df0-a2ef-4e9c593cc5a5 | -12.54517 | -57.70836 | 2024-12-14 05:52:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b846539f-456b-39b2-bb43-36553bb6d642 | -12.54869 | -57.71577 | 2024-12-14 05:52:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 1a13e57b-b1c2-34ac-a920-f4d6cc61c08c | -14.69228 | -52.63428 | 2024-12-14 05:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 46ebec99-034d-3da1-80c0-7b11344f7762 | -12.56318 | -57.75893 | 2024-12-14 05:52:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 0fde4e03-bb65-36e8-b58e-a27bd856baf2 | -12.55574 | -57.71009 | 2024-12-14 05:52:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| a95fa993-f040-3501-8d8c-5a93be440ba6 | 4.83119 | -60.22146 | 2024-12-14 06:01:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 684ddccf-b22a-345b-9c0d-26c3fa23465a | 4.8259 | -60.22165 | 2024-12-14 06:01:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d08d795-ea7e-37c0-a182-00856dfcdccb | 4.83011 | -60.22227 | 2024-12-14 06:01:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68abb795-22c3-3d1e-ade5-1593981a3be7 | -9.64942 | -66.56554 | 2024-12-14 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f9f154a-c93b-3121-a0c4-02d582eb9c99 | -9.65361 | -66.56621 | 2024-12-14 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60dcddfc-bf0f-35a8-8476-c0914d539590 | -4.1696 | -42.4346 | 2024-12-14 06:50:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 1abcfdf0-13fa-39c3-b36d-f1bf85b708d5 | -4.1696 | -42.4346 | 2024-12-14 07:10:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 7af3ded2-64ce-3450-88d1-5530ded6fa44 | -4.1696 | -42.4346 | 2024-12-14 07:20:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 35ff7f7e-6c01-364c-80a6-51451d471d4c | -4.1696 | -42.4346 | 2024-12-14 07:30:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 8fd4527d-4813-320f-888b-4bd7b9004e59 | -4.1696 | -42.4346 | 2024-12-14 07:40:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |


