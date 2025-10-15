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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 914759be-e119-39b2-ad20-60b60b2ea9cb | -7.48396 | -42.15093 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 099cf932-d3cf-3d3e-b6d7-cba7a2cf3922 | -6.88759 | -43.96345 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aaf8cb60-1594-30a9-95eb-216f7fee35c5 | -5.56589 | -42.98944 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae7b994e-c1e5-340c-8551-5f089ab007a6 | -4.82547 | -45.44723 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cfaa53b-3e57-3991-ac72-644b84697fdf | -6.58576 | -43.92358 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb3f4139-c58a-3318-9e44-86682d1eb1da | -10.16688 | -36.17876 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d97aa454-991a-3922-bd2f-b4afda1dc8fb | -6.17913 | -44.30246 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e80969a7-a405-3b97-b92f-94e6c9b011a4 | -4.91995 | -41.54309 | 2025-10-15 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e48ecffa-33f7-32e1-8f27-b134e863ea3f | -5.5895 | -42.84227 | 2025-10-15 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d56fdc40-c309-3fec-96c2-a1a98d0fbb31 | -5.31483 | -42.91553 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35ec8f94-be79-3604-bb65-63784cf7254b | -6.88344 | -43.96679 | 2025-10-15 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32e0439c-2bae-3ad9-90ec-cd16d05e8ce8 | -5.03228 | -45.01551 | 2025-10-15 04:06:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf79b4da-dfad-3f53-a9ad-89ec08ac69a2 | -4.92437 | -41.53667 | 2025-10-15 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cdf75616-23a1-3ae5-b1eb-b38a1c3d56b9 | -5.42607 | -44.23045 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76460c9c-f336-3f2a-b33b-4923d8bd4dec | -6.13962 | -41.7583 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a9fe356c-4e28-397b-829a-271d60c7b154 | -5.33952 | -40.52009 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea90afc3-23bb-382a-b43a-39d2682aca57 | -5.40746 | -43.23226 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be1a4c4d-7c0c-3060-8dde-711975fca721 | -6.22938 | -41.55608 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18aa5c34-6cc2-3930-b4a0-f9524f0a7f65 | -4.65574 | -43.13102 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4533ffa-f0fd-3712-bfb0-e01d2e0de1a5 | -6.39031 | -41.48239 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4df04dbb-f92d-3d73-a592-a9582e89a09c | -6.76959 | -42.81235 | 2025-10-15 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f254903-cc53-3199-9c80-df87747f0531 | -10.16431 | -36.16579 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 252e1117-92f2-3b19-b522-2fa28b8f1459 | -4.8028 | -45.33627 | 2025-10-15 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 737087cd-87ea-3b71-b2e2-3da6afb388cd | -5.09658 | -42.63367 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1dda10a7-9d43-312b-b534-3a7df5b86690 | -10.06013 | -42.61591 | 2025-10-15 04:06:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5aeb9ec0-d678-3ed9-8142-7e3a7b96afa7 | -7.95025 | -44.13731 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6e1d5e5-0086-3d69-bfd3-a8c3b7461a3d | -4.23157 | -44.43114 | 2025-10-15 04:06:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 827d3140-8c95-31e7-82fa-ca447fe7d341 | -8.19357 | -43.98117 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f26793f1-6393-3fce-b71a-6f5b9806cb32 | -7.94456 | -44.12836 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9865cf91-7561-3467-a62e-abf017165047 | -5.0589 | -40.4689 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66e487a9-c71f-3ece-a538-6e8749ab4a27 | -5.87024 | -42.82183 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 00add9ec-6d55-318b-912c-f288ab4c64cc | -5.83168 | -42.32312 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d00fad13-619e-3f58-9c0c-2793d2ed8326 | -6.57624 | -42.96424 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59dbc50c-c80f-3961-aa95-23f207dc8d24 | -5.88627 | -42.78715 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| aee3f80e-6cae-3344-af2c-e1213a181c03 | -5.91132 | -42.8473 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9e7d055e-7346-3aa5-b20e-1bb6081b613b | -3.07366 | -49.51364 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d1b7e17-926b-37cd-a175-eb20a9aa38ee | -7.55079 | -42.71017 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c6a3f6c-f060-3144-957b-631c4f7db353 | -8.24159 | -43.40564 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3d2d37e9-f783-34fa-9610-431e7ca0a7e9 | -5.87156 | -42.79218 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 46148270-eded-39a8-adb4-d9de9a8d0cb8 | -5.65809 | -42.78851 | 2025-10-15 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f5068e0-7f04-374f-af4e-ee75975d8225 | -6.03978 | -44.1393 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0fb21f9-fa88-3ac4-b8ad-e4e132295837 | -5.29516 | -42.66471 | 2025-10-15 04:06:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08e0e4e2-ed61-3e9d-8fca-65416e00d0f0 | -4.89365 | -43.45489 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e05b297-2905-3b67-814b-e0508f40f48c | -6.45169 | -44.58124 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8ae60cbc-7719-3157-b678-3690cbb018c5 | -5.91235 | -42.64686 | 2025-10-15 04:06:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38c094b8-e850-3582-aef4-e99a0549942d | -5.2467 | -44.47802 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f912f789-b854-35c6-8c6e-6e22d99757fc | -4.89237 | -43.46272 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d2d1e903-52f7-3d35-b798-91926614c232 | -5.29969 | -42.52813 | 2025-10-15 04:06:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9bd6700-830d-3c24-be82-07cf8ed60042 | -9.16403 | -41.05863 | 2025-10-15 04:06:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c1a85b24-2aa4-3678-9f2a-c9ae8307dfb7 | -5.90749 | -42.82785 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bbe52914-04b1-3582-8540-4c0dfd8f510e | -5.95915 | -42.24888 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9de32f73-8240-3f5b-9cf8-2d5162e11cb0 | -4.20437 | -41.64077 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d4fb5fd7-8026-3eb8-b4b9-578fffea2134 | -6.58639 | -43.91972 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b2b4d4a-5f0f-38df-8aed-8c431fc136d1 | -8.2566 | -43.35558 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a883b57b-e99e-3e06-a070-a8b4448d0a07 | -6.99905 | -41.99491 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 578f309f-e236-327a-ada7-b7ab59f5bbfd | -5.90631 | -42.8352 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 316bbb2a-ddda-3c8f-b72a-8fe4f24214ef | -4.94744 | -41.71118 | 2025-10-15 04:06:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb11fe03-102e-32f6-a66a-73e5a5b001ff | -6.07006 | -44.52953 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fde1545-4c8f-37cb-921a-32e64f39c2e5 | -6.23214 | -41.56007 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7868b7e9-e741-3dde-8f2e-6f1ef448d21d | -7.53691 | -42.68974 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f84ae99a-f05a-3ba1-bc9e-e47d4be8b1f8 | -6.05186 | -43.39116 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4224db13-93ce-3ea5-8602-624570fa45fe | -5.91204 | -42.82117 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d1391879-3a96-3092-ad86-c84bd66fe947 | -6.58925 | -43.92422 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5cd7123-65c9-3664-b215-0a8703ed4bee | -6.40174 | -42.52275 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f250e606-0744-3476-83aa-69f2a4fbc500 | -6.14403 | -41.77323 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3840bf3f-2d06-31a9-8c8e-bd4efb8898af | -3.72808 | -44.14001 | 2025-10-15 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb9cf0d1-3837-3dcc-b8e7-38c6dc17a4bd | -4.9035 | -43.46049 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c43e3098-e505-375c-accc-c0bec50d087e | -5.32957 | -42.31997 | 2025-10-15 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 785533a2-b0db-38d7-a1a7-82f139143e06 | -6.5336 | -41.48014 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65e4df86-ba9d-3bf0-9e2c-37a0c583a95c | -5.87203 | -43.855 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3148e02a-38e6-3461-8a22-9553a24a26f2 | -7.1622 | -42.50637 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43e9ffcd-9f37-380b-a8e3-b379edfbda38 | -5.94609 | -43.75708 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80a422e2-1927-3837-89cc-14e74d2d9545 | -7.64551 | -42.58365 | 2025-10-15 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69664d1c-549a-3352-92cd-596a1c910fad | -5.16376 | -46.28046 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8572489-9208-3593-9162-0af6c3d63bf2 | -7.94043 | -44.13168 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09ed0bdd-7bc7-3c0f-9132-1fd98aea962c | -8.18341 | -44.04286 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 339ab22d-a85c-3d8e-abbd-16f547c9c75c | -8.21152 | -44.02354 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 798c285f-2761-3106-ac93-608dd8d3e549 | -5.38738 | -43.22517 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f17f7da-6263-364a-8124-b23e730dae45 | -8.22069 | -44.07647 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acf93a4f-5f4c-3e6d-a68d-92632536316e | -4.54434 | -45.42083 | 2025-10-15 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28bf7843-eb77-3a21-9300-ea330b522af5 | -3.42505 | -50.25521 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7cd638a-b1cd-3c59-82d3-b1c2fa204360 | -6.57963 | -42.9648 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afba77a7-ef6b-3826-9d58-e686c5855f65 | -8.20596 | -43.32482 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5478f48-aa9a-34a6-8ad1-af6c8edb292c | -5.98304 | -42.92651 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 00d74b62-1f6e-3643-bfea-d961a6f0af70 | -6.52866 | -42.19555 | 2025-10-15 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7650f54d-b22d-30b4-bcf5-75a8b62eab8b | -6.57905 | -42.96843 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 902e1895-ad20-3599-963e-d1306579894a | -8.45959 | -44.18631 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df4b92bc-b3c1-3214-ac84-801d2b715d37 | -6.43678 | -41.81245 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76b5758b-b34b-3a36-97ac-fa1bf91930a6 | -3.60851 | -48.92295 | 2025-10-15 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77ffc987-0796-3db3-bce1-667083e2043b | -4.88494 | -42.77276 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0aad6f0-7cb5-3afc-a843-8d56440bcb94 | -7.25433 | -44.91718 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d978120b-de1c-385e-8a09-62bf24983c4f | -4.017 | -48.96856 | 2025-10-15 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2943aa26-8bb9-36ee-b0ac-6b3df1b63d4a | -6.58595 | -41.5132 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3dbd139f-cc5b-307d-b00d-d2533f516f89 | -8.28531 | -43.44225 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 047474ac-070d-3f67-a7f5-9d8c4f9d31b5 | -3.08324 | -47.73359 | 2025-10-15 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 715003a0-e425-3a6e-8e71-a224f00a5869 | -5.34549 | -43.74983 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d2da28ad-f7aa-3dd9-8ffb-c17e935b58a1 | -5.44115 | -44.22873 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 06574d93-3111-3c59-8068-8c451278c3bb | -5.94836 | -42.31608 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75c8384e-c7d0-356a-b0c2-06f06640de10 | -4.4255 | -41.61798 | 2025-10-15 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f732983d-f2b4-3439-aaa8-c5db58617eda | -4.24977 | -48.55439 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README23.md)
