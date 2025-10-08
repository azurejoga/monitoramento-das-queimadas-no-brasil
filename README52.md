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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53a3a9db-cdc9-32f9-b9a1-1e5fb1448b24 | -8.47282 | -46.28728 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a33993c1-4deb-3eb0-af0d-fea8dbe99904 | -15.34768 | -47.33265 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d70bd942-5bbf-37a0-ae30-857c93a30397 | -15.49208 | -47.93229 | 2025-10-08 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2b30917-bcba-3873-98ba-3d07b915494e | -8.89112 | -46.02675 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ac14ed7-27d5-34f5-8e5b-b43c3ab78618 | -17.43314 | -45.80798 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f654409-6131-3700-b5e7-5a29790fada8 | -7.8206 | -44.18433 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 958984e6-abca-305a-8672-0ec4e4109a3a | -8.47216 | -46.29131 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 52a35797-ed96-3681-ad3a-46fcb24604ae | -14.51584 | -46.93025 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b77b9d57-d3ce-3416-885c-78216cb8fa00 | -9.67706 | -45.67071 | 2025-10-08 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a6a9553-f198-3702-8242-17dc60358ae6 | -7.80114 | -46.02299 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00a0ebe2-99f3-3ceb-b80c-6c37cbebdbdb | -14.5398 | -48.70206 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48b04432-a3ac-34dd-9648-7a59e423436a | -7.77434 | -44.19505 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 858e8048-8b65-30ac-8158-85d2e055c199 | -20.26595 | -43.26167 | 2025-10-08 04:19:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 2c994b03-366a-3ede-aab9-574429820671 | -13.3028 | -48.02979 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b21d0253-7153-3c9f-aa79-00b988cdadcf | -13.79945 | -45.80365 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2981d95b-8256-34da-9773-ae8a0768f345 | -7.7632 | -44.20042 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6eb7d14-1629-338f-9db4-c8b7bfaf582b | -16.88795 | -46.9593 | 2025-10-08 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3f51f21-00e2-3d6a-bc42-38a3dea6b1a1 | -17.27768 | -42.64944 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f7c87c4-a60b-31f7-a403-3797bd41fab4 | -13.80281 | -45.80421 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67c8e3d7-ebb7-345e-9824-98f277925972 | -8.18472 | -43.33966 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c830b134-515d-3440-8423-86bcd2a8b3b0 | -7.80275 | -44.2103 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 309dd2ba-5b2f-328a-831b-e85f6551201a | -8.161 | -50.16557 | 2025-10-08 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 090c6e5f-7d61-3a18-8646-36c141a9f07b | -9.0877 | -47.95822 | 2025-10-08 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b14fbecc-1348-37da-b586-c782ea77438e | -9.19175 | -46.57024 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4860244a-65cc-30a0-88f3-8c5af836601e | -13.73335 | -45.71112 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b67074c-9c81-36e1-a793-9743dfa787a9 | -17.27361 | -58.11483 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 10dc3c07-7df6-36b5-9cb3-59e5f89ce66a | -15.39122 | -46.28088 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ed380f1-9722-33f0-a992-ad1011bdeefc | -15.28172 | -46.3112 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67bee1a0-4d91-3c07-aa6c-85b04a0f7859 | -7.80992 | -44.25118 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2399a4d-029e-3bd4-9d3e-9f9edb3fdae0 | -8.18582 | -43.33268 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 540729aa-3830-3dd5-aae5-35aed0144115 | -20.3814 | -44.44375 | 2025-10-08 04:19:00 | NPP-375D | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f529771-75c9-3aa6-bc70-86033a6078f3 | -13.84293 | -51.86221 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7b1edbf8-478b-3ce3-abe3-7e8c078d8a8c | -7.8195 | -44.16976 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed651206-4207-3412-8009-d61a055a86d8 | -16.88261 | -49.74236 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d47c2ee0-a9c9-37ef-9ccc-70a550d3b35d | -18.04841 | -44.44917 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1c8f431-a9e2-38ab-add4-a2048d5506e1 | -9.29514 | -45.65527 | 2025-10-08 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0df74073-1e9b-3e7d-b82f-eac16ed49e0a | -8.10705 | -44.77669 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb5b5ca5-546b-3719-86d7-1a2b637d0c2c | -17.6378 | -44.09735 | 2025-10-08 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72e6eba4-7950-35b3-9d65-814020aa4bbb | -19.30315 | -43.16582 | 2025-10-08 04:19:00 | NPP-375D | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 420ccde4-e3d2-3f0c-aa51-0d2bb7d1d047 | -16.74774 | -42.51425 | 2025-10-08 04:19:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1eda2eb-2cfc-3348-a2a9-ecc85a21587b | -19.38769 | -44.39001 | 2025-10-08 04:19:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d0caf9b-ae9b-3530-be4b-08442f8d5f7f | -9.18744 | -46.9144 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bba61e0f-a74d-3b2c-996a-1e2b8466df59 | -9.18894 | -47.80146 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0e68d8a7-5602-3ccb-b0aa-a1ee4853efcb | -17.4359 | -45.81218 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eda8d7b1-e49b-3a0c-a12a-7448b114bede | -14.71619 | -46.02467 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf829e1d-7f6a-30f7-a40f-f91257ced611 | -14.91585 | -46.81426 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0ad085b-fbb1-31b2-a104-584ecc03fb25 | -8.5283 | -46.23421 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c19b0e5d-4fa8-34e0-9351-e833846f854b | -8.40059 | -49.7387 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ab45379-ec8e-38ba-a882-7e761a7179d8 | -17.16633 | -56.60884 | 2025-10-08 04:19:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6cbb07ae-355d-36e9-91bf-0f550f242da4 | -7.58291 | -47.21022 | 2025-10-08 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84fd6d1c-daaf-3f69-b978-ea5de1ca46c4 | -8.5177 | -46.29792 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dd45019-d36c-30ef-a127-4feeec596e4a | -7.82064 | -44.1412 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ba0e917-781a-3dc6-b1dd-c18bc5cc2a0f | -8.59606 | -44.9032 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ae6ed37-d43f-3d67-9393-50cdf0b4d255 | -18.02515 | -44.94162 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35b910d6-b56c-35d7-ba4a-e5a7bfe32b14 | -17.29013 | -42.64984 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8bcdb4b1-db63-33ee-80e8-c63cd54ddcd1 | -7.78991 | -44.2263 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6094eb2e-9798-3540-96c3-ba5f22166c2a | -18.44849 | -42.91145 | 2025-10-08 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 952ad69c-ad85-3ffc-b04d-5bbca1e0553b | -18.01615 | -44.29297 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0abfce99-78c6-366a-a328-9f6bf1b4cfd0 | -17.1649 | -56.61153 | 2025-10-08 04:19:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 652a72de-c89a-357c-afa5-3fe47249e149 | -14.7114 | -46.08321 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4833df33-0abb-3079-a2cc-7a3a5bbf2f3d | -19.09735 | -43.73 | 2025-10-08 04:19:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3be839be-60f8-3f6d-8c44-0320f608c3fe | -13.88679 | -51.90538 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4faa0d8c-d3a0-3e23-b989-ec41e155cd25 | -17.45466 | -43.38392 | 2025-10-08 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac4ba32e-30b9-3242-a2bf-286ee3e000c8 | -15.36792 | -47.29636 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e27c6086-4215-366d-b1bc-3707a897fc8d | -14.82207 | -48.4114 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ef58581-e7e1-3ad8-9f8d-6b346679ec11 | -14.36176 | -45.23466 | 2025-10-08 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 597ea17d-452e-3d33-9b1e-ab5cd820d0fd | -9.41878 | -47.65218 | 2025-10-08 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0378578-ded5-3657-8f55-e6780393a324 | -8.51902 | -46.28998 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dd6dde07-b548-34be-896b-59a4a343b8b3 | -17.1406 | -45.79151 | 2025-10-08 04:19:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3e1845b-5541-3cc3-bc29-d0180bd21ae9 | -17.55926 | -46.07467 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d5c0eec-ab96-3347-9628-00b258448da1 | -7.45807 | -47.03034 | 2025-10-08 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd3b6742-5143-3920-b3de-bc8f7b5ab981 | -7.79826 | -46.01849 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2c4395f-6493-33c2-8e36-48276d3b9a79 | -9.00513 | -45.50489 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96e33e8f-0517-33e1-8589-27fc74b0edec | -15.40186 | -48.01858 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7cdebde-304f-3bad-8ebf-7222d8aa74e1 | -8.22039 | -44.15808 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e03e8ecb-a8fd-38b5-99a1-8213e833ef8d | -8.69497 | -47.02676 | 2025-10-08 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5868f64e-3855-3cb1-b586-fc3b2f904cf1 | -17.28893 | -42.65834 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cec330ab-d7b9-308a-9952-ab64c1fb5501 | -19.46865 | -45.95901 | 2025-10-08 04:19:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e12f9f14-afaf-3dab-9e43-7e4d084954a8 | -8.55406 | -44.62831 | 2025-10-08 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 03a17125-804c-3c8e-b0ad-45d535b46a33 | -19.52093 | -44.07674 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d3412a1-0607-30d9-b221-ae8d8a561e83 | -15.25894 | -46.34488 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d727917b-ec31-3260-abed-fc45f5ed886f | -8.22871 | -44.17022 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6cf3c4b8-640f-3383-8876-330fdc78e1db | -17.82891 | -57.63012 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 446d4cdc-e331-32ab-85c0-895764a5aab2 | -7.79663 | -44.20572 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e1826ac-66d0-341c-b36b-4a011c20958f | -19.83481 | -46.16468 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64e2ee48-a2f6-3f80-863d-c72fed6f083a | -17.97869 | -44.97543 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0c177ef3-7d6c-3122-8a7e-86022d7fc938 | -9.17821 | -47.81887 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0447adc-f626-3b94-98ab-c65866cd48d9 | -18.00771 | -44.30413 | 2025-10-08 04:19:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bcdbf5cb-b926-360d-bae3-5a37dbe037dd | -8.19069 | -44.1139 | 2025-10-08 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 980540c5-0a8f-3e45-8376-d5581db2406b | -18.05267 | -57.53732 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 57136d88-efba-30af-b9a9-9ff0a157dcca | -7.62702 | -46.55307 | 2025-10-08 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7683cb70-6f7e-3128-8035-f1aab3c6a351 | -14.36987 | -47.73453 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3900a01f-d35e-36fc-9a34-11cf2ffe1413 | -20.18471 | -43.93586 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1450cd98-23e8-36e2-bae0-3a2124bf8a2f | -17.48734 | -43.33159 | 2025-10-08 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3a74384-6fec-34bf-af8d-04f699283001 | -17.83333 | -57.63941 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 1338e443-2878-3355-9975-2911924867f0 | -19.15557 | -43.32131 | 2025-10-08 04:19:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 05834b4c-8480-3737-bb42-68450a4b7a38 | -20.28503 | -48.51367 | 2025-10-08 04:19:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5000a36e-97b7-322e-ad6c-e19b0f8367a6 | -8.67974 | -44.73257 | 2025-10-08 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df497445-f532-33b6-a21f-d780c93d7f07 | -9.17284 | -47.8275 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff307c5d-01ec-30dc-8555-485d1e1ac01b | -13.37691 | -47.85604 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
