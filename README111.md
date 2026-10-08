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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06d626a0-bc2c-3938-8162-f33275dcc309 | -3.28609 | -54.0589 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88cdbeca-feaa-36b5-8f17-ad8f65c82146 | -8.72829 | -45.18264 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e147f8d-35c7-3de3-bea2-fc18251d990f | -7.47384 | -42.84386 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15a12ccf-4931-3dea-8d25-66adaeabed17 | -4.00812 | -56.25352 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 531ddbbd-e30d-3fba-8abc-abc1d44c25a5 | -2.84514 | -54.11672 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79caaaad-d82a-3edf-b8c4-0f780c5b4e38 | -6.89782 | -45.89588 | 2026-10-08 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99bd94ac-9e82-3178-b780-a1b303367cf9 | -10.42724 | -54.44521 | 2026-10-08 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e3d7274-8cfd-33dc-8ab5-eda16845df66 | -3.30568 | -53.8694 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd37b344-9b8e-3cff-b4f6-5ac8a2ebcc71 | -3.65616 | -50.95044 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c0945df-3d6a-323a-bb61-c2c67a80be43 | -2.9313 | -53.95609 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 224b6f8a-e49d-3fad-bbd4-bb2681fb3d78 | -3.08861 | -54.28738 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07e64f98-182c-3bf5-bacc-621d38b06ef7 | -4.06373 | -54.03189 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5915f646-282c-368d-8bec-38bfbed32975 | -3.29622 | -54.04284 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fad5bc50-3f62-39c0-a4df-6ba6c2b1a391 | -5.83706 | -50.14396 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8aab711-cb85-3cf3-8756-c824672fdd33 | -3.01529 | -54.06511 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bfc9d69a-21d3-3e91-a817-b7d8f7b81525 | -3.55661 | -54.66484 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5872a40f-bff7-36bd-96c5-fdf52708c452 | -2.50595 | -56.14186 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 62d19369-8db1-3786-89ee-1d2b7127f2cb | -3.29465 | -54.02936 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74346519-1338-3f80-b319-7ae9ec258925 | -4.28461 | -50.78581 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a197ecb5-d20b-3f93-b38c-26902966c183 | -3.28335 | -54.00694 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1529a184-2e30-3693-ba53-fd57e211ad04 | -2.8769 | -54.20327 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9becf628-9ba0-339f-a52d-ab64c356c756 | -3.2902 | -51.57145 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c46b26ce-71f0-31bc-890e-f25959b254e0 | -2.49336 | -56.11177 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0268a64-c46b-3079-afa4-2548841fe751 | -3.58776 | -54.68871 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d984c937-99d2-3f15-bb48-423ac9c8bc34 | -3.30494 | -54.03537 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9bf46ef-0b46-3f0e-bdec-f208f5d247cc | -7.20213 | -46.52485 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3fb2f03-68cc-381f-a178-3ce14b5f716b | -6.46924 | -55.48267 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bbcf168-27b0-3a8d-9d00-7b202896d9d4 | -4.962 | -55.82462 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1567652-e031-31bb-b1fd-8e822b3be717 | -6.22514 | -52.78779 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ce157ed-a20d-331e-ad22-eafc2807585a | -4.96314 | -55.12069 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| de78e31d-794f-399b-b0ca-817fba42390c | -2.93239 | -54.11679 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66d8e88e-b0bb-385f-abd0-c6a34182db0d | -8.22648 | -46.34443 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60cc9642-601d-3b27-8321-17d63749a414 | -5.48434 | -42.8507 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 69ef5f7d-e8dc-35ee-8f33-d39a6cc6f7de | -8.91057 | -46.00269 | 2026-10-08 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb517ca8-05e7-30c8-84a0-33e1592012ee | -3.07345 | -54.14443 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2ba6c60-56e3-37c8-bc2a-1c0781411e5f | -3.04614 | -54.14912 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b0200fd-5053-3d58-8960-f757a98c6510 | -3.54846 | -50.09356 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5aa1168b-f474-3d64-a850-e2a8be11a54c | -2.94169 | -54.15436 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| de6d6761-8ac9-3d6f-9bb1-419d7b74e3eb | -6.14515 | -52.6497 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a1ac7a4-3877-3d9a-b4e5-b04bc0b9f997 | -2.98934 | -54.13288 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 423bf4bc-7fb3-3548-a1a8-54a5f05ac286 | -3.28297 | -54.03335 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f54aa8c-c85d-39bc-a0be-9b1fc403067f | -3.85494 | -50.42322 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34a1d365-f6cc-3b93-8cf9-408baf047858 | -9.3986 | -49.01102 | 2026-10-08 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0794580-b56c-3028-9e63-d27eef5bfcc5 | -3.029 | -53.90811 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 344615ce-0858-33c4-bd6c-169ea1de1311 | -11.2382 | -46.24347 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae093cb8-d1eb-3011-a366-45004e00c404 | -7.0081 | -59.12165 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3547fd07-2ecd-31f8-90b4-e4eab3e94b71 | -5.04376 | -49.77255 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d831f15f-4955-38ed-bd32-59fa32533605 | -3.44044 | -56.94158 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5eb82c5-f24e-3dcb-924a-49adc7d3472e | -3.78526 | -50.75655 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0795d77-93c1-32a9-9466-83eb34449baf | -4.18571 | -51.09403 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6c608e7-579e-397c-a022-317aa69eecee | -4.37807 | -55.16021 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1734450c-3f2f-3e19-be64-2f691fcc2b65 | -7.16312 | -55.1195 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4ed69b3-b420-3c39-a37f-5534797873cc | -3.11998 | -53.7864 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0869e8a9-34ef-3b3c-88e7-656124792454 | -7.0044 | -59.11912 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c6ec0314-e3d5-3d49-b889-687c69a94736 | -3.16692 | -58.63355 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4ceaeac-d0cd-3636-a229-8150183b009f | -2.48604 | -56.13063 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 73ee1760-65b4-3e2f-9e1c-92ee9e72229d | -6.31968 | -43.34363 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 67b13a57-0b7a-33a7-8fdd-81f6a023ba49 | -4.15919 | -55.1449 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fb2192d-da33-3341-a3a2-73ff4bb23fae | -3.00659 | -54.23978 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6315072b-b869-321b-b65d-047b4e090410 | -4.26786 | -46.399 | 2026-10-08 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a4f833a-e04f-37a2-a9e7-38450b3b3eff | -5.68457 | -53.4827 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55926597-51f4-3d19-b0be-dc85d3e2ac7d | -3.8406 | -55.98499 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb150c2f-9f15-3f35-b2c1-0991baa68e7d | -3.80748 | -55.69916 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10493e28-6ade-3ad8-8445-03a4169e9bf7 | -4.09659 | -53.98959 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dac84ef-e312-3100-a0e8-02ec2190d967 | -4.07392 | -59.8396 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 48d75ff1-8b24-3929-84af-8c5b30c50cd1 | -2.39263 | -57.89175 | 2026-10-08 04:46:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0a016cac-43e8-342f-8ff8-dd4cdbc58795 | -2.77156 | -54.11069 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a0984eb-5cbd-3090-bfb7-08ff661ba801 | -7.22602 | -55.10672 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 601b6742-8f81-3934-bc10-e170a12ed953 | -3.59316 | -54.55754 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a764557-b81a-31b4-b30f-337f52402639 | -5.73504 | -41.7618 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7fa908cd-6ada-3eaf-b0fa-9d0a0d8bf6e8 | -6.11915 | -51.95705 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9be8db3a-bd7b-3bed-9956-f9356be60635 | -2.49274 | -56.11569 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e07e125e-2b43-3143-a07e-e07d5e6026eb | -7.88067 | -55.0046 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44d8495a-8ff5-368c-99fc-57224bf15106 | -4.38257 | -59.90369 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91060b27-d5c6-3f3a-b35a-f5f0084ef1d6 | -3.27102 | -54.01381 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dbbd2d9-7306-3cd1-a7a5-2dcdb83fd204 | -3.57324 | -54.65792 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a337efd-7a98-3710-914d-5aeaa106e4ac | -7.15132 | -46.52108 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25fa1a11-6086-3b31-8a66-11a88da05fdf | -3.00214 | -54.0765 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 20434554-1835-3f0d-9632-b72e6b2258eb | -3.05829 | -59.26895 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4df0e31b-08c2-3a91-b489-7dba06a6b6ab | -5.77888 | -52.36454 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a65e3976-b31e-3780-80c4-57c925adb3b2 | -5.24489 | -50.9124 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0798c555-289b-3a6f-9450-7206d7f977ec | -2.88856 | -54.17786 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b640632-dd80-3362-87e4-9c1a96fe830f | -7.22111 | -55.16044 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96be9fda-4dae-3a87-b344-38b560f4b7ce | -3.10669 | -54.1499 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b87e1e3c-4db8-3d51-a7b7-b819aa8cb145 | -7.88053 | -54.98259 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffb4471e-1f9a-3152-b8b6-8531d704c8ed | -2.96806 | -57.76797 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55b8ca64-68d7-39c6-bf96-f97538972e3b | -2.49956 | -56.07262 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b1c0bcc1-38df-3c0c-879b-c540d6d4f36e | -3.52558 | -54.66452 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55cf388f-5602-31a2-a72c-93a3ba74aaf5 | -3.28397 | -54.07195 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcbcf2a0-296d-3553-b011-3e9a0299a66b | -10.4216 | -47.26989 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 10ff01f6-57bc-3029-89cb-75611790de37 | -3.3102 | -54.04941 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c3fc5891-5bce-30e8-b8aa-62605bb67f26 | -5.33859 | -50.98753 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18a8e9c8-d742-3f76-af2d-f2ee298f6e93 | -11.24138 | -46.25241 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00ccd293-6cfc-3938-a6a6-74398ef12783 | -3.89092 | -55.87799 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f45e2eb7-e63c-39fa-9d61-7329a81d7935 | -3.80632 | -49.11304 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f6ef47e-94b4-302f-b88b-69b04893e5c6 | -4.13586 | -54.2574 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5196851-548c-3219-b078-de9edcffe44a | -2.46568 | -56.09535 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b72f8f9c-edab-3787-8848-d871e2ae4181 | -7.88502 | -55.0009 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad082cdd-1bb1-34c7-8c2e-a34544266772 | -7.20322 | -55.13005 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 925fe08d-7376-3ffb-9e50-ce25ee977926 | -7.47301 | -42.85005 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README112.md)
