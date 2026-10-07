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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4737c45-1190-3f9f-be75-77178965230a | -2.96491 | -40.39548 | 2026-10-07 03:21:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 4bee8683-1bc9-353c-b69f-390294f8e4c9 | -2.9656 | -40.39133 | 2026-10-07 03:21:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7f49f318-ff3a-3928-8cf0-e63cbd2a4764 | -3.30506 | -42.27322 | 2026-10-07 03:21:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b314ca19-c71c-303c-aa5b-980e62874217 | -3.3051 | -42.27743 | 2026-10-07 03:21:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a97a64c6-48ee-33a9-8e7d-1bdedc665142 | -3.30606 | -42.27174 | 2026-10-07 03:21:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5532c8b7-8684-3bfe-b121-1ce992ebb0d6 | -3.30405 | -42.27897 | 2026-10-07 03:21:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 105a9440-6f38-35e0-ade3-ed18954a0340 | -4.51271 | -42.89139 | 2026-10-07 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a74b0a88-4a37-3486-9d9a-74638c0927a7 | -5.68771 | -40.8901 | 2026-10-07 03:23:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f96b5821-4685-3a41-959a-853c8a3907d6 | -6.31574 | -43.34187 | 2026-10-07 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aaf58fdd-7edb-3b26-a522-8b1a1dfbcdcf | -5.7483 | -43.27016 | 2026-10-07 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 185d710d-4621-3fcb-8a1a-93443fc2d008 | -5.7472 | -43.2762 | 2026-10-07 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0afa2dd6-7d73-36ce-becd-35444be89380 | -7.87325 | -44.19576 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 229d0474-3936-3ada-918b-91d2dca3d735 | -4.92004 | -42.74991 | 2026-10-07 03:23:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73ae24c2-4c97-3f57-bd20-c6c1e12fbac8 | -6.87613 | -43.68857 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a4fcf7a-7433-39bb-a3c1-4b7719073355 | -3.35582 | -43.39421 | 2026-10-07 03:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c41e3431-a901-3687-bd3a-6cc2375d0942 | -4.23912 | -42.66494 | 2026-10-07 03:23:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 842c7f0c-2c25-3dad-a50c-154b6c14a9e6 | -6.22842 | -41.98673 | 2026-10-07 03:23:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 976cd06c-e848-306e-9387-645e06db44d3 | -4.51583 | -42.89058 | 2026-10-07 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e784664e-ae39-3108-8c3c-87ea0da7e545 | -6.87047 | -43.68166 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 074bdd49-7c95-304d-86eb-1d6c780153b8 | -6.94103 | -43.67537 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5e893155-6067-3e9e-b6ca-71c7c9d6463b | -6.89322 | -43.68617 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3dba6eaf-c60e-33f3-819d-c2380b004470 | -6.92758 | -43.67313 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbb8c7eb-edb0-3bdb-ac87-49a77f648092 | -6.3169 | -43.33576 | 2026-10-07 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 19fe4a79-65dc-3a20-a3ba-2913ac31f7c2 | -7.87573 | -44.21395 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7fede9e-970f-3c9b-9a96-cc3177a9bc75 | -6.31459 | -43.34796 | 2026-10-07 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6dc15213-5214-3a2c-928d-4118e71a3d3b | -5.69396 | -40.89175 | 2026-10-07 03:23:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c121005-bfa6-3247-9fa0-52a0e65563eb | -7.87913 | -44.19598 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72e37c71-47eb-3692-aed2-eaf1bd18474a | -7.86905 | -44.21195 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 876ca0f3-e7e2-32e5-8847-68b08ec13a18 | -4.91904 | -42.75552 | 2026-10-07 03:23:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a0b07e9-9dbd-3da7-848c-715116027f25 | -6.92301 | -43.66026 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f72d6041-514f-3caf-b4df-cd82536e4e2b | -7.86986 | -44.21305 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f4f31e8-8447-3998-9cb6-f724caafe32f | -3.35723 | -43.39355 | 2026-10-07 03:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b05dd7f4-ba9d-39dd-8c6b-634b0713ca4a | -5.97046 | -40.94984 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ff27d983-50f0-31a7-8451-b7564c406adc | -5.41216 | -39.10739 | 2026-10-07 03:23:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 52c7b601-7829-3d8a-b0ed-4aeb057b3d10 | -5.97773 | -40.94237 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 859d63c3-80a3-326b-8dc9-b51d25655ef5 | -4.51938 | -42.89243 | 2026-10-07 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8f04528-543c-3fbb-943c-1847ef0eaf2b | -5.27508 | -43.36637 | 2026-10-07 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db67bbdb-c687-3b1a-bdd9-ec61737a037b | -7.87685 | -44.20802 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0aa4353b-97d6-310b-91a8-ea59986aaa50 | -8.70853 | -45.21248 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b2db402e-a468-3a7d-ab54-2136a856cbb9 | -6.89075 | -43.68467 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 417b7fe4-64ff-3c2f-b65b-9eefb74c6841 | -4.24092 | -42.66425 | 2026-10-07 03:23:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 1f438e86-974b-388e-9430-2eb3a4306cae | -6.91896 | -43.66053 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a40d1e7f-84d8-35aa-b318-323e08029d71 | -7.87351 | -44.18842 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f97ee089-b1e1-381e-a129-4716f9093565 | -5.27262 | -43.36785 | 2026-10-07 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 00e31934-26e0-3e53-8f79-aa9b736c2c97 | -8.71838 | -45.20001 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ce96aa9e-0a80-3a1a-986f-e612fb6218af | -3.36419 | -43.39475 | 2026-10-07 03:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6292dd31-934d-352c-9ddf-36ac74e2fb3b | -5.74055 | -43.27482 | 2026-10-07 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 81310fc7-147b-3a5d-aff7-b7af5a435749 | -5.9776 | -40.90949 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 34e80967-2153-3e48-831f-a9c895a83bda | -5.7777 | -41.92703 | 2026-10-07 03:23:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a2110dcb-1082-35f7-b9d4-4987a52cdb15 | -5.97411 | -40.9292 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0b508f02-08dc-32e2-b0c4-89b1afb9993f | -6.8944 | -43.68003 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9cd69dd-f4ff-3c02-b805-6b68cb6a7c4e | -5.73073 | -41.73047 | 2026-10-07 03:23:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0fc8badc-0215-3d03-b601-1a88eb788a83 | -8.71694 | -45.20731 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80081cbf-f547-31ac-9589-2caf260ab316 | -7.87106 | -44.20693 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 533a3969-f6bf-3350-9615-5ea92ea4a572 | -4.24674 | -42.66026 | 2026-10-07 03:23:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 93c8f634-c489-3ae7-a092-dce9b5e1c64f | -9.77632 | -36.14202 | 2026-10-07 03:23:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8cca01f3-fd6d-3b56-a86d-ca60451761e4 | -9.7894 | -37.32436 | 2026-10-07 03:23:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9bf9e62c-26f4-33d3-a2e3-a3b68fcb9289 | -5.97268 | -40.93731 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 01c92cc5-aa63-376b-b278-fbefc640b540 | -3.36279 | -43.39536 | 2026-10-07 03:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e99abe2e-50ad-34cd-80fe-69218148bac8 | -6.6195 | -43.72986 | 2026-10-07 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24b02c10-7934-3de2-9151-9f778baa700d | -7.87446 | -44.18961 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 04585ed3-5092-37b1-afdd-8bc144d5721a | -5.97548 | -40.92145 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7d5d7082-6fa8-3d68-9f33-7bdec216bd5e | -5.97845 | -40.93825 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b562a084-ef3e-38c3-b54b-d16d74a26190 | -6.93694 | -43.67543 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 568c894b-5117-3580-8283-ffd47ebdf803 | -5.73155 | -41.72581 | 2026-10-07 03:23:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d4d9ca85-83e3-30c8-bb95-919830ae671a | -4.24575 | -42.66584 | 2026-10-07 03:23:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 70a72bd9-88fe-328e-92ce-283d06a61b51 | -5.69358 | -40.89051 | 2026-10-07 03:23:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5a006b14-5c4e-3c4a-b2ce-d31ca5bfe274 | -6.8829 | -43.68952 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8ad932c-3dc8-3eb9-89fd-6a08418883b9 | -5.69293 | -40.89425 | 2026-10-07 03:23:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9cd06420-d886-383b-8898-28ed64f27837 | -8.70291 | -45.20357 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 21bbeba4-1f2e-33f9-90a2-7018262c1add | -6.92569 | -43.66159 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c25fb54-102d-32a9-a82e-208810e9f7ee | -5.98057 | -40.92623 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 9e992dc1-30c2-3450-9adb-60e682139e37 | -6.87726 | -43.68251 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48bad866-3ed9-3ae6-83c3-31c65bc46008 | -4.24012 | -42.65926 | 2026-10-07 03:23:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fcffd47b-10bb-38a4-970e-f63035e7d210 | -4.34973 | -43.79668 | 2026-10-07 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c42edb8a-c352-3e5a-bc27-6331a99de8d1 | -5.9748 | -40.9253 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d8e15301-77bd-3c6e-b43c-a298d4ce0ae1 | -8.71142 | -45.19792 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| caf4e0b2-ce6a-3e2e-9e8e-b86bfe74c837 | -8.70434 | -45.19641 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 6ab6a387-cdb5-38bd-a7cb-c5aee217a138 | -6.19316 | -35.3031 | 2026-10-07 03:23:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0c2b5777-e628-3f70-91d9-10c9ac3029b6 | -5.68711 | -40.89354 | 2026-10-07 03:23:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 811480b4-75a6-3494-b781-6a347a199b4e | -7.87234 | -44.19461 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb2d6e71-4866-3a7e-93ac-ef0b249e086f | -7.86445 | -44.19901 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8bdfae9d-73a9-3f1a-afe3-338f113f61ea | -8.70998 | -45.20515 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 94b3a43f-1925-3699-8d14-b0884cfb79c5 | -6.88402 | -43.68355 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e5c3fb04-f802-32bc-9ffd-3b6d6a4a3386 | -5.97122 | -40.94558 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 271404a2-cc35-3910-af1f-2a6998a9cc22 | -4.82512 | -38.68748 | 2026-10-07 03:23:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ce79ab6-4e78-3fca-87b8-8fa1f898497b | -5.97195 | -40.94143 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 48a0d574-07e7-37e3-b26a-e29ff6bb8438 | -5.73238 | -41.72117 | 2026-10-07 03:23:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1e4b8fb2-e9ef-3fff-aa12-d7ebdcb55f44 | -5.97624 | -40.95079 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1e1f0e98-1181-34a2-96e0-8f801794991b | -6.32121 | -43.34927 | 2026-10-07 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd0b9f5f-63a4-3cbd-ac40-3832a885e13d | -5.97699 | -40.94653 | 2026-10-07 03:23:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f2324fa0-8040-3267-99ae-7ce7601b8036 | -7.86534 | -44.20009 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa6f2fa3-813e-360a-9f84-765df8da892c | -6.18924 | -35.30237 | 2026-10-07 03:23:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b9ab76e9-1480-384e-8c64-2d5a414078a2 | -9.79364 | -37.3251 | 2026-10-07 03:23:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4c4f649c-c4bf-3992-94bd-33299a6b3dc9 | -6.23458 | -41.98767 | 2026-10-07 03:23:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 6ac26340-2344-345f-bc28-0d068746b412 | -7.84427 | -44.15701 | 2026-10-07 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ab3bebc9-635d-382d-9dea-ac54e3506fa9 | -5.92074 | -42.98762 | 2026-10-07 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 495c2f65-5fd5-3076-bdde-9b977ba8508c | -6.3176 | -43.34669 | 2026-10-07 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5225bece-7946-37b9-8a54-08c01658cf25 | -6.92456 | -43.66754 | 2026-10-07 03:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d38ca53c-ac89-389c-913e-67d29c138aca | -8.70148 | -45.21077 | 2026-10-07 03:23:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |


[Clique aqui para ver as próximas entradas](README32.md)
