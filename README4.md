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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 947f6a1d-dbd2-3c11-b905-082b209b4a32 | -14.0349 | -47.61973 | 2026-05-04 11:42:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1523ef55-b110-3302-9991-8239cbbfd671 | -15.07878 | -42.3659 | 2026-05-04 11:42:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 97c2b645-5964-3003-b5ba-ac89141598f4 | -11.78982 | -43.62663 | 2026-05-04 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 27ea81d8-b374-3bab-829a-1df1cf1164ef | -15.07743 | -42.37592 | 2026-05-04 11:42:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 8.5 |
| e9db2688-936f-3c95-b491-df5f05c05c18 | -14.04308 | -47.63385 | 2026-05-04 11:42:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 6f0b6bef-29ca-37c5-b784-e7140e0f1401 | -13.18215 | -45.27936 | 2026-05-04 11:42:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e501d726-9272-3661-af23-0917381a7e84 | -15.93143 | -43.72762 | 2026-05-04 11:42:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71f0bfa8-0397-3103-8786-8387fd17c355 | -11.7985 | -40.08121 | 2026-05-04 11:42:00 | TERRA_M-M | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 344537cc-1bf9-3e7e-a69e-f74eb2fc9d58 | -14.03298 | -47.63205 | 2026-05-04 11:42:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| f119e3a2-a52e-35f3-828c-a28fb4a1b160 | -11.88629 | -43.79944 | 2026-05-04 11:42:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a6fc406-063a-30d5-aaaa-e8b5b5d06528 | -15.53689 | -41.68586 | 2026-05-04 11:42:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| fc0b2530-0fcd-32a8-b4b4-c5e1b2a69c17 | -11.43429 | -44.68233 | 2026-05-04 11:42:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 34d549de-c604-3751-a93e-91f6b588b0e1 | -11.43565 | -44.67305 | 2026-05-04 11:42:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c7e48c50-287e-3544-b2dd-e3bf73f73864 | -15.53832 | -41.67493 | 2026-05-04 11:42:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| 0a630944-6d44-3fde-adb3-513a880a8c56 | -11.885 | -43.80841 | 2026-05-04 11:42:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 714eee74-9427-3fda-b96a-eff3db361344 | -20.44199 | -45.70332 | 2026-05-04 11:45:00 | TERRA_M-M | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d33c50ca-c33e-304f-9a64-43a36f56da33 | -20.35179 | -48.30028 | 2026-05-04 11:45:00 | TERRA_M-M | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f8d8246-08e6-3c20-8680-7b3ddfb9f27a | -18.72462 | -46.89674 | 2026-05-04 11:45:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 808a246a-a862-3ce1-a982-f6624385c551 | -21.85287 | -45.37284 | 2026-05-04 11:45:00 | TERRA_M-M | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4729152e-0ce0-3cb0-9536-de78edb11735 | -12.3321 | -50.0073 | 2026-05-04 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 7019e267-96c4-3fde-a36f-d8a8738dfaed | -12.3321 | -50.0073 | 2026-05-04 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| cb93e2cb-91ec-3b61-affe-1940d8093e1c | -12.3512 | -50.005 | 2026-05-04 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a17ca5f3-e48f-3d8c-9642-4f6ca4bc5c83 | -12.3321 | -50.0073 | 2026-05-04 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 98a966ff-0276-30fd-b160-02ae27528c34 | -12.3321 | -50.0073 | 2026-05-04 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| a7b4f9d6-ace6-3d74-86e8-32fe1a4d008b | -12.3512 | -50.005 | 2026-05-04 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e9f6d451-c631-3e84-993c-2f106295a1d4 | -12.3321 | -50.0073 | 2026-05-04 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 88f9738a-092b-3eef-ad4b-f4cb513c8e87 | -12.3512 | -50.005 | 2026-05-04 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 608e9681-40fe-39d1-b9a4-c654f9ac60c4 | -12.3321 | -50.0073 | 2026-05-04 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 3f7268ec-3101-3526-b771-2737df57fedb | -16.115 | -49.2355 | 2026-05-04 13:40:00 | GOES-19 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7942d0b7-31e1-3e97-bc38-819226214ec0 | -12.3512 | -50.005 | 2026-05-04 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3eab0637-fc5d-3af2-8795-02883d52d5a1 | -12.3321 | -50.0073 | 2026-05-04 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 5344200e-1973-3772-88a7-aff381cdfa4d | -16.115 | -49.2355 | 2026-05-04 13:50:00 | GOES-19 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8f323a19-bd45-336d-97fb-8790a0a7fa40 | -16.115 | -49.2355 | 2026-05-04 14:00:00 | GOES-19 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a7672f9b-01fb-3c4a-a8ad-6753c2e80191 | -12.2864 | -57.5421 | 2026-05-04 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| fd7768bf-cee2-346b-bb04-8e78e5343505 | -12.2862 | -57.5621 | 2026-05-04 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3dd36f20-1725-316f-a1b9-88f56713f34b | -12.2862 | -57.5621 | 2026-05-04 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5287a797-6ebf-3f3a-82ce-ac77801d969b | -12.2864 | -57.5421 | 2026-05-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| d857473c-990f-3e7d-b706-6b9d2a684f64 | -12.2862 | -57.5621 | 2026-05-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 6565cdf2-c35d-386c-aca8-f525b0ce5ee2 | -12.2862 | -57.5621 | 2026-05-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 7a805e27-ab43-37d4-a7c5-177a9de30ca4 | -12.2864 | -57.5421 | 2026-05-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 0ab786b4-57b3-3c36-9f8a-6c8f2748c153 | -12.2862 | -57.5621 | 2026-05-04 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 4097bf74-70af-3a00-8574-febf35b0bf02 | -12.3512 | -50.005 | 2026-05-04 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 32ebeb7c-3e95-3ed1-8d94-03644c7e0c12 | -12.2864 | -57.5421 | 2026-05-04 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| e11fdc5f-7574-31be-b1ab-fc80055bdab3 | -12.3512 | -50.005 | 2026-05-04 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 697c1605-3aad-3dc5-9589-db0b23b88ef5 | -12.2862 | -57.5621 | 2026-05-04 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 292f0305-2028-3d20-bbaa-e82342deae9c | -12.2864 | -57.5421 | 2026-05-04 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 2ea73705-fde0-3e81-8077-ae027f4481d5 | -12.2862 | -57.5621 | 2026-05-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| b649366a-39dd-3086-afe9-603a571acdee | -12.679 | -45.4827 | 2026-05-04 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f4c0b84f-20f2-362c-8c15-d7b404682a19 | -12.2864 | -57.5421 | 2026-05-04 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 9b522032-0c49-3a32-a918-3bfc51654985 | -11.7917 | -43.6163 | 2026-05-04 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 73d7294c-be98-3bf4-9551-97ca1e97d7ae | -12.3512 | -50.005 | 2026-05-04 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ec9fbfd3-6dac-3ad6-8605-6bffacadb2af | -12.2864 | -57.5421 | 2026-05-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d84337f7-886b-3a4c-90bf-7d70b5bf3632 | -12.2862 | -57.5621 | 2026-05-04 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 37894256-15ee-33ef-8bb5-44f445935c7e | -12.2862 | -57.5621 | 2026-05-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 6cb1692d-b4e3-3e9d-8e3d-bdec539ae360 | -18.0067 | -52.9645 | 2026-05-04 15:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7a22b5b1-272f-3b4c-a182-2ccbee57ef3b | -12.2864 | -57.5421 | 2026-05-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 37389548-bc0a-3449-84d7-a11613bd3a61 | -12.307 | -57.4008 | 2026-05-04 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4ab0243f-927c-3e62-80c8-6465a7b1275c | -12.2862 | -57.5621 | 2026-05-04 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 6d47f02e-a560-3085-a0ae-eba568fdcaa9 | -12.2864 | -57.5421 | 2026-05-04 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |


