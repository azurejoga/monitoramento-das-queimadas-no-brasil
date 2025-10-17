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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db18ee5e-d057-30ad-810e-94f0f32a00eb | -5.27941 | -43.26197 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| cbb70392-d14c-3b4b-9661-2ef39cafc12f | -7.95473 | -44.12654 | 2025-10-17 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| c2e44bb6-59b1-3632-b102-9b5f2b6fdb8d | -11.0908 | -45.85947 | 2025-10-17 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cd443aff-7ab0-3cf6-88a5-38d7ebdd9f38 | -10.8625 | -50.21996 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 200ac5cd-f438-3f03-8c2c-4a58f80aedaa | -7.48561 | -47.03197 | 2025-10-17 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2e8c99a6-8b04-312d-80c2-d511a2089765 | -8.24427 | -44.82319 | 2025-10-17 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| adb88d59-f619-3090-8309-2d3aa1328b5e | -10.62171 | -42.31893 | 2025-10-17 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 26bb6559-a9b4-3059-939b-6d0168d6a0d5 | -6.93233 | -45.13605 | 2025-10-17 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2b030ffe-0f02-35c1-a3de-a5de9d9dbaf5 | -6.42375 | -44.72498 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 274714ae-136b-37f7-895a-20aa5f86eb38 | -6.84736 | -44.39113 | 2025-10-17 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8a0687a2-515e-38f3-913c-c56843f229b9 | -5.22456 | -46.18529 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d1e558bf-0ffc-3977-af06-aa4ad10bbadf | -8.30554 | -43.40633 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d7a31a8f-b5cc-344f-85ce-4d14df727cc6 | -8.29363 | -43.46062 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 21909e49-0d23-3de5-9870-3134836087e2 | -6.13254 | -41.7709 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| a862a15a-7a7c-3193-8084-4b9fc13cfcf3 | -7.03921 | -42.73688 | 2025-10-17 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f1652d26-6b5f-38bb-b87a-b54fcb2ef34f | -4.86318 | -44.43159 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 524bfa8f-ea53-31bd-95fc-689d3f71cb20 | -10.08239 | -45.33961 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bc0a6dfc-dd25-3cba-a100-7dd09815c6fd | -5.47754 | -44.67759 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 76508c6e-9911-3123-a525-921ef631bec9 | -5.87635 | -44.83017 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1c279b83-2afa-3940-bfd6-38106f391178 | -6.16696 | -44.33253 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 922086bf-e490-339a-96da-e7876050feef | -10.44802 | -44.57412 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 211882a3-87e8-3d8e-94f5-6f5c78e0350f | -6.56472 | -42.96086 | 2025-10-17 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 91b90924-1d42-357d-bd14-aedcbb6f2d5c | -6.69797 | -40.87532 | 2025-10-17 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9b5aeac1-232c-3361-89fe-dbd4d7cabe21 | -9.22139 | -48.58507 | 2025-10-17 00:13:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 35131ba4-44a1-32b4-aeb3-0c6e4ef0643e | -10.46898 | -45.06508 | 2025-10-17 00:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3e4500db-41f7-3dc1-b686-d98171a012a9 | -6.69617 | -40.86302 | 2025-10-17 00:13:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 4f99b1fb-bd78-3b5c-8770-d47178747372 | -6.74757 | -42.36322 | 2025-10-17 00:13:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a77aa359-d285-3253-9414-6522d0fdb88c | -8.38195 | -46.24369 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7e8fb03c-fc27-3a98-ab1d-89bfccc6a796 | -8.4586 | -44.17718 | 2025-10-17 00:13:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| c343eb74-b774-3792-b099-e2d2ce88e8f2 | -7.82611 | -44.13907 | 2025-10-17 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 88aaec08-e3a6-3b91-ae0e-6aacfb28cc89 | -6.6046 | -42.07433 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d5ca556c-41c6-3b8f-ad94-b552681880e2 | -5.9339 | -43.32705 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d93048a9-72c6-3c00-ac44-609d9db1df25 | -6.22343 | -47.04233 | 2025-10-17 00:13:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 93860810-f97c-3758-8a2e-7f8d110de969 | -6.21082 | -47.88227 | 2025-10-17 00:13:00 | TERRA_M-M | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 14c0bb74-a034-3144-996d-bea2fd8708bf | -5.93523 | -43.33644 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 10674f52-e228-3625-96d2-f2eb53a7df06 | -10.27975 | -44.01953 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| df4c0178-7cbe-36e0-a02b-1e7856203c30 | -8.16481 | -46.06897 | 2025-10-17 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d3e228f6-ed67-3bc3-b699-729e14252fbc | -6.03141 | -41.93171 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9aa92415-27b7-3716-a8a5-44e6aa217355 | -8.21097 | -43.98079 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8585e2f4-1043-3dc1-92e5-484adf86186d | -9.25806 | -44.35173 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa1b02c3-fdf5-34a9-a442-22cde0223c9c | -10.42584 | -45.02045 | 2025-10-17 00:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| aa416552-fbee-340d-8ae9-180c41864978 | -6.25471 | -44.49425 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 81ef29cd-b5a1-309c-97e9-b8aea10d51c8 | -7.48876 | -39.0047 | 2025-10-17 00:13:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 157c073d-05ce-39be-94c3-1da35813a08c | -6.1208 | -44.85783 | 2025-10-17 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 16ace857-a7ad-3bf6-ba51-d19793bc78ce | -9.09131 | -48.03952 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e1d3382d-f31f-3cb7-904c-e07ff65197da | -5.48548 | -45.4011 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eeb3e3b2-d246-3760-aca7-8092b5c90125 | -11.76469 | -51.17999 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| fe06a3d2-3553-3156-8e70-0274dda62d28 | -5.49733 | -47.30072 | 2025-10-17 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 63d6cd92-eeca-3a3f-8d24-9427a6e6e6d7 | -6.94701 | -47.72777 | 2025-10-17 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8ef999d8-b55d-3270-8aae-abfc6ff78e11 | -6.59021 | -43.93261 | 2025-10-17 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4bb12905-795d-3295-9dac-c329c92c773f | -8.82047 | -47.30759 | 2025-10-17 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 96e3180b-7c18-3270-97f0-a4c82c67ccb0 | -6.58706 | -47.08253 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 73ac2026-dda4-3872-b189-e5d3387a49b3 | -8.45673 | -41.27456 | 2025-10-17 00:13:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 63f508c6-2861-39ee-83c4-73e198f0513c | -9.24918 | -44.36789 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4132c764-942c-3b24-aca5-ac88120a4451 | -6.31853 | -40.94476 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 33.8 |
| c54cdcaa-b94a-3d68-b976-f47c7c1e5a3a | -4.47502 | -44.29289 | 2025-10-17 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 73f33193-c0ee-3094-9415-7eb6f9656e7a | -6.59517 | -47.07088 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a4b27ea9-63a8-35ec-8d15-fa0d1bd62251 | -9.50051 | -47.272 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 19bd253a-bd4a-3f0e-b045-e4f305836fa8 | -7.445 | -46.66222 | 2025-10-17 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| addb9331-2ae4-3b69-afb1-1c2bd4dd458e | -6.33088 | -44.31517 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 689d248b-6aa1-3faf-9d03-04b03980ecd4 | -6.20821 | -44.43504 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bfa2109a-00fc-322c-a4c4-e5b4d721d527 | -8.38202 | -46.31416 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| a765c36c-1e4b-35cc-a018-ec86120c2988 | -10.27339 | -44.0386 | 2025-10-17 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| c2577cf2-db7c-3ebb-9ec6-9e15712d1cf4 | -4.92761 | -45.90334 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5112e385-214d-331e-b483-b90d343d113c | -5.71011 | -46.50556 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 50f651e6-c497-30fe-afd0-a6f30131c3f5 | -8.20056 | -43.31659 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 69fbfbcb-ec6f-3a3c-a9b9-b5dbe68fd902 | -7.6831 | -44.63181 | 2025-10-17 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2d5bd990-03c6-3ee7-8a40-e27ed68c12bb | -9.9767 | -47.01548 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 45ba665a-7f09-3236-b640-49090b97b00f | -10.28979 | -44.02716 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| c97f86d6-e0ac-3e1f-9ec7-c234eceadae3 | -5.20784 | -46.19695 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8a169be5-47d1-35b5-b8a3-4863df37ddcd | -5.09455 | -45.43521 | 2025-10-17 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 0da6a757-818a-388c-9109-e569bd1289cd | -6.34938 | -41.50742 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f4d88047-a60b-382d-a64b-556a91023b1c | -9.28988 | -46.91452 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 51a143fd-e4c0-3abe-88eb-fb6832cae566 | -5.16306 | -46.27521 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 56650ed6-1508-340b-b02e-a0d9f6d426a0 | -7.53249 | -46.83997 | 2025-10-17 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3fe113a9-03f2-3f86-a932-36727b97151d | -10.10912 | -44.59171 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9aa34599-2c8c-3e55-99b1-776565255c06 | -5.7139 | -44.51763 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 2cf8c450-c676-35f0-b626-5eedc1c94ca1 | -8.15477 | -47.98344 | 2025-10-17 00:13:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| bc171c76-2e0f-354d-8a79-298da7523b1c | -10.54025 | -44.50848 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8cad42ff-dffe-328b-b5c5-d1556c64c3f7 | -4.41302 | -43.38924 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 7ef31605-c75a-3fdb-8378-2f2ed2e84271 | -5.74639 | -49.01273 | 2025-10-17 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 711d2845-aa37-346f-b394-95ff6908db5d | -4.11584 | -42.20552 | 2025-10-17 00:13:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 33601258-4b39-340f-907b-0c832301e74d | -10.51162 | -43.42452 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e974b2f0-7280-3ffc-96db-4bedaebf0aed | -8.12181 | -45.5494 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 92b47dea-3de5-3927-ba48-3f6f3b357a2c | -6.76973 | -42.45222 | 2025-10-17 00:13:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| beb0d2bc-2929-387a-a874-c340913c6978 | -6.20119 | -41.75989 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 147e8401-c899-3835-b862-ab602adfc9b5 | -4.48266 | -44.28267 | 2025-10-17 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 92e142ad-fdce-3003-b1f4-aa49ef6be1a6 | -10.26335 | -44.03097 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| cc723b11-b552-3141-abe8-c7203f04526f | -6.18127 | -42.60606 | 2025-10-17 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f86dc290-208b-3a4e-819d-0995937bdd1a | -9.08963 | -48.02679 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 1a804350-f3d9-3606-9003-ad8cfdc7d89c | -7.3552 | -43.85908 | 2025-10-17 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2f3cb8fa-8ad9-3694-8f4a-5aeca2e84684 | -10.50788 | -43.39779 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6864f2e4-acd4-3b4a-9b29-e52d882f7e0a | -6.03806 | -41.90849 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| d359c3c3-2594-3841-9ea8-e083f5a25588 | -4.37768 | -43.40409 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fc598490-c02b-35d8-bc72-f9277731cd7e | -8.49731 | -48.49226 | 2025-10-17 00:13:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 010a8ccd-eb06-34fd-876b-ce45607a4d6d | -10.43608 | -45.02847 | 2025-10-17 00:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ab8f00c3-d34d-30d2-9f43-9630cdf051b2 | -8.21844 | -43.31404 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2cd900b4-1286-3892-b960-c21622978228 | -7.68746 | -42.55878 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a2efcafc-dbd7-357b-ba25-bcb2b428686b | -5.24734 | -50.96404 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ddd0244a-a2cc-33b0-bac1-44ba8c8ba108 | -9.05321 | -46.98573 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README7.md)
