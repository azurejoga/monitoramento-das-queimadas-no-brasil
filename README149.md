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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2951e880-ee8c-365f-8da0-672cb4f1795f | -7.35674 | -64.68925 | 2024-10-05 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 142c80a8-cb67-3c79-9b89-b1542de22e8f | -7.45303 | -64.44897 | 2024-10-05 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7c2ae65-d0d9-3eed-9359-f4f0f6e421f3 | -9.53296 | -62.97902 | 2024-10-05 05:53:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5321a71a-cd55-381d-92c5-16862f2155b8 | -9.53505 | -63.15118 | 2024-10-05 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 298a7e2f-82f3-3d84-811b-a80beacee21c | -9.53933 | -63.15184 | 2024-10-05 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fb5a0aa-532d-33da-a927-72b0d2a1fdeb | -8.83379 | -63.02999 | 2024-10-05 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19b4c99d-11e7-346d-beee-ace86b19e462 | -8.83435 | -63.02595 | 2024-10-05 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4763480-feeb-3daf-9b7e-d7688009b0fe | -6.98138 | -62.917 | 2024-10-05 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f223370-e50d-31fd-8511-f32aff2fda3a | -6.98194 | -62.91316 | 2024-10-05 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db50f6b1-d98d-3d9c-bba5-547d2ae2c473 | -7.50326 | -63.35752 | 2024-10-05 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c062eb8-6fba-3bec-a935-f97cd95049f0 | -7.52113 | -63.26193 | 2024-10-05 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6d5d5cb4-17cb-306a-91f2-758e7aeefdf4 | -7.52527 | -63.26253 | 2024-10-05 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4483b440-2992-3d4a-ae35-8eed7381b377 | -7.82723 | -63.40371 | 2024-10-05 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e73770c3-da3c-3af0-96d4-889659e2b533 | -7.83134 | -63.40432 | 2024-10-05 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05dab01d-9ea0-369b-b488-13b60094ffb6 | -7.86966 | -63.45877 | 2024-10-05 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9a6b276-6bac-3201-a965-97926c3f77c1 | 1.329 | -60.71992 | 2024-10-05 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf943485-fe63-35f6-8030-103b83855618 | -10.38032 | -61.17622 | 2024-10-05 05:55:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f420960a-f71e-3b5e-a2df-2f20f31a3063 | -10.37534 | -61.17549 | 2024-10-05 05:55:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66068151-f719-3f04-b25a-c043754f96f4 | -10.3746 | -61.18121 | 2024-10-05 05:55:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8a71487-ef38-30d0-b81d-f16cb50d7b02 | -11.80444 | -60.69519 | 2024-10-05 05:55:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 38a61851-3212-30ce-a00d-233b0f5dabf6 | -11.80363 | -60.69484 | 2024-10-05 05:55:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21095942-5001-3345-acdc-e5a44f5bde2f | -11.79919 | -60.69445 | 2024-10-05 05:55:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 875b8c33-ad87-3207-b451-d0d2bf3f325b | -11.79839 | -60.69409 | 2024-10-05 05:55:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96e40426-6d97-3480-8151-fc71899f3ec8 | -11.26586 | -60.5789 | 2024-10-05 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 420b64e1-67b2-3e7b-988b-5427ab32da48 | -11.26542 | -60.58227 | 2024-10-05 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0df1b8f0-8657-3489-8646-94b8fe3f6255 | -11.26498 | -60.58566 | 2024-10-05 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21effdbf-9904-387b-b2b7-3efbd470ef68 | -11.26061 | -60.57816 | 2024-10-05 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c504d1-a1f7-3453-ab1b-94e141ec0f73 | -11.26018 | -60.58147 | 2024-10-05 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4eb5acfd-f2d7-3d1f-8902-d35b767e841b | -11.25976 | -60.58476 | 2024-10-05 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08218d95-12dc-30c8-9c0a-d776e345cfbb | -11.24413 | -60.58177 | 2024-10-05 05:55:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 255fec63-556a-377a-8ac7-0082362c2996 | -11.18845 | -61.28693 | 2024-10-05 05:55:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c55f6d0-b511-3f31-abb3-cff21574a9ab | -13.41656 | -61.91876 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 83df3d50-7c2e-3113-bcd4-850f5b62c3cd | -13.41374 | -61.90121 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73389721-f420-3fae-8f6d-b0d663d0b47a | -13.41303 | -61.90683 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7e58b7a-4672-3c06-9574-c40ec68d1ccd | -13.41233 | -61.91246 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24469cd0-f9ef-3ec3-951e-5e19247eccc8 | -13.4095 | -61.93494 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89abfe2a-8eca-32b0-b6fc-82d8d9b87410 | -13.40809 | -61.90617 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ca3685d-4d39-33bc-940a-87145fcb47b2 | -13.40738 | -61.9118 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c117215b-d72a-375d-a9b6-59a7e99b5bb4 | -13.40668 | -61.91745 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72a4b812-f814-3cdf-af4a-82d3ca2ad3cd | -13.40456 | -61.9343 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84345b92-b120-3a66-8ec6-e2d563c621a3 | -13.40386 | -61.93993 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d528d57d-2c14-3883-ad98-6f6c126dc4bb | -13.40244 | -61.91114 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b14d162-5172-351b-a532-642d548f3fcf | -13.40174 | -61.91679 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 129a5d37-bd7d-32ed-b6a8-381aa3cb72b1 | -13.39963 | -61.93365 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 85ee74c9-8959-35cf-b7ba-260d398e8bfb | -13.39893 | -61.93927 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98438b71-188e-3dc5-b820-14f8a7c0c51c | -13.39822 | -61.94492 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f8a07f5a-d4dd-3042-81ef-9ee6ba797269 | -13.39469 | -61.933 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba1c1c21-d228-3088-8ae7-ce34b0ca9a97 | -13.39399 | -61.93861 | 2024-10-05 05:55:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f96eb7db-e3cb-3b35-9618-2802a10193d9 | -12.64115 | -63.10183 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4041f6b8-36a9-3fae-aa6f-83869be9dec3 | -12.70914 | -62.94355 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dd7febf-f7a1-348f-b844-d6c82bf8ad20 | -12.70974 | -62.93886 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb77b282-9187-365c-827a-105be7c2df36 | -12.71431 | -62.93949 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa511119-3192-3d1e-b1c7-5a19e7b7788c | -12.71766 | -62.9495 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be7cc90b-3a88-3436-b174-8cd959dff2cf | -12.71826 | -62.94481 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c2dcb2c-4323-3a4c-8b89-b6332e6b0822 | -12.71887 | -62.94012 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b55af8ea-4ca0-305c-8b24-c7869edf5ae2 | -12.72283 | -62.94544 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ad64121-36c4-3eeb-a697-e891ce5a3df2 | -12.72343 | -62.94075 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2811beb8-200c-33be-a241-cbd288e207c7 | -12.72861 | -62.93668 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4255321d-1856-3f0d-907a-058e7257847c | -12.87379 | -62.45047 | 2024-10-05 05:55:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c133ed1b-cf2d-33a2-822f-7497f6ed6dc9 | -12.87443 | -62.44541 | 2024-10-05 05:55:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b038abb9-f020-3689-8a23-29cb5bbe4a2f | -12.87852 | -62.45112 | 2024-10-05 05:55:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fee3ca56-a226-3f8d-bf7c-bc45c6d6fd96 | -12.91755 | -62.72703 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dcc29d1-e208-3198-9846-9e4e3ae2484f | -12.91859 | -62.73037 | 2024-10-05 05:55:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5654dceb-3951-3dd6-8cd2-1f4d92d99c51 | -12.9849 | -62.6813 | 2024-10-05 05:55:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c13037c9-98ea-3113-8187-fb3c0b86b3c6 | -15.49192 | -59.80667 | 2024-10-05 05:55:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 175c12a9-3bf0-3e14-8e9a-1ea065858895 | -4.22813 | -59.87151 | 2024-10-05 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09f76b72-410c-3e79-9e1e-9fc6ca75e2ce | -4.22799 | -59.87197 | 2024-10-05 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b405538f-a657-396c-a00f-170b2c9adb28 | -4.28777 | -60.01707 | 2024-10-05 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0c3919b9-03a1-3274-a008-6cd35ef541f5 | -4.28695 | -60.02258 | 2024-10-05 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf43cba5-6eff-37f0-853a-de1b21f65411 | -4.90645 | -65.32917 | 2024-10-05 05:55:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a12dceb0-b4ad-32e4-a7ae-e28d5ac0b1b1 | -4.9029 | -65.32863 | 2024-10-05 05:55:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce614bf3-1c78-377f-aba8-141a6e056a89 | -10.82986 | -68.32133 | 2024-10-05 05:55:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d17d0620-ad2d-378b-84a1-8052afe2c762 | -10.68894 | -69.02953 | 2024-10-05 05:55:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00f7e757-ac0c-3e4e-989b-8d49e00e31d5 | -10.50842 | -68.66879 | 2024-10-05 05:55:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77cc42ee-f049-383a-8282-57edc7c5f034 | -10.50787 | -68.67233 | 2024-10-05 05:55:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14858027-7908-33f4-892d-dcf8738e07bc | -10.03551 | -68.47505 | 2024-10-05 05:55:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86d229e1-c318-3636-b9e6-b6068abf33ea | -10.95271 | -68.34781 | 2024-10-05 05:55:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e7c6e50-5a78-3aa4-b580-0598c26dbaf9 | -17.07846 | -56.67635 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a8559b50-2343-36ef-b16e-3b29d0b3defc | -17.07068 | -56.68285 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 364d4fb6-8a0f-3af7-bad9-a5bde1f282e9 | -17.0486 | -56.68789 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9e0dc807-709e-3b8e-ba23-79e4d0d860ff | -17.04799 | -56.69512 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bbb6f5e6-07ee-34cb-96e0-7f784feceb17 | -17.04618 | -56.6894 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| feff0a13-5e3c-3e3c-b74c-6b3467d62d6f | -17.04144 | -56.68717 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3f392c88-9005-384a-a866-81a3235e9b5f | -17.04083 | -56.6944 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 18cf3aae-b0ac-3d90-9d37-2b53c4ccb144 | -17.03968 | -56.68147 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6c9bfa1e-43f8-3b30-a008-b33f3888b9a7 | -17.03903 | -56.68872 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 16e8da25-915f-30ce-ba13-9100d3e0e93a | -17.03838 | -56.69592 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 159ee71d-3801-31bb-be18-3849bb784b5c | -17.03187 | -56.68803 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 2b2205e4-14c5-3d0b-8bf9-aa9975c0eb67 | -17.03123 | -56.69524 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| ecbb9bdd-1205-3590-bab2-e2bfd10cca78 | -17.02472 | -56.68732 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 4a3a2fce-8396-31cd-922b-0daba343db4f | -17.02407 | -56.69455 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| bd1f90d3-9666-3d7b-b66a-7b60d3a6162e | -17.01756 | -56.68661 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| ce18a05b-bd39-388c-92b9-387b703cc0bf | -17.01692 | -56.69384 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.2 |
| d4c2420d-32e1-3307-9613-b7b89ec1790f | -17.0104 | -56.68591 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| ee8440d1-26df-3062-bc43-8301151547ae | -11.91524 | -56.93695 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0c0cab27-f322-33bb-891e-b09b51e5af17 | -11.9146 | -56.94286 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd316c3a-cf73-38e8-95c4-5bf4e281b5a5 | -11.91151 | -56.93652 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1706edf-aea9-387d-8f0f-15ad91714bdf | -11.91083 | -56.94246 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72fc5ff7-c082-37cc-be32-ea07727f77a4 | -11.90792 | -56.94206 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c4e1a2d-7552-3d05-9821-770bda99a169 | -11.90727 | -56.94806 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README150.md)
