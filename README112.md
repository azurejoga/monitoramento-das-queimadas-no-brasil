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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45f67b8c-4731-34f9-8397-139aa3485cc7 | -7.9117 | -45.242 | 2025-09-04 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 82466763-5fc7-3d40-9075-fd41aea7a894 | -10.9867 | -45.9325 | 2025-09-04 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 447d2f4c-0ad5-388f-ad8c-f0bf4ef065f9 | -6.2977 | -45.2702 | 2025-09-04 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7a5a8415-0c13-37b6-8d34-a4e76fa486d6 | -22.6558 | -43.7079 | 2025-09-04 14:30:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 138.3 |
| ed60443e-1b02-3ce0-bbb9-fde275436707 | -10.1457 | -46.2424 | 2025-09-04 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 04be98d1-b81e-3d50-a5cc-b05f02f785b3 | -7.0128 | -43.2525 | 2025-09-04 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| a0086fd6-beeb-3078-b847-da20f930c74a | -5.699 | -45.2918 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 7cd7c28f-c961-38ff-8441-6579a195f3d6 | -5.829 | -45.3955 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 4a281c95-0110-34dd-b08f-71d70c1c9955 | -5.6784 | -45.5188 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| bd048905-a559-35e2-a186-1b102bdc495e | -8.8851 | -45.7541 | 2025-09-04 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 562815a1-7dd6-30ad-86bb-0514dfe3d4dd | -5.811 | -45.3065 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 5bbe8f8f-d68b-3cf4-ac13-0c0e839753ad | -6.8754 | -45.5625 | 2025-09-04 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 3564a997-4a4f-3201-9324-874e70b3c0f5 | -9.6851 | -51.0186 | 2025-09-04 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 16380316-ce58-336a-9643-e4b88f09008c | -6.2315 | -42.4515 | 2025-09-04 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 205.2 |
| cb3d786d-ca94-3ba0-be38-bb43c85f8530 | -8.0985 | -45.3598 | 2025-09-04 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 6237404b-eeca-30cb-b2bd-439c6022f48a | -6.7504 | -58.7268 | 2025-09-04 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 830546a8-fa1b-3f1f-84b0-e2b12ce77eef | -11.5963 | -52.155 | 2025-09-04 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 03cf5fee-5059-3979-8cb5-4d36c4f1457b | -8.0799 | -45.339 | 2025-09-04 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 178.8 |
| b2e39cf4-4c8d-3bd2-94b5-c3b6ad68bee3 | -11.2005 | -55.0195 | 2025-09-04 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 521f865e-6d38-3065-bf03-ef4d7155ba1b | -6.2393 | -43.5543 | 2025-09-04 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| cbbaadd7-1a98-364b-a706-05ae773dbd26 | -5.8105 | -45.3743 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ca43550a-ba5d-35ef-959c-05b13e21ceda | -5.7179 | -45.2679 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 35f91116-2392-3655-a92b-4dad99621abb | -22.6567 | -43.6825 | 2025-09-04 14:30:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 136.2 |
| 3509b26e-d88a-3d5e-8d91-8cdb3a0b4992 | -11.7887 | -50.6521 | 2025-09-04 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 441c9d71-3e95-3694-be1a-366591e2b03f | -11.5969 | -52.113 | 2025-09-04 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 217.5 |
| ca18ea0b-1366-3be2-bc0f-300b6615b4e5 | -8.0389 | -44.082 | 2025-09-04 14:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| b2dfd1eb-61f0-3168-9275-b19f949fde8a | -8.0417 | -45.3882 | 2025-09-04 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| acdd87e4-a60c-3e94-ac0c-22ced1a86241 | -12.5233 | -53.8071 | 2025-09-04 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 4d96b7a3-c4e0-3fed-a844-3e92f65fe6e3 | -5.7921 | -45.3304 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 224dcdc4-4e21-38ee-8f4f-13ba0fd30176 | -5.7736 | -45.3091 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 207.1 |
| b0210211-5f01-3d76-9a65-7458e262cb05 | -8.3644 | -48.3116 | 2025-09-04 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| aba44311-517c-3bc5-b8bf-379bd1edbc92 | -5.7547 | -45.3331 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 20e05315-e71b-39b3-9574-d00abfeff0a8 | -7.7252 | -50.3174 | 2025-09-04 14:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 82f8ea7d-a7c9-369e-b178-e80d3184af11 | -9.5025 | -57.8032 | 2025-09-04 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 24c5554c-169a-3fe1-abad-c89c56d39d4a | -6.8941 | -45.5609 | 2025-09-04 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 852c40c8-dad5-3335-923f-39068f139194 | -8.2001 | -49.5988 | 2025-09-04 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 4cf2e4f9-3213-31b8-8f0f-e0f59b17a65c | -11.6525 | -52.212 | 2025-09-04 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 1959572f-e256-30c9-aba6-be29d33f21b1 | -8.9037 | -45.7747 | 2025-09-04 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| fc1b97df-28e1-38f1-83b3-50eb7aa71d0c | -10.6577 | -51.5996 | 2025-09-04 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 157.9 |
| c17f1d68-c65d-352f-a47b-270a8f40d093 | -11.0062 | -45.9072 | 2025-09-04 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1f2bc05e-e9e4-3262-a3c0-57a3aaa0f87a | -9.7108 | -48.9636 | 2025-09-04 14:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 8db15a8e-f0cb-3f57-be50-57015dea18dc | -11.5856 | -47.7836 | 2025-09-04 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 3dd840f0-7ab8-3c6c-9fe4-582ac2984cf8 | -11.7385 | -47.7637 | 2025-09-04 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| dc7edcbc-3af9-3557-82e7-1679b5331e01 | -14.5852 | -53.0268 | 2025-09-04 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2f045ad0-24af-3129-aef7-fcc6a6e81045 | -5.7002 | -45.156 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a951a6d9-e53a-3362-b2e5-b4c07a8356d2 | -11.9635 | -45.7741 | 2025-09-04 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 331b38dc-6dda-3aa9-b96c-ec77453c8e2e | -15.229 | -52.7101 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 176.1 |
| dc30ca76-3cb2-3055-8cc8-d1ce4a9d5b2d | -7.7575 | -43.9719 | 2025-09-04 14:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 09d4cb74-ca79-3c5a-916f-27c3b46d124f | -7.6851 | -48.7386 | 2025-09-04 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 30d511d3-efa0-3f56-8227-a78003a71fa6 | -5.6963 | -45.6076 | 2025-09-04 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 7b88355a-e0d1-3756-8242-e8569bad2905 | -6.2289 | -42.7118 | 2025-09-04 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 713db496-0fae-3424-b96d-92ab333ab054 | -5.1191 | -43.0795 | 2025-09-04 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 59fb593f-239b-3f4c-bee8-70b1eda2fdf5 | -11.5972 | -52.092 | 2025-09-04 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| a8b8bd46-ee32-3ef2-9bba-69be01fe5b15 | -5.6992 | -45.2692 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 259.2 |
| f12ff264-adc3-3cb8-9fa4-e97a03437415 | -6.0317 | -43.6873 | 2025-09-04 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| a7583df0-cdc6-39de-af5e-72239824ae3a | -8.3641 | -48.3334 | 2025-09-04 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 358e7978-279a-3ef0-8771-0e111ec8b2f9 | -6.0234 | -46.6562 | 2025-09-04 14:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 0a7d2f6e-ec40-36b6-9b02-41d04076a8ff | -15.4564 | -53.0183 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 61cca13b-d1d8-384c-b563-f8a26ce18221 | -11.7884 | -50.6735 | 2025-09-04 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| eeb182c7-6e59-34c8-b729-03931847610e | -11.3897 | -43.5839 | 2025-09-04 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| a58c6104-7b26-3ce3-bf1a-7bc05af0efb7 | -9.6848 | -51.0397 | 2025-09-04 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 513a2a9b-17a3-37b5-af4a-a5fe354e2636 | -10.4658 | -50.3907 | 2025-09-04 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 1d33ccca-6ac1-367c-89ec-fc014811f4f9 | -11.853 | -51.453 | 2025-09-04 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8908e1c0-40e3-319b-884a-d9e44705137e | -6.1665 | -43.3273 | 2025-09-04 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| d46143e3-1752-36ee-a0be-b6dbeaeb1aad | -13.8647 | -47.9958 | 2025-09-04 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| ab9d502a-7c4c-3f0f-986e-f01494c48511 | -8.0796 | -45.3617 | 2025-09-04 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 89fe1f61-8350-3226-ae59-2c2ac6223400 | -5.8692 | -52.0868 | 2025-09-04 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5891ae18-d797-3775-a55b-a0957226ec09 | -6.2208 | -43.5325 | 2025-09-04 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 53dbb02c-2549-35fc-a7c4-60f88278cbac | -10.4818 | -53.6321 | 2025-09-04 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| c7f27596-9375-38d0-a9bd-f2e3956fe7f0 | -14.9865 | -50.0769 | 2025-09-04 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 45.8 |
| b1331b12-9208-3c7e-96e4-977062c99c31 | -5.7727 | -45.4221 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| e29090dd-6911-3c02-85b5-2c7da1a643ec | -11.6047 | -47.7811 | 2025-09-04 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 5e8f3879-e68b-366f-970e-08d9e89d2992 | -6.2062 | -45.0506 | 2025-09-04 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8a38140e-7401-335c-8f79-8f6089e7d354 | -12.9189 | -57.0074 | 2025-09-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 0c47aaad-66e9-3559-b956-e75eb9d249b7 | -5.4391 | -42.8925 | 2025-09-04 14:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| b214e85b-97c8-34f4-91c6-8f7be42eb351 | -5.7343 | -45.5375 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 618fbf22-ade2-31cd-ac76-8c834e706551 | -8.02 | -44.084 | 2025-09-04 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 8816aba6-c9cd-3094-b2cb-46a648aeabf4 | -11.6601 | -54.5093 | 2025-09-04 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 00ad53b2-6924-3876-8aa4-c53d06b7eeb2 | -16.0474 | -47.835 | 2025-09-04 14:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 94c5b6a7-ead4-3bb8-9211-aa91ac229638 | -12.4981 | -48.061 | 2025-09-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 0bce0af0-781a-3050-9e08-90f506c44dad | -7.7036 | -48.7587 | 2025-09-04 14:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 112.2 |
| c4256e0c-f688-3bbc-b701-cd838b76ddca | -5.753 | -45.5362 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7a4cd90b-c808-3abf-90d8-be072d3cc94d | -13.8453 | -47.9988 | 2025-09-04 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 265586b1-5da3-388f-8dfe-5bdba42f1eb2 | -8.0417 | -45.3882 | 2025-09-04 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 5fe542d4-94e4-3e7f-a2f5-a041ff38a342 | -22.6558 | -43.7079 | 2025-09-04 14:40:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 113.8 |
| 5b538e02-de8c-3083-b6a2-3b9bd0aef7f0 | -11.3888 | -43.6312 | 2025-09-04 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 23bdbc91-415b-32ff-8fa1-29973eba9897 | -5.7002 | -45.156 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d6aeaaba-6362-321c-acbc-82a9317a10d9 | -8.0389 | -44.082 | 2025-09-04 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| e0aa54cb-9be0-3b61-8b3d-4675a280c996 | -11.5782 | -52.094 | 2025-09-04 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 0d2f03c2-20c7-32ed-b751-f1344c71ad62 | -6.8941 | -45.5609 | 2025-09-04 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 507cc68d-073f-3331-b44a-15a06c97b2d3 | -8.0197 | -44.1072 | 2025-09-04 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a79990b3-d651-3eb1-b1af-eb9b55e9881c | -6.1665 | -43.3273 | 2025-09-04 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 6f54b834-e96f-302c-9b99-d43a3a3efa65 | -7.8078 | -46.0874 | 2025-09-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 02758f8e-b7b9-39cb-88f1-60855b129652 | -4.8862 | -41.771 | 2025-09-04 14:40:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 208.6 |
| 6339c406-763f-3efe-af3b-562fa0ac26e6 | -12.8999 | -57.0091 | 2025-09-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 18932b01-89c9-3345-a663-159c90b789aa | -5.7179 | -45.2679 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 80190b5d-79f6-3d00-82f1-3b9eb12319b1 | -17.0652 | -46.449 | 2025-09-04 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9826ca53-3f8c-38ba-8a38-eaaea8074dc2 | -12.5233 | -53.8071 | 2025-09-04 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 177.1 |
| c821b778-3337-3a4c-8c2c-f9b7bc093399 | -12.9189 | -57.0074 | 2025-09-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| fbc6cecd-235a-3173-9b25-a3cda5c2bc3e | -7.7066 | -50.3188 | 2025-09-04 14:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |


[Clique aqui para ver as próximas entradas](README113.md)
