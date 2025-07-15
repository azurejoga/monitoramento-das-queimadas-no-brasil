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
| 2b2799e2-d706-3f6a-9712-cb287464cc2c | -4.6898 | -43.24788 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79456da8-3e47-3723-a488-bf0352201841 | -3.33423 | -48.71657 | 2025-07-15 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6b2c8f9-067f-3517-9885-003ae146499f | -2.9287 | -48.23603 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b8ed8cb-120a-3daa-a2ef-0cc6096f5954 | -4.01068 | -49.47159 | 2025-07-15 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 586101e8-61b9-36fd-ada1-544e342b9a41 | -6.18145 | -44.38385 | 2025-07-15 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51066d3a-2bee-39a3-923c-ddce046fb50d | -4.00378 | -43.231 | 2025-07-15 04:08:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a13fe5c-50bb-36c1-beae-a546c22f310c | -4.82013 | -44.35348 | 2025-07-15 04:08:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc083462-b8fc-3b4c-b07f-7c0a2f0d9e92 | -5.33155 | -43.7516 | 2025-07-15 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30cce27b-5d2a-39fb-916c-578558e0dca4 | -5.79021 | -45.11794 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f252302-34a2-317d-b738-1768bacec79e | -5.78565 | -45.09868 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fb0e5f2-99c7-3b7a-9e46-5d0c11d740dc | -5.78492 | -45.10318 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8785cf47-e5ed-3e17-85bd-d8c6f233184f | -3.38476 | -47.46917 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00a28866-48df-33e4-8fcb-cc4c3d1ad5bd | -6.13604 | -44.08884 | 2025-07-15 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85825724-e192-346b-b171-3e58e8b4ff16 | -4.68199 | -48.86935 | 2025-07-15 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49e60932-ad46-3299-9b20-4b4a2f1f2a52 | -2.91256 | -48.24408 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c836776f-fb06-34b4-b9df-c2f23abe8e54 | -3.58264 | -47.52058 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32749e03-36f9-3481-a29a-aef9ce8ed6c5 | -3.9658 | -40.4395 | 2025-07-15 04:08:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f375e7fb-b470-3e4a-94a5-c3e14ccc9484 | -5.37148 | -43.9264 | 2025-07-15 04:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ace0df75-4c5f-3f21-acb5-1484a9817da5 | -4.6892 | -43.25165 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 950e3f92-3b07-3728-86cf-591a6e96fe74 | -4.86694 | -45.3092 | 2025-07-15 04:08:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 449b6b61-bc00-33b3-ad9f-f767f3894c15 | -3.38474 | -47.49719 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05b508d5-ebb5-33a6-9146-b9144cdfb2fd | -6.17721 | -44.38734 | 2025-07-15 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36136b51-fbd6-35df-9fdb-808d67a81013 | -6.53425 | -42.37026 | 2025-07-15 04:08:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 27d0b6db-bcea-312a-bfc8-7870c9b0b871 | -4.78094 | -45.34146 | 2025-07-15 04:08:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 59e5e6e6-3e49-3d76-bc43-e2a14a7d067a | -3.51297 | -47.21823 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 917aec7e-f9f4-3a98-bb97-2ee047cb362f | -4.0511 | -48.75224 | 2025-07-15 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 238178c4-a1fb-32fb-8854-150bde167503 | -4.00726 | -43.23155 | 2025-07-15 04:08:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f172eb86-f0c9-3e2e-964b-f663599379b4 | -5.98266 | -43.76498 | 2025-07-15 04:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a68b35d4-0192-384e-8850-d8a554388431 | -6.85748 | -39.75715 | 2025-07-15 04:08:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 326589f0-1112-3d06-ba3c-64a35663a317 | -5.48289 | -42.14953 | 2025-07-15 04:08:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2976ac85-642a-386c-8c92-f9fa6edc62fc | -5.5369 | -43.88808 | 2025-07-15 04:08:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 338d2dc0-d40e-319f-819e-31f23abe9abd | -3.66706 | -48.3284 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c418842-46cc-3aed-b077-edb819de42c1 | -4.03863 | -48.06895 | 2025-07-15 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73d15114-e902-3c94-bfd8-a22d1b5447d2 | -4.03397 | -48.06817 | 2025-07-15 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49989b0e-af9e-31ad-ab9c-40ce7ef454ed | -3.38402 | -47.47365 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6010a582-0660-30c4-b0cb-957b8003ad7e | -4.68168 | -43.2543 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc18eece-df89-366d-a3d2-1ce20cde1867 | -3.92946 | -43.15352 | 2025-07-15 04:08:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb9d9461-0aae-3c84-955b-88b9a75289ec | -3.58716 | -47.52132 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d2223133-3a0a-3feb-856f-ef52d662a7dc | -5.6997 | -44.2443 | 2025-07-15 04:08:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 924d017e-a0c2-3353-b56c-373cc27817fc | -3.5834 | -47.51607 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e4a5750-f66a-3233-be9e-b11141a2de0c | -4.78325 | -45.33927 | 2025-07-15 04:08:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f670f42-d63c-382b-be11-5c2e9e14eea6 | -3.39721 | -46.90457 | 2025-07-15 04:08:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 013682ac-e3af-35a8-ba08-9d8dd3f5edc1 | -5.53337 | -43.88753 | 2025-07-15 04:08:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0031a436-6aba-370d-a2d9-d0af9c4053b7 | -3.22537 | -46.7994 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95856f96-b6ea-3b1a-b8b8-33425b7eee42 | -3.38098 | -47.49187 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d17b0a5b-462e-3e47-8e4d-eff54e1a9fde | -4.77941 | -45.3386 | 2025-07-15 04:08:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d485205-82ab-3eff-8787-1d68d507ae48 | -4.2253 | -47.7686 | 2025-07-15 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 675004c0-c019-33fc-b76a-95c82e921b56 | -2.92303 | -48.24047 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 499e5c1d-3c5c-340d-a2f2-b074f31c1250 | -3.3795 | -47.47289 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 606c479c-4f46-3eb4-9327-4064880c17d8 | -5.54106 | -43.88467 | 2025-07-15 04:08:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea0aa6ac-d5bb-3905-ad4c-306e80ab5ec8 | -3.66792 | -48.32331 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bc8c1d1-59ff-3509-be41-eecce469bbfc | -3.58827 | -49.42758 | 2025-07-15 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b28f5219-9547-3b59-ae79-f865c352f80c | -6.28964 | -43.41522 | 2025-07-15 04:08:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 162b3ab4-e406-37c1-b859-756b67bca56f | -5.98328 | -43.76113 | 2025-07-15 04:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fce0982a-19da-32a3-aa83-a43e7b8c319e | -6.18079 | -44.38789 | 2025-07-15 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b01ef73b-6145-3234-b596-13719b116e4a | -5.78647 | -45.11733 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46fc483d-f89e-3680-98e7-2e95116d05c5 | -5.36794 | -43.92585 | 2025-07-15 04:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 614dcb69-2a5c-3eaa-9609-59b9aa2fe9f3 | -2.91736 | -48.24488 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 03af74e4-432d-35a9-81e3-0175bb7bda6d | -3.38326 | -47.47815 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a64c9579-f7f8-328e-99ea-94e1176f3ac0 | -5.79011 | -45.09483 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e057c75f-f1bb-35df-8202-5934fae30744 | -5.07051 | -37.71624 | 2025-07-15 04:08:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84a06e4f-cd23-3930-af63-519b7372091a | -4.60303 | -43.32345 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e28cfe8-1780-3f3c-b9df-4d606dd449f1 | -3.75711 | -47.12156 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6d54e79b-be52-3718-838c-9e3e808432b5 | -2.91467 | -48.23786 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1828f652-6d62-35ab-9cdc-7f962c75909b | -4.68228 | -43.25053 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 142bd266-ebee-35dc-9cd3-232d74c986c5 | -5.1868 | -37.63838 | 2025-07-15 04:08:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 75104049-2f54-3744-af42-dc036e841f1b | -4.00317 | -43.23479 | 2025-07-15 04:08:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba1baadc-52d6-3a15-a559-ec0e7d04d709 | -5.73215 | -44.5056 | 2025-07-15 04:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99d96ef9-9341-3a6b-bcc9-1a56940f85ff | -6.53481 | -42.36674 | 2025-07-15 04:08:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 674f318a-3266-3dcb-b2b2-fcf1efe54d2f | -6.14091 | -44.0812 | 2025-07-15 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f13fb1f-cd75-3f34-8ac7-75979cb7beb1 | -4.68574 | -43.25109 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b646ef5-352f-3e50-a395-ce8cc288920a | -3.75782 | -47.11735 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0812891d-5842-39b6-946f-3434b307f980 | -5.78638 | -45.09419 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6ed94a2-762d-3e13-8841-b17b30d00917 | -4.03479 | -48.06331 | 2025-07-15 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 69e2af36-67e4-37df-b106-be98c8a398e8 | -2.91344 | -48.23888 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cdc20782-8328-3215-a5cc-cd86034acd32 | -5.33443 | -43.75606 | 2025-07-15 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fb6eae3-0504-317f-965f-3c8c9dcf7cc0 | -2.91863 | -48.24389 | 2025-07-15 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7140b5f1-3fcd-39c1-b81d-7d8136e919a1 | -5.79485 | -45.11642 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08bc9324-0197-33eb-a158-6fb8c9a6b4f9 | -4.60365 | -43.31964 | 2025-07-15 04:08:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc7f94d1-46e7-3440-a67a-4e08debda86c | -6.14445 | -44.08172 | 2025-07-15 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 427a86ff-9879-3d71-b8bf-dd5eef903aca | -5.53401 | -43.88356 | 2025-07-15 04:08:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 981f9ace-d772-3fa8-b679-b5a5ab50fbb1 | -5.78273 | -45.11675 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96501431-6656-3c46-aa98-1c5328bda1d6 | -3.38551 | -47.49259 | 2025-07-15 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a7fea73-c251-367d-a162-b610147eb493 | -6.24246 | -43.34351 | 2025-07-15 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0dddd11-356d-302d-b94d-3732a9ae9211 | -4.68297 | -48.8636 | 2025-07-15 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 792800ca-1f01-3472-8049-e9533aead5e3 | -4.27333 | -48.18339 | 2025-07-15 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5ad49875-86c9-3832-ab49-8cbc58b9f656 | -3.58775 | -49.43063 | 2025-07-15 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d16e83a8-8336-3a54-98bb-f3a038f5b52b | -4.78244 | -45.34409 | 2025-07-15 04:08:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 779fc484-9718-34a9-97d2-5bbffc031f2a | -3.45955 | -48.88884 | 2025-07-15 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22ff2cfe-75f6-3875-ab68-43080adc3da5 | -3.5111 | -47.22026 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da565dfd-005a-3da4-9fb6-95459233feac | -3.42582 | -43.34879 | 2025-07-15 04:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ca03d74-ac7f-30ca-969c-632011a1843f | -4.03943 | -48.06416 | 2025-07-15 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dc47c71-b4ac-3a40-a3cc-baaddeac1a75 | -5.78118 | -45.10258 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cb48a35e-17a7-3a38-b19a-df6d560f2c93 | -3.36307 | -49.16404 | 2025-07-15 04:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 673155db-2dd8-3066-9c5f-136e34f5a84d | -3.58189 | -47.52509 | 2025-07-15 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf0b612c-9bfd-3a70-a3a7-c3ae909d331e | -6.85405 | -39.75662 | 2025-07-15 04:08:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29bee682-f39a-3520-b1f0-1de906d6a40d | -5.54042 | -43.88864 | 2025-07-15 04:08:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9681f4f7-271f-38bf-aa57-b3f1cfa51254 | -5.18309 | -37.63782 | 2025-07-15 04:08:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42e9ce25-52d3-3b36-9def-9a6cde36a709 | -5.78191 | -45.09809 | 2025-07-15 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf16c09b-c0c4-325f-b830-acb878d5d7bc | -5.37213 | -43.92243 | 2025-07-15 04:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README10.md)
