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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3f08860-149b-3336-abf3-277d036e8c14 | -9.1781 | -59.60647 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ab809f8-cd21-363c-b081-17e51cd5babb | -6.87945 | -45.65719 | 2025-08-25 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a03b865-2bb3-397b-9a75-172a3e9fec6c | -9.00078 | -65.40086 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77c29c6d-def2-3d4c-91c6-55157a5293b5 | -6.83562 | -58.95031 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7487eb67-25cb-37c7-b6f2-fc1a8ff0427d | -11.93172 | -46.72808 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54f68840-dbaf-35dc-a356-d549f3d5201f | -8.59863 | -62.60713 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d009abd9-5679-38e6-824e-903fec2a033d | -8.87827 | -62.45992 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 68e85584-8334-372a-917e-04b302d11178 | -10.02827 | -51.07543 | 2025-08-25 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b8e2f72-8f2a-33b2-9023-4a14583112c0 | -10.89134 | -55.78257 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038ecebb-06b0-3386-8cd7-83bba9711a8b | -12.75864 | -48.11963 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5ea1510-f6c1-37bf-a992-905943af7c6e | -8.57761 | -62.62516 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddf8389e-1c6c-3df5-bcc5-616c0de58243 | -9.15284 | -59.47026 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c330c125-0ff9-314a-bcc1-d24368100678 | -11.13509 | -46.339 | 2025-08-25 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9259fc62-fe21-3c78-82ee-6075d5bb4bbc | -5.42385 | -60.17022 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6a45e33-0142-38b7-9a4b-a864e8080b2f | -5.8059 | -59.21249 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f20d4f6b-4aec-39d1-a0c9-9371992b8e72 | -9.19112 | -59.61714 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7bfceff-101b-3f7d-81bc-5c808fb255df | -8.06353 | -49.68988 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2628cea2-d3d1-3a34-a984-0b4b61af6237 | -10.72896 | -47.1122 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cfb0abe0-3992-389b-b804-21a30857d03a | -8.92605 | -62.43896 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7133f941-a757-35b9-be5f-6c69f40790aa | -9.64836 | -59.63767 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 567d4ab0-9ec8-365c-ac7b-712848674f8e | -11.60197 | -46.33257 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fca85273-abff-3bd9-aa8a-bd01c35ea9fe | -8.60196 | -62.59364 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37f8d747-85f3-31cf-8f7d-49850b475ccf | -7.62838 | -62.73069 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6839cfe6-09fe-3ea9-9d63-f1c8295bc9b7 | -9.20249 | -59.43653 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7c0f89-8efc-3758-b2f0-6423fa180ec2 | -8.89967 | -62.43852 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4d7a4c9-c636-36bf-bc41-6d756bad477d | -13.05398 | -46.32362 | 2025-08-25 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ac6324b-c8a2-3e61-9bd0-5607e7df836c | -9.09427 | -65.71776 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0223f2d7-4005-35ca-a951-a3d71c010d0b | -11.18378 | -55.01694 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d6d4c06-c202-3a61-933d-b0f3a1f1d93f | -10.40517 | -57.68152 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a925638-18f6-3930-a4f8-466a6d914d39 | -9.25177 | -59.6389 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e978a876-d2d1-3d7e-a45e-820020d69bc1 | -7.5314 | -63.81732 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03107a67-2444-390e-9aec-fbee155fcbda | -9.19424 | -59.64323 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86b86234-c144-305e-b789-88c5e3948652 | -6.03002 | -44.21244 | 2025-08-25 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 107058f2-f32d-3f46-b21f-f5bb0f1fac42 | -8.91533 | -62.42445 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fb9ac83-2654-31b1-b651-e9e9cf7964bb | -7.58106 | -45.23097 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f45ad7c-88d2-3a21-9cd4-43ce6770667c | -9.12381 | -60.33211 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d4a7819-5eb9-3c10-a487-2b0b01ba4f40 | -7.35355 | -57.62757 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 776c721e-c574-31ff-827f-92ae4f20f8af | -9.81091 | -64.25455 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6067ddd5-691a-3f63-a579-7fb1ab437953 | -7.65519 | -63.52671 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20a924f4-e2e1-36e7-a320-c4bf10f0912f | -9.20643 | -59.47936 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18c5c1d3-2ad2-3323-88a5-e55ab5f4feba | -6.62363 | -58.54284 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4f3628c-5a23-305b-81ef-3636d55415ce | -8.62209 | -62.63208 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7762f46f-4619-3f45-96b5-85063656cf2b | -7.35693 | -57.62812 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a125bc-3f81-34b7-bf51-415175a0814e | -8.12145 | -62.86516 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41adfca3-a9cf-376c-baea-63ca274f1443 | -6.68495 | -58.85676 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b785f820-6130-3aae-b939-6c057308f558 | -8.61848 | -62.62706 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89cf71a4-672c-3b76-95fa-7a027ff50dfd | -5.75573 | -57.57776 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e64386b9-9c0b-36f4-901b-70aaea6cc641 | -9.01356 | -65.38999 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db1ff9e7-7eec-3a6e-8be3-0f542c1e6703 | -8.90041 | -62.45967 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7d4f8a2-0bb3-3892-a6c4-019e75c2bfb4 | -9.20525 | -60.79444 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02703492-97d0-33a1-8cad-c36fef5158f5 | -6.75178 | -50.96417 | 2025-08-25 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8360cb34-85bb-38ca-a5da-55fe08d22fdf | -10.72836 | -47.11631 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fe587830-0cf2-388e-a7c7-801f592d7ddf | -9.1571 | -59.46675 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d116181-d0ec-33a4-85bf-3b4be8761b87 | -8.0674 | -47.31892 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2652ba19-ceb5-3288-8143-615bd52d8c74 | -9.15215 | -59.47438 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 610c4abc-418b-3aab-9463-ea5dd21da236 | -9.19622 | -59.45227 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3439bf7e-ec52-3904-8238-71286947cdd6 | -9.18304 | -60.78567 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 130082e1-b500-35bd-b8a7-a939a2e1999c | -8.17592 | -45.07079 | 2025-08-25 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23129036-9b11-3181-a543-a465981d3f1c | -9.18415 | -59.45867 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6ead6d82-9a9b-38cd-9106-19c30295833f | -9.06998 | -65.73026 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f9e9a5d-6d4c-3680-95bb-3818205c7abb | -9.15008 | -59.48677 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d0189a-a875-3e97-89d9-52cf03331fc2 | -11.17866 | -55.02772 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 842702a3-43d3-3a77-b5bd-3d7de7face61 | -4.96337 | -55.82102 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adfbaaf7-ca6c-3db4-bfee-3f0bdc5e896a | -11.27319 | -44.96556 | 2025-08-25 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6f7088d-64b3-385b-83c2-2f745a477b17 | -12.75977 | -48.11024 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 110d7b92-f861-370d-a2f0-30233313895f | -10.61207 | -55.0494 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 62f8f08a-cd36-3474-9bd6-e026c6069830 | -11.19532 | -48.46813 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d4ce6ef-10f8-3bc2-9547-7cc310c1d7c3 | -5.74488 | -57.57981 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61a23fe6-dc1c-3dac-b8fb-46a2920929de | -9.15642 | -59.47086 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25e0929d-a809-3153-acf8-f8a8dc428db9 | -9.00432 | -65.38164 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5dc707d-e15e-3320-bb9e-505f2b802cad | -9.49121 | -58.93806 | 2025-08-25 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1d2c6b1-47be-3ac7-902d-513ffa040a89 | -6.78374 | -59.65051 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44835206-b0aa-331f-b1d7-b62393c80141 | -8.21698 | -61.38158 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6abc7a93-429b-3a18-9e60-212b7a2d7222 | -9.61068 | -55.34887 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ecba8c6-318c-388f-8f56-7bea2e188d7c | -7.91057 | -63.08379 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96b2a354-32bb-3be2-9713-7a5117c98730 | -6.79845 | -58.62661 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f518b00-7172-328f-892e-7977acc045c3 | -6.77558 | -59.65374 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63cafcf6-3c2d-30ad-8971-0488966e813b | -6.82407 | -58.96267 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6c2e19b-a4ff-3c9e-b4cc-37c9c52c9ee8 | -9.20666 | -60.80959 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69651b91-8d6b-3ad1-a4a0-a136197d5554 | -9.65041 | -59.63659 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8448c574-b0a5-3762-a1b3-9077ac835ad3 | -8.12354 | -62.86859 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10a115cc-961b-37f6-b0b4-78ec34c372a0 | -8.1244 | -62.87492 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 466ed288-e4bb-35e3-8c78-9dfed9ebc1f1 | -9.18324 | -59.62013 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7bb209d-607e-3a06-b28f-cc2f778ad075 | -6.88462 | -45.6622 | 2025-08-25 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49a3e6df-7d02-331b-b629-b83b0e642141 | -8.94367 | -62.13457 | 2025-08-25 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49051f30-e265-3b0c-8b0d-8898607fba41 | -8.58487 | -62.63524 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1b349a7-57f6-3ec0-a135-743fcb8bb5a9 | -9.2678 | -59.78831 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7667bea9-d22e-36a8-a6b2-cbad14a35aac | -6.33749 | -58.18695 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0926305e-c671-3a45-981b-97117cb52825 | -7.47063 | -45.02571 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec791543-6443-3996-8d59-426fcc2e826e | -6.91262 | -62.99709 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c8dc05d-ff56-3ca3-9598-c8d83d17f8db | -5.43236 | -60.16858 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f2f93e78-0e69-30d4-bca7-b4024a7f7c2f | -11.19406 | -55.04165 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e4bf3bf-de60-3683-9674-410ed7573f9e | -11.20091 | -55.04269 | 2025-08-25 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 444628da-6a9d-305a-8b18-7a4f6d866927 | -8.22035 | -49.56738 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7bf017ae-3a84-353b-b937-0827bea8e713 | -8.51023 | -63.87273 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ee4c19f-03d4-3c01-bf7d-941f4560bd9d | -11.61847 | -46.24467 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e8e0686-f4b7-392b-9bc3-349bf20b9263 | -9.00315 | -65.38801 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91b21902-390c-39a2-b647-51989291aa1a | -6.91721 | -62.9979 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b8ba757-97b2-3960-93f3-eca1f82aca40 | -8.21233 | -61.38445 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 45fcea71-1eab-34a9-92aa-8975dd071ea2 | -9.08773 | -65.72352 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README66.md)
