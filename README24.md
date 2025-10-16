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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f3336c1-a420-3421-a90e-3cc46260c48b | -11.21305 | -43.99879 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05fa1b7a-7ba0-3ef2-8521-cf25c45e5024 | -11.47399 | -49.82489 | 2025-10-16 03:47:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca5dcc94-3266-3be4-9161-98cffd3e1d5b | -6.32649 | -44.32401 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5b389a3-a150-32db-8ad7-392618749b9d | -5.89139 | -42.83855 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f1a1494b-59c6-3666-b412-d9adc2fcfc6f | -5.54743 | -41.33178 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| da0f8628-c2af-3a2f-b525-0d9ff3ffa210 | -5.4259 | -44.23838 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20e0be5d-8f48-3bb5-b5c1-062d4e9e0824 | -5.32913 | -42.56021 | 2025-10-16 03:47:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab8511b0-1367-3c83-a1e7-bdc35698b1c2 | -9.71566 | -44.51581 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a3e8ce8-322d-3291-bea3-ac1065b8c5e5 | -10.13402 | -44.55056 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8333b800-07f8-3d8e-85a9-9e26c6c699af | -3.6828 | -47.63179 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5d78979-2f17-3a47-b642-790974759b75 | -10.66573 | -45.33242 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b45a98e6-d9c8-3247-bed7-5f9d1ce7e21b | -4.36487 | -43.40167 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21435290-076f-3188-9add-2b076f15af4c | -10.15045 | -44.53888 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a154f79-8791-3ad8-9433-250358cf3b6e | -6.73895 | -38.79124 | 2025-10-16 03:47:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 655c8c8f-ce38-3064-bad9-51d3d9ff95f4 | -6.69029 | -40.86953 | 2025-10-16 03:47:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c03bbf01-7e92-3f43-a912-3a48d4d03406 | -6.17824 | -44.30648 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cd7e350-f29e-3ec2-a3f3-babc003021cd | -10.87629 | -48.80897 | 2025-10-16 03:47:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6a21febc-2216-3355-aab9-bc5c686f7e59 | -6.17287 | -41.78329 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c2258e16-3462-3533-b7ea-2a25fd6c54fc | -11.5808 | -44.06977 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4e2b557-a93c-3424-b345-b3898be6edf6 | -5.47705 | -42.93976 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d865805f-0022-30ba-9d09-f57e8c177d9d | -6.22146 | -44.5986 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0749398b-b5d0-3f19-8e34-d6db5c8d9893 | -6.39332 | -41.78903 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f8bc6b1f-2789-394a-a07e-cff34880a45c | -6.99151 | -38.44376 | 2025-10-16 03:47:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f84008f1-470f-3bef-a24a-9dfc3529a13e | -10.83587 | -43.95775 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adeee360-435b-3551-804d-f44db8b6404d | -4.86675 | -44.58135 | 2025-10-16 03:47:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a823168e-4d06-34ad-9c97-35686e642825 | -5.50158 | -47.30912 | 2025-10-16 03:47:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ea98f9ff-fd4b-3be7-b877-e0fe1296df74 | -6.16444 | -40.90757 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 035be95c-b3a2-3a38-b735-db86ce60b3f7 | -4.39085 | -43.39054 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c93391e3-6ab9-304e-853c-a8697d3a6639 | -10.13127 | -44.56544 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e461ae-6d89-3787-8a23-06e42826575b | -5.57088 | -41.31449 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8159a632-3106-3462-836f-8e39974f451e | -5.23975 | -42.00829 | 2025-10-16 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c5a0ce26-3938-321a-9fa0-74d269f1bddd | -6.42684 | -41.88897 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| efcb9d01-f7e4-3dbe-9dd2-c4b5f79f6be7 | -10.14526 | -44.54601 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e5a3d37-4fe4-3308-8521-67cfd7127531 | -5.38807 | -42.79824 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f38076d5-3f51-30f4-8105-3f437e1d7165 | -4.38616 | -43.38971 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d0ed34a1-83cf-3cf7-9482-313ffeff498c | -5.47182 | -42.94345 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 38f45a42-cee5-3737-a1f5-c031b6151e82 | -9.07996 | -47.95313 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2e6e95a6-1e8e-30b2-b4ee-e99d2dc9dc7d | -11.56883 | -48.56259 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e68071f3-1db1-32df-9210-8dda7ed0a8c3 | -3.84006 | -44.55321 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 859d1eb1-622a-3cc3-ae88-274bf85a05e0 | -6.09964 | -41.87415 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 97c05aaf-f701-33df-97e5-8a4b4ece2669 | -4.59203 | -43.57485 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de04f8ce-2dec-33a6-8bd3-60275b37238c | -6.05647 | -41.9285 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 515b0644-c951-3a82-9237-e54b9c8149f9 | -5.92164 | -44.727 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fff14ed6-7722-362d-a052-adcdb6323f6d | -5.40924 | -40.87906 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 270fc5f7-9354-3649-a64f-4c2aaa471d10 | -10.81641 | -43.94041 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bad77ed8-ce94-3713-918e-fac15d3770f3 | -5.48303 | -42.93163 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0cc32b33-e818-3131-8128-9e8d65a49b45 | -10.72597 | -47.58923 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 952350a9-6504-3205-80fd-d337be71c073 | -4.95473 | -45.10274 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5687ba53-4b5e-3ff4-8c3e-0bcb021710f9 | -5.54105 | -41.32058 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aa3ede56-06e1-3111-a9ff-40ac482d5a81 | -5.97781 | -42.80991 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e4e7641-336a-33eb-b177-5cd91b152847 | -6.31808 | -42.77164 | 2025-10-16 03:47:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 276798cb-8166-3875-8914-08074952cf83 | -6.45131 | -43.3805 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4126acc5-5479-38d5-9141-37776dacefd1 | -5.39046 | -41.16655 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c9aaa065-6b36-3f33-9d05-8b2417f98cd7 | -5.47056 | -42.87014 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f27567b-29a4-34f9-8879-1416bf807e23 | -5.68249 | -45.10294 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5bfb1dbf-9a9c-328c-9d49-b9923f5ba8fa | -6.07717 | -35.33913 | 2025-10-16 03:47:00 | NOAA-20 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ee7b2475-a046-371e-9903-b806560082b5 | -3.68036 | -47.62756 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb57bf44-c7e2-33dd-8383-4fe26944a93c | -5.85184 | -42.88783 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 48db6fb2-b9e9-35cf-8043-412b3eb062df | -6.45062 | -44.0348 | 2025-10-16 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ce08340-9176-3155-8505-20032c375465 | -10.70366 | -44.43177 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 00f568fc-8f60-3031-b317-594614d04e4e | -5.89673 | -42.8364 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e49b2aee-e4df-3d2e-aa8c-63e0555500f0 | -4.92719 | -45.90101 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be1b88fa-fa71-3a60-b9ed-7ff60c80f7ca | -10.52667 | -43.37712 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6561ecf9-4806-3765-a6d5-f14c246d74df | -6.33135 | -44.00984 | 2025-10-16 03:47:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a9bfc1-5028-35c5-99ce-56f8778c3ce1 | -5.45215 | -41.03117 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a9970230-8070-36f3-adf7-45f165c824de | -10.6405 | -45.22455 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51acd284-0001-3874-838c-141289b1f1e5 | -10.62315 | -37.73076 | 2025-10-16 03:47:00 | NOAA-20 | PINHÃO | SERGIPE | Brasil | 2805208 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3674aced-2456-3064-aabf-26e2de99d364 | -5.42952 | -44.23259 | 2025-10-16 03:47:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70cee580-9574-39e3-8060-36931360f40f | -5.43663 | -44.23466 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b1f35da-9aaa-3e5f-99ac-72067a28b23c | -6.21638 | -41.55338 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a78aaac6-a37d-37e9-bf95-969055aa724a | -5.8783 | -42.81081 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f657d704-35c7-3c0e-88f3-aa718481985d | -4.39526 | -43.4034 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f5227c1-520a-3754-b1c5-fdbb74fa1472 | -4.92685 | -45.90438 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdc3b130-6c29-3008-b33f-1f575e53b57c | -5.31704 | -44.8399 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1c0a2f4-30dc-3920-b2a6-4d3aa4cb4aa8 | -9.26775 | -44.36227 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bd7a1a0-da5a-36ff-88bc-6505ec5943a6 | -12.66338 | -43.27888 | 2025-10-16 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8a97e49-4d8a-3596-b093-235f2a5f541b | -13.00394 | -43.03029 | 2025-10-16 03:47:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 424a6d82-4fdc-3ee7-8327-db787c937e47 | -10.87714 | -48.80456 | 2025-10-16 03:47:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 65b57f60-3180-3c69-9fe5-a692cb0549e3 | -3.01165 | -45.38183 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 0bfae5f3-e0fc-31f2-9ba6-7d1fab693034 | -11.46711 | -44.14743 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6474a79-38d9-3635-b9a5-d1973eb098da | -4.87182 | -44.58209 | 2025-10-16 03:47:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 638c16a3-81a1-3a4a-9df0-b91a373babc8 | -9.68713 | -44.52328 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b851c423-5ef2-3138-8e4d-bf7390d46cec | -9.71745 | -44.50599 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4fa9162c-cbc8-378c-aefb-27c59358caf8 | -5.98051 | -44.56529 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9751734-d4de-3331-9fb6-5b8c85f71095 | -5.68357 | -45.09663 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| c13f7811-2698-3291-b3c1-a8de702518ba | -11.48876 | -44.10233 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d974aac-7094-353b-b64e-8d8b8943f4d3 | -5.83932 | -40.80813 | 2025-10-16 03:47:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b645c4db-61ca-3abb-8950-c7b29269b147 | -5.67788 | -45.0988 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 1060583b-c8bf-3e4d-be66-9d11bb35f40b | -5.06908 | -41.192 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 221e1b7e-c7d1-3198-8cf1-618bca2bd2ae | -11.0598 | -44.78398 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eca56c4f-b9d1-3c9d-b0f8-e6b12a93d248 | -5.86171 | -43.88325 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8be19f28-2765-3393-9379-5f2552169cc1 | -5.89889 | -42.82327 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1e278f8d-7979-3811-88b3-4909fdd9e4cb | -6.06225 | -41.89463 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bc7fb85e-33fc-3f86-889a-95edb77c5e3f | -5.92615 | -44.73077 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ab19e26-0093-368b-beaf-3853d1ac9f54 | -10.66171 | -45.29527 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 457a5bb4-0a4b-34ca-b6bb-9b48ff377c14 | -9.37351 | -46.95362 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a464178a-d1e3-34c7-9e0e-91e5082ae97d | -4.86778 | -44.57536 | 2025-10-16 03:47:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3de4cebe-89ff-3559-bd00-0e55d3b9bc2f | -4.01905 | -48.96881 | 2025-10-16 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2df112a-4640-386e-ace3-919498a28565 | -5.47259 | -42.93894 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| a5f956b4-5a7e-371d-9fb3-7e51c8c5bb58 | -6.44225 | -43.37891 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README25.md)
