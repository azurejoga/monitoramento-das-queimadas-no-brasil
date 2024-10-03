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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4660ecf7-0292-3404-a766-3559daa57aee | -4.93538 | -43.77986 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| fd19bbac-d4ca-3595-a917-eb9090347e76 | -4.93501 | -43.77915 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d25a92b7-5441-3581-b44f-2bcbf116b59f | -4.93251 | -43.77562 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ebc1f1d-8334-3a17-8551-beae58f632ce | -4.93193 | -43.77936 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 67c69a53-2e82-3ebd-b355-3348090e81a9 | -4.92907 | -43.7751 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fd363f7-3966-36b0-9e35-feb4bd007063 | -4.92849 | -43.77885 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3f59d005-7b6c-3bf5-8343-9172e5220e36 | -4.92505 | -43.77831 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 90ab794a-e805-3224-a6f8-c3e3e5544964 | -4.78479 | -43.79963 | 2024-10-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db5c2532-55cd-3f18-bb23-fac25e608ad6 | -4.66479 | -43.75891 | 2024-10-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11d5d8ab-9b6d-3687-8a95-3d86ccafa68c | -4.66422 | -43.76266 | 2024-10-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75336547-2c49-3a46-9206-7bd37e07db9a | -4.66303 | -43.81603 | 2024-10-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ccafd53-a76c-3ca7-951b-5448f996f44e | -4.66136 | -43.75837 | 2024-10-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39b4579c-ec99-36af-ae76-103c81bb058e | -4.66078 | -43.76213 | 2024-10-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5614c293-4152-3f2f-86bb-df2280fb3bd4 | -4.54503 | -43.30818 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fe6f8c4f-ad2d-3e5e-8b4d-bab889a63974 | -4.54443 | -43.31206 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 72577c51-a95f-3c0c-9d00-898a0c35ad04 | -4.54153 | -43.30764 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fc7be581-397b-38ab-ace4-617e1eb1242f | -4.54094 | -43.31153 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c85c78aa-3867-3a3b-97bd-91d9bd85af9e | -4.53864 | -43.30323 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27466682-620d-3bb1-8df7-97e3ba7b8db4 | -4.53804 | -43.30711 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 1a6d77f0-e1e6-34b6-b4fd-8c0250e2435d | -4.53744 | -43.31099 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 053cf5aa-6091-3485-953d-c0238d52a0ea | -4.53455 | -43.30657 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| b17b1ca1-de95-3bd7-99bd-9872ccb8e8eb | -4.53395 | -43.31044 | 2024-10-03 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 2acdc862-4bf8-396f-8da9-ee175cb98c98 | -4.20676 | -43.24664 | 2024-10-03 04:25:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b27f4a2-c7f8-33f5-8a7a-ce99ddc06a9e | -4.03991 | -43.24235 | 2024-10-03 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac2cf15d-aaf2-3092-b2e4-21c749e256eb | -4.03818 | -43.24166 | 2024-10-03 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 854eff25-5b3f-3014-8b22-fb165eb2d3a7 | -4.81843 | -44.35289 | 2024-10-03 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8093ff0-8b38-378a-9b98-cf8087d90638 | -6.07599 | -43.79665 | 2024-10-03 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7576c049-f7b5-3513-b01c-786d0c3a91fc | -5.83855 | -43.71794 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbe586fe-d53a-39a6-a9c7-66220485e4f7 | -5.83275 | -43.70921 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07e3960a-5f6a-3a96-97cb-193df9feb738 | -5.82927 | -43.7087 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 382fdcd0-d5fc-3d47-9391-0df9bb254933 | -5.82869 | -43.71253 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97a19cba-bd5e-3b3c-b0bd-a2528859c747 | -5.82812 | -43.71635 | 2024-10-03 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb528fb4-f2a6-36df-8499-5057a1dc86c9 | -5.7195 | -43.78704 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae90430c-d79a-3b49-88eb-c8b20ecc190b | -5.71892 | -43.79085 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96bdba9a-76c6-3230-8de3-73710cadbe8c | -5.71603 | -43.78653 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1cd65ce-3239-386c-af33-0e48830f82dd | -5.63452 | -43.77037 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b6391d2-0330-3eb8-a268-15db4c3f9f64 | -5.54904 | -43.73462 | 2024-10-03 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15af35f8-a3f5-3122-9968-0d0cc7eea718 | -5.24633 | -43.81059 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75e7e7cf-ded6-3829-8725-24bc74839048 | -5.24405 | -43.80251 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56c6a286-1d68-398a-ae06-1104bd03859c | -5.24347 | -43.80628 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1003a17c-f628-3ef2-8921-42c55241d49c | -5.24288 | -43.81006 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28106c22-50ff-3ccd-be74-f7f288ce4d24 | -5.24061 | -43.80197 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c22e1ad-3540-3e0e-b8ac-d31cdbfc15ee | -5.24003 | -43.80575 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 746da9e2-761e-3363-80e3-dfd0d46b50c1 | -5.23944 | -43.80953 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d9c3f7c-0153-30ff-ad9f-8e7713b76ebd | -5.23658 | -43.80521 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed9b8b88-d71e-3800-ab68-54fe4d755c8d | -5.20622 | -44.52597 | 2024-10-03 04:25:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4500dfbe-247e-3f96-b8fd-bfcb1ab53e83 | -6.46765 | -43.57855 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4bc715c-3e51-3ded-8f74-dbd8cc221675 | -6.32884 | -43.77451 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76f85977-e2d3-37bb-89ae-5e0c461ff375 | -6.32535 | -43.77403 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aacf9cc3-7aab-3b73-8ee1-307ff388f72f | -6.32186 | -43.77356 | 2024-10-03 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea2f4d13-c7a1-35a9-8d7d-b4590b3572d5 | -6.29091 | -43.85965 | 2024-10-03 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4949e0e7-3ae8-3389-8cfa-6ee8f34efe7e | -6.24596 | -43.72297 | 2024-10-03 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43085623-15e5-359e-8c2b-2138a8a39177 | -6.24247 | -43.7224 | 2024-10-03 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08ea347a-fd11-3424-b85c-d520b08997d2 | -5.83717 | -43.95989 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3aa95263-9ed2-3119-a05d-34c72b8f68b1 | -5.8343 | -43.95557 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d54861cf-d4c3-305d-93e1-85e6ac7a1793 | -5.83373 | -43.95934 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70f28de5-871a-3ef9-93e7-6414f179f966 | -5.83086 | -43.95503 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed2dc7d1-6a40-33b7-bcf9-f0ca93930854 | -5.71198 | -43.9297 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b0123fd-f6fe-3293-baa9-f65e06f03a51 | -5.70854 | -43.92916 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14b264c4-5c99-3713-8350-994a2c4a770d | -6.19768 | -44.12501 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a6f730c-09eb-363b-812d-27f6ec3087b3 | -6.1948 | -44.12079 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 412ccc82-2998-3a85-b72c-efdaa509a5ff | -6.19425 | -44.12447 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a3f5078-f1a4-3a2a-842c-e96deed11ecf | -6.15488 | -44.13065 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed3fc076-900f-3dd5-8e65-86d0ad352725 | -6.15431 | -44.13437 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23f67d99-6b33-3d08-a1af-fbbf708ba0a6 | -6.15203 | -44.12637 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cf97ac4-169a-340c-9a1c-024ecc4dbf63 | -6.15088 | -44.13385 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c87c384-f602-3ebe-beea-080442564b57 | -6.14745 | -44.13333 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d3e8796-27aa-344f-beb0-4ce5d7c13eb4 | -6.14402 | -44.1328 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e002ade-d49a-3480-99ab-2b40406635ed | -6.14345 | -44.13652 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab29835a-c281-3cf3-8995-4d2e91637115 | -6.14002 | -44.13599 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 868d4e21-5514-3a27-abcd-e041344a73ed | -6.12231 | -44.04462 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3667aef9-632a-38ab-8a60-8b12dd108b13 | -6.12174 | -44.04841 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e43e9dc6-e138-32f1-8046-974f23800262 | -6.1183 | -44.04787 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19257062-8270-3275-b36a-2b8aac036956 | -6.11486 | -44.04733 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 146ab426-fe99-3824-9ecc-050a46f9013b | -6.11428 | -44.05117 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e39680b6-5925-3c05-98a2-c295a7dda123 | -6.11084 | -44.05063 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fa7992b-eb41-35db-b649-b22daa8696cd | -6.11027 | -44.05447 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b02a1093-c1f9-34bf-9190-4a97fc9fb912 | -6.09306 | -44.05194 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b51efa6-ec26-3caf-8d4d-b3d8e7f12817 | -6.09248 | -44.05579 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b8bad7-b8e1-3ae4-8ac2-0bc181ef3af7 | -6.09095 | -44.04465 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a2469ed-ac14-3280-bc86-b86bb28f5946 | -6.09077 | -44.04374 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb1fc659-3e08-3e3d-a5ca-7a0112ff8002 | -6.09019 | -44.04758 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a36fc8f-c29d-30ef-be21-39884e0a2cb4 | -6.08916 | -44.05619 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9a7710b-78cf-3768-8386-bbcff2678ece | -6.08904 | -44.05529 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50e94a1a-068f-3850-be81-94b5805fe610 | -6.04676 | -44.14881 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6827eb57-5f96-37b7-b83e-6c01086651cc | -6.04618 | -44.15254 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88266f6b-a0b2-3983-af0e-9367afc54a8a | -6.03934 | -44.15143 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c470a3f0-f897-3030-8734-7de4c87054ba | -6.03766 | -44.00182 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f60993b3-0e2d-3893-9210-44f871f8d75b | -6.03761 | -44.1855 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28d71320-d6ee-3193-8cd4-dd96f37c539d | -6.03707 | -44.00565 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 671e10b4-8de3-3e9f-b0e0-9eba24e9de2c | -6.03704 | -44.18919 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70ebb926-1d67-3dae-9e12-e7a329e3df8b | -5.96968 | -44.12558 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29d18a43-7f59-3901-a27d-5eb608650a95 | -5.96967 | -44.12561 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4de6015a-67b5-3735-a24d-78744ce29182 | -5.96911 | -44.1293 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa2c3607-4dc6-3633-a316-da27e62e1696 | -5.9691 | -44.12933 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2167505-afd7-37f7-86f2-e720eef4f8aa | -5.96417 | -44.00204 | 2024-10-03 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 284ddb16-0c2b-35d6-80fe-873ac50598ab | -5.86128 | -44.12387 | 2024-10-03 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6893629-9cd3-3040-8cdf-2ff84a5efd7f | -5.86098 | -44.12459 | 2024-10-03 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8315268-9cc6-399b-a41d-57c9d8bfa1bc | -5.79761 | -44.01152 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ece2a4f8-ff9d-3b0f-ae6e-148c2ae799bc | -5.79418 | -44.01098 | 2024-10-03 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README79.md)
