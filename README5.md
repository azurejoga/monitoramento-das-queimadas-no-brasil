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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa8d22de-b5d1-35f5-adf9-8162161d01e9 | -20.45598 | -44.18575 | 2025-06-03 03:34:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dcbb5b73-8af0-32d4-9906-b60489254a75 | -20.45667 | -44.1825 | 2025-06-03 03:34:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6752e383-6bd6-3a77-b3d9-b337f3bef9ef | -21.34207 | -48.67485 | 2025-06-03 03:34:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| b0ee8e27-e8f4-386e-91fa-81f0f87569b3 | -22.78249 | -43.04701 | 2025-06-03 03:34:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3050788-e35a-3bc2-9db0-f572264a9ff9 | -18.83409 | -47.68227 | 2025-06-03 03:34:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dc93c651-ccd3-39fe-b959-5af6e07c790a | -19.90714 | -41.84667 | 2025-06-03 03:34:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fd7973f7-0853-3f25-bb1f-f93969689332 | -20.45106 | -44.18441 | 2025-06-03 03:34:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fb2ecb21-81fe-3a9c-84bf-d75f8c0a851e | -18.83745 | -47.68666 | 2025-06-03 03:34:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cf590f51-0ef6-39c5-a53b-4981e7f2824f | -18.84042 | -47.6837 | 2025-06-03 03:34:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b08d7aaa-f689-38db-90e1-14da51a3695f | -21.34837 | -48.67668 | 2025-06-03 03:34:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8e8ec45e-9636-38a6-b055-fd4cbc1d3b2d | -18.8675 | -53.6434 | 2025-06-03 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 112.3 |
| c636455d-cb8d-3d51-bf53-f8186ebbe14e | -18.8875 | -53.6402 | 2025-06-03 03:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| cb69ae56-e289-37b0-a991-c2de931be088 | -6.96925 | -42.90874 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| fcfe99f7-1fed-31a3-b221-092e672c9838 | -7.70376 | -45.77818 | 2025-06-03 03:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10b848e3-4455-3f94-a375-7f7d7b486235 | -4.81236 | -45.26602 | 2025-06-03 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 25c5dfee-d811-30af-88f0-30b611ea02c5 | -7.28109 | -44.22241 | 2025-06-03 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c805df4-f0d3-32c3-a2a8-564e21586f1f | -6.72141 | -42.90615 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ce07b9fe-2ade-3085-b4a9-f8d715a0720f | -3.0366 | -49.42832 | 2025-06-03 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 39f417fb-3ef2-30bc-8685-92fd2326fa07 | -7.01601 | -44.58085 | 2025-06-03 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf3357f9-4b92-3729-8c88-b56d1360a3dc | -5.49928 | -35.58266 | 2025-06-03 03:55:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be28275d-1403-3ee0-aaa3-10c4adbc674d | -7.70461 | -45.77335 | 2025-06-03 03:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ee5ea96-43e1-3db9-b340-8b9da042f832 | -3.98735 | -48.4084 | 2025-06-03 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 630ee8e1-b18e-3d95-b251-291c0f24fab6 | -8.07587 | -43.11736 | 2025-06-03 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 704f6990-b5ee-34a1-8c1e-93e85f68caf1 | -7.37484 | -43.11688 | 2025-06-03 03:55:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72651c0c-cee4-341d-8a8c-82fba612bf7c | -8.06814 | -43.11603 | 2025-06-03 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e92b01ff-bb52-3344-b69e-3494cb5daab5 | -3.98979 | -48.40398 | 2025-06-03 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9326bd36-a471-367a-b5c2-47a16bf07d0c | -5.50281 | -35.58322 | 2025-06-03 03:55:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 056b87c0-176b-3824-8faf-b92c9d9bdd6c | -7.01744 | -44.57259 | 2025-06-03 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4c182390-69b6-3fc5-b627-5eb9c46557a8 | -6.73001 | -42.90253 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3eaae79d-a189-35ab-8977-4bb99992cab4 | -6.01041 | -44.32792 | 2025-06-03 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e104e98c-e87c-3922-89df-0aae0c242673 | -3.98391 | -48.40297 | 2025-06-03 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfd0d2a7-65da-3b80-a683-4d6e9f51ce44 | -7.69201 | -44.57341 | 2025-06-03 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc689dbe-bce9-377b-8aaa-8cc1f3f2eb9a | -3.03618 | -49.42229 | 2025-06-03 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0bf93ee-bce6-31b0-9a04-77e3671ef52f | -3.04169 | -49.42845 | 2025-06-03 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4741e06a-e535-3639-a481-8ea6fd9b4e82 | -7.86871 | -45.98488 | 2025-06-03 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f4e7790-2fcc-31ad-b0aa-2ec712d1b5cf | -7.00814 | -44.60055 | 2025-06-03 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 821e012a-2597-396c-ac1d-547ea19107aa | -6.91378 | -38.55787 | 2025-06-03 03:55:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e6c1ac46-94f4-3c31-9c44-34b104aabdc1 | -7.22989 | -43.12354 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 72c84e85-8eda-3556-b722-5f3ab3ce4e0a | -7.21731 | -43.12656 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f86a7494-c1b9-36e2-8d33-add9d2f1b7a7 | -7.68704 | -44.57671 | 2025-06-03 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e78c92af-b27f-3ede-878d-204948cae66f | -7.07947 | -46.5604 | 2025-06-03 03:55:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83924754-e5ee-31c8-9d63-e04e58017a5a | -7.19989 | -43.55919 | 2025-06-03 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e1b656eb-6602-386b-bb55-e843136b94ca | -5.65548 | -44.35256 | 2025-06-03 03:55:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfd484ad-6a03-352f-927c-66d13011282e | -6.72611 | -42.90189 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 95d9a081-3af8-3fbf-8512-22bcb117ae0b | -7.88485 | -46.22691 | 2025-06-03 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1458114c-79fe-357f-ba03-625fedddbc63 | -7.08542 | -46.5556 | 2025-06-03 03:55:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93d3b6ab-ec65-32f6-970b-0eb94bc3294c | -3.98909 | -48.40816 | 2025-06-03 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 748f73e9-548f-38c9-b80e-d49321265127 | -6.10299 | -43.95842 | 2025-06-03 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14ebb29e-af3a-3d77-b3e5-f52ce702925d | -6.72061 | -42.91106 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 88330ee1-a186-3233-a21f-0c5edb5eb809 | -7.02181 | -44.57298 | 2025-06-03 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aa0a348f-ffde-3c8c-85e4-612dfb3b1d81 | -6.24052 | -43.37797 | 2025-06-03 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cf2d1f8-8fdc-33ec-b80e-a9d1d9f224a6 | -7.56822 | -43.27598 | 2025-06-03 03:55:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 360720b1-ca80-394e-9922-c3bc49d613a0 | -8.07201 | -43.11669 | 2025-06-03 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 969ac87e-ba17-3342-a7cb-6e47f2501d90 | -3.98807 | -48.40425 | 2025-06-03 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d392e7d2-0003-3f32-82db-6b2d9daf6cea | -7.88526 | -46.22309 | 2025-06-03 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5d709c8-7652-3cad-82e8-ec1ea6c8f6fa | -7.00885 | -44.59647 | 2025-06-03 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4f2b9a60-e1cd-3a23-be4b-8afc17f99dc9 | -7.0837 | -46.55972 | 2025-06-03 03:55:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6490729f-84d9-3379-8c12-1f76d8eb5aac | -5.92308 | -45.53094 | 2025-06-03 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f4b9f7c-cc93-3bb1-8651-25216bf63ec6 | -7.22907 | -43.12852 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| abb45126-572d-3e6c-a3b8-a8cebb2e7425 | -6.97231 | -42.91428 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| c0bf4d5a-a941-3e5a-aa76-a298e10c0268 | -8.63247 | -47.13958 | 2025-06-03 03:55:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a5307bc-27b3-322d-b84d-a8cec4cdff27 | -7.01392 | -44.59293 | 2025-06-03 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0422404a-7dd0-3141-b749-84f1fcb67eca | -7.90449 | -50.36523 | 2025-06-03 03:55:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56de094a-7912-386a-870c-0c66fbcff3f0 | -7.95994 | -43.23702 | 2025-06-03 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93c105de-2f89-3f55-b780-b10384d2e0bd | -6.96843 | -42.91359 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 893375d2-adb9-3f1b-9591-8f23ed6e38a7 | -6.23709 | -43.37375 | 2025-06-03 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2315cd4-6c84-38bb-b03b-284ac83ca566 | -3.03749 | -49.42326 | 2025-06-03 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 55e17b6b-aacd-34b6-a140-178badbc0d46 | -7.56429 | -43.27529 | 2025-06-03 03:55:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04e69ddf-e866-3b77-a688-25a0a59e5802 | -6.97008 | -42.90389 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7fc4b5d3-9bfa-3ec8-98ac-66fbe2f25d39 | -7.90359 | -50.37014 | 2025-06-03 03:55:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2768a3c-4cbd-31f6-bc5c-5fccd6dd93c4 | -3.03533 | -49.42736 | 2025-06-03 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6cef457-94ad-300d-a930-8995013d940d | -7.22597 | -43.1229 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1dec6513-5148-30c5-82a1-85e6905f83c3 | -7.28175 | -44.2186 | 2025-06-03 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cc0e7ed-ef07-33da-8e28-27f10a699cab | -4.81892 | -44.35367 | 2025-06-03 03:55:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8b06cba-1913-3ea0-afc6-38c3713d1f74 | -8.07431 | -34.97628 | 2025-06-03 03:55:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1d5c3af6-7786-3d00-b997-10fe97fa7763 | -3.98877 | -48.40026 | 2025-06-03 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8191d78-11ca-35e9-aa98-fd5449d1134c | -6.97396 | -42.90454 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f2dc2c0f-c00e-3e2e-bee1-0ea729504493 | -7.88575 | -46.22172 | 2025-06-03 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63fbd417-d089-3bea-8979-14479a5d202e | -7.01322 | -44.59694 | 2025-06-03 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f687a00-c8c5-3be5-8e43-fec877189bf3 | -7.01672 | -44.57673 | 2025-06-03 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fc616de-d54d-3a43-8570-4956b55890d6 | -7.88433 | -46.22826 | 2025-06-03 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fce4085c-6e55-3525-b2a2-e8437501f5b2 | -6.71978 | -42.91609 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 6112a352-e205-3f63-bd9c-dc973cd263b3 | -8.09643 | -46.27903 | 2025-06-03 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6be5fc9-0abf-3945-97bb-17be6a567348 | -4.81319 | -45.26103 | 2025-06-03 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8249e9c-467a-3911-bac2-ae5221d4c41d | -8.08054 | -43.11322 | 2025-06-03 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5bafe2e7-17c4-3e9e-b07f-1b332bc9a7c4 | -6.9171 | -38.55839 | 2025-06-03 03:55:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 727fd2b9-5ff5-3e0a-bb81-b53558e4a001 | -7.22123 | -43.1272 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 98571730-50d4-3a5a-9a70-ca1359fd433f | -8.07668 | -43.11254 | 2025-06-03 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3174c902-4233-3067-8f86-5ec5994bd6e4 | -7.68774 | -44.57267 | 2025-06-03 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13da2171-70dd-3eb5-a9ed-06fa2d3c9fa9 | -4.80848 | -45.26033 | 2025-06-03 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4bf0455-6852-3dc7-bca1-94dd4009e5a8 | -8.07974 | -43.11803 | 2025-06-03 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| da23d739-72f5-3d40-8843-cbda13674df9 | -2.94288 | -41.73227 | 2025-06-03 03:55:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b11261d-9a39-31f2-9395-f208196cd712 | -7.22515 | -43.12786 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 75287a94-29b1-3f67-b086-8d84e707cdd7 | -8.46781 | -46.50753 | 2025-06-03 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b868353b-7ef8-3aff-b78d-5f4cedd37412 | -6.97313 | -42.90942 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 21362c4a-4060-3c3d-803d-cbaba24b097f | -4.82334 | -44.3544 | 2025-06-03 03:55:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bfca7e3-0a9a-35ed-bd78-2d0845adcf25 | -7.68277 | -44.57597 | 2025-06-03 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e40e27fa-c821-3452-a406-b3ee051dd49a | -6.97089 | -42.89907 | 2025-06-03 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bb2702f4-88b8-381d-8b03-fafdab950f41 | -10.23389 | -52.22521 | 2025-06-03 03:57:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e9d3407-9b35-34e7-8a76-a71f209a1874 | -11.57678 | -47.44994 | 2025-06-03 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README6.md)
