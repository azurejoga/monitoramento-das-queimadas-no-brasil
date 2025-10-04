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
| 8b356688-59bf-39ab-9254-e07ba331d5a0 | -7.78428 | -42.59431 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3ebd2e27-01f6-3a9b-bb5f-74d9c5f67124 | -11.07336 | -47.70106 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36b13a07-79eb-324f-ad3f-89611070b584 | -6.28607 | -44.04748 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 648f487f-dd5e-3629-8a7b-b851c38d771f | -7.80392 | -42.52797 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3eeeec5d-8d48-3c09-bcab-b349aa906ede | -5.89349 | -42.53488 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2dcee604-55a7-3b4d-87a3-deb60296ac9d | -7.31096 | -39.14072 | 2025-10-04 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 083a0ccd-1c45-3e06-8184-928bde834ab5 | -10.31821 | -50.35241 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ea82f9f3-2e11-356a-b1d2-89f36079206a | -6.66685 | -42.82138 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ae5a161b-3485-3665-a847-1978acaca8a0 | -5.25881 | -39.26192 | 2025-10-04 03:51:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 44f1ec0d-ca1f-3941-9588-2c65d259d620 | -11.12946 | -47.84986 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e01fe57b-7289-35f8-a682-da8b5d5b6bc7 | -5.71423 | -44.23766 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90bfaa9b-8ea9-3c94-b04a-e3785584934d | -5.5502 | -39.24456 | 2025-10-04 03:51:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecedc932-ca5c-3d71-be10-36e1229d46f6 | -5.41119 | -41.34193 | 2025-10-04 03:51:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9465f754-5671-3cd4-b378-5d13ffdc4881 | -5.83596 | -44.98682 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0730126a-26dc-37b6-ab6e-2d3821f5a72f | -9.11454 | -44.39258 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b2733ad-4d88-3698-810f-7a8ace82ef63 | -7.79478 | -42.55714 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1f57ebd-2481-3c3d-ae0c-b9e727c2a3aa | -11.67405 | -44.26943 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5a874d2-9c06-3500-a39f-99fd3d64bd54 | -9.91412 | -50.50694 | 2025-10-04 03:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fe480d2e-5f28-32bc-9c66-0b08e19ff951 | -9.90251 | -43.74057 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1270dbb5-9574-3126-833b-23da7ffaf840 | -6.46474 | -44.58832 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d305894-4ff8-3fc8-b76d-b00627bab5c7 | -7.77078 | -42.52233 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1891ee0c-3c4e-3690-a63d-f9e6f793657c | -6.06979 | -42.5184 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| f8851484-0206-34f7-93d0-f152409eee52 | -5.26172 | -39.26648 | 2025-10-04 03:51:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 84844f15-e798-37f6-b116-6af0750a105a | -7.71008 | -42.5775 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 309cd692-43ec-3300-ae32-b5c92b90ae96 | -6.28434 | -42.44759 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edefb802-f9dc-38f1-a71d-c9981f912b34 | -5.97928 | -44.09217 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f83a0488-868e-3111-80c8-0cf3f0195d54 | -10.33483 | -50.3381 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f2dbabaf-57fe-3f86-8ff2-0c365d9bfaf6 | -8.17826 | -44.14415 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0afbe00-731d-3fa1-b4c4-f27cc49a7f36 | -5.7285 | -42.68607 | 2025-10-04 03:51:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da6c030f-30c3-3ee2-a27b-25552c4e2c8e | -4.95698 | -45.068 | 2025-10-04 03:51:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3855a5c6-d17b-3923-9c48-ee31fe63dbd6 | -8.84888 | -46.79068 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afe54269-ee55-3eeb-a44a-b2d347c3c6ab | -7.80018 | -42.55034 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d866eaf8-2e0a-341a-a0ca-3838df4a702a | -5.20397 | -45.06579 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e26b3195-2ab7-3593-8f5f-66484273ff79 | -7.54995 | -42.40024 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8e230120-9930-3569-9660-1745a3f573bc | -6.23135 | -45.3499 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 845d60d5-db23-364e-993b-b9fc9e22897b | -8.90517 | -46.6033 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eacf994f-7386-3c55-8bce-4cfc2f228362 | -9.94223 | -43.74334 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d618d548-5bb5-3859-a976-4ff338066e9a | -6.66048 | -43.47748 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41109cdb-d45f-37fa-9418-af2869538f8b | -7.77885 | -42.60113 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4ffd445e-61ae-35a7-a202-376637b73135 | -9.90585 | -43.79755 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 091e3d47-1b72-3ae6-b2ac-5cea8304cec4 | -7.71026 | -42.60127 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc9d1147-42d0-388e-9051-2c695eeda128 | -6.22182 | -44.27586 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 82db11c9-32e3-3a3a-9c75-6cffb6c1c677 | -5.48271 | -44.10774 | 2025-10-04 03:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 48462e35-1888-3fea-a070-0d4f2227b3c8 | -5.41269 | -41.3448 | 2025-10-04 03:51:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ca07d5fc-2311-37d7-8723-7ed1d5c502b7 | -10.02476 | -44.01405 | 2025-10-04 03:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6074adbc-9256-35ba-a663-8692b6b83787 | -6.99126 | -42.33316 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47f87d57-4ac9-3490-abba-b58e8e28423a | -10.33075 | -50.33744 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c12cd234-3ed2-3d77-832e-42518715fcc9 | -9.11371 | -44.3972 | 2025-10-04 03:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01009e3d-3318-30bc-9667-7ccfdaf85bfc | -8.95625 | -48.68967 | 2025-10-04 03:51:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 78bdf923-59a9-30f6-84e3-8a94fd1072e9 | -6.22658 | -44.27682 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba308c94-cd05-32d2-bb9c-773951537a21 | -6.55586 | -44.15475 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17b125a2-700b-3dab-bf80-675fbf7d147f | -7.73717 | -46.30776 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 061c1b80-e988-3c6e-9dac-a204ab80d280 | -6.12251 | -43.11713 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d459fe02-5acb-340c-bb51-a8ef8fa7f4b1 | -9.34831 | -45.78817 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddaa4ab2-347a-37a1-acec-18c9dc7d9132 | -6.34304 | -43.44894 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07240ecf-f973-33b4-a340-2623d4eb308b | -8.55935 | -44.63942 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 507dc53a-1baa-3a66-a8e6-eab04099ad25 | -8.55191 | -44.79131 | 2025-10-04 03:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c502fec4-c93d-3954-a8b0-d99d5b54f268 | -7.3116 | -39.13684 | 2025-10-04 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 95fc7eef-44d3-358c-8f05-40e76baf8239 | -4.2703 | -48.87788 | 2025-10-04 03:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6d555c9-3079-3760-8a94-f658617b920b | -6.42349 | -43.04079 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cced8812-1e3e-3db9-8e76-79253962c47a | -4.2537 | -48.5624 | 2025-10-04 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2221af9-7466-3ca3-b1bd-5ddadc3e4947 | -6.65454 | -42.81565 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2bc38ab6-77c0-3720-a25d-9bbf21dc12b3 | -6.20199 | -44.33247 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87cbfffc-82d8-3e8b-95d3-7bde7529606a | -5.2456 | -45.55288 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 504dd3da-0646-3c1c-b22b-1b36e026222c | -8.62858 | -43.9873 | 2025-10-04 03:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d5e540b-712c-31c0-a985-2f8de1af8fd4 | -4.42271 | -46.4158 | 2025-10-04 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7feeaea0-3366-394d-83ce-5b732db4311b | -7.54108 | -42.40249 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c5f119f2-0775-312c-aa8d-d3b98c8ff818 | -8.2303 | -46.80152 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e739d894-803d-3b78-999a-4252547d5b34 | -9.33926 | -45.78087 | 2025-10-04 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 53c6a823-273f-33e1-849f-3add53d6642c | -7.71202 | -42.5663 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7d4aae1f-fa22-333b-8da1-7004bfe94d9a | -6.31012 | -44.27361 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f2b40ec-87a0-34e7-93e5-5a0ce5bcb5c1 | -6.67187 | -42.81776 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 05ee4a7a-df42-37e0-b185-d492ddb2fd9c | -8.9565 | -48.68542 | 2025-10-04 03:51:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e0747aa-c577-3e9a-9830-0d183665c568 | -5.48247 | -44.10376 | 2025-10-04 03:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 766ae206-a4d8-3514-b8d7-e2b79e2343a4 | -7.04913 | -42.7756 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 747ee8c4-1f03-3a35-82bc-b78e4389e1e8 | -5.40826 | -41.32267 | 2025-10-04 03:51:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a43a8201-a0d0-3f15-bb56-4c431f482f68 | -5.74145 | -42.92585 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f859ee28-7ca1-3512-b717-6b1954052e1a | -7.05135 | -42.78826 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e689d4e2-5e4a-3e8e-a972-1583219f83b8 | -7.5628 | -42.62753 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c837b65-73e0-3053-8bbb-3ed2256b9592 | -5.26592 | -39.26305 | 2025-10-04 03:51:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bde5e704-10a4-3db3-8e80-b7ca5de34802 | -6.65594 | -42.80733 | 2025-10-04 03:51:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 24fcff12-17cf-3b85-a44b-dd5ee62d9a80 | -6.55252 | -43.10068 | 2025-10-04 03:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0b2b8aa-8eef-3bb8-8d59-aeca0743ee3b | -6.7172 | -42.16228 | 2025-10-04 03:51:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 36949031-5faf-30c1-b7b7-89074a90b9a2 | -7.72672 | -42.58035 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 356ee46e-6495-31cf-ab43-921fd97ea137 | -7.45973 | -47.18319 | 2025-10-04 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac9a2726-5441-33a6-8e6f-5c139dd22a77 | -6.17607 | -46.31376 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94488d05-4566-3c1a-b010-438adad06555 | -11.4773 | -43.50084 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46a233b4-e4cc-35f7-b287-651c01a8ee55 | -8.84791 | -46.82667 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff4e2448-8bc8-34a5-89ce-020cdb2228a2 | -11.7188 | -44.44412 | 2025-10-04 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 798c059b-a52a-313c-9ad8-95ca836ca248 | -9.94874 | -50.24638 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be0fb95b-f111-35ff-90e1-9f2b37d7e9a2 | -11.50592 | -45.01694 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bc77077-0c26-3d1b-935c-689b3557e842 | -6.87213 | -47.23641 | 2025-10-04 03:51:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4a3e252-2edb-3393-ac21-89fef6417a82 | -8.83943 | -46.84236 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27f6d3eb-b7e9-3aab-ae05-f70a1bb2307b | -7.77016 | -46.27747 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a329cbd-ea01-3a6a-a517-4d2f21352356 | -3.68558 | -49.05594 | 2025-10-04 03:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 259aba98-208d-3e7e-acab-308ad0227370 | -7.72099 | -42.56391 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2350307c-648e-35cf-813b-d23b65f06164 | -6.24426 | -45.33698 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abd1f5ee-f068-3f19-a200-93e00d2522eb | -6.29351 | -42.49329 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4a6b364-2245-3cf1-a04e-8f5ba5163e1b | -8.8977 | -45.02236 | 2025-10-04 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55b7d44b-5c91-30df-91db-243a766abfce | -7.80268 | -42.53538 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README32.md)
