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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c383b393-8a57-318f-bdfb-2e3008d8df64 | -6.65907 | -43.0507 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e6a996f-4597-3dbc-9207-11169ee8bd9d | -4.8651 | -37.45558 | 2025-07-26 04:02:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de2c22fe-7df2-3a65-826b-71bb740016a5 | -6.57165 | -41.49739 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b993b480-7ed2-3c01-85e8-82efba3f8bf5 | -7.243 | -43.07088 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e07b95ec-bab4-334e-951e-06097df728a4 | -7.24522 | -43.0797 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5d460403-b0bf-3962-86fe-91fee6cf85e6 | -6.21186 | -44.80611 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ee11b96-ffb8-3f85-a633-f159dc295b25 | -6.90406 | -44.21825 | 2025-07-26 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c4ffd56-bfd7-394c-8b57-df0397cddf6d | -6.56767 | -41.50049 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc40da17-a6d6-3b5e-8118-bcbd03d3ad57 | -7.23537 | -43.06266 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f89a9c39-db21-3c71-bfb8-8f17f8d0b0cb | -6.15444 | -42.60031 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f927dbaa-f30e-38e5-b9d6-f2427323399b | -6.90301 | -44.29649 | 2025-07-26 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fcd3916-934e-381c-9031-142c65e9ca16 | -6.15575 | -42.59228 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 033ff9d8-937b-3479-8761-783973b53440 | -6.9166 | -38.56303 | 2025-07-26 04:02:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 036d3e5b-eb9c-314c-a72a-8202de994f4b | -5.04115 | -44.46687 | 2025-07-26 04:02:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b74c22a-0f65-326c-9dd7-6451acaee6d9 | -2.82537 | -47.52575 | 2025-07-26 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 504ed6b9-b8e7-32e0-ae43-35768b153507 | -6.42642 | -41.16022 | 2025-07-26 04:02:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc934b17-caf8-363c-bc91-c38b6da73453 | -7.24659 | -43.07147 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 7e896648-0164-35e0-bee3-32fa8338ac03 | -4.30305 | -48.10372 | 2025-07-26 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 68a3ca5d-96cc-3607-a279-a8a5cfbf3b19 | -5.6711 | -51.36366 | 2025-07-26 04:02:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6260a4db-555c-3a25-b366-44995b054dc9 | -7.17619 | -43.49233 | 2025-07-26 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 36830e93-ffc5-3a14-8e27-aca0cb94e628 | -6.15865 | -42.59686 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1d1afbc8-bcc9-3d80-bfb0-d096ae9205e5 | -3.65936 | -48.44346 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cd6f3b5-f11a-3797-8896-e5c679ed8f6b | -5.80329 | -43.62587 | 2025-07-26 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bee68581-6627-31d5-a694-65881c68429f | -3.39127 | -47.4936 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cbae6f96-919e-3223-b196-1b41bcd87864 | -4.3737 | -48.06804 | 2025-07-26 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49b8c4e5-008b-34c0-8332-8e6b118898e5 | -4.77794 | -45.33903 | 2025-07-26 04:02:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff4d89db-dd43-3bd4-ace6-7c49b4214a13 | -2.90608 | -48.24818 | 2025-07-26 04:02:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f213781b-c2be-38a0-9d56-64d1364a898e | -7.23804 | -43.07853 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7465d504-2968-3af9-ab09-357d67e67893 | -5.66479 | -51.36278 | 2025-07-26 04:02:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 220a4060-e561-37dc-b28b-248d38179216 | -5.74211 | -43.97446 | 2025-07-26 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd43b39a-9161-3146-a5a2-90d80676f8b1 | -6.88801 | -43.11124 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ec6c1a2-83e2-3d6a-b33e-9014299fee73 | -6.14798 | -42.59518 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 77e0c8d6-3fa6-32a0-bd72-ef9e416c0d48 | -4.04225 | -42.52139 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eb919eec-4acf-3afa-b78f-49b5437c34ce | -6.32797 | -44.0946 | 2025-07-26 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e86dc71-49c1-3e93-bfe0-7af1f599ed3d | -5.90542 | -44.32056 | 2025-07-26 04:02:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1b4e665-8cd4-31ae-8bfe-541dba31d7bf | -4.07469 | -46.8997 | 2025-07-26 04:02:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1af4a06d-4fc2-3acf-9a4e-4c5a05ff971c | -7.24009 | -43.06621 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 721ee216-a578-3e60-8cee-9deabad615b2 | -5.48045 | -42.15226 | 2025-07-26 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cab933d3-43dd-3dad-9ea0-3f70dbfcd1ac | -4.30823 | -48.10464 | 2025-07-26 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f806b9f4-7462-319f-9644-1ca60ab30f8d | -6.69277 | -44.16302 | 2025-07-26 04:02:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7569678e-39fc-3d2c-bd3a-51324f32f4bf | -2.574 | -49.11234 | 2025-07-26 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bba72763-f29f-3c99-8c16-f13f838f85ae | -4.07155 | -42.54755 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 66a8cd3c-5143-3202-b32b-43315a44520c | -4.07222 | -42.54335 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| d28ba0da-fd3f-3496-a497-928cdfa2f346 | -7.23719 | -43.06153 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 146450a8-8e0a-3ac1-8d76-24636b2439b9 | -3.39632 | -47.49446 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0bb49ce6-4b00-3bd5-ad80-c8a43901ecfe | -6.67064 | -43.96663 | 2025-07-26 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8b9ec72-0e7b-3398-b728-a5f8a5c74dde | -6.98621 | -43.33236 | 2025-07-26 04:02:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a93a30c8-ee98-3674-ada9-2cbc92f84cad | -6.88003 | -43.68291 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f698a95c-a49c-3e6f-912a-926f33ca247f | -4.79455 | -39.95082 | 2025-07-26 04:02:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2f353664-3a88-36b2-b969-fdb45c959332 | -7.2365 | -43.06562 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e81146f9-bffa-350e-9e65-cf6a5c2d25d5 | -3.43623 | -43.14201 | 2025-07-26 04:02:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcb8f7ea-9aad-36fa-9769-79925327ba58 | -7.24591 | -43.07558 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 42a8e396-ab51-3bc5-b4aa-55af51cdae73 | -3.31425 | -48.71333 | 2025-07-26 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f4e985d-b015-3a6f-81fa-976b440f915b | -6.93369 | -42.80696 | 2025-07-26 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f819721e-fa10-3496-83c8-d0fb3c90163e | -5.74291 | -43.96959 | 2025-07-26 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94f2a650-58f4-3285-8fd9-592be2ee08f5 | -3.57992 | -47.52662 | 2025-07-26 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2894df4e-ed94-3ca7-857f-8e0023b7a759 | -6.86811 | -43.68564 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b9698b0c-3297-312c-becd-d409c0177fd6 | -6.15509 | -42.5963 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 24643cd8-55ee-3c24-b9c3-0aedd9093ed5 | -4.60881 | -43.32333 | 2025-07-26 04:02:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1051073-96a6-3e18-a4ad-8bd2cecfb12a | -6.86585 | -43.67614 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b7a087f-7eac-3812-9959-9cc4b9889e12 | -6.70239 | -43.05791 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d357a07-41c2-3505-ab50-8733ccd422c4 | -6.3944 | -44.75699 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4adca8a-b588-37b8-9b44-9821955b87d5 | -4.77861 | -45.335 | 2025-07-26 04:02:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 094a6f35-d3d1-3b6f-9024-3419bbb29caa | -7.2399 | -43.0803 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a55a40a4-f99f-38ab-9e33-a43e69a52de2 | -4.03862 | -42.52081 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 19d3c164-0518-3ab0-a47a-1bfe211b6224 | -3.58495 | -47.52755 | 2025-07-26 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1b03d35-11c1-305d-ad1f-607c0b070744 | -6.59467 | -41.78774 | 2025-07-26 04:02:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d1c7e9cd-07c1-3a51-93ed-77162c7b277f | -6.65253 | -43.04535 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| daf5c5ca-7506-3f24-ab72-af87d8bcdd30 | -3.43331 | -43.13943 | 2025-07-26 04:02:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 388e1fbf-4840-349c-a399-24be9575b52e | -3.7522 | -49.05137 | 2025-07-26 04:02:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4ea08f4-4514-3c69-b4a8-1d791b890a36 | -6.41075 | -41.1503 | 2025-07-26 04:02:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f26b43db-96a5-30ec-a3d1-f6f0d3a75b42 | -2.82586 | -47.52271 | 2025-07-26 04:02:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1040c80-1ea1-3a0c-9f21-abc1f2638280 | -4.07288 | -42.53916 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2def6235-2b6d-3c6d-a5ab-01bf18821199 | -5.2056 | -38.02464 | 2025-07-26 04:02:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 741e8655-a7ed-3568-8200-d34fb12d8e31 | -5.65257 | -42.58231 | 2025-07-26 04:02:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ff1937a-20e3-32ef-8ede-011232e50c7d | -3.81055 | -42.5474 | 2025-07-26 04:02:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e684d2f8-24fc-342c-b20a-93f8bcd63033 | -6.78592 | -43.04903 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| daa06e38-b073-309f-b852-6222fb40aa86 | -3.82327 | -41.57356 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 271be8a8-0d3a-3986-a37f-5ae7935532eb | -5.91749 | -44.97749 | 2025-07-26 04:02:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6849f0df-29ae-32b4-809c-9367425b4aa5 | -3.04247 | -47.38242 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b65ff672-1182-38f6-9723-3eaf5831b2d5 | -6.70171 | -43.06208 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 951b0d75-310d-3f2c-babc-72acf7961495 | -6.86884 | -43.68119 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25dcada9-17a3-3dd3-addb-69040f1ec49b | -5.7437 | -43.96474 | 2025-07-26 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3824ebc-23ed-301f-bfa2-634b833e2ad3 | -3.82736 | -41.5703 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60acf7e4-222f-338d-a305-30a5a4d08e2c | -6.8896 | -43.12428 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2feae4d-21b9-31aa-8b23-d3236eba9dd6 | -3.05324 | -40.02618 | 2025-07-26 04:02:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 61719eef-5c36-3c63-87e8-29a7b771a60c | -6.93592 | -42.8157 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ac307b3-9edd-3941-aea7-82a1502f86be | -6.56826 | -41.49685 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63747864-27ce-36ef-ba48-b7402bd79f32 | -7.24232 | -43.07499 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| b7b7da15-e380-335d-9c3e-73702a4f5dec | -3.43709 | -43.14003 | 2025-07-26 04:02:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d95b926-5213-3cf6-b569-5e1ddb2ff57d | -2.99713 | -49.3226 | 2025-07-26 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63d6bf49-6784-30ab-affb-92b865cd11a2 | -7.24056 | -43.07617 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 7d38c8c1-7140-3102-9e29-6d94dfda32cd | -6.22802 | -44.52883 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d88f68c-3181-3866-9481-a0779a69154a | -2.90071 | -48.24731 | 2025-07-26 04:02:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fe6171d-13e3-301c-9f6f-ebedee2e38b4 | -7.23405 | -43.07086 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 44d12722-c6cd-34b0-9d2f-44dbbe7fab3b | -7.19489 | -44.02297 | 2025-07-26 04:02:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e995287-60a0-3699-97d5-6a1ddffd21de | -5.743 | -43.05855 | 2025-07-26 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 915a04ed-b2e6-304c-9592-56edf1a53410 | -3.38115 | -47.49194 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6dce3b2-6b3e-36c5-82c0-69cf3c6551f3 | -6.56369 | -41.50359 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 31717dcb-d95b-3e2f-abe9-c8556a9c2616 | -3.94594 | -41.48339 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README10.md)
