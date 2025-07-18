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
| 7209062c-d3e6-360e-a3ec-ac5dbf68c5ae | -7.1651 | -43.59359 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18fbefeb-84e3-3d43-8640-3ba7df519875 | -6.91047 | -44.13126 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dace1a88-1ab4-3da2-ab76-896f846a78a8 | -6.99795 | -44.47563 | 2025-07-18 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14a77b0f-9bc0-3479-958e-60e23d408561 | -7.20239 | -43.01573 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63ccc81c-a053-3730-b14e-d0219cad9cf5 | -3.71463 | -49.07035 | 2025-07-18 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25b6ab24-6336-3f50-ac3d-5737cbe323fc | -5.64867 | -43.71399 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| bcb03b56-9548-368e-a908-f1c2c9034cfc | -3.82779 | -47.74582 | 2025-07-18 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2850296f-15f8-3153-9744-69f17f5aa037 | -5.20322 | -45.48599 | 2025-07-18 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 89c04736-8070-30ba-9647-07488dbeb66f | -4.10931 | -48.20789 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a202850d-7c1b-3b9a-90c5-72e261733002 | -5.74315 | -46.25377 | 2025-07-18 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5d4ed56-3949-3976-8de1-4cd7c385063b | -7.92703 | -42.88796 | 2025-07-18 04:25:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dbeefe77-a2d1-3321-a3bd-4619f21b32d1 | -7.10745 | -43.64467 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1f562a7-24fe-34dd-84a3-369129cefafb | -2.65468 | -48.80354 | 2025-07-18 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 356356db-10d0-3034-a365-c57012d26a89 | -7.17226 | -43.59472 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88380b4f-3105-34ce-b3a9-210a0dee5267 | -6.45733 | -45.07359 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a91f99c6-c432-3be8-9507-f51c8ac4c953 | -5.83969 | -44.09614 | 2025-07-18 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bfa0302-4b7a-3d27-97fb-5d3f9794e279 | -5.78088 | -45.07188 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1779fdb3-89da-3607-93e3-668752613780 | -7.05903 | -44.05747 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 458a12ff-07f0-37c1-be5b-9b66d83d8e7d | -5.74261 | -46.25721 | 2025-07-18 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7f10c83-9d42-3eca-b5f3-5afcbe1d5800 | -5.48641 | -43.08275 | 2025-07-18 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3bdb6b2-874f-3783-87de-fdc680151792 | -7.40719 | -43.84004 | 2025-07-18 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f32c5411-bb18-3da4-bab7-2caf1efc95bb | -5.73984 | -46.25325 | 2025-07-18 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c3c0b0f-0e0f-38d0-ba6c-b4a0ca016410 | -5.91687 | -43.47325 | 2025-07-18 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 700fb2b2-fabe-3510-8a33-46bbc238897c | -3.85795 | -50.08425 | 2025-07-18 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75d78af9-32e1-35f3-9c48-a92a61186e7e | -6.83742 | -42.74494 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 17ef104f-818c-3f90-8124-d72d2d2e41eb | -3.71396 | -49.07454 | 2025-07-18 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b4dddde-113d-3aed-bf19-345ca9f85178 | -5.78648 | -45.08003 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a29a109d-cd5a-3fcd-8cad-2e76c7d7fce4 | -6.16109 | -45.09379 | 2025-07-18 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9958f7d-c242-3bd2-8448-8aa277a115d1 | -7.34961 | -44.19525 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6112735-ef2b-30e4-bf4d-4a8883be23ce | -3.39575 | -47.48278 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 8e6f229e-4b29-3cf9-ad48-7693290f846b | -6.90062 | -44.12572 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15f0aad9-2d4c-39dd-97eb-fd070153af88 | -5.78983 | -45.08055 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de14ef4a-d7fd-337f-b662-c45a05898669 | -3.22632 | -46.79353 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0b3466d-22ed-336e-8118-23983fd57ec1 | -6.87999 | -41.7278 | 2025-07-18 04:25:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d293e0c-f976-348d-a73f-a169dffaff16 | -5.88933 | -44.91722 | 2025-07-18 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 618bb712-65b0-322f-822e-7ddbf446df40 | -4.15272 | -48.2178 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e9856d3-89c0-3f8e-9ad5-b808cbb8f443 | -5.61702 | -45.33923 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf8c8412-06ef-31a7-a947-077e14159be4 | -8.10948 | -43.14914 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e0061312-31ad-388a-8474-399112cb8e9c | -5.65508 | -43.71899 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 0217d006-3db4-3d6e-85d6-3a778d497400 | -7.19165 | -44.07249 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3033ea1d-8593-3509-b361-f5cd45bb510e | -6.86474 | -44.77875 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eaddd0b2-a50b-3e02-ba6d-63f4582eb331 | -5.66267 | -43.71617 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e290a203-211e-3473-9616-4f9d58358114 | -7.94391 | -43.85793 | 2025-07-18 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bed2944e-659d-3aa0-aa52-2d7a2e37af68 | -6.90989 | -44.13512 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39dd0427-72dc-39eb-be14-4ea216f0a708 | -3.38615 | -47.47753 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f22f7008-0fa0-3ed9-bf14-8a4c0edbb219 | -5.65627 | -43.71116 | 2025-07-18 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fa3621a8-64a6-3aa4-95ce-a9203d80c998 | -4.87599 | -48.90866 | 2025-07-18 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c57552c-8793-328a-b559-0fce37e273c2 | -5.59297 | -51.1945 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01426cc9-50dd-3ea3-ab1a-28b6ecf7d434 | -6.934 | -43.8093 | 2025-07-18 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7039cd0-227f-3629-ba0a-34815c41aaba | -6.81785 | -44.76088 | 2025-07-18 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbf16a88-dcf2-3c6e-81ad-05385d06194f | -5.79866 | -43.63179 | 2025-07-18 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f26fdeeb-cd52-3987-9290-ec98be9fbd60 | -3.03362 | -47.85994 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0822e58-6549-3dba-9d24-d14f13692307 | -6.69088 | -43.18379 | 2025-07-18 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 410fedc1-7358-3724-a00f-2537d2fd33b8 | -6.73239 | -44.33259 | 2025-07-18 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93ce3a74-42fc-30cb-91db-2a3fb25c2ff5 | -3.84572 | -50.06306 | 2025-07-18 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86fe93f3-55a1-3fc0-8e22-b073427f9ea5 | -7.25186 | -44.51279 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 019bfc25-3ef3-3000-900a-ea20168c95dc | -6.49721 | -43.46842 | 2025-07-18 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0d7cf8b-02be-36d0-95dd-0ed7850516d9 | -7.22483 | -44.13739 | 2025-07-18 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb21ba27-cca4-383c-ad3b-dc5cfcb7bfbc | -6.96487 | -43.74857 | 2025-07-18 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 037e614b-161b-3036-82a5-5c6039dc2687 | -3.11759 | -47.01192 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8742328b-4aab-33a4-a15b-16e08441da58 | -6.89063 | -42.77185 | 2025-07-18 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a936291-3595-337a-a6d7-8321a8826734 | -3.7308 | -53.99348 | 2025-07-18 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96c6ed25-0cb8-3513-85f6-b9f5e90a99e1 | -6.61969 | -47.19424 | 2025-07-18 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a07afb89-efb4-3c75-9a86-858e04721c7b | -6.94685 | -44.56012 | 2025-07-18 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 066995e2-77a1-3c14-859c-7f82b753c91d | -7.84129 | -44.83412 | 2025-07-18 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faa7df9c-b5c9-3062-8ed1-8707d903d6c9 | -5.52811 | -43.88643 | 2025-07-18 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3eda9db2-0e0a-3afb-bbdf-43d6147ee5f6 | -3.60946 | -43.54614 | 2025-07-18 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f012d24-8deb-3175-b4df-8e2e1c47ca97 | -6.40152 | -46.54856 | 2025-07-18 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84c365bc-45a8-38f8-9fd1-37d375727e16 | -3.38557 | -47.48118 | 2025-07-18 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8214dd-42b8-3643-aa15-84a450648d47 | -8.09032 | -43.15076 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 95dd8b08-d762-386a-af65-67c7c3800935 | -2.91075 | -48.24287 | 2025-07-18 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d619512-dcb9-37de-8646-d382c71991d2 | -6.91395 | -44.1318 | 2025-07-18 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15c2f5b3-eb70-377c-a3dc-9510f97e898a | -4.19429 | -48.22433 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31491aaf-7bda-311c-a5ff-11c3f1778779 | -7.05724 | -42.98283 | 2025-07-18 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b096f32-730b-33de-875b-78f989ba6890 | -7.61027 | -45.54995 | 2025-07-18 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68f528ed-d397-3f0b-be2b-c9a835a5509b | -5.75747 | -43.40064 | 2025-07-18 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a003b05-9c08-3bff-b37f-2d2aaab7c118 | -6.91524 | -44.8352 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d64ae0c9-4be1-32d9-beb4-279e6af463bc | -5.99764 | -52.19871 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb4c4088-bf14-32ec-b7bd-3103743ddc96 | -6.52733 | -43.14924 | 2025-07-18 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fc87217-ed14-327f-8a50-d1b3f5669273 | -6.86134 | -44.77821 | 2025-07-18 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45b61c6c-58ef-348b-ae42-21e1d520ad1d | -4.11039 | -47.93393 | 2025-07-18 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd1747f1-d62d-38bc-aff6-5a2893e9b4c3 | -5.83852 | -44.10378 | 2025-07-18 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bba18e0c-18d4-3b45-8504-af2044d2729e | -4.48383 | -48.86519 | 2025-07-18 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7474afa7-dc7a-3fa0-a009-046035fbab99 | -5.91748 | -43.46923 | 2025-07-18 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12dc6b33-068c-3824-91e1-ec3280dae36e | -7.13487 | -43.79703 | 2025-07-18 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0217956-e5e4-3152-a682-d062f2137a1f | -8.11318 | -43.1497 | 2025-07-18 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20b37fff-cac6-3833-a141-dcda8b6a4ae8 | -5.36175 | -45.12321 | 2025-07-18 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44c34018-edd5-39a5-97c4-7df57ebbb548 | -6.97439 | -43.73356 | 2025-07-18 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2b0c567-7291-33f9-9c32-614a30b169cc | -6.14511 | -47.76613 | 2025-07-18 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9de03a4c-b5ae-3c9e-89e8-0cf637ef23aa | -6.45985 | -45.3399 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2c4761a-5181-3c8a-b91a-7935e678f1d6 | -4.32491 | -48.39016 | 2025-07-18 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5bcad89-dc5c-396e-a798-5ffda1665723 | -6.37125 | -44.74629 | 2025-07-18 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61b667e3-926a-397d-bbe4-dfeeab4b4e4f | -5.16897 | -40.76241 | 2025-07-18 04:25:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30ee88ee-406b-38ad-835e-02dd3567d7d7 | -5.43908 | -46.28683 | 2025-07-18 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 75560dfd-17ea-3394-aadf-d5b8b8d860da | -6.14455 | -47.76971 | 2025-07-18 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3476c8f-4136-3679-bbd9-01517d618324 | -3.93641 | -50.44111 | 2025-07-18 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3572f870-3395-3b98-af47-b0b41b8b12cd | -4.95425 | -47.70383 | 2025-07-18 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c52f253c-1b7d-3200-97f0-6808a4669cb6 | -6.14848 | -47.76665 | 2025-07-18 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d793b1aa-07bb-3f48-a406-babc345bb162 | -6.96011 | -43.75607 | 2025-07-18 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67c12cc5-4099-3356-9926-7293468c76de | -6.63746 | -47.8553 | 2025-07-18 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README12.md)
