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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d19da27-8086-3d82-96cf-000f273238bf | -2.79519 | -48.56743 | 2024-11-06 12:40:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 6962d375-f1a0-3d14-8a5a-f5f9ee7daf5c | -7.49979 | -39.56812 | 2024-11-06 12:40:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 93293b11-e664-3ea9-8f90-b59a4e3ec6d4 | -6.51252 | -44.67849 | 2024-11-06 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8e6cce0f-e248-3c90-bf9d-27f440342c88 | -4.96039 | -40.19394 | 2024-11-06 12:40:00 | TERRA_M-T | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 6814e878-aeda-3651-bc48-6aa5dead3878 | -4.17523 | -41.94058 | 2024-11-06 12:40:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 114d5ba4-9dc1-3e15-bc58-79dfba560479 | -8.11406 | -44.42369 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 2b1d9844-b58a-3478-8061-84990889e9b0 | -8.26372 | -44.85313 | 2024-11-06 12:40:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2c75b35f-d01e-318c-b0bf-3edad915267c | -3.04313 | -46.61944 | 2024-11-06 12:40:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab55897a-6353-375f-879e-8dd09951fba6 | -4.95817 | -40.18726 | 2024-11-06 12:40:00 | TERRA_M-T | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 4be8e14d-e9b9-315c-baed-dd8ef415a35a | -4.18986 | -44.29412 | 2024-11-06 12:40:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| adf398bb-4e0f-32f4-b12a-b86af898b29a | -6.06992 | -44.14326 | 2024-11-06 12:40:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 09202d1a-4f28-3c54-b385-0c96d1f71714 | -7.22948 | -44.30371 | 2024-11-06 12:40:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 838f919d-8e64-36ba-a422-96e060a6a768 | -3.4671 | -41.89994 | 2024-11-06 12:40:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| be67d1ec-8270-336d-8e1a-9f0c951e7fde | -6.5033 | -44.6772 | 2024-11-06 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a4195a62-9d93-38c6-9361-c56514f8f545 | -3.54984 | -47.38198 | 2024-11-06 12:40:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4eb89d38-e42c-3426-9dc3-7a019d3f415b | -8.32028 | -43.60096 | 2024-11-06 12:40:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 63913b97-82ba-3f4f-9e59-f6e35e626489 | -7.78314 | -44.08646 | 2024-11-06 12:40:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 472e5f42-01e7-3a66-815a-5c8ed81e2f9a | -2.82452 | -52.95114 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 15895f23-79d5-3cf8-a08c-6b0351786105 | -2.43747 | -45.83357 | 2024-11-06 12:40:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6078b18a-efaa-3fe5-bbc2-3062f2937ebf | -6.93091 | -47.78974 | 2024-11-06 12:40:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0983ed62-1b7f-33a4-90aa-e0633f9e0253 | -3.2511 | -48.46676 | 2024-11-06 12:40:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 585f456c-08a6-3847-a133-24f0f263ac06 | -6.30551 | -39.30663 | 2024-11-06 12:40:00 | TERRA_M-T | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 3e097a59-9e46-3626-992c-ef1558fc593c | -3.83364 | -44.14207 | 2024-11-06 12:40:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 69530e96-51b4-3186-a058-b181eebd3f04 | -6.95883 | -47.85008 | 2024-11-06 12:40:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 19c60f66-6668-3c5f-9160-2ece44a2054b | 0.3789 | -50.98335 | 2024-11-06 12:40:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 90af3d56-56a1-36ae-bf2b-29ab91fc02e4 | -4.34438 | -48.62287 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9d07d07a-de02-32ab-aba1-03164564b53e | -2.83163 | -52.90532 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 306.2 |
| 0e213b69-a946-3120-9da0-cb36e2b4b57b | -4.18204 | -44.28334 | 2024-11-06 12:40:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 76ef1a61-7697-37ad-9f8e-b3901885bb74 | -8.77637 | -44.07838 | 2024-11-06 12:40:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5b90ec72-e46c-39cb-8d0b-a1d5f3ccf127 | -2.82808 | -52.92817 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 9f803f60-7231-3a74-9d3b-3b1bcbec71cb | 0.39129 | -50.9572 | 2024-11-06 12:40:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 380390f0-4271-3497-ad44-009eb2276e03 | -7.22379 | -42.88422 | 2024-11-06 12:40:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 29bc6ce4-bcfd-396c-8a18-429b79ec790a | -3.63015 | -50.24945 | 2024-11-06 12:40:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| da4abc23-1dc2-3215-848a-f9a6c691efd8 | -3.96145 | -48.1594 | 2024-11-06 12:40:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3ff93eba-4688-3306-813f-3872536997ad | -6.49554 | -47.48451 | 2024-11-06 12:40:00 | TERRA_M-T | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| de9e034c-4d70-3117-b4e2-75f66341ff96 | -4.05788 | -46.9321 | 2024-11-06 12:40:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| dedf7c33-32b1-3972-9f6f-085d8ef35f04 | -3.54847 | -47.39142 | 2024-11-06 12:40:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9219189-b813-3704-bb34-ef3579b08d1b | -8.57625 | -44.86443 | 2024-11-06 12:40:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 73a02120-8f5e-317b-8662-ec2ae6ec97c5 | -2.81632 | -48.55929 | 2024-11-06 12:40:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fb447d0d-96db-3152-ba75-6b86d2b4bfcf | -4.12225 | -43.58385 | 2024-11-06 12:40:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a9b551f8-71c4-38b6-92a1-bbe811b3786e | -2.83859 | -52.90039 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 500.7 |
| 2a615fcb-8022-3401-b80f-f22f3e5bccf1 | -6.44477 | -41.94978 | 2024-11-06 12:40:00 | TERRA_M-T | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 71c33625-1c1a-3edf-ba8c-8aaef7cbbb23 | -6.56394 | -44.96445 | 2024-11-06 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a76c3aee-e2f6-314f-85e2-cbecfd3af89b | -2.92621 | -49.34229 | 2024-11-06 12:40:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a2edd80b-db45-371f-a58f-e7184a72bab4 | -7.81954 | -44.94127 | 2024-11-06 12:40:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9dc8f146-6429-3bdc-91bf-2f98e3cd4533 | -8.5037 | -42.08129 | 2024-11-06 12:40:00 | TERRA_M-T | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 4dd63494-548f-36df-9eae-70092247fefc | -7.61704 | -45.27057 | 2024-11-06 12:40:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06608ddf-bab3-3bac-bf1c-429d3bc1cdf8 | -6.53672 | -39.73576 | 2024-11-06 12:40:00 | TERRA_M-T | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 2a2f1c35-8337-3fb8-8cab-fc04b58c3d8b | -4.14127 | -43.58651 | 2024-11-06 12:40:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b80a92d3-2286-3909-a970-c87ef98a9b79 | -4.27478 | -43.74214 | 2024-11-06 12:40:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2a7da1f0-94dd-3ba1-a903-4e01c1a76fae | -1.8029 | -47.92046 | 2024-11-06 12:40:00 | TERRA_M-T | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d6f102e3-d22d-32f5-8d98-00e77b2a766e | -1.48902 | -47.21473 | 2024-11-06 12:40:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dfa2593a-3cf0-3291-b7ec-7e62f629d4a1 | -3.37057 | -48.68712 | 2024-11-06 12:40:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 026f053f-855e-3cf3-9265-945f028ad005 | 0.22352 | -51.0676 | 2024-11-06 12:40:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a6ff71ac-6659-338e-bcfd-8080a14f372b | -6.7417 | -45.72002 | 2024-11-06 12:40:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 662d491f-8a62-3f48-97a7-dd10bd39e49d | -3.04597 | -53.26165 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 28497ea5-7e27-3c22-9f22-7d889cb427dd | -8.78317 | -44.10153 | 2024-11-06 12:40:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 227282fe-ac47-3d49-9356-07daa57ec10e | -6.2536 | -46.17204 | 2024-11-06 12:40:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5e563760-593a-3234-9566-8084763a728a | -2.81432 | -52.92648 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 97f82a64-cd6e-3b11-8df6-107023ebeeeb | -1.31447 | -47.27598 | 2024-11-06 12:40:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 996e8bbd-d3f7-379d-8444-c38eec8db7de | -2.91414 | -51.04395 | 2024-11-06 12:40:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a79077ad-43da-3810-a239-c71529bb9208 | -4.73154 | -45.97868 | 2024-11-06 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7056b18e-ad04-33c5-90c4-424d1b2eb325 | -4.55262 | -38.95757 | 2024-11-06 12:40:00 | TERRA_M-T | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 33.2 |
| d581c9dc-5612-3b62-800e-715a6ccf9656 | -8.74902 | -41.69913 | 2024-11-06 12:40:00 | TERRA_M-T | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 41727f07-df37-3822-bda9-8ddda9bf21f0 | -8.12587 | -44.47741 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fa28d53c-b36d-3fb4-9a70-e161eed33a38 | -4.26378 | -43.44001 | 2024-11-06 12:40:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 89eb72bd-2a2d-3d48-8eea-ad92d8567e6d | -6.132 | -43.97471 | 2024-11-06 12:40:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 970b564d-ca6b-32d6-9bb0-bc6e9f5777d0 | -8.50184 | -42.09538 | 2024-11-06 12:40:00 | TERRA_M-T | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| fd7bfd31-102d-359a-b55e-a65f21cc4d95 | -5.28997 | -46.25627 | 2024-11-06 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2d6ba269-4cad-3b50-9627-dee782f15936 | -4.85698 | -38.99914 | 2024-11-06 12:40:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 32.3 |
| bc2230cc-f5dc-3469-b2cb-faf02836968b | -3.30442 | -43.84425 | 2024-11-06 12:40:00 | TERRA_M-T | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b3f24e58-fe9b-3abd-8264-eeff6134c148 | -6.50194 | -44.68679 | 2024-11-06 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 834a3515-7165-3df9-aa0b-688358b31b2d | -4.77854 | -48.67348 | 2024-11-06 12:40:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 563e17e3-9bbe-3551-b4ff-11a73b8a2784 | -6.54213 | -41.91077 | 2024-11-06 12:40:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| fed0c5d1-2f67-3cd4-a075-bbf708969140 | -5.15957 | -43.96024 | 2024-11-06 12:40:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5a22e145-1964-39ca-940b-5d2cc5c8bfd9 | -2.61391 | -47.91533 | 2024-11-06 12:40:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d984c30d-05f6-3dd2-a503-057865719a01 | -2.30428 | -46.17779 | 2024-11-06 12:40:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b56ae3e7-eab9-335a-8fea-b316ff854490 | -4.84919 | -48.52526 | 2024-11-06 12:40:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| ba47ec19-b087-33b3-90f8-51a5b080dadf | -6.63564 | -41.99487 | 2024-11-06 12:40:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 64299e38-d506-3efe-8454-7e23590f2e96 | -3.06211 | -50.50559 | 2024-11-06 12:40:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2cc159fa-b08d-3ab1-af12-82efcd979edc | -8.31873 | -43.61224 | 2024-11-06 12:40:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 71e1942b-23d9-3fa8-b141-cdbf2cc9fbe6 | -4.12485 | -46.85579 | 2024-11-06 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3b53d6f5-4f63-3b69-aa51-1412e89e582e | -4.13175 | -43.58524 | 2024-11-06 12:40:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 4d9fd2d4-808b-328e-8372-0e93aa93f4ca | -8.31716 | -43.62363 | 2024-11-06 12:40:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ed6a5e9b-a9d6-3612-bf89-59b85feab212 | -6.44611 | -41.95584 | 2024-11-06 12:40:00 | TERRA_M-T | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 2c052acc-1f00-3b16-b784-8c556b804d3d | -6.39938 | -43.82743 | 2024-11-06 12:40:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e1fd2a49-ff79-3fc8-8c1b-5267f910afce | -2.32259 | -48.85672 | 2024-11-06 12:40:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e258adba-8dcf-3c65-a465-ed4fbbc534ab | -4.8477 | -48.5354 | 2024-11-06 12:40:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 600ac137-e089-35a6-ab80-6f993b31876b | -7.09895 | -40.22692 | 2024-11-06 12:40:00 | TERRA_M-T | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 083d4376-415f-32e1-a32b-253a829227df | -8.08133 | -44.45027 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 4e7979df-a869-321a-be8f-b07c540d7864 | -6.52968 | -42.08126 | 2024-11-06 12:40:00 | TERRA_M-T | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 6259dee3-8ad3-3e6c-95ac-0f9395745a75 | -4.70654 | -44.54756 | 2024-11-06 12:40:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7926cade-80a3-3405-9d99-48d9407938b1 | -4.73744 | -43.79492 | 2024-11-06 12:40:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b62e7bbf-3efb-3e74-a583-afd2067faea2 | -2.81815 | -52.94413 | 2024-11-06 12:40:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 193.4 |
| ffcf80a4-52d5-3f86-8ef0-5b7bf212a208 | -5.35971 | -47.74279 | 2024-11-06 12:40:00 | TERRA_M-T | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| be549146-57bb-3087-a05a-08345532789f | -8.77785 | -44.0675 | 2024-11-06 12:40:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| c1abd620-4ac9-3271-9d12-ed7b181c8a88 | -2.4088 | -46.7912 | 2024-11-06 12:40:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d37a7721-e697-3701-9a67-b35cb20792dc | -4.13378 | -46.85702 | 2024-11-06 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| bb109504-2395-385b-9e8c-db962b932ebd | -4.5558 | -48.00922 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 41c60e08-db25-3527-af39-b5b5c682e2c5 | -4.13381 | -41.5716 | 2024-11-06 12:40:00 | TERRA_M-T | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |


[Clique aqui para ver as próximas entradas](README71.md)
