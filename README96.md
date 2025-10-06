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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72331f57-d647-33cc-9712-6a17f628548b | -8.9472 | -49.8545 | 2025-10-06 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e35b3093-adc2-32e9-a521-6f65dcbcbc71 | -12.9844 | -51.0433 | 2025-10-06 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 144ac94d-3a71-3895-9917-34e783625b01 | -6.8553 | -43.8958 | 2025-10-06 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 49a4c7b8-50fd-30be-ae7b-6398fbd14012 | -8.1891 | -44.1357 | 2025-10-06 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3b26d7f0-f744-3c86-8285-cc0461e08d27 | -7.8074 | -44.5209 | 2025-10-06 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f1e735c0-c36a-344a-9b2b-5eda7c8a3d55 | -14.8828 | -51.4777 | 2025-10-06 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 485.0 |
| 2ed654a1-21eb-3659-9d51-4706e856aa73 | -6.5941 | -43.7333 | 2025-10-06 14:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 60bce3bf-0507-33a5-8c46-f7dd15914e8f | -7.7496 | -46.2496 | 2025-10-06 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 27006742-b2d7-33a3-8335-d5a028276c90 | -6.6506 | -41.9613 | 2025-10-06 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 9e31f1a4-ae41-3926-93a1-57c9071a102f | -7.4672 | -43.0438 | 2025-10-06 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| c5b7b3d4-f3c8-355f-8d54-b6994f2b4432 | -8.5956 | -46.2798 | 2025-10-06 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e1deaf02-f277-3e5f-a0dc-71a355d74e13 | -9.3165 | -45.9779 | 2025-10-06 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| a8a7af53-ae1a-3402-be14-6a80167dbdcb | -8.1615 | -43.3465 | 2025-10-06 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 301a3180-0314-3d4d-a413-a3d29b1b267a | -7.5329 | -43.8552 | 2025-10-06 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9990d324-735c-3b89-8ff1-a360e1e35fa8 | -9.9779 | -48.7405 | 2025-10-06 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 312d6a47-106e-36bd-b0a6-18de513f9e86 | -6.7051 | -42.1473 | 2025-10-06 14:20:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 4be00776-30f2-34d5-9c1a-373dad6b7cf3 | -7.348 | -45.227 | 2025-10-06 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 0d29ff19-6d88-3e6d-ab24-98603ce3d3f2 | -7.2778 | -44.7778 | 2025-10-06 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| dd378020-1940-37f5-abd1-673a6eab32b7 | -17.2717 | -46.9164 | 2025-10-06 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 889e2cff-a13d-31a0-b691-f9366bb0edbc | -8.1699 | -44.1608 | 2025-10-06 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 232be190-babc-328c-b054-026e10fa31c4 | -8.6139 | -46.3227 | 2025-10-06 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 5b2b04d6-b04f-3b99-8052-8360f0bbc6d7 | -13.2586 | -48.4635 | 2025-10-06 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d66a1509-4a6f-3242-a5f8-d0b1af2204ad | -15.8868 | -46.2641 | 2025-10-06 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 31060be9-cc5b-37c7-bff7-1f83228997e7 | -12.3917 | -51.0726 | 2025-10-06 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 0e9acd70-9ebf-305e-a0fb-edeae77eb73b | -8.0866 | -44.791 | 2025-10-06 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 3a246794-99ab-37cb-92de-27d97eee960e | -7.2416 | -42.9957 | 2025-10-06 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 5d9b37f8-6439-3723-8319-c546a5ace116 | -8.6397 | -47.2769 | 2025-10-06 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 51a6c29c-81d3-3df2-aa93-e56072a9d02b | -3.95 | -41.6864 | 2025-10-06 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| c5f1cea7-97b6-3f5a-b361-236ae6f5f191 | -14.6703 | -48.3828 | 2025-10-06 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 054e11c9-0028-3604-93e7-91167ac5e576 | -9.6804 | -48.4014 | 2025-10-06 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| e8f09b93-44f4-3570-97d6-601c5cfed261 | -7.7368 | -42.5906 | 2025-10-06 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| ff5c937e-b7aa-3e35-902d-4cd03ba049b8 | -8.5196 | -46.3323 | 2025-10-06 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2aaf6f1b-70bd-35ba-8cc5-916cc716c87d | -8.1888 | -44.1588 | 2025-10-06 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 6b015484-60aa-3c6a-835f-4b7e09687a4f | -9.9587 | -48.7642 | 2025-10-06 14:20:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a3274f3b-98a7-395b-a214-c133141f53dc | -14.6325 | -52.5137 | 2025-10-06 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 17935dcb-bb00-385f-b6eb-b9f3126131c3 | -15.7499 | -46.2438 | 2025-10-06 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a1124192-98b4-33b5-9590-0f143016445b | -12.5541 | -48.1419 | 2025-10-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 609ce9d4-2bde-3ce1-8545-f1fdc5685cc6 | -8.1885 | -44.182 | 2025-10-06 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 75d0e01b-517b-30cd-91db-03dbe160c790 | -6.0804 | -42.5354 | 2025-10-06 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 67d95760-0be3-3115-8ea9-7d480a348488 | -9.9776 | -48.7622 | 2025-10-06 14:20:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 37b857a4-cb4e-3da4-b508-30fed68ae3d8 | -10.4054 | -45.3931 | 2025-10-06 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 25a5f3cc-e5ff-3707-b77b-817f26c9e48c | -11.6845 | -45.3103 | 2025-10-06 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7386367d-202f-3ef9-9faa-0216a63175bb | -13.3904 | -47.576 | 2025-10-06 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 50bca122-0059-3d2d-8d79-02ef24025a2b | -5.854 | -42.6486 | 2025-10-06 14:30:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 0ff9dea4-d9d5-37ac-b24e-6ce17dc68f12 | -7.2389 | -44.8955 | 2025-10-06 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 28321271-61ce-32ad-aeb2-569346490403 | -8.5578 | -46.2836 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a7100499-9e71-3bd5-999a-1c885266f09e | -5.7688 | -41.7278 | 2025-10-06 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| c958e666-6224-3e13-a3e6-ada07d12ea83 | -19.5986 | -44.639 | 2025-10-06 14:30:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e3b1a29d-d7eb-32bb-bb24-afe6444ce59e | -8.0866 | -44.791 | 2025-10-06 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| c239181a-3885-355f-9ccb-9d08dcb01746 | -7.2776 | -44.8007 | 2025-10-06 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 25325278-a373-3d67-812d-b2b66d29f0e8 | -10.4099 | -50.3324 | 2025-10-06 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 167.6 |
| f3d5d0a8-0af7-308e-ab30-026abb75ddef | -10.86 | -47.9621 | 2025-10-06 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6d56396f-54ed-350d-8c59-999536b50eee | -12.9841 | -51.0648 | 2025-10-06 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 293.1 |
| c6e0edf3-cfff-3d30-9c97-708ef2bd5f29 | -7.2662 | -44.1356 | 2025-10-06 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| ec2eb417-4e43-36af-95f3-ec831cde31a7 | -7.358 | -44.3344 | 2025-10-06 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 72dacd4f-f8ea-3079-aa24-e1440edbb4c5 | -7.7885 | -44.5228 | 2025-10-06 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a9343588-bc7c-3e47-9d9f-1f8bd19707d4 | -11.8033 | -45.0856 | 2025-10-06 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 49f670ab-8729-3172-a587-5f9d349a8080 | -5.8526 | -42.7901 | 2025-10-06 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 3c591018-f738-3c5c-ad5d-604520ee2d40 | -9.9587 | -48.7642 | 2025-10-06 14:30:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7be7e370-e2c6-3842-8f7f-fe80ad7cea59 | -3.95 | -41.6864 | 2025-10-06 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 30da1f04-94d9-3e3f-a25a-ef9b886b94ae | -13.0763 | -47.9127 | 2025-10-06 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ce008413-5e57-35db-b218-8a3455796f40 | -8.1699 | -44.1608 | 2025-10-06 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| fa2dd54e-b0f2-38fc-830a-d05c6ab9b514 | -7.348 | -45.227 | 2025-10-06 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 59f8d397-e499-3103-8b32-df3502a6da23 | -9.3162 | -46.0005 | 2025-10-06 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 55e37013-99a2-3225-b497-1dbf0759c446 | -1.3558 | -49.2732 | 2025-10-06 14:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6c2f1d16-1ebf-32a3-91cf-b75757656373 | -13.0759 | -47.9351 | 2025-10-06 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d155928c-2f65-3ac1-abc0-b0f421a7dee5 | -10.386 | -45.4184 | 2025-10-06 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 7648b858-c4df-37f2-a96c-a280d0bd519e | -8.8537 | -46.7228 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a79aa294-3141-3f4d-8e1e-2c24b6463c64 | -3.2713 | -42.6457 | 2025-10-06 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 6a7d15f5-3447-34d1-836f-f47b1b9c28d2 | -8.8351 | -46.7024 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b57fd2e8-44ec-3f60-8a7f-d0ed724c1bcb | -11.6849 | -45.2872 | 2025-10-06 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ef359737-0dcf-3f4f-9aa2-e207bfc903c6 | -16.0604 | -50.9364 | 2025-10-06 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ab064d55-60bc-3310-bb62-764818c86ce2 | -6.5424 | -45.1374 | 2025-10-06 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 64e5e4f9-7879-38a1-b71e-44541b5f9c6c | -8.5032 | -44.6556 | 2025-10-06 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4727a174-d229-3f0d-9fd0-f6eadbc332d6 | -17.9308 | -55.8758 | 2025-10-06 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.2 |
| bfdf3ba1-d1ab-34d1-9cbb-93861fb8bbe4 | -10.4285 | -50.3518 | 2025-10-06 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| aaabc9ff-8890-3307-9d08-a78ab558cbc5 | -10.1766 | -45.4449 | 2025-10-06 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 817b3b92-5018-3701-ab86-11be19f46f2e | -8.5576 | -46.306 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9fecfa7b-05ae-3490-a923-92d1bb133ce4 | -13.3706 | -47.6013 | 2025-10-06 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 311db6b9-7427-3c22-89a7-bec60a0808cc | -7.5922 | -45.2272 | 2025-10-06 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 11ec07ed-99ef-336a-86d2-d6ac3f9a9aaa | -7.8074 | -44.5209 | 2025-10-06 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8aa3cc9b-f96e-3f28-b5b3-e45ed8ad9733 | -6.6976 | -42.8354 | 2025-10-06 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 781e456f-6ef1-3ac3-8b50-5e3924eba669 | -11.8422 | -45.0567 | 2025-10-06 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ef4d8b46-8c35-3a5c-bf4c-5f8fc23665d2 | -14.882 | -51.5207 | 2025-10-06 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 078618be-e37b-379d-a6f2-af29b0cdb7cd | -7.2778 | -44.7778 | 2025-10-06 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 842378d4-5e1d-3a4c-979b-edafbff47199 | -6.6506 | -41.9613 | 2025-10-06 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| bfbfe57f-aa60-32da-a9ab-a7c660e0da65 | -8.5196 | -46.3323 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| abe8e0d4-14f0-3a1d-8d19-40f43fd0c63f | -6.5799 | -45.1344 | 2025-10-06 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| d4c2d6e8-0d91-3860-b46e-ccef1f1a1e42 | -12.4099 | -51.1344 | 2025-10-06 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e8eed452-0c55-3b8a-a137-29db620ca8d1 | -13.2515 | -47.7979 | 2025-10-06 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| e24338d0-f426-3b17-9620-7e604079a716 | -10.391 | -50.3344 | 2025-10-06 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 157.2 |
| afea8b7a-8ed0-394a-9608-4cfecdd8c1bd | -6.0602 | -42.6789 | 2025-10-06 14:30:00 | GOES-19 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 4014715b-04af-3b30-b095-31e031f13b24 | -6.454 | -44.5978 | 2025-10-06 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 21e8abc3-beca-3941-a51f-50c6fd2d65fe | -16.0083 | -56.0155 | 2025-10-06 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| ef7e3775-8f77-39d0-a0f5-c5f74c0328e4 | -15.9842 | -50.8395 | 2025-10-06 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5272653b-cbad-3042-9107-38873398b198 | -12.8205 | -50.528 | 2025-10-06 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 022c082b-d2b4-37aa-abad-9ab77a010601 | -7.5329 | -43.8552 | 2025-10-06 14:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 9133ba94-126f-3047-81b4-1580560946f1 | -8.1702 | -44.1377 | 2025-10-06 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1a55f257-4e65-3b7a-a0e2-2b24c0918887 | -3.2712 | -42.6692 | 2025-10-06 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4874b540-8ee1-33be-96f6-de3d9025e5de | -9.3354 | -45.9758 | 2025-10-06 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |


[Clique aqui para ver as próximas entradas](README97.md)
