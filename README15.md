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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5523e5d3-bc2e-3733-91ac-58f2dade3c5b | -6.86447 | -45.60213 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b5e0f7d-6d6f-3460-a3de-993a1426355a | -10.33394 | -47.73436 | 2025-09-09 03:42:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a23d7cad-59cc-3175-8da6-90ef1ef2ac98 | -8.33177 | -45.07073 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29fe8fcc-b90e-332d-8a94-c03131acd253 | -6.19399 | -41.02891 | 2025-09-09 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a1eb587b-bc80-31ca-a6af-fc61874df039 | -5.66511 | -45.4637 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2485534-72f3-3f2a-ba70-dd4712309da7 | -10.96654 | -46.81145 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a1ff761-702e-3173-b8f9-52ca6d7fa21b | -10.96111 | -46.81034 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54e40e05-2a6c-307c-b71a-68f9b0e93862 | -8.20821 | -44.77296 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd840e22-096b-3304-9a63-d9b62a135778 | -6.88403 | -45.53514 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4851d405-3e47-30e6-8d56-7ecc4f9be7b2 | -5.36274 | -44.80239 | 2025-09-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c6bc339-e4d5-3a91-ac30-4f8e31c556ea | -14.3248 | -47.33151 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d6e8e22d-ecc1-3476-8cb9-eb475cbdb54b | -16.69448 | -48.63765 | 2025-09-09 03:45:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 595b3921-4e12-3a02-a305-2b8c45aaaa66 | -13.84305 | -46.23643 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2a34aac-9490-3700-bbb3-9dc3653be767 | -11.3019 | -46.50481 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6b974f5-0cf1-3d18-96a3-17df84b20c7a | -17.72935 | -44.48959 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0571f6b6-947d-3074-9dd0-e7cab33e110e | -13.80026 | -46.25829 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81a9a55c-9187-3511-85b7-d59407165da4 | -11.83142 | -46.75326 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67cfd8c6-46f2-3604-840f-468bd01d4cb7 | -14.32559 | -47.32768 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 55c304eb-48da-3167-8472-7cad5f25760b | -11.55105 | -49.05123 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 84be8c5c-7613-3c5d-8296-4bab8e5c6666 | -13.79364 | -46.2639 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54434b9d-422a-38f4-a3d7-fcd504ab1695 | -14.32289 | -47.32467 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac325d30-f786-3d8e-b082-a965291a1f31 | -11.34445 | -46.57049 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2400ab97-0347-3548-bdeb-7ecd69137f49 | -17.71476 | -44.47091 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5207cd3-3a82-3b65-9c90-12c942cef4c0 | -16.27765 | -45.68399 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5af7d4dc-433c-35c2-8fac-0c4921fd36c4 | -19.51639 | -43.99712 | 2025-09-09 03:45:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 370da746-a126-3763-92a8-af30630cd95b | -19.41572 | -44.34373 | 2025-09-09 03:45:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42b212a6-8d09-34aa-b314-797ba4e4a6bc | -11.47333 | -49.26294 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e58b38e2-7806-3ae8-bfae-6f359da907eb | -12.14939 | -49.0852 | 2025-09-09 03:45:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b51a9cc-e87e-3f03-9ff2-1df0260515eb | -15.53094 | -48.36541 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4f5b47a-f348-370b-9d0b-a9a446027876 | -17.29749 | -46.7206 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 646a7511-b46e-36c0-9c1e-3677b536536e | -14.41007 | -48.46895 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bafacb76-1e64-3a0a-b236-9fd5f9e8f0b7 | -17.2718 | -46.74169 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4388c34e-c12d-3029-bc92-564c21babe3f | -17.2769 | -46.74282 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb7d8a0b-53e3-3718-923f-a865c4aa5bbc | -12.51945 | -45.28842 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67c04107-35aa-3b9b-b91d-97848863a009 | -17.16117 | -44.45039 | 2025-09-09 03:45:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ab9802f-de6c-3e7a-8314-19d7087474c3 | -17.76559 | -40.19327 | 2025-09-09 03:45:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| ca9f6394-9ded-3404-beee-d65ee3de5554 | -11.45095 | -49.27103 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 128f75f6-61e9-3b21-9329-3bbaca67fcc4 | -18.01402 | -47.1215 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe7bc9e-fd49-31fe-9fb3-40a34b90bc01 | -14.19389 | -42.04623 | 2025-09-09 03:45:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5dc6945c-0b47-3c29-8000-240d9c6c3d5f | -15.13191 | -43.97925 | 2025-09-09 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dad43f4-2696-39d1-b9c6-f6e97d017ba1 | -15.54555 | -48.37478 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6380fa95-cde4-33c5-a75b-709e2740d6de | -11.29285 | -46.4913 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74af44a8-1663-3f31-a126-2a7e1a9e68c0 | -13.81415 | -46.24373 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a0fd8a6-1ff8-3637-911f-f834f8fa793a | -13.79457 | -46.28682 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 901ee01a-a26b-38d0-80a4-9787744dfcc2 | -16.28737 | -45.68608 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a68a4c3d-e26a-3221-842e-1fadb397abba | -14.35508 | -47.32632 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bed39b6-cc91-36f7-85be-d6b15f593928 | -13.17955 | -47.24912 | 2025-09-09 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 926e94d2-e052-3073-a183-8f04317acf2f | -11.83845 | -46.777 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5df4d964-0f73-3825-a86b-17182f249aa5 | -17.34843 | -43.58941 | 2025-09-09 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c7f73d7-d981-3a7c-8880-dc4e0a37a036 | -14.3244 | -47.31708 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 985ea229-64aa-3a12-ad44-09d3b63c76f6 | -13.75041 | -46.90417 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a3a9e76-faf3-36e2-bcb5-440d7691f52f | -17.27248 | -46.73838 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0aed0d93-89e5-34b8-a64b-1e6a0512be45 | -17.26423 | -46.72674 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23b93d01-83c6-3abe-98f7-bee6f4ab3918 | -17.26764 | -46.68473 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa78264b-12a8-3117-bea2-1cf766758ecd | -14.5252 | -48.74277 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16eed7c1-420f-349f-853c-1f2a3c8369d6 | -13.82668 | -46.23592 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 545ea05f-2388-354a-af20-34352af86696 | -13.27567 | -43.74558 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f46c921-ceb3-3b11-b2ed-0787f9b206ae | -13.82568 | -43.86089 | 2025-09-09 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba0d1980-6821-37d1-ac5f-cdd5db44ef23 | -15.82448 | -48.95012 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e55a976-2ff5-3dd8-9c1d-4a847e5c2583 | -11.8419 | -46.77801 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b67f4685-c650-3832-9ff0-7e1de77ddca9 | -14.52431 | -48.74702 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 263d4def-f0a7-3df0-b2dc-7443b1b1c3d0 | -15.24765 | -48.81622 | 2025-09-09 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74bce6ce-685d-3bdb-b1e0-e0a37d277ebf | -17.34013 | -43.58755 | 2025-09-09 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1693d90f-3f19-3830-be38-be7eec0fc454 | -17.2953 | -46.75718 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac2cdfaf-f734-3a06-9063-4381df2470a4 | -13.8049 | -46.29032 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ae1be32e-cd4a-3ffe-b567-62b97283d397 | -11.82069 | -46.77747 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8bde1cf-1912-3d05-9c31-edaab114774a | -18.02218 | -47.13432 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54ea200a-6db2-3ded-84fb-ca3a2af7f097 | -15.05777 | -50.13277 | 2025-09-09 03:45:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1cd6e6e5-f65f-3f55-b3bb-6cff8c900bd1 | -18.0297 | -47.12394 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5092eec-cdce-389c-a26c-0e576ff46f2c | -13.93662 | -48.24471 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d013cbd6-81d1-37d4-800f-5c3f443e9740 | -18.00944 | -47.11758 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3ec8e3d-3c36-3d6c-92d5-2370b36213e3 | -17.72599 | -44.48341 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5d56ecf3-8b67-3837-ae8f-0c1d1aaccce4 | -13.27447 | -43.74731 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d59f828e-3307-3ee1-b550-f76b99bb41ab | -16.28361 | -45.67934 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d20e136-1bd2-3b80-a5a6-ce0ce8b79de3 | -11.83934 | -46.77255 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c371433c-5af2-35b8-89d9-9d9ac742ed92 | -16.96098 | -45.84728 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3c4d5fb2-fab6-33d9-ae03-cb5c5eb0a613 | -13.79975 | -46.2885 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90b82160-588a-377b-b76d-12eeae3f9a51 | -16.89599 | -45.8311 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d043a8a8-9ce5-3947-b09c-d8b8e3dea7c4 | -14.16849 | -48.99065 | 2025-09-09 03:45:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62d64c4c-b319-36a3-a5ff-544969f2fb38 | -17.27891 | -46.69542 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e72efa9-1d1b-31f1-9b28-78110a10cb06 | -12.81789 | -48.18104 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e882cdfc-8853-3c6f-8082-19ea8321fdf0 | -17.27953 | -46.69231 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89a8d037-b345-3665-85d5-5dad60ead20f | -13.93587 | -48.23703 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ff512ea-7e3b-360b-8dff-39c9c3a3b041 | -11.34248 | -46.56747 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c7ac6e2-557b-33a9-9789-682d15e249b0 | -14.54159 | -48.75563 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c7f69a67-58d6-3db6-a5ba-84412aa0f289 | -11.46544 | -49.26772 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07e48f86-c858-3e8f-83fb-26b1ec6d9ccf | -17.72398 | -44.49374 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e075f25-217d-361c-9456-6389cc45a818 | -13.28608 | -43.73498 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ba96f5a-718b-3d74-97d5-6d48d2b90a5d | -16.8971 | -45.8254 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80ba5673-2dfe-3ddf-9a49-391a28b3431e | -15.09656 | -48.0781 | 2025-09-09 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bb1058a-1c35-3aee-bdaa-48460d6692f0 | -11.30339 | -46.49708 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| efad7266-a245-3227-b4fb-838dfe77f6fd | -12.86593 | -47.97396 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51eb5217-2068-356a-a997-e62c25989f4f | -16.27955 | -45.68558 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb236749-941b-34be-8fbf-4f9e5bd6fc1d | -16.90269 | -45.81015 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a1f0097-05c1-3795-bb69-24233580d511 | -14.76692 | -47.77885 | 2025-09-09 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eb7b552-f59e-3858-b3c3-763fe8703a00 | -14.32644 | -47.32359 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d05bf4e6-8819-3d58-aa48-bbeced8cb698 | -11.63969 | -46.62974 | 2025-09-09 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc7f9790-3595-3c35-8ece-2e61b781b970 | -14.34867 | -47.32911 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2645c784-2617-3f83-8d5e-b4442d975698 | -17.65618 | -44.18085 | 2025-09-09 03:45:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ef66875-ca38-3ebe-8104-11d04cf2b93b | -14.53225 | -48.73948 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README16.md)
