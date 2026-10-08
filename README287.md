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

## Dados Diários - Página 287

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa25c725-440f-3a00-b3fb-f681d27c8411 | -5.76935 | -42.07157 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 781a9cfc-43fa-3d43-811f-f22e244cae0e | -5.9546 | -40.93704 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8f9b3275-a3e4-3e53-89e8-83efc9e6ed4d | -6.8996 | -44.91693 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8c67f8fe-6017-3680-bfbe-da4881da64e9 | -7.31343 | -44.0063 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7d71a95b-68fa-3a30-a398-378708d45570 | -5.94776 | -45.68748 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 67fe25f7-8a92-3675-951f-10bd6bb4e932 | -6.88295 | -43.69678 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 258a90a3-ed6a-3396-af12-7b8acb835740 | -7.76683 | -44.17241 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e32328b6-ffb9-365b-880c-4caf4f144219 | -5.39831 | -45.90723 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3d70083f-3458-343c-9524-83c25e42f9ae | -3.2943 | -53.70464 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 79a2c61e-8959-3707-bcbb-e372057bc556 | -5.43492 | -46.64368 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c5ea59b6-e183-3811-8659-dff9cab44c9c | -6.37759 | -45.78878 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2ff38851-0599-3ee6-be20-2f5c5997fbd2 | -5.5309 | -48.17561 | 2026-10-08 16:20:00 | NPP-375 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2204ccdb-500a-3353-8e76-f68ae2763a7e | -3.07046 | -53.96582 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 96dbe1e6-9b19-3f2e-bf7f-cd65aad41722 | -5.48394 | -41.21402 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 737aa186-2c7f-318b-8c65-07c14c3864f9 | -5.72171 | -41.77605 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 536b2df9-97e9-3a1e-8318-59e2918965fd | -6.4955 | -41.82494 | 2026-10-08 16:20:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 375e694b-4dd2-3859-a98d-ccc9a5e75a94 | -5.97109 | -40.90873 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 84dddc0e-6989-353e-9e6b-18bc5deaba63 | -6.16081 | -47.93952 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| a5a6cd19-a2e4-3fec-9cf6-26fab70c0b89 | -6.16951 | -44.85836 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 348f77c2-995e-335e-8adf-1b7f684f9e9d | -7.73519 | -49.59658 | 2026-10-08 16:20:00 | NPP-375 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b7be16a1-2d4c-33c3-93de-744433101239 | -4.33292 | -42.74852 | 2026-10-08 16:20:00 | NPP-375 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a7352b41-8997-32c0-a8eb-52fb7dedcc9c | -7.76632 | -44.16879 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2aa126ab-19eb-3c17-a55b-3bca1974ad2e | -3.78914 | -41.67396 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 7da5b62c-7373-32db-9858-19c7eb403f99 | -2.74898 | -54.12303 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6b5a7dbf-3db6-3f95-8e99-4c7e81c7a6d9 | -6.02907 | -42.71907 | 2026-10-08 16:20:00 | NPP-375 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 5499bf1c-b269-30d8-b0d1-f4512a4d79a7 | -7.40163 | -44.45326 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ed3fb57-7e78-3d13-a6c7-38c384c2062c | -7.40438 | -48.10468 | 2026-10-08 16:20:00 | NPP-375 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13af0bce-f44d-3bf5-bacb-64215d6ae20a | -7.31794 | -44.5334 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8a56f788-1263-367d-bf25-1f4533cf57a9 | -3.78517 | -41.67082 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 67637b2a-02b6-3245-bc52-362ce2117f87 | -7.59945 | -42.39193 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 161.8 |
| 63c62646-c196-386c-b6df-9965ca47f355 | -7.21808 | -44.15305 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d35bd4a4-257e-3fa3-b064-212e9ae390af | -3.08494 | -53.964 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7b6477de-788a-3544-98af-568d22b23497 | -6.61716 | -37.89735 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 35.0 |
| e8264fc7-06d7-3a94-bdf9-94b9a5127349 | -5.92413 | -39.42744 | 2026-10-08 16:20:00 | NPP-375 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8cb4f4f6-8826-319c-9497-d4a68be2bec3 | -3.77084 | -52.6298 | 2026-10-08 16:20:00 | NPP-375 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| aae3627f-8f5a-340d-b282-2d137a1616f9 | -5.47986 | -44.60986 | 2026-10-08 16:20:00 | NPP-375 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 65d3cc18-68cb-3de6-90b4-e52b1880ce56 | -3.02217 | -43.3477 | 2026-10-08 16:20:00 | NPP-375 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a91f11e6-2eba-3110-8e8c-d2bde446e697 | -5.7202 | -41.64736 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| af5078a2-a17d-3b52-ace3-72a2180fff3b | -2.07625 | -46.577 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 279.0 |
| fddc7405-edd5-3789-aee0-ac44494c65fa | -3.13665 | -40.0778 | 2026-10-08 16:20:00 | NPP-375 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ff4ca95a-a0d7-37e6-a9d9-80ee6ac0aade | -4.087 | -44.13869 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 72a0abf8-7b0a-3514-9bd2-a61eb46c20a6 | -2.08937 | -46.57584 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 42efbc59-edb0-3102-a27a-381c6350481a | -6.5345 | -45.37618 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| eb76eb9d-b43f-38cf-9267-95c2f808fe84 | -5.9932 | -40.93451 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 32968e0e-e5ca-370a-9fcb-da05132dcec7 | -3.26077 | -41.84827 | 2026-10-08 16:20:00 | NPP-375 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 41a4778b-6acc-32f5-8e01-64125686d002 | -5.88204 | -45.97927 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 91ca6b87-7f78-33e5-aea6-2c8c92b56edb | -3.46698 | -45.11076 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2acb30bc-a349-3923-914e-db0f4fc794b1 | -5.77406 | -42.05476 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 71ff804b-9b87-3847-b0f1-035dd99793dc | -7.78778 | -46.74439 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ff34b894-52fd-32bc-bc25-95d9f5f060e4 | -3.15296 | -43.03246 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 528dd8e6-2ecd-37a1-bfbb-b18584940938 | -6.85212 | -41.7535 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 46.5 |
| f31baa67-5a65-3b6d-b74f-c4b7d4efc1ae | -6.92601 | -38.55553 | 2026-10-08 16:20:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 889bc0bd-60d4-3dfa-9590-686081921952 | -7.18695 | -44.33841 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9967f15e-5ad3-356a-9514-88e6adca2d0c | -6.16115 | -52.65516 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| e3b38620-cd8b-32c7-966f-936fd586567b | -5.32933 | -40.90038 | 2026-10-08 16:20:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 5f0764ff-8baf-30c4-9bab-a5f9429e80cf | -2.05486 | -54.30419 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 64ae6861-bf0b-3f47-8e9d-491d8a85fbf1 | -7.35191 | -43.19334 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d0af6aa3-84c3-34a0-8da8-c68653e2340f | -7.48647 | -42.79498 | 2026-10-08 16:20:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| ea42b405-26a1-3987-aece-ab4faa71c513 | -7.2529 | -39.40501 | 2026-10-08 16:20:00 | NPP-375 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3808685e-7eb0-350c-a615-8ade4ae95400 | -2.99115 | -54.08998 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68df9492-3694-31fc-a743-1db8c6286d8f | -5.1781 | -38.45149 | 2026-10-08 16:20:00 | NPP-375 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 854cd088-e062-3e24-8ad8-1acbf24e9ca3 | -5.47971 | -45.63435 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c75206be-3f4d-325f-9d23-ee4f521f635e | -7.37954 | -46.23376 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 763b644e-2fda-3850-bdb2-b10fedb138c7 | -7.86106 | -44.96107 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b240efdd-a41e-35ea-9301-10ee138b3953 | -6.79676 | -45.06323 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| cff3e4eb-86f3-32ae-b31f-fc57b0147ea3 | -8.21311 | -46.32895 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b9ae93bf-d4a7-3bff-a3d6-845ab56d1f58 | -6.33213 | -43.83345 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a4385345-a963-341f-ba58-25d431eb0e60 | -7.4635 | -42.82088 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 1ff90631-0b35-368f-8878-c908cebea06d | -5.71112 | -53.4589 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 37bb6977-49ac-3b2f-adcc-291e14612928 | -7.18739 | -44.31245 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7f6e2bb-0dc1-37a3-bb7b-4a52844e996d | -6.20196 | -37.9004 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8f250f62-31a5-35d3-a9c3-1a35741866f2 | -5.68306 | -42.59567 | 2026-10-08 16:20:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| afb9583a-df96-33d4-8444-3a6ef4f32fc6 | -1.97268 | -46.22053 | 2026-10-08 16:20:00 | NPP-375 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e22ca8d-2261-335f-9eac-66ff75584883 | -7.59579 | -42.39248 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 161.8 |
| d3336e8d-55b4-3b6a-832a-d785a199df1f | -5.50165 | -42.8538 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| eb0510d8-7222-3b7a-84e6-83100d706ba2 | -7.21522 | -44.27477 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abd12c8a-2260-3143-b3a8-2ff2fd3b9d27 | -3.43729 | -39.15716 | 2026-10-08 16:20:00 | NPP-375 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e075e362-1925-37e9-99a8-6e41cd016063 | -3.29579 | -44.67793 | 2026-10-08 16:20:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 921ef6cc-0936-35f5-a5fd-376d38fa1559 | -1.74356 | -50.14552 | 2026-10-08 16:20:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbc2929c-d262-33ad-8c7b-178ffcc3ea2c | -6.8517 | -39.458 | 2026-10-08 16:20:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1f63e70c-06bc-35fa-9a88-b215e3d7482a | -7.18081 | -44.3247 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 42882020-a5e4-3ff0-8ba0-facb72622a77 | -7.54045 | -42.09549 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| a940116c-a0da-3bba-a646-1b3370565c78 | -3.26623 | -42.95876 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5bfc6a83-7985-3e98-94f0-6bd0a90157c2 | -7.17099 | -47.79635 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b22601b2-f975-3006-85bb-8c42699cc547 | -3.00237 | -43.11695 | 2026-10-08 16:20:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 42c11de1-1931-392d-b024-9cf53399bdc0 | -5.96257 | -40.92107 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 0b721886-0f3e-38dd-b173-173b17ae6275 | -3.46563 | -45.10751 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 8660ce7f-7309-3291-b8ef-4ea4c0b8e0fe | -2.43086 | -49.63079 | 2026-10-08 16:20:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9bc592f5-ed2b-3410-bd94-138774068f2f | -5.74085 | -53.45415 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c40e68d0-98e6-3483-a820-ae1c12b8bf8d | -6.20202 | -52.86362 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 818670ee-ca14-3489-9d28-70bb1e3c5036 | -6.36559 | -42.90248 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c91a5aee-44eb-3b1b-badc-e808596f24e8 | -6.96663 | -47.66663 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 089595d1-0d55-32ab-ae96-af4577c0f60c | -1.56092 | -48.22593 | 2026-10-08 16:20:00 | NPP-375 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 005f1cd7-1111-3ac3-98fc-b9d963566e17 | -5.28742 | -42.73657 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| e52ec358-1efb-33ac-833b-bd6461756252 | -5.71673 | -41.6479 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0559d7f4-d169-37a4-9a06-7f4f8d89e69f | -1.11384 | -46.49607 | 2026-10-08 16:20:00 | NPP-375 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| acdf2c3e-09fc-30ac-9fb9-290206371097 | -6.14962 | -47.93459 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ddbc8562-513d-3050-9926-45545cc89935 | -6.15242 | -52.64333 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 27bfc6b1-8b12-38d8-b1b9-d44e2cdd9f69 | -3.28432 | -50.0888 | 2026-10-08 16:20:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2cc4e142-1576-3ff8-a447-b0f19f9002e5 | -7.80771 | -44.59309 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README288.md)
