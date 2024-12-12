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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 465ebe8d-c4d6-3eba-beee-9f7087832a5d | -3.56563 | -43.49427 | 2024-12-12 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a707f35-cc91-37ca-9c7a-d271504ca2ef | -6.12856 | -42.54258 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ece24468-7f12-3f7f-9d1e-c5c0cdd30d3f | -5.93194 | -48.04636 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abff90a3-c682-32e2-ac2e-cda8a4146e31 | -2.52769 | -51.79099 | 2024-12-12 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74f90429-6c29-33f0-a92f-28a0f2a1bcbf | -4.54698 | -43.56188 | 2024-12-12 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c863c630-8ae9-39b1-8f41-74fd35a5094a | -4.09534 | -46.6787 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 580cd91e-455b-3a16-8a72-5bdc481b3a29 | -2.99157 | -48.07701 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb53475f-cb4a-314a-85f3-6621dcaf8548 | -6.9679 | -42.99849 | 2024-12-12 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 28e5e5f1-7424-3bae-a1af-ebc18354c4a6 | -6.14239 | -43.91744 | 2024-12-12 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4059d3f7-225f-3610-8635-8de4b12e27d5 | -3.99666 | -46.89323 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4020412e-90ec-3610-a04e-008e6c18d811 | -3.14047 | -48.5293 | 2024-12-12 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fa12f69-175c-369a-be54-f9feae37a6e2 | -3.18289 | -52.4479 | 2024-12-12 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c4920ce-edff-3fc8-b290-e20bc072103b | -2.52043 | -51.78979 | 2024-12-12 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c93b02b6-d8ff-35ca-a79d-31b8e3ea644e | -4.1932 | -50.54668 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26823c4f-65d0-36da-8e22-e49689e1dd6f | -2.73479 | -47.53465 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99876144-dbb7-37d1-add7-a0fc46e8eac9 | -6.92511 | -43.52527 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 7121fbdd-335c-34f1-85f5-1d2348ad2264 | -4.03031 | -46.89373 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bff2eb0-145c-38aa-9be9-f5cfd2df2e5e | -4.08131 | -46.72346 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c62b7dca-2b90-3b58-9d87-9ab6d6f4cdf7 | -4.30042 | -48.10069 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24bf76cd-494a-3b97-978c-a8297d907e83 | -7.2988 | -44.5202 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63fdde0b-3160-344f-8e4e-4e3ee1f9dc5a | -4.03706 | -46.74853 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5db0a66e-80f7-3b6a-baa9-ebd3899c301a | -4.51215 | -44.0757 | 2024-12-12 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a034d27e-2ed6-3c77-a3e9-adc99d32103e | -2.81667 | -52.97923 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3c498b3-1ee3-340c-af78-d24b45c3f7fb | -4.37431 | -48.07969 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91fe9603-1a38-33d6-916d-a6767804c055 | -6.39957 | -44.04225 | 2024-12-12 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfbaaf7c-044d-3f23-9dbf-aa32e62eaf86 | -6.96256 | -42.99571 | 2024-12-12 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| fdf8b96e-2fab-3bb5-baea-513070684406 | -6.9724 | -42.99921 | 2024-12-12 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 44f3fb8f-4f03-373b-bd41-b9d4af5450a6 | -5.87509 | -35.41155 | 2024-12-12 04:38:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2691b773-2ebb-323c-8fbc-4fa1b7e5499e | -5.35146 | -44.19668 | 2024-12-12 04:38:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b86efc1d-04b9-3698-910d-34bd744301c9 | -6.9634 | -42.99776 | 2024-12-12 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c425c47c-82e1-3fee-b6cd-fd921bc05ff8 | -2.95989 | -41.8218 | 2024-12-12 04:38:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a75435c3-7846-365e-b10e-b2c50efa8280 | -3.59607 | -53.74723 | 2024-12-12 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5f66678-9736-3a13-90fd-ae53bab51359 | -4.35708 | -45.92095 | 2024-12-12 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea28fac2-242c-3baf-8c1a-a95f58d581b5 | -2.74017 | -47.67632 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dfd7d1d-d931-3ff9-8408-6e0a699b7c22 | -3.99725 | -46.88947 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65e140c1-9f20-355f-9888-160bc76c0f09 | -5.88228 | -35.41289 | 2024-12-12 04:38:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7f31e8c8-92b3-3715-9065-5ba3450b4b0c | -4.35106 | -48.46978 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f14a8445-75b0-3ef2-8482-c001b3457590 | -2.95146 | -53.11363 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 532cc5aa-0728-3e0f-b14f-a37106bd7931 | -6.05749 | -44.04801 | 2024-12-12 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ffbb166a-f741-3353-b957-878072b11480 | -4.03787 | -46.75162 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 146f7c1f-621b-3616-be99-44e56cb746b3 | -4.07608 | -46.1269 | 2024-12-12 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce942c9-85ec-3f6f-bac4-7dbc7b890b3b | -3.24866 | -46.87695 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 80bc9a28-43c4-321b-b4b5-5f2b9a961811 | -6.93261 | -43.5348 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d47bba0-97af-3db4-a191-ecfe6b39c03d | -6.92688 | -43.51287 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 267b9674-c863-33ea-8adb-1cca6eae7348 | -3.7018 | -45.29168 | 2024-12-12 04:38:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e48b299-24d0-323c-9b13-cdabc2c09ece | -3.98445 | -48.39527 | 2024-12-12 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d567806-7aa5-3572-8ff9-28961a24b5e8 | -8.15279 | -43.79185 | 2024-12-12 04:38:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 23bfa463-00e4-357f-85d9-ac46a2c3955c | -4.01018 | -46.64691 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22c2d0b9-88e3-3322-9a2d-ce5300abc39d | -3.78228 | -47.1 | 2024-12-12 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13b5385c-c599-3ab2-825b-e2a739f67d5d | -1.87234 | -54.68778 | 2024-12-12 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 102f0004-ce1f-3848-ab14-b4bb1ed40574 | -5.84945 | -39.04696 | 2024-12-12 04:38:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eea4b7fa-40f5-3992-a301-a2d3703f49c3 | -3.24581 | -46.87271 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0b476ecc-24e5-3641-9947-1cc239c58c6b | -5.928 | -48.04945 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4581852d-bda0-3ee8-8df1-b8ed1d608e47 | -2.92347 | -41.46659 | 2024-12-12 04:38:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9d69cd3-b11c-3ffa-8f49-742fd946937f | -6.12007 | -42.53646 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 593b53f5-d141-3013-866d-dcf27098cae4 | -6.92451 | -43.52943 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 5127be80-b284-301d-89d6-8e717183d02a | -4.57004 | -48.4758 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb395fed-93ca-30a0-a209-bdc1ab3de387 | -4.18552 | -49.28403 | 2024-12-12 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 799a011e-a538-3863-b8a2-0c3e50da103d | -3.42814 | -42.98367 | 2024-12-12 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3b021ae-226c-3e9a-9654-6c4e2a24bdee | -2.96404 | -53.72374 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d6c7c2e-a548-394a-a017-3f831a1e82ea | -6.92886 | -43.53004 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| a4254dd5-b168-32c9-a2e7-7dec5e59d694 | -3.24464 | -46.88014 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a3a3d869-3022-3111-b174-1ac95c80eaa6 | -1.61378 | -54.6753 | 2024-12-12 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b97ad4e-e63b-3022-99fc-88bd7e3bba49 | -4.512 | -43.61942 | 2024-12-12 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bfbd83b-efd2-3d7f-8c09-408c48cfbe0f | -5.29576 | -48.3157 | 2024-12-12 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae4aab65-9cec-3fc7-9869-2642ae25ba8e | -3.01199 | -48.03389 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18b8c46e-8ebc-3d04-9763-e7f9650c5f2d | -4.8696 | -48.52599 | 2024-12-12 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59dd83a7-93ba-30ce-bc97-0153de006e93 | -6.92253 | -43.51225 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 18081ef2-c1f7-314b-bbda-83ab18bd878b | -3.78628 | -47.09682 | 2024-12-12 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21a6bb0d-9916-3705-8235-fb03277948ca | -4.83529 | -44.21363 | 2024-12-12 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e393d68e-a717-348b-ad7f-b4e61a9e9ec4 | -2.83554 | -53.01357 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd91ebb1-4a14-3c86-99d6-b11aa2a6addd | -5.02872 | -45.0889 | 2024-12-12 04:38:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c464bc64-f5e6-39c1-9559-945362c62dd8 | -6.93575 | -43.54376 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a873b3ce-1a91-3424-bc29-3339e3e71d9b | -2.95104 | -51.78048 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d589f13b-d778-36e8-9a14-c200a2575ccf | -4.08073 | -46.72721 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ff4155-db27-3513-846e-a0dca08ee0e3 | -3.7041 | -50.9395 | 2024-12-12 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f693152-17fa-310d-9c43-7c36df20edc2 | -0.75496 | -47.75724 | 2024-12-12 04:38:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4d94245-966b-3a21-be24-35b87cb9dc78 | -4.06932 | -48.95072 | 2024-12-12 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddd83750-56d4-3ab5-b284-70de242551ea | -5.59596 | -41.38761 | 2024-12-12 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| fc353597-a958-3a75-9c9b-1af4c1ce28ee | -2.91496 | -48.00769 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfdef478-a1fe-3ea1-a8d1-da379a5052cb | -4.49977 | -46.06221 | 2024-12-12 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f26b8c66-f4ef-3429-bb8a-478dbf928507 | -6.93619 | -43.50987 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d7b958a-7209-3aba-9dd1-ab13779360f4 | -5.26443 | -44.77599 | 2024-12-12 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75fe2f10-2e44-3c53-af20-ae40cbb38928 | -2.79093 | -47.63729 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caca1404-c1e6-3005-9412-d71976148e60 | -6.93679 | -43.50571 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6f35432-f192-3528-84ef-0968461446eb | -2.83244 | -53.00824 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3746e61-e6b7-368f-8781-f3f7e0847ab7 | -4.06337 | -46.70122 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e52a2166-a8f5-3826-9fa5-0a1fd19f7849 | -3.69809 | -45.2911 | 2024-12-12 04:38:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afed515a-93b3-3359-b71c-950f5856ddc6 | -2.96448 | -41.82249 | 2024-12-12 04:38:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af0b3fac-91d2-34c9-b174-69131c4cdcaa | -5.90454 | -44.01345 | 2024-12-12 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16312cea-9b75-3869-8cb7-6e289e757d27 | -4.0826 | -46.6688 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f41a3227-fd37-35a8-81d1-784b6f17fb0f | -4.02206 | -53.98556 | 2024-12-12 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fd989e7-2cd5-322e-975c-8c2879c3fc16 | -2.5168 | -51.78922 | 2024-12-12 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b6de28b-292e-3689-b2d1-68a84aadd831 | -4.10376 | -54.6719 | 2024-12-12 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5358f059-bfea-3c47-bf89-036a7f3ac575 | -4.09245 | -46.67431 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45551e91-c840-3a29-a93a-c6231f949f7c | -6.93005 | -43.5217 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 17afe654-ba3d-3590-ac38-2fa816f43e73 | -6.92826 | -43.5342 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d18b3df-e1c3-3bd8-831a-660d54a5be4f | -2.50621 | -49.0561 | 2024-12-12 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf1cfce8-1d18-3171-90d7-4ca13eb2ac64 | -4.04342 | -53.98205 | 2024-12-12 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b2d952e-f625-38b5-9c76-e5ba015a4b88 | -4.77992 | -50.65657 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
