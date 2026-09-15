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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 586cc9b4-cdbc-337a-a3a2-b3e84b1b32d5 | -7.47869 | -42.11954 | 2026-09-15 04:32:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f1b16ac-f0ac-3258-ae3a-bdb5bc713a53 | -3.42462 | -58.22235 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94782928-8bfe-3f6f-895e-f0160acabe77 | -6.26138 | -41.95343 | 2026-09-15 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa97b6e8-99ed-307b-8d4c-bff67824f854 | -7.08527 | -41.82615 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 444f2c4f-d83d-3aa3-92d7-f96bf8a020d7 | -4.11733 | -51.03165 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22551200-cc57-3c91-8219-3c222b601d7a | -7.08129 | -41.82559 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e4c377b4-cc4b-36a1-a357-5d4ca4e88ad4 | -3.97143 | -43.11551 | 2026-09-15 04:32:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1211bf21-16a0-3c6d-b8b7-82bc11c3ee15 | -6.2576 | -41.97824 | 2026-09-15 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2558eda7-9ae6-3af8-83ee-05abf8582a1a | -6.95796 | -44.54634 | 2026-09-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e905c5e-1e06-3f97-9301-ae9740b95ece | -5.63295 | -40.85464 | 2026-09-15 04:32:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c3b3e7f4-809e-36d7-89f8-a686fb9a14dd | -6.83708 | -51.49475 | 2026-09-15 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab272612-2acf-33a2-a9d9-14d4ea79dfbe | -2.9443 | -50.39717 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d63ba2ee-3f67-34e3-a0a6-251314cd8365 | -6.33307 | -44.12431 | 2026-09-15 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 647063bb-3d8a-35b0-a95c-6a639e0b78c0 | -7.24903 | -46.15653 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 68623e26-8606-3ab4-9914-3727959b9684 | -7.54888 | -44.89048 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8ec66fa-3ad7-3003-a4b0-6b932eeda9da | -7.09482 | -45.03946 | 2026-09-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3500ba9-fd1e-3e8a-8303-1a61ee666299 | -7.10679 | -47.48028 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d23eedf-ce26-356d-9574-83a3ac2f6973 | -5.46918 | -45.11671 | 2026-09-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b3a2d37-8934-3023-82eb-ef01bd5e14c5 | -6.95511 | -44.54203 | 2026-09-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6787b86f-e5ee-3b54-909e-2b7d2aaf930b | -7.22749 | -46.16386 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ba1f552-2de9-3463-bbed-f43acbf094d4 | -3.86472 | -51.97959 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a52afdc3-aec3-32ce-aa1f-df95a47ebfa6 | -4.24567 | -38.06078 | 2026-09-15 04:32:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 2e5f35d3-07f0-3f26-a516-674d9d122608 | -3.07545 | -51.19883 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5acbe272-fd36-3ce5-86d6-8e9c136851e4 | -6.15599 | -52.79671 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cfea572-6af0-3a8a-9076-fc4ce8ad3a39 | -6.00645 | -52.18556 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb40a057-64b6-3b78-be76-49d4a36047de | -2.95847 | -50.40985 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d38d425-3f61-3189-8b68-ef128e4c500d | -3.3323 | -54.18956 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b6e1a48-f7b8-374b-a81a-df4943c5f67b | -3.25511 | -47.09011 | 2026-09-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98ceca0c-6f83-334f-b6af-c40e3920e421 | -7.09795 | -41.82272 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 87e0d512-0725-37b2-8da5-c5fd30b73190 | -4.95584 | -45.14584 | 2026-09-15 04:32:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b9bed55c-7988-3d5e-8618-804b024e56c0 | -8.29252 | -41.35525 | 2026-09-15 04:32:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4461d8b4-b1ce-31d2-8cc6-981c2858ca44 | -6.78678 | -46.46004 | 2026-09-15 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d62c604-ac7f-395f-aa55-8456fe9e0a1f | -7.29178 | -46.74653 | 2026-09-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e75a6aad-b4e4-363e-adc3-6a9f1c16676b | -3.84938 | -51.76118 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85cbbd26-b2fa-3852-9e1b-2f4400e6b174 | -2.96091 | -50.39469 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| efe6d279-9e81-3007-a1c7-1af0b649d2ee | -2.89729 | -50.43638 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d1eb9142-2e53-39fe-b17d-15b9c948d6ae | -7.16171 | -42.09746 | 2026-09-15 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a79378a7-679d-3404-b66d-ec4c6d5dfed9 | -8.39726 | -42.2192 | 2026-09-15 04:32:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f691a6b0-417b-3562-bbd6-69e1186fc4ad | -5.7117 | -51.8506 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62c45d86-1bf4-3ead-8775-11fd15213ad5 | -3.10901 | -53.95369 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d98650be-08aa-3053-84f2-4606fff281a3 | -7.54739 | -46.86928 | 2026-09-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e01ef982-caa7-3dfb-8dcc-7d53b7e942b5 | 0.17825 | -51.47527 | 2026-09-15 04:32:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 981917ae-50c4-37b4-8fc5-4e6c0763af22 | -2.90376 | -50.42179 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e2e8529f-c4fd-319b-9e44-a8084075f43d | -6.06843 | -57.86467 | 2026-09-15 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 812eec11-8701-34c6-805a-dcf187e6f966 | -8.02882 | -39.00595 | 2026-09-15 04:32:00 | NOAA-20 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f52a7562-1776-31fe-af6c-71b3d5c7180f | -2.91396 | -50.43392 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7497d4b5-284f-3a74-8a99-78771cedfcf7 | -3.78266 | -51.34544 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d18979d3-8921-333c-b226-af5f79f920ec | -6.16451 | -52.7458 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 774eb240-531b-3557-88a9-64b69e22a28d | -3.07307 | -50.57526 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b58663d2-4114-30dc-8637-59270b603f88 | -7.10346 | -47.47974 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c96cccf5-7bdf-3f90-b4b0-b6355c0fab94 | -5.07501 | -56.24942 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3e3476a-7476-308c-b983-8b046eddde77 | -6.94976 | -42.56227 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f290a374-f173-3272-9dba-cadc31e7ffd6 | -3.57897 | -58.54903 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 862dc4fa-ec7c-3108-aedd-bb81965c5b71 | -3.58268 | -58.54732 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bf7dfa7-6cf3-3642-929d-ada68064be37 | -2.95533 | -50.40417 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc233f5d-0f4d-33d4-b175-65bea3e6ca00 | -1.00879 | -53.04091 | 2026-09-15 04:32:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea8c591b-3305-3c71-9d57-669364bc4a40 | -3.49676 | -50.3845 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4abe65a8-e8e3-3868-b621-189f24715684 | -2.9872 | -39.97148 | 2026-09-15 04:32:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ac99a1f9-f5f1-38ff-a7a7-6c3dd7c3d94a | -3.49056 | -50.37323 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2ad7a601-11d7-341a-8d5b-5671f223df6b | -4.08319 | -48.953 | 2026-09-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 192d0e56-49cd-3d44-b874-1e2e032bc930 | -3.41901 | -58.21557 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a28f0281-df6f-3916-9f95-3ab0153d92de | -4.36611 | -55.03394 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9b6c43c-409c-35bf-b867-b87cc1f083ff | -2.65444 | -57.5046 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fba66ae-7521-3467-92ec-7ad5ed10f765 | -3.23168 | -50.58116 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1eba7bb0-9157-3d51-aed7-16a83b482622 | -2.6628 | -57.55916 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d557bec7-7acd-38e4-bd38-27a0b1f8e390 | -3.25568 | -47.08656 | 2026-09-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97c2382a-c726-3e33-8b78-d8b852dcc14e | -3.07212 | -50.56796 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcfa53ed-d292-319e-bbce-ccc310d99c2b | -7.62712 | -46.14878 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dc81dd8-ede5-3c82-aea1-2392126404ae | -3.42557 | -58.21673 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12ce510a-2418-3731-bede-2e134a9781a0 | -6.10563 | -55.66675 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c65df90-2d79-3658-8341-232d84ab2c3c | -2.90292 | -50.42688 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dcba3d7b-53d1-3e86-b796-a001fe93ca77 | -3.10948 | -53.95084 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8895585-3b77-3e9b-9482-103220fbeb1c | -2.88937 | -50.43508 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ee96dc91-da43-3b47-85fe-fc0fa764b049 | -5.92718 | -53.54305 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd44706c-fa6a-397b-b96c-9e71cf27c558 | -3.07363 | -50.57175 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0da95b63-035f-33b0-b8e3-81ed9361e1b4 | -2.91416 | -50.40787 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2dca5e7b-843c-35f2-9bc6-a891da39d89a | -2.91665 | -50.3927 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39198260-3de6-3bc1-ac7b-6c4bdbf9943e | -4.95639 | -45.14231 | 2026-09-15 04:32:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fea7639-1750-3742-8c6c-1116fc44c9a3 | -1.22213 | -54.12887 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cf497ed-b242-38a9-a8d1-42de8a6c471b | -6.43108 | -43.06654 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42876f5c-8148-30e7-a811-a6818d707be6 | -2.95056 | -50.40859 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ef530db-8454-3a9e-8926-55c2c15769ef | -6.1913 | -44.01632 | 2026-09-15 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0c828a6-6b38-3099-9e31-3a9b87622dd6 | -6.94903 | -42.56937 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e3ac2dd3-04c0-3362-892d-f3e7296e811b | -4.5338 | -55.6193 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cced19a2-f55b-3ba5-a7db-b28550b8a826 | -2.92811 | -49.19965 | 2026-09-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c611fc7-800c-3d23-8c35-f90cf82d9919 | -7.01987 | -44.62104 | 2026-09-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9104524c-ee89-3fbc-bd9a-f2bdf1fd9396 | -6.32493 | -44.13097 | 2026-09-15 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36c9d826-155c-3f55-96be-9cb23a1e15af | -5.8512 | -51.94699 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bce01d5-1c64-34e9-9ac7-84a50492b819 | -7.38043 | -49.52248 | 2026-09-15 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 352f6202-2f65-3d07-a4d5-9de7737bd652 | -2.88872 | -50.42275 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0589666c-43e3-3552-a9da-198aadb35f2c | -7.46768 | -46.14837 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4d1519f-efa6-37b9-874a-33d1e28c1022 | -7.21088 | -46.13984 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27c0fbb9-081a-371d-b9a6-09b1a7d79985 | -7.10155 | -42.09624 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd94584f-55c0-3a99-9b52-4fbe58045636 | -7.09871 | -41.81759 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e966dcb-e4db-30b9-aa13-6155a500075e | -7.16735 | -42.11343 | 2026-09-15 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 38fd2ce4-43af-3945-9190-f69abdb1cf52 | -2.88712 | -50.43291 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 01915106-1564-3b80-9e61-6c636ddb2188 | -7.52069 | -47.33489 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dea5dcf2-6c26-3aa9-9345-6643f578abf4 | -5.31231 | -49.25533 | 2026-09-15 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 355ad61a-9b95-3299-9f47-e4c4eda0891b | -2.90771 | -50.42244 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e3f3df35-b1e6-38a5-81ee-6ceabe0c15b5 | -6.40063 | -44.04272 | 2026-09-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README40.md)
