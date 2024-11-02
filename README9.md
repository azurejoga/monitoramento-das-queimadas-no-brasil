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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1058b822-bc2b-3e82-8f57-bd9ccc2d8958 | -3.74636 | -46.05748 | 2024-11-02 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| ee5a8dc2-e0cb-3a71-9586-05b56eb25f14 | -3.74488 | -46.04723 | 2024-11-02 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| ac32d51b-6496-3b3d-ba5b-ae7ca19b28ec | -3.73687 | -46.05883 | 2024-11-02 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 549fb780-3496-33a7-8908-2c75e34fdba6 | -3.73538 | -46.04858 | 2024-11-02 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 03d4940a-74fc-308f-b20e-41f25de59499 | -3.71468 | -46.00477 | 2024-11-02 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3d562691-409d-3b1c-b69d-ae0ea6bfa521 | -3.66745 | -45.80872 | 2024-11-02 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d9d9c379-f9cc-30b8-b672-7e80d3160b04 | -3.66595 | -45.79812 | 2024-11-02 00:54:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e20b741c-7f31-342e-b8f5-b7abf4d8c76f | -3.63901 | -45.95222 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c0d16610-36fc-3a4d-bd97-1467c662fe0c | -3.63751 | -45.94181 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 723cb54d-2941-3f37-8790-53960ac83bbb | -5.01949 | -45.53168 | 2024-11-02 00:54:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6dddb2a4-ec7e-3e88-8838-bd1e0386922e | -4.99004 | -45.60007 | 2024-11-02 00:54:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4eb602d5-8bf8-35f2-ba9d-97f054f5d346 | -4.96644 | -45.87415 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 87b34829-2923-3184-aaea-245b9d79e0c4 | -4.95356 | -45.55179 | 2024-11-02 00:54:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c69bd344-0079-38be-a01b-c6d465a84a5b | -4.95203 | -45.54137 | 2024-11-02 00:54:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eebcc1cd-8242-36fa-bba5-85bfd6040a97 | -4.94939 | -45.54767 | 2024-11-02 00:54:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 30fe5086-7d31-36ca-8f40-2888f7ac3ac5 | -4.89649 | -45.96285 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 30.1 |
| dac7807d-5891-326a-8c47-9e83871574d7 | -4.89506 | -45.95274 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e1992038-0095-3b93-b9f4-f222928c213f | -4.86249 | -45.79149 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cfcb92f2-359c-3946-9017-a809aff55902 | -4.86099 | -45.78096 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9eb0cee0-ba7d-3557-ac7a-82df554b7d16 | -4.85299 | -45.79287 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7bb112ef-7074-318a-b5f3-75904d655780 | -4.85148 | -45.78232 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 033c50dc-31cb-3179-b655-4b32616e10fc | -4.81195 | -45.77762 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 013cb10f-943e-3a24-bd36-872da1badf5e | -4.79726 | -45.77511 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 99839e2c-cc5e-3709-8dbd-5e46d459dd32 | -4.79544 | -46.03463 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4e77574-d258-3778-ac71-acc75bf5b849 | -4.73361 | -45.97802 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 949dcaed-181a-35d3-a70a-6357dce50e88 | -4.72605 | -45.75341 | 2024-11-02 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ef372ebd-ae58-313b-821e-ff3fd0e3cee4 | -4.72456 | -45.74308 | 2024-11-02 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b4fac3fb-d02b-3e02-bb10-2312be7ec4f3 | -4.70408 | -45.83699 | 2024-11-02 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 757cced0-4a5a-352b-8930-e5f30573038c | -4.69332 | -45.66272 | 2024-11-02 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a6ac1049-dbd0-362d-8544-070ecf582968 | -4.68873 | -45.65899 | 2024-11-02 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 519ca7e8-fd65-3003-84f4-1685dbc5b880 | -4.68288 | -45.89224 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| efe24f9c-3c73-32c5-9e3f-8155137a4302 | -4.62175 | -46.04163 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| e6e3be53-09cc-3b96-abc1-26744a34f2d3 | -4.61235 | -46.04296 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6c56e80f-2c4c-3fd4-936b-90183ddea5f3 | -4.61092 | -46.03299 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2832c4c4-e8cc-35f6-8926-e68f3c4f29e3 | -4.5706 | -45.68199 | 2024-11-02 00:54:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e09b2b63-1c6b-34bf-a141-cca8b7c42eea | -4.8216 | -44.79016 | 2024-11-02 00:54:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fd9a40d7-e9ef-3d3c-908d-847c3288d94d | -4.81312 | -44.80322 | 2024-11-02 00:54:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 815684f3-ca2e-3dbc-b6e1-3a1ca5b95ffa | -4.81143 | -44.79143 | 2024-11-02 00:54:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 6f5cf8b2-2797-3598-8b56-f0ed2fc15249 | -6.35464 | -45.91647 | 2024-11-02 00:54:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6dd2ebac-32b7-301b-bb0b-eeee12bfe9ab | -6.35325 | -45.90668 | 2024-11-02 00:54:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 939c6dd6-3408-302e-98d8-d37868ce26d0 | -5.72315 | -46.20984 | 2024-11-02 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 008efceb-0830-334b-9263-0e89853665c3 | -5.60233 | -46.25954 | 2024-11-02 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 918418e4-4352-32d1-91cb-2c5780671a5e | -5.43643 | -46.27058 | 2024-11-02 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4aba1618-b4ee-3f5a-9521-4780358140f9 | -5.27832 | -46.25656 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4f88e8f0-7893-3604-b776-8d7f81434b01 | -5.26677 | -46.30743 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32b6c147-bbd8-3365-98ae-5e843f2e2a69 | -5.21867 | -46.15157 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b9a7a7ee-3ae7-3e33-a0fa-229c0eb3464d | -5.19079 | -46.15559 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 727fdf07-d6d6-365b-a96d-cdecd56e3989 | -5.1894 | -46.14575 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9d186507-a83a-313c-b3e4-a8ec4145c953 | -5.17096 | -45.71082 | 2024-11-02 00:54:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77bc5c45-effc-3eb6-ac79-b352a3c17bb7 | -5.16659 | -46.119 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4381ad85-9270-3118-8c60-10a6e64a7252 | -5.16562 | -45.33398 | 2024-11-02 00:54:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9936b79a-fff6-35c3-bd50-ef00cf571800 | -5.16518 | -46.10913 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6fb55bfc-6bc9-3f02-a9c8-03962e023877 | -5.15526 | -46.03982 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c42be089-a3a3-35bd-be17-6735a800980c | -5.12777 | -46.16098 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b5cad7ef-95af-3b12-96ae-e44b9c9d72be | -5.11642 | -46.03526 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 837abd1c-9cef-378b-9dc5-9ae4594d4f63 | -5.11496 | -46.02521 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 48885fa7-c75d-38f7-a7db-c1ba53988787 | -5.11152 | -46.11308 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4f370b12-8eee-399b-91ab-456084dcbe23 | -5.10969 | -46.03242 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| f72169aa-ee39-30a8-806e-2cd3ecbd8f87 | -5.10828 | -46.02237 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 69f20212-15c3-3d35-8ce8-485b9d6526f0 | -5.0966 | -46.07484 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 10cbe5aa-856b-336d-bb20-10ccf9e57683 | -5.09616 | -45.6958 | 2024-11-02 00:54:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a3167b8c-3b54-3fe4-8159-1418cbd38d6b | -4.99873 | -46.03389 | 2024-11-02 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b8ef4b61-d51d-38df-b140-cb4c7748ac1b | -7.4326 | -46.62524 | 2024-11-02 00:54:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5dbd5f16-a817-3ab2-aae7-ef35b521bb8b | -7.42754 | -46.65393 | 2024-11-02 00:54:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 71609b32-466f-3cf6-8d90-75d617609704 | -7.12085 | -46.37917 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b416ff9a-9c22-3ebb-8183-8166459745e1 | -7.11587 | -46.1498 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c1cbf642-5e91-336c-b8b0-5185bf2b6247 | -2.15401 | -46.38627 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 910fe139-44eb-335a-99e5-5cb37db6587b | -2.13502 | -46.38899 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 85e6d228-d080-38aa-9471-63eee3b21e6e | -2.0844 | -46.33914 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 277d6865-1759-30d4-a402-7c0f385341ed | -2.07906 | -46.50693 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 35a2f228-08e8-3075-8ca6-cee2aa9e40fa | -2.01331 | -46.82704 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e5d3e47c-1dba-37a2-8c75-0772661885fd | -1.9671 | -46.43565 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8b478b22-12da-3030-9a74-1f72ed98ad8e | -1.95139 | -47.03917 | 2024-11-02 00:54:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 83745502-7cd4-34df-b606-69aeee4dccc2 | -1.94218 | -47.0405 | 2024-11-02 00:54:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| ccdddb30-a994-387e-ba9d-6542305d1ef0 | -1.94082 | -47.0309 | 2024-11-02 00:54:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d2826754-ed9d-3eb9-b4a1-f6b9e27703d5 | -2.07543 | -47.13247 | 2024-11-02 00:54:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2443de08-ab3a-331e-a307-894f9a5c1613 | -1.95003 | -47.0296 | 2024-11-02 00:54:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1b484fa3-4c4d-348e-81e9-36fd528cb69b | -1.46559 | -46.72971 | 2024-11-02 00:54:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 613a7a84-e3d5-3ddc-9a5f-3eaa8af478ca | -1.46418 | -46.7197 | 2024-11-02 00:54:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4ed839d5-4d45-3950-b1b2-6c57819d7773 | -1.45479 | -46.72108 | 2024-11-02 00:54:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ab4d270b-97ce-30e6-b736-4bfda8dcbbd8 | -1.22213 | -46.51735 | 2024-11-02 00:54:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d6da1345-2d10-32a5-9a23-2a27bd40d771 | -1.21849 | -46.52377 | 2024-11-02 00:54:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c89e3480-e9e6-341f-935f-b72915472834 | -3.30303 | -47.01218 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 59c00135-b27c-37ed-b39a-149f676fc722 | -3.18847 | -46.59902 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f35b344-a436-3d6e-8d92-9b37b012f170 | -3.17919 | -46.60034 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 0b340afe-c26a-3173-bd4e-14d2ba33efde | -3.17779 | -46.59058 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0774c8d2-a327-388d-931f-cef8a062a935 | -3.06047 | -47.38692 | 2024-11-02 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9c3def8e-64bf-3073-8e94-05e24960375a | -3.0394 | -46.51231 | 2024-11-02 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6231439e-07d2-33d6-9b5c-f649e795a9ee | -2.57034 | -47.3086 | 2024-11-02 00:54:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 9617eb91-5389-3027-8133-4bbbf0247d43 | -2.56904 | -47.29932 | 2024-11-02 00:54:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b4662339-a649-369e-80fb-9832e144f750 | -2.39405 | -46.57685 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| daedaaab-25eb-3057-a6d8-53e5ac7e1047 | -2.38468 | -46.57819 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 2e202bef-deb9-3d9b-b4ca-d1da428b501e | -2.37256 | -46.76117 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 78d2314a-cfac-35f5-9f45-548c94d4191a | -2.36887 | -46.80157 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f79d210f-c55d-3860-9976-70a4b961f888 | -2.34003 | -46.53349 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 21ad5696-5029-3e24-899a-a4661500fade | -2.3386 | -46.52352 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5dd420c9-a3d5-3d52-842e-0b7fdf36c3e5 | -2.32755 | -46.62273 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5a23e2c2-7388-3483-b851-ea7d496412a3 | -2.31362 | -46.52277 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2584037a-f9d1-37cc-b7ec-b884921c7cd8 | -2.30862 | -46.82598 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cae8c177-5e36-31c5-b4d1-b150ea7048c5 | -2.27846 | -46.68034 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README10.md)
