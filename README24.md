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
| dcbbc351-6bb1-3208-9a84-d107078257c4 | -10.2709 | -57.71923 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 56ceb47d-d0c8-3754-ae02-62739181477e | -10.23155 | -57.82512 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2255e2cb-c608-3446-9e7a-aeb1cf8ae620 | -10.23031 | -57.81618 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 794e3574-394f-33a5-b860-07897cf17f17 | -10.13212 | -57.77308 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 90fd72cb-130e-393f-882e-abfa711cd9ad | -10.13088 | -57.76416 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 22759937-6eee-3b06-b321-13964778cd4a | -10.12329 | -57.77436 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 855c594b-ce4e-3672-a6e2-9a8cde6a4bc1 | -10.12205 | -57.76544 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4fca9f6b-edb1-3d25-b7ab-b19544968777 | -10.1208 | -57.75652 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7b23f7c7-0c16-3af5-806f-151cc4d9f9e6 | -10.9188 | -58.0673 | 2024-10-12 01:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9817616-f36e-3fa0-b118-e398d6772a95 | -6.89145 | -59.05377 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 53b3f748-870f-3964-92e1-af9e65b2c4fe | -3.16985 | -57.9514 | 2024-10-12 01:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| df7b5dea-0d62-323e-b3e7-ceac2eb44dc5 | -3.16856 | -57.94223 | 2024-10-12 01:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a16361b4-7410-388d-a9ae-8f269bbc7bf9 | -3.16571 | -57.40148 | 2024-10-12 01:37:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0cf03e7e-1ed6-340f-a308-0a3057379c83 | -6.47404 | -58.44103 | 2024-10-12 01:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ef8a4286-9598-3d6c-865b-d6262196051e | -6.35503 | -58.18481 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3326f90f-7cbe-3c0d-8bc6-334bfc651974 | -6.35379 | -58.17596 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3a9f80ee-9dc1-362e-a32d-b1b6ca0d4a2b | -6.34619 | -58.18608 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5877df0b-46b0-33f6-96db-56814d29c00c | -6.34495 | -58.17723 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| eab7666f-3a84-39d7-8059-5fd1c39cae63 | -6.34371 | -58.16837 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fd20f8c0-dc0e-33f7-bbe6-9b28641aa414 | -6.32942 | -58.32383 | 2024-10-12 01:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ea93292-280f-385d-a3ea-29cd127ec266 | -5.95538 | -57.69596 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8482ea2a-6d44-3035-b068-7f79f10270e9 | -5.8452 | -57.70572 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae45e253-8807-3042-b540-1407ebe7e8e8 | -5.84393 | -57.69667 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1cb27ed0-f3d0-3245-90df-cff9359568e4 | -5.835 | -57.69791 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7824147c-2b93-36cf-985e-47ef12fbf185 | -5.80315 | -57.73028 | 2024-10-12 01:37:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6788eff3-2cee-31b8-a78a-24eeceffd566 | -7.44507 | -58.60231 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d3f45caa-db13-39a3-81ba-17493c7eef7a | -6.90798 | -59.0423 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ecc7b95e-e37d-3a9e-9c3f-18d2f7274bd3 | -6.86778 | -59.09072 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5114fb04-c050-3006-b43d-3a3fa8c855a1 | -6.86654 | -59.08178 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f8561a39-18bf-3ba6-9bc9-e9540ad5a721 | -6.8653 | -59.07283 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b41b7705-a49b-3fcb-91f4-797b3ca5243c | -6.86406 | -59.06388 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 991c4e02-2688-302e-996a-c0e2c615c528 | -6.85889 | -59.09199 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| baf8f899-9fa1-3a50-a1fc-2b1eeece1000 | -6.85765 | -59.08304 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c6bdb939-6ecf-3bba-97ad-a3bccde60b7a | -6.81595 | -59.04331 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 225eb659-293b-3ec5-9e8e-54e7de37ce76 | -6.81471 | -59.03436 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7baf852d-e7b9-370d-a223-1b617f25a999 | -6.7473 | -58.88623 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 3e047936-28dc-3f0a-a04c-31f219494f06 | -6.74608 | -58.87737 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 57590aae-e7f7-3e26-9990-75736912ff01 | -6.73722 | -58.87863 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| afbe24e7-0baf-3cd4-a905-a4f875b3406e | -6.66939 | -58.77968 | 2024-10-12 01:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 42ecd32c-d07f-3b5c-892a-ce98d697f017 | -6.52576 | -58.40968 | 2024-10-12 01:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 506294b6-c937-3537-a6f2-4457ccebe88a | -6.52452 | -58.40085 | 2024-10-12 01:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 6e6956ba-e1ec-31dc-9f7a-768f906e74a5 | -6.51693 | -58.41095 | 2024-10-12 01:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a8ed2d16-743d-363b-8d37-216849cac565 | -6.5157 | -58.40211 | 2024-10-12 01:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7c3bb510-243f-3b3e-8edc-52cc810a56b2 | -9.30725 | -59.28174 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1a64dc3e-c396-3997-83b5-32000ebdb7f6 | -9.26799 | -59.39922 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f2b722b9-904e-3c8c-970c-da7e611709b5 | -9.21632 | -58.28159 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6d54e04f-e250-3738-82d3-34b54452d528 | -8.80953 | -58.20074 | 2024-10-12 01:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 28630e04-e01c-30d8-8b12-eb2714f4f071 | -8.22218 | -58.29176 | 2024-10-12 01:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 253cf144-d526-3817-beba-cc4bd4f6c918 | -9.90903 | -58.28864 | 2024-10-12 01:37:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 610b554f-171b-3b1d-ac09-6e9abfc24869 | -9.78753 | -59.02184 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2946d065-7869-387c-a037-497b95d6ab09 | -9.69138 | -58.65139 | 2024-10-12 01:37:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 145a8dfe-c4c5-377a-9109-d8fc2fd5a34c | -10.65154 | -58.40718 | 2024-10-12 01:37:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c4073699-31f1-366f-b53a-a45ef8862e76 | -10.64673 | -58.77275 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3e881b52-6d6a-3852-b9b8-80b167f08f3d | -10.6455 | -58.76364 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 15cb742b-d6a4-32ed-978d-f86f5c3e020b | -10.47043 | -58.76273 | 2024-10-12 01:37:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0b827900-2236-3f04-85e5-0a4b8ae6f125 | -10.46273 | -58.77343 | 2024-10-12 01:37:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a5fc16ed-7a66-3bfe-9ed0-cbf970d932f0 | -10.46148 | -58.7642 | 2024-10-12 01:37:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 53d2e6bf-288e-3737-9416-bce63e35a94f | -10.3588 | -58.88876 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a651a012-7f78-3599-be19-2db8680b4297 | -10.04921 | -59.45565 | 2024-10-12 01:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8deec8e9-183f-3f45-a821-8b0fefd74ed7 | -10.99218 | -59.01178 | 2024-10-12 01:37:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3121f565-6e3e-3872-8823-3f95cbd5fbaf | -3.47928 | -59.50454 | 2024-10-12 01:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c2c95d8-6fc1-3167-8745-4ab999a39be1 | -3.44742 | -59.61436 | 2024-10-12 01:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9806b7fb-5921-3306-a657-5b323bb71111 | -3.43981 | -59.62446 | 2024-10-12 01:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ba2e9a08-4378-3f90-892b-1aafc79e47cd | -3.43857 | -59.61561 | 2024-10-12 01:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7949bfb2-9d93-3e17-8ae5-07d788c44f5d | -4.26696 | -60.00054 | 2024-10-12 01:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 182749ff-54e8-3a15-978e-8cd8ee779846 | -4.25675 | -59.99272 | 2024-10-12 01:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1c30e4ba-69ef-32a7-8c86-b6ff75d3d1c2 | -4.21463 | -59.95877 | 2024-10-12 01:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 66e902ed-d5e1-3941-a326-ec4721c266a7 | -3.93205 | -59.12305 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 089fb190-128b-360d-aff7-8501d85b010f | -3.72256 | -58.47542 | 2024-10-12 01:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3cd616e9-3850-3f53-a777-76ae206d6ef2 | -6.38339 | -59.98748 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b8252243-b1e5-3099-b5db-d9dfb18778a5 | -5.36636 | -60.09166 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 68dafbab-a466-3610-8d79-88c61f7a6c50 | -5.33366 | -60.12153 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3490fdd4-92bc-3bc2-a1cf-89b0eeb2a6cb | -5.32716 | -60.14142 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a8b6acb-2070-3bea-8c4c-2aa1273a0a50 | -5.29071 | -60.21318 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| affa544e-32b1-3c1f-9cf6-8576c759a0e1 | -5.28944 | -60.2038 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 28eeec89-ab86-394f-8b38-9b9ea871a8c4 | -5.26094 | -60.19463 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 873a4abe-4d16-3868-b38b-a7c4440fe27a | -5.17918 | -60.13636 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 11319511-e702-30b9-9044-2261569e5667 | -7.40611 | -59.7202 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d3bc4739-48e1-38bf-9b9c-d43d9fc8b40f | -7.39704 | -59.72145 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 142e4295-e99e-3cd1-a587-19f27fd3a2d9 | -7.39576 | -59.7121 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 69e3ab40-38cf-379b-becb-9bd84af96627 | -7.02637 | -59.43377 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 28ce0894-5a21-3c72-9113-103266a499ab | -6.91828 | -59.79026 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 48a38f9e-ee0b-3233-b739-b8be0acfa26f | -6.89362 | -59.81271 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8546ed09-f478-3581-ad33-8f256845abf6 | -6.89235 | -59.80336 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 76bd992e-8ef8-35ec-9c4e-ef02a9e2015c | -6.81173 | -59.14433 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d777817e-b663-3725-9323-1b0eb79b5362 | -6.80914 | -60.13592 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5b0be171-9152-36df-836a-c6f79bb34bed | -6.80783 | -60.12632 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a7002809-b05e-3845-9477-c7274fffc7e4 | -6.80522 | -60.10726 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b8ce2226-ff5d-3639-a4d4-8852ec06332a | -6.80283 | -59.14558 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e8accf8-0ab3-311a-b709-9477168323d6 | -6.79404 | -59.35484 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| fcbe841b-9743-3eed-9721-5a2b325f34a6 | -6.7878 | -59.3096 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c2d83dcc-98ea-3759-8ce3-dd28786ffba8 | -6.75458 | -59.33271 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| acca7d4d-70e7-3e5f-a2d0-3d377763ca8c | -6.75334 | -59.32365 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f6300540-5c6d-3c14-a536-246f2b226b34 | -6.74689 | -59.34299 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| c09533ef-f336-398f-936c-29f0be4fcea3 | -6.74565 | -59.33395 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 339.8 |
| f7c3294d-abc3-3775-a634-608683160558 | -6.74442 | -59.32491 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| a932a07c-be65-3a20-8a80-741bfec47519 | -6.74071 | -59.29781 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 882d0165-bfb4-3b20-bd01-7bd85475be10 | -6.73673 | -59.33523 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fd65975e-a00e-349e-b392-62c49610c563 | -6.68977 | -59.86894 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 05659219-fae2-3ebb-816e-5d201c5f71a7 | -6.67992 | -59.46047 | 2024-10-12 01:37:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README25.md)
