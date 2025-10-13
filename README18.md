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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a0b1df0-040a-3c1a-b682-73f76515c5f6 | -2.78476 | -49.57872 | 2025-10-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 294e8ee1-3d83-339a-8acb-7d4a716e80a6 | -2.53022 | -47.80702 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d14414d3-2a40-3225-881c-efd7516189c6 | -5.32064 | -43.43245 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ad663a4-7aa0-3115-9b40-4dbb9277a4e1 | -4.5369 | -42.88766 | 2025-10-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e7b55696-7a5e-3388-aab4-195212d52786 | -4.47719 | -44.93755 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2ec2e029-eb92-37f8-93b0-1686c169d8a7 | -4.40307 | -41.59333 | 2025-10-13 04:21:00 | NPP-375D | LAGOA DE SÃO FRANCISCO | PIAUÍ | Brasil | 2205573 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 64f87c69-a8ba-355a-9bfe-fad76d2338b8 | -5.91792 | -45.43074 | 2025-10-13 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63d19c9b-3755-3d4f-94cc-96a9ebb3d6b5 | -4.70248 | -46.01285 | 2025-10-13 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dac9350-e2f9-3a08-b62a-c4a71b3b311e | -4.83392 | -43.3502 | 2025-10-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c1f2a4e-b1da-37cd-8814-2548eb53c2a8 | -5.56188 | -41.32239 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 63e7a256-0b22-3ef5-82a9-0e8c0c3ae4c1 | -5.88305 | -41.38798 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1c5d7843-76ea-34e2-a65c-6d2ab897ec67 | -5.62462 | -42.68983 | 2025-10-13 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6e6ab7eb-9498-3bd2-8863-a168ed2e64b8 | -2.24915 | -47.87732 | 2025-10-13 04:21:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7bdb7ed5-c3d9-3623-8623-a27c99912418 | -5.48048 | -44.65495 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ce4abde-a141-3324-9a77-2d54561aaff4 | -2.46172 | -48.66301 | 2025-10-13 04:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c11af29-d064-3ff0-9119-025891cf3013 | -3.07157 | -49.38137 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b273011b-3041-3ba2-8f79-bc0e208367e2 | -6.40856 | -42.53632 | 2025-10-13 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| dcacba7a-57b3-3ec0-ad9c-932b40a195f5 | -3.8527 | -50.96893 | 2025-10-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 099a606f-536f-32d4-9bf7-dcc7a4c7ce8c | -2.53096 | -47.80243 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ae99fa88-b3d3-3ae3-92b0-f9b037790d2c | -3.82345 | -47.7424 | 2025-10-13 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39ab6ef4-220d-36a5-a500-b824f07a97ff | -5.34928 | -45.96519 | 2025-10-13 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b57b1584-b4fe-3e7c-b486-6f79429dc2a5 | -2.26119 | -47.85072 | 2025-10-13 04:21:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 039ae460-67ca-37ed-8c87-9de572c24cb9 | -5.49835 | -43.7888 | 2025-10-13 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e07c5d5f-49f0-3b44-afaa-3db8c2fdef58 | -5.8179 | -44.03207 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4ce27be-fabd-3e51-ba13-c0bdc6f72469 | -5.83457 | -42.30766 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 60ed962c-c806-3c89-b9c6-c98168f630fe | -2.79066 | -49.59563 | 2025-10-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54cf5c0a-c3ac-35ce-ad14-c967771f3a57 | -5.4788 | -44.64403 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8535857-3ea6-3b48-aed7-f4d7afee5032 | -5.29786 | -47.85793 | 2025-10-13 04:21:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22951fd-a6c9-3d82-8f9e-5867639c6b96 | -3.06742 | -49.38068 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fa1b644-7cb7-3cd6-b20a-27e58c7f2bec | -5.81184 | -44.049 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca41f225-4478-37d4-9e43-6cea22a4fa32 | -6.22083 | -41.56644 | 2025-10-13 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 402d508a-5a0c-3372-a0b1-9711ad227cf9 | -4.86581 | -45.73378 | 2025-10-13 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77868893-fdc4-30f1-8ee0-7ae37dcf1f69 | -4.87244 | -45.91179 | 2025-10-13 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b62ccdd-d7bd-39bb-8010-b894c34375dd | 1.78399 | -55.80862 | 2025-10-13 04:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4bbdb30f-6a79-3883-8eb8-bd422060f58f | -3.43737 | -49.84008 | 2025-10-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2ffffd5-a7ad-3cd3-b0c3-1a0c5b58f09b | -4.75859 | -46.42816 | 2025-10-13 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25c2ac53-422a-3ded-8edb-3d435da27f2d | -5.88735 | -41.38426 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31c41596-c942-348b-a210-d1d7d598c147 | -2.53474 | -47.80308 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| dea96fbe-f171-3077-99a1-0a59b3145e0f | -2.14631 | -47.50802 | 2025-10-13 04:21:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b89f7f-b22e-3fde-a5a3-bb33af0bb008 | -5.89745 | -44.73498 | 2025-10-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7ab69c5-5cac-3610-8f61-1286ba966870 | -2.29183 | -47.99232 | 2025-10-13 04:21:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc461c07-52d3-34e5-b522-3f47f27cce84 | -2.76458 | -45.07152 | 2025-10-13 04:21:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87652c3c-aa3d-3100-8794-7f59e41f5c18 | -5.85913 | -43.85586 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 369122b5-7275-311c-9177-4f44515eabf6 | -4.51182 | -50.38845 | 2025-10-13 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92b0a26e-86b2-323d-aabc-8ff66eeaffd3 | -4.52378 | -50.21021 | 2025-10-13 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7bbc152-0245-351f-b8ce-9f94cb5c8f5d | -3.09888 | -50.37349 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e29937a5-5d8f-3a93-921e-64c4a53392d4 | -5.24841 | -45.59663 | 2025-10-13 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29cde82f-198a-3917-a731-d3e1f62cc24a | -7.77629 | -44.04892 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52d523fb-b654-3c81-9293-d208bc5b46d7 | -7.70072 | -42.37267 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bd513678-c52d-3b4b-8dfc-33305b6ea27c | -8.23848 | -43.35858 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aafc3288-38f4-31c8-aa56-80e70596d372 | -7.80492 | -42.44422 | 2025-10-13 04:23:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 34330ec5-b8bd-3dc9-a19a-8a4fa6c3628a | -6.73587 | -42.85933 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be760f18-63ee-3578-b82f-94153d90e31b | -7.28506 | -41.95943 | 2025-10-13 04:23:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 364569d4-db50-3a40-b228-b935598fe1b7 | -7.21703 | -39.90321 | 2025-10-13 04:23:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| efed9d9c-a6a3-3d37-909c-860c1c6b5ecc | -8.46347 | -46.12706 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4d1c5e1-0e1e-367a-a5f8-63fc33baf10a | -8.54438 | -45.42697 | 2025-10-13 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26a6abda-aa38-326c-bfec-04d51b751de2 | -10.81207 | -43.98902 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3421fac6-86e9-328f-8bd2-1eb9a75d1561 | -8.47877 | -46.24648 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59c659b5-ad38-3cf1-935f-b2490b469737 | -7.37791 | -44.07047 | 2025-10-13 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00aa00d4-4539-3464-84aa-6df0f1b96f99 | -10.80977 | -43.98105 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56a5ffd4-b9d7-3116-96ee-ff95d13f4807 | -7.50915 | -42.16046 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 68b281ed-6a29-3641-8fba-5569431f2386 | -7.92129 | -43.31118 | 2025-10-13 04:23:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 970c4fd8-b6a3-3d9a-9c13-4275dd4a1ebd | -8.23791 | -43.3623 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 079b2877-9b31-3beb-a8ee-c6a6e0114272 | -8.32935 | -46.24384 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e93151f9-4490-3c79-abe2-65831675833d | -10.14623 | -44.55235 | 2025-10-13 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63f538bc-d95b-3354-819a-5ac63f504d36 | -6.58024 | -45.97567 | 2025-10-13 04:23:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5b00e47-6434-3926-b8ca-680053997ee4 | -7.62399 | -43.04507 | 2025-10-13 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a75e8e3f-f37a-320c-8105-d6dbdf1e0908 | -7.76351 | -45.69987 | 2025-10-13 04:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b283cf18-bc8d-30b4-89bf-6cd470be125d | -7.49075 | -44.62317 | 2025-10-13 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7137b499-1fcb-3ed7-aca7-7aa261026bad | -7.40347 | -41.81896 | 2025-10-13 04:23:00 | NPP-375D | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2914356c-95b0-31f3-823b-4e0fba3220e3 | -6.77055 | -42.83352 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 70b56391-d2a3-3b2b-9902-915161f4262f | -10.80523 | -43.98795 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51beede9-a2ab-326c-9215-b898c0aa3a8a | -7.50975 | -42.15642 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4d73d5b9-60eb-335a-ae37-f296acba2f53 | -6.74709 | -42.16088 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 883da992-04e8-3797-94ea-354eafe9b6d0 | -8.4701 | -46.15005 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd7043c4-4c26-3427-a13a-8c46efb44dbc | -7.54088 | -46.09225 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ee09c40d-ad00-3787-8d4d-00d2a6091b6b | -7.55683 | -43.83977 | 2025-10-13 04:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db4b0c5d-02da-320f-804d-ca680dee3b5c | -9.37977 | -47.02989 | 2025-10-13 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8c26d09-f2e5-33b3-9ead-791963d50f5b | -8.54216 | -45.41946 | 2025-10-13 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf6d506c-4a86-302a-bdd6-eeb308655e5d | -10.81319 | -43.98158 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3e82da7-5226-373f-ab5d-9a21be39e9b6 | -8.46625 | -46.13114 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a2345ef-ab31-325b-b9ae-47413a9300db | -6.76305 | -42.8132 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 41b5c807-5647-3d9e-a724-2cd6bac8f96d | -6.27435 | -43.90184 | 2025-10-13 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa980e63-0b22-33af-9500-d8f7a40038d9 | -10.81662 | -43.98211 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6b10608-825b-370e-84b3-428a78bff44f | -10.80062 | -43.97206 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e733bde-6233-370a-9822-f824cc6c3a16 | -8.23619 | -43.37348 | 2025-10-13 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3141d6ae-9d40-392d-b75d-691fb541848d | -7.68496 | -42.38359 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e4321b78-65c0-3a7b-acde-2e061602136c | -6.2738 | -43.90535 | 2025-10-13 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15132950-2dd6-3765-bf8e-eac3c43ad34c | -7.69718 | -42.37211 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e732dba-1716-3f03-b88a-8037c43252f7 | -6.77282 | -42.8186 | 2025-10-13 04:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e686b281-f640-3781-94f9-0fa15fdab2fd | -7.49795 | -43.06842 | 2025-10-13 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2832ac72-cd6a-332d-8c4c-016f51060de0 | -6.74416 | -42.1564 | 2025-10-13 04:23:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 93400d89-f2f3-38ba-a292-7f315d91634f | -7.77909 | -44.05301 | 2025-10-13 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e51cfcf-8356-350f-b205-f6cbc66e81c9 | -7.6885 | -42.38415 | 2025-10-13 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bdd1eb94-d736-37c4-9b57-a8cd936d5c59 | -8.52221 | -45.39479 | 2025-10-13 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbeca168-1c3d-3aab-acf1-8a1a5f74d0ea | -10.80348 | -43.97629 | 2025-10-13 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a82d6657-79e3-3bbf-a522-21120b8b8770 | -7.51508 | -42.16961 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e522f549-9ac2-34fd-9438-f2cd8244b7f5 | -7.51629 | -42.16154 | 2025-10-13 04:23:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 679eb00e-b909-3858-9743-1f45a60d7a52 | -8.32657 | -46.23974 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4ea799a-7040-3536-8416-61230d3eed90 | -7.53934 | -46.09214 | 2025-10-13 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README19.md)
