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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d6807eb-1193-3054-b690-34f853f29252 | -16.48572 | -51.3064 | 2025-07-27 04:10:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72be75e5-0025-338d-bfcc-777ffe95faca | -18.22236 | -54.55161 | 2025-07-27 04:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1838d9b7-ea71-3d94-afe0-5196e22d3ce0 | -15.99046 | -42.64966 | 2025-07-27 04:10:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| de578bb1-a4c1-325d-aa97-c43992b830a3 | -17.04391 | -43.76862 | 2025-07-27 04:10:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d247a6a9-1ab6-3ad7-a9ce-f26e7b06722e | -21.3411 | -45.63503 | 2025-07-27 04:10:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dbf74003-f199-37fb-ba9b-d351c5a18bab | -15.27113 | -43.07618 | 2025-07-27 04:10:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 44c2ec2b-78c7-3655-b85c-0a3810443fd9 | -17.98919 | -53.17246 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d1dcfd14-ee30-3ad9-8816-d79020592401 | -20.86659 | -45.51994 | 2025-07-27 04:10:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cac3191-3505-38e9-bced-7bafccf44cd5 | -15.03691 | -46.52241 | 2025-07-27 04:10:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea5e6246-9c3b-30ca-997f-68332c64ebb2 | -15.03538 | -49.25747 | 2025-07-27 04:10:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23a71659-7b6b-3d0f-a189-fc9a51243061 | -15.01888 | -49.25427 | 2025-07-27 04:10:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d3926a5-86c2-3fa1-bbe2-9071dda0d94e | -15.52483 | -42.66251 | 2025-07-27 04:10:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bf4c83ce-9cf7-30e4-94bd-183b881b7f5a | -20.34917 | -45.98959 | 2025-07-27 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7738654-3871-34b1-a9d9-ed17070f4210 | -19.14327 | -46.59579 | 2025-07-27 04:10:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 240b3202-1ef8-39b4-90af-521c90cc910e | -16.48476 | -51.31133 | 2025-07-27 04:10:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4b2c82f-619b-30c8-a959-e99ff08676aa | -18.39419 | -44.18764 | 2025-07-27 04:10:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5476442-8cb0-30d5-9478-4399eb4c870d | -17.99869 | -53.17737 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36083095-bfa6-31e0-ab8a-9c5273960370 | -18.81278 | -44.46341 | 2025-07-27 04:10:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71abb490-5e76-3d78-80f3-17a5dc586e28 | -19.39223 | -44.31933 | 2025-07-27 04:10:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfea809c-fa02-34da-9b1b-4273f73d0426 | -15.0366 | -46.52134 | 2025-07-27 04:10:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b05f0e9-c2e4-38ae-8439-fb297e1706cc | -15.26781 | -43.07564 | 2025-07-27 04:10:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 36ea47b9-9e57-3d51-8706-e1469ce171c6 | -17.99991 | -53.1714 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7d044a2a-f900-3fe0-9a89-3dd0e46151ba | -18.20719 | -44.62056 | 2025-07-27 04:10:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e242dd6-6288-35a5-a293-44e724b3fa12 | -19.39166 | -44.32298 | 2025-07-27 04:10:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d34c25d6-c6a1-3616-bdd1-a4ff8eec4c4d | -18.39145 | -44.18345 | 2025-07-27 04:10:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 915aef0b-70ad-38a5-a14d-22ba7c519a42 | -14.96493 | -46.97136 | 2025-07-27 04:10:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 324ebb87-42ac-39e6-bf28-e619735f61fb | -14.96228 | -46.96938 | 2025-07-27 04:10:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89463697-f26c-334f-adf4-c7de85c76a81 | -16.26266 | -47.82164 | 2025-07-27 04:10:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb4b51e9-2401-37a5-af5d-bcf7f44cc463 | -16.1858 | -48.72178 | 2025-07-27 04:10:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 779337b2-17cb-375f-aaf5-fe011138ffb6 | -17.98741 | -53.18112 | 2025-07-27 04:10:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cf3aef5-0904-355d-af08-09c09cd910e0 | -22.61572 | -44.12738 | 2025-07-27 04:10:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 41841de6-65f2-3030-926c-427014c4437b | -18.99011 | -48.42112 | 2025-07-27 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 309d5f0b-bacd-360e-aee3-098e5a0154ff | -26.02209 | -49.00362 | 2025-07-27 04:12:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 8923752a-9a94-30d0-a770-776978d96071 | -26.01898 | -48.98017 | 2025-07-27 04:12:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6442a1a3-5578-32fa-81b0-a8eaafd401f5 | -26.02129 | -49.00817 | 2025-07-27 04:12:00 | NOAA-20 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| e1525aca-4f4a-349b-b07f-52eb53d27821 | -23.52014 | -46.97402 | 2025-07-27 04:12:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ebd72bcd-8622-3dde-a26c-99a62157a8ce | -21.423 | -54.13575 | 2025-07-27 04:12:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb05eacf-460e-33c9-bf3a-dd592f1aabca | -26.01856 | -48.96201 | 2025-07-27 04:12:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bf9c519f-9ec1-358c-8080-5951d2abaf17 | -25.81247 | -49.16107 | 2025-07-27 04:12:00 | NOAA-20 | TIJUCAS DO SUL | PARANÁ | Brasil | 4127601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f1b85315-de12-3d43-97e4-ad47b5f2c6c6 | -23.06861 | -49.67269 | 2025-07-27 04:12:00 | NOAA-20 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 334f355a-9aae-3429-98dd-982bdefda704 | -22.36275 | -49.09999 | 2025-07-27 04:12:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49ca393c-1ccc-3bcf-84c3-15919c962107 | -21.41865 | -54.13149 | 2025-07-27 04:12:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a794d2b6-0d92-3b4e-b25a-68e9cdd163c0 | -23.2399 | -48.06979 | 2025-07-27 04:12:00 | NOAA-20 | PORANGABA | SÃO PAULO | Brasil | 3540507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fce5d0d9-a321-35c4-abb7-0f8e58acd9fe | -23.0649 | -49.67182 | 2025-07-27 04:12:00 | NOAA-20 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0536bd6d-599a-3b34-9209-0983d93ab77c | -26.01628 | -48.97504 | 2025-07-27 04:12:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7853de44-3fd0-308e-a7fc-545d54419476 | -23.07231 | -49.67356 | 2025-07-27 04:12:00 | NOAA-20 | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c294461c-02a6-3b9d-b482-0f0658d5c4a2 | -22.43493 | -46.91047 | 2025-07-27 04:12:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4a9d72e-6681-3f5d-83ee-bd2b1b26af73 | -22.98769 | -46.4701 | 2025-07-27 04:12:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 899a2aed-5923-327a-89d4-a2eef4024611 | -26.01782 | -49.00744 | 2025-07-27 04:12:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 33f99213-dede-3120-a898-44e349d7c928 | -23.70688 | -46.80714 | 2025-07-27 04:12:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d13dcf8-84c4-3acf-89ed-ac351f8af0b6 | -22.31063 | -48.48201 | 2025-07-27 04:12:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d04d76db-3c52-39ae-b870-082c43c4c4ee | -23.3741 | -47.42585 | 2025-07-27 04:12:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8c71819b-2e1e-3e92-9dcb-e8b5cd28d7ee | -24.51698 | -48.85625 | 2025-07-27 04:12:00 | NOAA-20 | APIAÍ | SÃO PAULO | Brasil | 3502705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9f47d921-bdac-3300-9147-35778cac0ea4 | -23.06225 | -49.68637 | 2025-07-27 04:12:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1eab35ae-d74b-3503-be55-4bc47f7db2e2 | -26.02476 | -49.00897 | 2025-07-27 04:12:00 | NOAA-20 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| a92bbab9-c74f-3978-b025-6dcbe6003b6a | -26.01781 | -48.9663 | 2025-07-27 04:12:00 | NOAA-20 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| aa124ed5-e092-3208-94b8-72f4fac0ba5a | -6.6575 | -58.8468 | 2025-07-27 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d917e43e-d506-313b-b415-76ecda2dd481 | -6.5631 | -51.1126 | 2025-07-27 04:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 03c3049f-7443-3841-bb8f-2be9db90d947 | -6.639 | -58.8475 | 2025-07-27 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| acfe4d9c-f0ed-3b61-939e-9e99747c9017 | -6.6574 | -58.8661 | 2025-07-27 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 793de02a-3bd4-3e6e-be66-626430cf1358 | -6.639 | -58.8475 | 2025-07-27 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 6f23b193-1439-3e00-9d58-871f2e75f836 | -6.6206 | -58.8483 | 2025-07-27 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 1f94f002-41f8-302d-a061-4612af9715ba | -6.6575 | -58.8468 | 2025-07-27 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| f5246ec0-d14f-3d56-b96c-705005ea72bf | -6.6389 | -58.8669 | 2025-07-27 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5b9aa869-c59d-366b-9810-b5916a8e8fd3 | -6.639 | -58.8475 | 2025-07-27 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 6850b4b9-35bd-33f2-b53c-bfaad9e5f6fa | -6.6389 | -58.8669 | 2025-07-27 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 21895cf0-a49b-3301-8b78-6cc1763a7cf4 | -6.6206 | -58.8483 | 2025-07-27 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a787372f-f306-35bc-862f-3b8fa3de0de5 | -6.6575 | -58.8468 | 2025-07-27 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 75add07a-45bb-3e49-9ab3-10518e01ea40 | -6.6389 | -58.8669 | 2025-07-27 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5868f713-d2e0-3a0e-920f-0969f475fb58 | -6.639 | -58.8475 | 2025-07-27 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| ad7990be-9a87-3101-ba17-d2b77f036135 | -6.6575 | -58.8468 | 2025-07-27 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9586c378-3dae-353d-abf5-7c15a2149b4d | 1.0766 | -52.36222 | 2025-07-27 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d8d78b73-9560-3c24-a203-c3da6c6249c0 | -6.01838 | -44.05616 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d40d2de7-044b-3824-84a6-697bf93386d4 | -8.0159 | -48.16961 | 2025-07-27 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b388c85-1b6e-3d6d-9ebf-168479bf4dc2 | -6.65404 | -58.83026 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b314480c-5d4f-3f58-b89b-22a0b5170bc2 | -7.76023 | -51.1187 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd07dec1-30b8-38f9-8da4-35441c445c6e | -6.62152 | -58.83479 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 529362a8-8f48-3e85-bb7f-e5de8b6f6ef9 | -6.63778 | -58.83256 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95616426-2176-3529-bbfe-1722b4295f86 | -9.0353 | -45.39587 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aeb8f7f-cf5b-3727-b547-c11a90635c27 | -6.53734 | -56.18586 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6439afa-c8df-390d-9a2f-a226afe34e2c | -6.64614 | -58.8539 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f8980e67-e936-3458-be57-3780bac45577 | -6.49754 | -56.19463 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdd376d8-f6ad-3764-aeed-f5513b7c6d81 | -6.63923 | -58.84768 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6c87f027-5564-317b-b476-523fe47c1608 | -6.63858 | -58.82777 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26d60b0b-9673-33fa-9b94-f638ac14d24d | -4.61538 | -43.32431 | 2025-07-27 04:57:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc282320-72f9-3d27-8d4b-8a48ac1c9f56 | -2.98342 | -49.01032 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34864bc6-ae80-31e9-b9d9-15b38d66858d | -6.64711 | -58.82418 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf4e71ee-7b0d-33d0-b56f-4b8c80ce5214 | -3.06453 | -49.49724 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5c8755a-8fa4-3896-a532-7be40500e180 | -4.07079 | -42.53502 | 2025-07-27 04:57:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e996a1b1-0141-314a-a979-52eb21f5c869 | -6.62926 | -58.83604 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd2dea6e-9864-3eb3-b98b-41e169a3430d | -6.62763 | -58.84574 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a309180-9f23-3521-96ce-5dd489266d76 | -6.38848 | -47.33773 | 2025-07-27 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd76eb81-da16-3c11-83df-93e900304251 | -8.17135 | -43.20983 | 2025-07-27 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a589cda1-8399-3096-9dcb-e645fc22e20f | -9.43601 | -51.7478 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5da9f58d-4526-3046-b9c4-1a509af4527b | -3.05302 | -47.38161 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53592e2c-607e-3562-a329-a4ecd2557f05 | -6.65791 | -58.83087 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c7958b3-efbf-3739-8a28-cb95ba74df03 | -8.51107 | -47.48954 | 2025-07-27 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ca4ca8f-9818-3a7a-89ef-1d40385f5b8d | -6.65469 | -58.85027 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f40347bc-b768-30f1-898e-6d64d8e06312 | -4.07625 | -42.54066 | 2025-07-27 04:57:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 63604215-8eb8-3371-92d1-f7ff03dbcd6e | -4.11001 | -47.93885 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README14.md)
