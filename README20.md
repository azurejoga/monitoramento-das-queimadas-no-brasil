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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64ee9b20-731d-3cee-83b8-192f66499326 | -4.29082 | -48.24396 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f205cce-f28d-38ad-8691-7d68f74df87d | -4.00352 | -43.24709 | 2024-11-22 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 776ed08a-d289-38bf-abc9-e2e04b666b17 | -1.79037 | -53.63205 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aecc707c-c8dc-3fc0-9e05-d34b420a4e93 | -1.20608 | -51.77132 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef6ae18c-4666-35d7-a926-a610e8d0e4e7 | -1.2145 | -51.97791 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc3919db-8dd4-3771-a4c4-fd66d0e2b5af | -4.48482 | -45.53948 | 2024-11-22 04:12:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d80452dd-1d09-3de2-9913-39266c205942 | -4.68824 | -40.69055 | 2024-11-22 04:12:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f8cb0568-906c-30f3-8030-831c04b59d3f | -1.92277 | -47.06676 | 2024-11-22 04:12:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5c719bbf-250b-3cfe-8589-4b39e4a91349 | -2.72011 | -46.09562 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec5e86f4-6e6d-33ed-997a-ac4de3179fd2 | -1.92129 | -52.08712 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ea2ff33-57e9-3a51-b557-0f16189a6d2a | -1.2354 | -51.74506 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c35193e-9149-3fb3-b42f-a6845be2df2c | -3.09847 | -43.29686 | 2024-11-22 04:12:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4f5cfde-2647-3d11-bddb-f7fc80d9ef9e | -4.72108 | -44.42953 | 2024-11-22 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 368649f2-b36b-3697-bf39-f324570bb2a0 | -2.92024 | -46.83349 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83688f2a-009a-31b1-b326-648b2edff4fe | -2.94846 | -53.7221 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58e5dc40-9aaf-375c-b685-b90cbacd5067 | -6.11519 | -42.51363 | 2024-11-22 04:12:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 40373359-1ff1-3e68-9b19-d27a749f7681 | -2.67848 | -46.15985 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7a097dc-1be3-3c53-972c-7bb2c46f9902 | -2.67621 | -46.24558 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe333012-74c6-3599-b6d7-eecbe68e723a | -4.01188 | -49.92236 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b22caf5-4e22-34b4-94d4-ce0c65c960c2 | -3.53727 | -52.79032 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3123391-8722-38a9-b4de-454286ef545e | -3.80282 | -51.99412 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34a2865a-a3e7-3c17-b735-17e44ab9d6c3 | -5.32436 | -44.78366 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a966358-bee5-3060-b123-31d880b52450 | -1.8017 | -48.77085 | 2024-11-22 04:12:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2672a5ab-d26b-3e05-9cbb-3954c334c9ab | -3.21005 | -54.24657 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| eb774f4d-1f80-3c7b-9bfa-77f8819ef35b | -3.24902 | -54.25471 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c60b580e-171a-3953-8f47-0ba50e900dda | -5.10554 | -43.16388 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a73f54c6-0262-36d8-bfee-c92d36a64a0d | -3.63429 | -42.06819 | 2024-11-22 04:12:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 95020b50-e28e-373a-962c-54e393a7e1ac | -3.24502 | -54.23566 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fe5b9d57-6653-36d3-a30e-e3af147e750e | -3.32156 | -54.09333 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfe8ce3e-cfc9-3500-aced-71ad8e8d53d9 | -3.88954 | -43.99205 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb2cd79e-5fbd-3693-b638-649413372528 | -4.70581 | -48.29383 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31f6bf82-d300-3899-bcfe-344846359b99 | -3.08301 | -45.97492 | 2024-11-22 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8354873-3f90-39d2-90d6-8b41343c475b | -4.57465 | -48.01939 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04a8e466-697b-3442-a292-ea4468ed68f9 | -2.08397 | -46.28735 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b90e2ed-2e99-377c-9786-30f5e911688d | -4.43185 | -48.01729 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d356d853-9710-3a86-a480-3e8c0f06e7dd | -5.5907 | -45.21219 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab5a5b92-38a8-307e-bb2c-74a2147e0c30 | -3.27662 | -53.82083 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e64a281b-3d20-3e5e-98f9-15164bed25ff | -1.73302 | -52.71494 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65667b9e-ae44-3f44-97bd-106df41015b8 | -3.24999 | -54.24922 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e29679bd-1113-3145-8494-127ba0f74a0e | -2.65101 | -48.78612 | 2024-11-22 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24a50bcd-0dca-3f12-8c2b-82dafe661ebe | -3.4532 | -45.90604 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a0be5a6f-7a00-33ce-84ae-6e665fca2869 | -5.95184 | -48.05844 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a51cc5a-33a6-36c9-a1df-653b50bf2838 | -0.77308 | -51.77164 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4795d7ab-3db2-3484-a46d-16102f5ac3f2 | -1.96142 | -48.38696 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aefc3748-1c69-3893-8c46-0910221e8f3e | -3.83638 | -52.25713 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe8c0d4-bdb5-336a-b91d-863a98c31e10 | -2.66308 | -46.16449 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2157cfb4-4b84-36ab-bb17-30bd4e6064dc | -4.06788 | -46.84161 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41676bcd-e798-3cfe-a760-380547ac2502 | -2.00194 | -54.52364 | 2024-11-22 04:12:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f9925aa-fd7e-37a3-b2a2-369e63f8cd3b | -3.31478 | -44.07207 | 2024-11-22 04:12:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce6747d6-b39d-3a0d-b0bf-d4f540544a13 | -4.40362 | -44.12048 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c63ca35-3b96-3791-a046-06f9a60e1081 | -3.00425 | -51.30533 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e7f57f6-e973-33fa-b134-64d0a6731195 | -4.70591 | -45.81385 | 2024-11-22 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc35ec77-0c10-30ec-8b49-33462d5a6965 | -1.19515 | -51.95019 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4847ca97-bdee-3dfa-8af0-17ab80090142 | -3.75855 | -46.125 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4d8f4c7-6872-31c1-92b0-317a7e548162 | -4.23813 | -48.63666 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dcee5103-0bc3-382e-aa1b-a026b3df065e | -4.63341 | -49.54546 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f56d21a0-0d6b-3e66-9c71-b60d34ab948b | -1.70273 | -46.69903 | 2024-11-22 04:12:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cb70eb9-58fd-3a4b-89ea-15719a8fa2aa | -6.91878 | -37.10606 | 2024-11-22 04:12:00 | NPP-375D | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bfea1b02-bca1-3e8c-8ba6-cedb388ed52e | -5.26902 | -43.48261 | 2024-11-22 04:12:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1d9efd9-5321-3e09-9fff-1200d10b7cb4 | -1.24608 | -51.75079 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83e37f67-95d1-3b28-8c33-b52a4a5efc9e | -2.39954 | -46.06969 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7f6e135-13df-3644-921e-71ecfdf0b4e9 | -5.14601 | -45.81609 | 2024-11-22 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 768f541f-92f0-35cf-8b34-f1e27981e75d | -4.21173 | -50.69823 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bc97f96-6504-3232-8f35-9571cb3a8088 | -1.44465 | -53.3977 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c6e9cbf-d96e-3950-98c9-7d75bcb94960 | -0.26723 | -51.55832 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 105ed3da-fade-37db-b844-f1dc41636451 | -4.24114 | -41.92905 | 2024-11-22 04:12:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b91226ef-4b45-305f-ae3b-b21702e3dd6b | -2.69358 | -46.09142 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0dac066-759e-3205-90c2-66aa6437a13d | -1.26491 | -52.06837 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6605ce67-5b2c-32d1-aee2-a1a809f8c264 | -3.83943 | -41.55938 | 2024-11-22 04:12:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 152b670b-1f9f-3244-a236-f733b08b87bc | -1.19005 | -51.94526 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b1acb49c-178d-3270-87d0-b575ecfd1cfa | -2.55526 | -46.54312 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65f8cdc1-d4b6-3621-aa83-430907abb493 | -2.43643 | -46.53662 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f8cec96-26db-3b4d-a7ca-df74c09f348e | -2.78809 | -48.09962 | 2024-11-22 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2106a103-11f3-3192-91e4-bceb26b32d82 | -3.2876 | -53.83198 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce6e5d91-1d3a-3ac1-941b-de34f128d222 | -3.14826 | -53.13606 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fb01425-206b-38a4-8127-019cf6f6ab29 | -1.29972 | -52.21917 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b026b38-9384-3edc-beef-7fa4cdff81d1 | -5.5872 | -45.21161 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 10d3d037-36c8-3279-b421-1e9762da57db | -2.31043 | -53.60318 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c44997b4-3928-32cf-b5f2-a2a6419b8156 | -3.45691 | -45.90664 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0a9fa7a4-18b0-3b0c-a114-f3cf6e97a1f8 | -3.64447 | -51.45572 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0bb5f75-75f3-313e-bb7d-368c2e67d939 | -1.51638 | -47.06542 | 2024-11-22 04:12:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48e0a65a-5145-3c7a-bce6-3c4734ed8762 | -2.67115 | -46.23752 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8dcb6be-f893-332c-b8da-f07d092333dd | -3.75249 | -44.56805 | 2024-11-22 04:12:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3f2be481-69c5-32c4-bf2f-5daa5e5f8602 | -2.72916 | -46.08771 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fbb2e50-3b49-3f1c-8326-6b22f268e09d | -2.78424 | -51.71657 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50c1ca32-c95a-36da-a453-a056c85db4f6 | -3.64663 | -51.4571 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98d8e49e-f3fc-32d7-aa32-d3b5f3d52419 | -4.63422 | -49.54066 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dddb9608-0e11-3316-8337-71a151ed1dc1 | -0.05297 | -51.23624 | 2024-11-22 04:12:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 900fbb5b-e762-3240-ad94-1e4837b986df | -3.21644 | -54.248 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 42700a34-fe21-3048-a2e8-21cf787001d3 | -2.16033 | -50.46251 | 2024-11-22 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 176869de-f387-3a6d-afd9-7da17a296ba8 | -5.42945 | -45.33976 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 511e3be5-7ffd-3848-a2b1-5e6a82c4b269 | -2.56228 | -46.54921 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a25d147-98ee-3987-9b1f-4a4245aa48db | -3.80898 | -51.99133 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 355a22bb-5389-3d5a-a9b0-5c93d3fb97fb | -0.93851 | -47.55763 | 2024-11-22 04:12:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d071e04d-adef-3985-b8d5-692746fa2c8d | -3.47198 | -45.91587 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9653172b-b9f1-3319-90b0-67a1846e20d3 | -4.29149 | -48.23999 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d95e5ce-ee0c-33a8-90ec-653cfdfdc4c8 | -1.79125 | -53.63792 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dbd9ae5e-3b9d-39ce-ad62-e69fcca0ada4 | -1.42524 | -46.80231 | 2024-11-22 04:12:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d54a4e74-3301-380f-835d-525cd6070bc9 | -1.4258 | -46.79884 | 2024-11-22 04:12:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea693b7a-df65-3d63-aa50-6becd8298d6e | -5.93129 | -43.78567 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README21.md)
