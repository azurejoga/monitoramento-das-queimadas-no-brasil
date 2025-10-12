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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e38cc2-6675-308a-bff1-cbe6957ba9a4 | -6.72649 | -42.07956 | 2025-10-12 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 08557385-ae20-34b9-8f3d-adaffddeaa5b | -7.42154 | -42.96618 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 65f32812-bead-3a74-b2be-c5263813c7c7 | -3.51152 | -45.85186 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3faed7b1-1769-37f7-a68b-18c1e91efed6 | -4.47432 | -44.91777 | 2025-10-12 04:42:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b01d0ba1-2de6-3d55-8716-556bad3f7bf8 | -6.08328 | -44.30902 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d50c2465-f1c9-39ca-bf10-373c4247b8cd | -6.50684 | -44.4411 | 2025-10-12 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49e6a184-1dfa-320e-bdbf-9dc390cedfff | -7.52275 | -44.59925 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 343f80a1-f65c-3cee-abed-339f51b0e98a | -5.32462 | -42.87515 | 2025-10-12 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f91bd529-4249-3639-ac5b-6252ba118794 | -3.51935 | -45.84887 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 849adcfe-33cc-32e2-96cf-7f738cd72b33 | -7.26593 | -44.15308 | 2025-10-12 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 987f6c6a-81da-3724-8f1b-14133053f1ed | -8.47306 | -46.22145 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e904d470-b946-3519-9df1-4174ee823998 | -3.6978 | -43.20998 | 2025-10-12 04:42:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efd35faf-8bb8-3176-9abe-02ab72c8e558 | -5.19344 | -47.25059 | 2025-10-12 04:42:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 843bc2f7-137d-3a68-a820-a3103edcf391 | -5.86135 | -42.85184 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2362322c-39e1-3543-93c4-b39ee1a5bbad | -7.20643 | -45.49377 | 2025-10-12 04:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de22a8f2-8d87-396b-976f-2d0451a5ed22 | -5.43012 | -41.36911 | 2025-10-12 04:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9f4e1515-4b1b-3e06-8cc8-ed7734a271e0 | -8.48586 | -46.18736 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8ab17ad-61de-3eba-a9f2-0255369e6691 | -8.31597 | -45.93001 | 2025-10-12 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc716b6d-8368-301e-868b-e01cc3c40304 | -8.47786 | -46.24043 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0be6d9a2-a92a-3561-8707-d54577c7599d | -6.84445 | -47.3461 | 2025-10-12 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b9f79cc-0322-32ed-ad23-c5d0fbd97160 | -6.28359 | -44.41089 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff9a083f-69f0-35ea-93ee-2fc2d3126a43 | -5.47643 | -43.3965 | 2025-10-12 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14e529cb-a222-327f-af47-5fc4a49a7107 | -7.50385 | -42.15041 | 2025-10-12 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7a71836-716c-3067-bec4-6e306a9ee701 | -3.71691 | -52.0818 | 2025-10-12 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58c03a8e-28c7-3bc9-a36d-ae50522cb980 | -5.59174 | -45.839 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bde8eb9-a218-384b-9ac5-7b9a42d16677 | -7.85515 | -44.53155 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 559917d7-9d14-3cf2-bc6a-e2abff3d2745 | -7.79984 | -42.43473 | 2025-10-12 04:42:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 79a63b3c-cacb-3a3d-8e90-5f1eff7c1b1a | -3.51089 | -45.85594 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7bb7b09-b704-3851-ac71-68da82e66cc5 | -4.66001 | -49.38648 | 2025-10-12 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ba97e51-393e-383c-9a88-f0137b6b609a | -7.54481 | -43.83922 | 2025-10-12 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54208fc1-251e-3bd9-97c7-a6b5bad30e91 | -3.51512 | -45.85241 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 725913f0-8108-3519-b5b2-3d15bdbe0079 | -7.98824 | -44.47541 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1c0f42f-affe-3a98-9ca2-ac05e1d9a6a2 | -5.93403 | -43.94302 | 2025-10-12 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89df4102-4c3d-3cd9-bd54-b1df6e3a2b4f | -5.4721 | -45.23301 | 2025-10-12 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38fbbdda-3649-33db-9f68-403e39917716 | -5.86335 | -42.84972 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 47a6a986-394d-397a-9ec8-73b7da463016 | -2.44666 | -49.37299 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 326734de-7124-3f33-af24-62bd44a95777 | -3.87502 | -42.51305 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e794c7ba-296c-3cbf-9cb9-a58d9642fc2d | -4.27347 | -46.92924 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c77325a4-cf82-30c6-a7b6-4657b5e5b878 | -8.21684 | -43.33659 | 2025-10-12 04:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1baf5c53-9131-3e5d-9b26-8a62d334a3c6 | -5.11549 | -43.01575 | 2025-10-12 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32fd2147-85d7-3b9d-bca6-d1c1f2ad98da | -3.60262 | -51.33812 | 2025-10-12 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8e4178a-4907-3fd2-9a8d-5f232bb97a44 | -5.86268 | -42.84302 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a33df644-9570-3217-a6e2-eb03a7305bd9 | -5.31683 | -42.89006 | 2025-10-12 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50513eb5-e8f9-3ee6-99ed-8d6db5af86da | -7.26784 | -42.96959 | 2025-10-12 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40b70f45-45f7-3e36-b0a6-3d9f77301af7 | -7.50944 | -44.60467 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0fbd267-d041-36e3-b90d-ac19c3b8743d | -7.4261 | -42.96679 | 2025-10-12 04:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 573054bb-8785-3316-b0e5-7e070330493e | -5.86718 | -42.84355 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53676fcd-c531-3668-b21a-b282150bcaf9 | -6.58812 | -44.62332 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 701cb477-820a-3f74-aac4-ff6dffc323b8 | -6.8368 | -42.78741 | 2025-10-12 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1779094e-d207-3fb4-9ecf-7496952aea9a | -5.25277 | -46.15269 | 2025-10-12 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68566f13-13fa-3b8f-b9f6-de289797cc76 | -3.8699 | -42.5167 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 74f191e7-ec46-36c4-8000-86c28cf79fea | -4.27614 | -46.92522 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f42c372c-c001-39a4-bdb8-1659bf00e508 | -7.8825 | -44.46088 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e817f6c7-c02c-3233-98ca-e44228ab1b69 | -5.20641 | -44.35748 | 2025-10-12 04:42:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f1b549c-2bd0-3096-8467-f285e9a0c55d | -8.01933 | -44.4746 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e25c224-1e84-385f-96e0-89fd79f6cb2c | -3.43453 | -49.84049 | 2025-10-12 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef07d3a6-1054-34c9-b91e-db45f0443757 | -2.92401 | -48.29864 | 2025-10-12 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f37ea9a3-4187-35a4-855e-b498a5ce3b81 | -7.49288 | -42.76545 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 152c98c3-a897-308f-978f-55121d245f53 | -8.21811 | -43.35983 | 2025-10-12 04:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a1bcd072-8af0-375c-abac-d11a7480f474 | -3.50473 | -49.05861 | 2025-10-12 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ff6f8af-bfb9-3472-858f-e63aaa85ae2a | -6.65318 | -43.72948 | 2025-10-12 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90cc6432-87f4-3479-9ea4-13fbd60a1282 | -4.6718 | -43.25806 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12ceb06f-02c1-3082-8e69-76ebc6490083 | -3.87776 | -42.51541 | 2025-10-12 04:42:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 47ee580a-81a2-3942-a7db-c04eaceb1da4 | -3.81166 | -50.21284 | 2025-10-12 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c88220b-3580-3b12-a265-250b12281e1f | -3.54411 | -53.02271 | 2025-10-12 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03477b5d-8655-3e49-99a2-36a7ef277f6d | -7.74459 | -42.4099 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0c0dad5-b2d3-3c60-95da-cbd50df09c5f | -3.1727 | -48.6098 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0042648e-5912-3037-8026-1a5a7d602424 | -7.48755 | -42.76963 | 2025-10-12 04:42:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 39fc0a11-25be-351f-a938-b147f243bf9d | -8.70116 | -47.05657 | 2025-10-12 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f540f84-b18e-3cba-8d4f-63728b01b55e | -6.58915 | -44.61621 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 134cb41e-bd93-32b9-81b3-97af97cd84df | -4.53825 | -49.68731 | 2025-10-12 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 35fc3b3a-58cf-31b0-9d97-0e54306b41c7 | -3.51575 | -45.84831 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6fdc58c0-48d7-3a01-8a2a-678fecf52f9a | -7.81262 | -44.12211 | 2025-10-12 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfeabdb9-59b2-394e-9720-0b517c41638f | -7.51759 | -44.60595 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0f89c34d-60d3-35cd-bc44-933dc2ad4c94 | -7.00538 | -49.34042 | 2025-10-12 04:42:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a68f8e0-a98c-3b0d-bd0a-24fbcc1dbaed | -5.4298 | -41.36664 | 2025-10-12 04:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f2a9403-6617-3e16-810c-fe3e60afc1d3 | -5.91655 | -45.42118 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 038ce0ac-8ea7-3791-ad8b-2d842779cb14 | -5.59543 | -45.83955 | 2025-10-12 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a045b4d2-1604-3d0b-a79e-43938f406a4f | -6.83657 | -42.78999 | 2025-10-12 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| de62e38c-fab7-3254-aa76-f585253ecb30 | -2.99662 | -48.74179 | 2025-10-12 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0ddc5f7-f0e9-3fc3-bb9b-39e962c683c2 | -6.05257 | -41.89166 | 2025-10-12 04:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 05cf340f-8201-3cf9-bc32-3f553305be29 | -7.7477 | -44.21307 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdfc000e-139d-38ff-ac1e-5cb83e5c549b | -6.58512 | -44.61568 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eda8a266-4d60-34b3-8657-4d53bf19364a | -6.50038 | -42.43715 | 2025-10-12 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 072701aa-0f88-36b6-893a-b89a0223fc13 | -3.41034 | -52.66066 | 2025-10-12 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d55dbb1d-39c0-3684-ad61-a0e185afb2a8 | -7.85568 | -44.52796 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02d45d61-69bc-3bb7-bdfb-72e5291303ba | -7.85495 | -44.1212 | 2025-10-12 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a749f8c-0d86-3230-8caf-fe8460c0e39a | -7.54727 | -43.83805 | 2025-10-12 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3297c7bc-a88c-30b8-9e78-3f62fe646030 | -5.7319 | -51.1092 | 2025-10-12 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e31cbd7f-32e1-3da8-833d-487981d8fc5e | -8.47899 | -46.23916 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a0c3a20-eca5-3ad9-8cdd-7daf9892a07d | -6.07921 | -44.30837 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baa9ce6a-4f9c-3908-90e0-418b42b5090f | -3.50195 | -49.05463 | 2025-10-12 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 818d18f1-b76d-3cfb-9d91-e7b5ffd396ff | -3.72732 | -44.10865 | 2025-10-12 04:42:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e347ee89-5338-3dc6-af87-35116ec7f630 | -8.70055 | -47.06072 | 2025-10-12 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0803792e-c4d6-3b1d-a40e-7123dbe21fd9 | -7.06085 | -45.2064 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e10a61ac-1e32-3341-b454-92110979973b | -5.49214 | -43.07149 | 2025-10-12 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4840858c-09d4-3678-9749-783df10cc562 | -7.88515 | -44.5164 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 10323c75-d578-304e-a7fa-087047801896 | -2.88464 | -50.72803 | 2025-10-12 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dddf8662-a951-35c4-8100-4ed97270f4b1 | -4.41718 | -43.46521 | 2025-10-12 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e69a739-ed45-312a-941c-a4852c51665e | -6.1757 | -44.66763 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README30.md)
