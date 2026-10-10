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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aec85c6-4b01-318c-8053-54408a168d5c | -4.37969 | -55.15911 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44a1e1d0-6503-3adf-983c-79304d1743af | -1.87956 | -54.68415 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5603e5f6-0209-39fe-b027-23824c48a2a2 | -3.27637 | -53.8705 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 458d2d9b-d2fb-3b81-ba70-0008563c579f | -4.1195 | -54.03894 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f93f92e0-e5a3-37bb-81e0-fd1803c1537b | -3.37187 | -59.3842 | 2026-10-10 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dc29343-1902-3116-95a6-288630ffbf86 | -7.23145 | -44.17698 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e70c76f-4fbe-3d70-9d46-1d7e4095d5fe | -4.05754 | -50.96376 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe406904-c39a-39bf-8792-06140ad11624 | -6.07807 | -44.0075 | 2026-10-10 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e4e8bbd-7bf1-3837-8da5-32f22f1d78c6 | -6.19549 | -45.4296 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5755c417-5e02-3db7-86af-25ac0619c261 | -2.98641 | -54.17079 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbe69891-1879-3100-9e36-10682be02396 | -4.0538 | -50.96309 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ea57153-3776-3d07-8fad-82d181cd5d78 | -3.791 | -50.79971 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a33cb76-b6e9-3fdf-a9aa-6c52b6499c5c | -3.9073 | -59.59652 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5e87f35-f452-3f80-807e-cf4ad2c18c63 | -3.0568 | -54.03729 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0691827-7998-3db1-9a9a-16c8ee8986cd | -3.23614 | -50.17861 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbbfa14e-b1c7-3e78-946f-c56b0f07d9c2 | -5.04058 | -49.35042 | 2026-10-10 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f425a02-f077-3c04-a370-55358488b498 | -3.56506 | -54.68858 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9850c418-e86f-3941-b8b0-abba36e86f4e | -3.92857 | -52.2049 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff3d8290-df66-3c13-85e1-9ea81b6e4f84 | 1.41241 | -50.6759 | 2026-10-10 04:44:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5284918-477d-3054-8e54-6f0ee6f5c86b | -3.47493 | -46.07337 | 2026-10-10 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b15f837c-0af0-3f0e-9e4b-4c1040af6e9b | -3.80477 | -49.9412 | 2026-10-10 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 793450d6-92f5-32ee-b283-e78cd742d0e8 | -3.31431 | -54.01176 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2bbae53-f2b0-305e-9022-455bf4c537b8 | -5.62445 | -43.64876 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1103aa8-80c4-3adc-96ef-ecffd5516c72 | -2.46888 | -56.06321 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d32339e-86d5-3334-9b9c-49cf94d0843d | -5.87056 | -53.51625 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 013bc822-3f96-3234-ab5c-6381c42109cf | -7.23346 | -44.16352 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6457dad-0645-3a4a-9ec9-1cfd923f53cb | -3.30586 | -54.00543 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5318d126-1658-333d-a5f9-a8814b7f5267 | -3.35563 | -50.40766 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3695a11-3e3f-3749-9117-1236b16227d2 | -4.15334 | -55.1358 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f8b19ef-3de1-329d-a085-401561b93238 | -6.19958 | -45.4263 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 862300f8-b368-363a-81ac-cd7810bfe857 | -3.92129 | -55.77007 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0b6fe1a-c10a-3092-9033-8be6afddb80b | -2.93715 | -54.07951 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1740959e-240b-3c7e-bb4b-9960ad68e4d8 | -3.46523 | -50.58792 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| becbcf56-8624-3625-99f4-36b1ac4fc099 | -3.6013 | -54.58447 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ca946f7-634c-38ff-ac9e-5d07a2c6988d | -5.10106 | -46.22741 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8ebf390-d826-3824-9738-1426c46320a5 | -1.10813 | -54.17506 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a13c9e4a-3264-30ec-b909-27de0b62decc | -3.53633 | -54.74316 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e2abaf56-e763-3ac7-919c-acd0fc43d1d3 | -3.25696 | -50.42006 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb1abe99-59c3-363d-9d24-4c105fcac37f | -4.852 | -42.82476 | 2026-10-10 04:44:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af5cd926-92ef-34d5-b975-22ed53b8c462 | -7.24097 | -44.16469 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee0f9985-606c-3751-a5f7-45bf11cfc5a8 | -3.84319 | -55.78691 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb884700-bd43-3fc1-ae02-5874fea82278 | -5.74486 | -45.12928 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a8d23bc6-f752-305f-88cd-cf9e7ebcb2e6 | -3.25398 | -50.41517 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41b9bb7d-c676-3743-913a-94cdbc707bc3 | -2.4554 | -58.03041 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bc57884-c9aa-389f-aa8b-127ee7d629df | -3.98662 | -59.36082 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c835bfe6-4972-3396-b96d-35e5851b0472 | -3.22314 | -49.43753 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02b0511d-ab40-3e84-b9be-6b6e2703d12d | -3.96338 | -55.34575 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f9a6cc-0cb8-371e-89de-66234dbd167c | -3.04217 | -54.15427 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39c408ab-bce3-367c-8904-ab34af467d97 | -4.11597 | -50.98247 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6690da2a-06e2-3ec0-8f28-15a3c2ec3e50 | 0.28582 | -51.41578 | 2026-10-10 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f26b5180-7103-392f-8747-5d3a669ec2c5 | -5.04806 | -49.34782 | 2026-10-10 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46a630d3-5742-3503-a851-454fcf861c8c | -1.02678 | -52.42759 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51b81c6a-9eb0-3c34-8620-6bafc366ebc2 | -2.47424 | -56.06422 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67c453d1-25ae-382b-99bc-538b5fc28143 | -3.27443 | -54.69606 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0218165b-bb32-32b4-8da7-5ff6c81fab93 | -0.98224 | -52.44697 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2e0181e6-f61b-352d-a3fb-44bc4a3e507a | -2.88966 | -54.07667 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db322659-3aef-327c-b3c8-9383f4885eaa | -5.7473 | -45.13461 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77326dac-821c-3eb1-b107-278b1477b27e | -5.61874 | -44.84856 | 2026-10-10 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e03ba0e7-e9e6-3210-a2b4-bf30a6ce440f | -3.27532 | -54.69077 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 369fde8d-063a-34f4-852f-7c2e36a74464 | -2.4493 | -58.02925 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76773047-f864-36cf-bf56-6637d703420a | -1.6451 | -55.2 | 2026-10-10 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f92f804-919d-39d2-b8fa-1eb3e59311d1 | -4.31254 | -55.34319 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83aad38c-4b1b-3c49-be09-cae2811b65a9 | -5.69085 | -53.47355 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d80213b-8e63-3b09-bddc-39b22f2bceff | -2.21949 | -53.69205 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6856362-ba4d-37be-bbf5-aa2ff7811699 | -3.29354 | -53.99397 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb627db4-88d5-30fb-b51d-bea97475f141 | -2.78952 | -51.4119 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3927e43-d1a5-3358-a335-41edccd2b078 | -4.30945 | -50.7861 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 561b6436-3af2-3712-9a01-7b770997ebce | -4.81435 | -42.75256 | 2026-10-10 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71e5f98e-0b89-34ad-8ebf-293af4c67451 | -6.87071 | -45.04015 | 2026-10-10 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be4667e2-7bfe-30da-a998-e5e76e888133 | -4.81734 | -56.08827 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16246b8a-bfa3-380b-8d99-f85885f842e6 | -2.40054 | -45.57676 | 2026-10-10 04:44:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 579858dd-8b34-3e41-b0ed-35fc2dcfcb58 | -5.60203 | -47.27651 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea789845-42ea-3411-bdcf-0b816ea36fb6 | -5.09769 | -46.22688 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a6aeb3f-f7df-3f8a-8c16-0dc26e05f1a6 | -3.54597 | -54.745 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d7c64315-a5d1-3b43-8ba5-3ff422d88d52 | -3.66395 | -55.54631 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4b555a9-4d5c-353c-9281-7bc6017fb7d2 | -4.40549 | -49.77795 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e60d5417-71a3-311f-b76c-b7acfb228ed2 | -1.33413 | -56.40019 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb2e71cd-e8e3-3f88-9929-ce06e693dac1 | 1.73252 | -55.57158 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff18f411-8a3f-317f-8b3c-d3d1fa7470aa | -2.54941 | -58.0325 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ab12e26-c8ce-3f5c-b8bd-692373707188 | -3.16471 | -50.45367 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fc5ccae-1cdc-3d8f-90b1-eaf875de205f | -3.21332 | -50.55023 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7d5ba01-db14-31c2-a0f3-c759f37f8597 | -3.06218 | -51.13044 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6238f18-4c30-3ceb-8775-c084766fd7c5 | -3.27634 | -54.06908 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b5a6f15-c44d-3568-b122-b3de08c08c13 | -3.22483 | -54.29184 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 65d9c38d-1f87-36e7-b240-02b412847a63 | -5.5965 | -47.28986 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af67b0d3-a2f4-352f-894a-a46b57c98d7d | -3.62582 | -54.23967 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd5560f-ae12-34c6-82ab-42280ab36908 | -3.84162 | -55.79614 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 228db995-d41a-3d67-8ae5-8c9e3ba7b8e6 | -2.74776 | -54.09815 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10367b3c-e252-377e-a175-6299985af4eb | -3.98474 | -59.37157 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79ccf707-2b48-30f0-aa31-d1f1db0ba400 | -3.22214 | -49.44249 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d80b383c-8ed0-3dfa-9df1-dce0a49f7838 | -5.59647 | -47.26851 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 787fa425-9900-3c22-94e1-5a3bcb7b6b4a | -3.25329 | -50.41947 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53c58c2c-c1b4-39c7-a8e2-bddfa0616d1a | 0.48913 | -50.78411 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ee055cd9-9d5f-3df7-8e35-0b39ab9fa63a | -3.7423 | -58.50083 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 304ff65a-b2ec-3c22-92f1-8d402b651d1c | -3.10274 | -53.78884 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f60c4fe8-07d4-3760-91bd-a24c66e29785 | -5.68389 | -53.47371 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e396f9c3-a908-3e60-83b0-bc0827967746 | -6.06736 | -44.66771 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea2d97e1-d5d5-33fb-b7bf-57c8232abdd6 | -3.87325 | -55.98612 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3178a7b7-1085-37b6-afa0-15c177e85dc6 | -2.99038 | -53.90168 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f693e6a-6641-3d6c-86ce-7b4d25bb13d7 | -4.68231 | -48.51877 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README69.md)
