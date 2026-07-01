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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a3860f6-c757-397b-8733-61ec2dc89184 | -5.80162 | -45.067 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 270b7b4b-926b-3d5f-9545-5652d8c97331 | -9.19954 | -45.32823 | 2026-07-01 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4a07128-d6ac-3146-a8cd-b77436cfb21d | -10.66665 | -54.57653 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb3445e9-9c0a-3f2c-89db-c5ec0ccebe61 | -4.57979 | -48.02798 | 2026-07-01 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a291b50-c9f5-36fe-8d77-e4f29d25795c | -7.71363 | -45.93574 | 2026-07-01 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe189c2f-ee77-39de-9dd5-aad4bc0320bc | -7.72462 | -44.56221 | 2026-07-01 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cb359ae-e17e-378d-a9b3-af9b255c18a0 | -7.71448 | -45.93224 | 2026-07-01 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f8978fd-dfa4-3fa7-a3b5-2a7a769db310 | -6.9161 | -42.84656 | 2026-07-01 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1c6485d3-22e7-3ef9-af46-c932e3c3b7c0 | -5.8034 | -45.05602 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d1158f8-999f-3ce0-a25c-42e8a665062b | -10.77799 | -53.54564 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a990145e-f74e-3408-8b6f-8bd30bc6af56 | -7.02022 | -45.42969 | 2026-07-01 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac553bdf-3fd6-3660-be43-cfa195bf7454 | -10.80867 | -49.33865 | 2026-07-01 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3eb4b6b-acd7-3afb-87d0-4d17380b2f46 | -7.0196 | -45.43343 | 2026-07-01 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa9282c9-e714-318f-9c03-aa19cc1a517c | -7.1015 | -46.51149 | 2026-07-01 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f55a213-87d1-3189-b58e-ac19c15a11e4 | -5.35295 | -45.19194 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 90a2d0c5-faed-397b-a95b-b25fc6378cb6 | -10.12585 | -52.1011 | 2026-07-01 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 173cbf03-230e-39b3-83d0-61020e2161c6 | -11.91836 | -43.39022 | 2026-07-01 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48dd8a79-57c0-351b-8090-5242cead6fb3 | -8.63707 | -47.53073 | 2026-07-01 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9382e2e9-64e1-3d46-bc5e-6df895a27295 | -5.79888 | -45.05162 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8e32e10-28e2-33ea-89c5-b105f02ba641 | -11.5788 | -46.80795 | 2026-07-01 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1bad70d-fb16-3421-818e-525886fadf70 | -6.91255 | -42.84597 | 2026-07-01 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9ddafde-f91a-3f20-8cc6-6b34d5858b72 | -5.79348 | -45.03923 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 520471f8-c322-3e1d-b615-47ca183dc91d | -7.47744 | -44.75809 | 2026-07-01 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f53efc0d-e9f1-32f4-80e9-b711183f01c5 | -10.92469 | -43.05777 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e8d805c8-902e-3e92-8f8f-abbb9b3ea23c | -8.98685 | -45.71923 | 2026-07-01 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e163543-96e4-3128-b69c-7250a033d452 | -9.89254 | -50.39821 | 2026-07-01 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| df7159f5-2fbb-3ad9-90df-5e65ba54e2cc | -5.79469 | -45.03183 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33d3d90b-2e9b-3100-a485-6468cecad433 | -11.54243 | -47.45697 | 2026-07-01 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d7f749bb-c2a4-3339-b95f-55a758715f83 | -5.79765 | -45.05888 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 986bdd63-69c6-3ba8-ba3a-cb1231e6e135 | -5.78939 | -45.03852 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07373fd0-b09a-3af9-8335-667071fdae38 | -9.2035 | -45.32891 | 2026-07-01 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42f2ea7e-f197-3e63-ab97-565c9b354cd1 | -7.72722 | -44.56024 | 2026-07-01 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80c6d87e-6288-318f-91a2-2952d2924e7a | -10.66781 | -54.53473 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| a7ee3666-ff79-3e90-bfa0-9d2e9c498ff5 | -7.01547 | -45.43271 | 2026-07-01 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4867c580-0a41-3193-a6f7-e5a6818232a0 | -6.18912 | -44.87089 | 2026-07-01 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b361420a-db40-36e1-af02-f95f8bfc4077 | -10.12248 | -52.08596 | 2026-07-01 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d7a01942-49a9-31e0-a94e-ed003d273def | -7.7094 | -45.93506 | 2026-07-01 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ad5da0e3-fd2e-3f0c-a824-50a577e59cdb | -11.92181 | -43.39081 | 2026-07-01 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16a6855f-a86c-31ee-ad89-628e1f1deca0 | -7.00628 | -42.78213 | 2026-07-01 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ccb514a-f753-3c38-8858-ffb400659ede | -6.83972 | -47.94271 | 2026-07-01 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8fb7767d-5ff8-35b2-8fdd-b557260baf47 | -10.43895 | -49.595 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3693a3c9-c817-3be8-8466-6597610195e1 | -9.69488 | -47.69241 | 2026-07-01 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb1bc70c-fa38-3a71-97ce-864c9a26c238 | -9.88637 | -50.40085 | 2026-07-01 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e60c1308-3186-33a9-95a2-e8fb8fba8ba1 | -7.00339 | -42.77755 | 2026-07-01 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52d9301a-3ac7-333f-9290-3d1be66aa866 | -7.72642 | -44.56515 | 2026-07-01 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c86a8f47-dea9-30c4-beca-007c2837fdb8 | -10.79271 | -48.22976 | 2026-07-01 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b164aa86-b782-32dc-93bf-5e1e52a64d29 | -8.65254 | -47.76843 | 2026-07-01 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f85634b-4fb0-3902-963f-7e6b70851a72 | -10.67041 | -54.52185 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 2f27cbb5-2e4b-3e6f-84d5-81e862bf6488 | -7.07932 | -45.65015 | 2026-07-01 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2395029b-5bd2-3599-b4ce-d2e87915cdb5 | -9.97952 | -48.24207 | 2026-07-01 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e868de3-9bc1-305b-be8a-6758b54a3b98 | -12.84493 | -44.35574 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4503ac53-aebe-3a0d-98e0-1221840fa00b | -12.7621 | -44.49694 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| ece22f6b-e45d-336b-a458-afa816b9cda8 | -12.83066 | -44.35332 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 375c300d-0a46-3eeb-b9dc-dcf1b5093356 | -12.84632 | -44.34742 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 6855f21a-3999-3dfe-a578-730e412516da | -17.71489 | -46.78925 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 82d98348-ffcf-339f-aae7-06a1ea37eefe | -19.693 | -44.92783 | 2026-07-01 04:04:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 78bfb6f5-cf3d-37e6-a4e0-d0c39bf0fbbe | -12.84345 | -44.34264 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| a66ae48a-d987-3296-bb6e-4555d52f4ec8 | -15.22081 | -42.59241 | 2026-07-01 04:04:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bef22cae-64c7-3128-80a6-1481d6e88183 | -11.30666 | -51.39931 | 2026-07-01 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 479e3998-213e-36d3-b47f-0f38edf91dc4 | -13.47553 | -47.87746 | 2026-07-01 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2df7eee7-8805-32bf-959d-8260c59ec716 | -17.44004 | -47.16528 | 2026-07-01 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f0024c0-a90a-3e8a-b57e-06c9e9578b32 | -12.76858 | -44.48065 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce1dfc89-9e3e-388c-8e68-fe600158e1e7 | -10.67374 | -54.57082 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9e1a11b-e240-3870-befd-009a566e76e8 | -12.84563 | -44.35158 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ed9f8b9d-82ce-35cd-ae2a-de2b550d4bbc | -15.43927 | -41.372 | 2026-07-01 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14b1bc7d-9b7d-384e-b77f-1f733c697c48 | -10.66814 | -54.52808 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5dc6304e-2310-351a-bac1-512817b9e5ad | -13.88651 | -45.08883 | 2026-07-01 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd7d8127-1600-33f7-bccb-ad3610f665ae | -18.12803 | -49.09605 | 2026-07-01 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69120b27-2aeb-3b70-877b-ef6f432bebb7 | -20.1531 | -45.30745 | 2026-07-01 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0c252eb4-25f3-370b-a310-107db2529f41 | -15.60387 | -43.59769 | 2026-07-01 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c726097-6302-3548-807b-82127ef6e535 | -10.67642 | -54.523 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 81bc6f02-ff1b-3920-aec6-8bdaec4c48bf | -10.66684 | -54.56918 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e26eab9b-edee-39ef-90a7-412bf2502441 | -18.52211 | -47.24346 | 2026-07-01 04:04:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50d850fc-2d6e-3bfc-a671-b1ce38f9edfa | -17.71399 | -46.7942 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9523b1fa-da4b-32b3-9fa8-f83151fc9b3b | -12.52816 | -48.28812 | 2026-07-01 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 409eab49-354c-3430-889a-c646f96e1c8a | -12.75865 | -44.48463 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f851bdae-3fad-35a3-97b2-3ce3417b39be | -12.7736 | -44.49458 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35f50ac4-80e6-345d-901f-4b2ce872bce4 | -12.75795 | -44.48887 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2bb0f4fb-c143-3a27-b61c-d7a71a3640f4 | -12.82352 | -44.35208 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dca077fa-640f-32d4-aa0c-cd8090be1348 | -12.52718 | -48.29045 | 2026-07-01 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff80746d-0356-37aa-a3ea-9b03508705c1 | -17.7169 | -46.79984 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07c9ddaa-be2a-3e00-ab2a-1b2a69c075ef | -17.70851 | -46.78569 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7913b182-e801-3fe5-ac9d-dc2cca414568 | -19.67088 | -46.19648 | 2026-07-01 04:04:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85ae4101-aded-3751-87a8-fd8a7b2b5ffe | -14.63014 | -54.4643 | 2026-07-01 04:04:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc50310c-5561-30a8-a6e9-a2c0da9ae988 | -10.66126 | -54.56116 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c84537f-5b44-3c92-88d9-e5c2e7f04f4f | -16.35341 | -56.66688 | 2026-07-01 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 22a26bc8-cc6b-39b8-9425-9f56932725a3 | -17.71198 | -46.78366 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 510121bd-3ae5-370c-bbe6-7baa1ce3d016 | -10.68204 | -54.53074 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 058b5383-48db-3aa6-9576-d03da21158a6 | -13.47668 | -47.87587 | 2026-07-01 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be31072f-30eb-39f1-8f0e-4fc4a85d6e38 | -12.83136 | -44.34914 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| c3d8a5a1-2173-3096-aeb6-5098991f81a8 | -11.30587 | -51.40333 | 2026-07-01 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 574597f1-4b79-3d65-81bf-13b12000c6b8 | -19.14643 | -44.70177 | 2026-07-01 04:04:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f228532-2863-3332-9915-cdf858e92259 | -12.83493 | -44.34975 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| bd2f8a36-d067-3023-97c5-4266ffb679dc | -12.77217 | -44.48127 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bd9801b-2039-30f8-abfa-2777b8b1f8b2 | -12.82849 | -44.34437 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 296601b7-787a-327d-b680-d4a516d1ac26 | -17.7696 | -43.99109 | 2026-07-01 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1f10ee1-a5fa-37a4-a59d-67af5db670f7 | -12.84206 | -44.35097 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| e482f69f-83f8-3c39-be43-6a4d855cae30 | -19.52575 | -43.93948 | 2026-07-01 04:04:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23b25dde-403b-3edd-9e97-2fb2894c1a9e | -12.76929 | -44.4982 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d21c789e-7068-3b5b-8cb0-fd8cefbcc8af | -10.6751 | -54.52938 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |


[Clique aqui para ver as próximas entradas](README12.md)
