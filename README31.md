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
| 45619306-5b0a-3ec3-9fcb-59e4ba61d3d4 | -8.4362 | -46.86782 | 2025-09-28 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bee9a731-9551-3094-84e1-2371f97d9d07 | -6.1556 | -42.81124 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 124d6db2-f9db-3210-9552-e8379ddc951b | -7.33852 | -45.49185 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cccb2fd7-7203-36c4-b6aa-3cdd121d1865 | -4.81467 | -48.24528 | 2025-09-28 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f68e77a0-1251-3974-9dfe-84d7eb554900 | -6.83441 | -44.09109 | 2025-09-28 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c97325c7-cc7c-3ab8-951b-9bc26b0b83e1 | -6.48189 | -44.50515 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9692c94-1bdb-396f-b31c-61e171901440 | -7.94169 | -45.68397 | 2025-09-28 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97154f9b-683e-3c1b-8f49-a4de1fe88865 | -7.25774 | -42.99295 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c2fba441-4bfa-3e44-b504-ef69a3d52d99 | -5.61328 | -43.36627 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 771b0434-88f5-38ec-8d22-4e00f52e55e0 | -8.20751 | -44.4032 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a5dc26e-03b2-3f6e-a0e3-d0c4689191fe | -5.764 | -42.807 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b37c17cd-022b-37f4-b45f-8b7e26fe3ea3 | -6.11891 | -41.8093 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e20911e4-a7d9-3535-a48c-78b76fa75e19 | -6.2656 | -44.07442 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c3912cd-1d7a-3bad-9e20-5c64fa8ad37f | -6.58055 | -45.10038 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54d46045-fe37-3d4d-96a5-0d9d3fbe30b6 | -6.22748 | -44.65923 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7661f3c-da66-30d8-b15a-023f64ca3fc8 | -8.92131 | -46.09905 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bc2d152-e275-31b5-8c1d-ab58bacba0a8 | -6.71071 | -44.59833 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6b0343c-afb2-3c32-ba2d-7df22cdd9d44 | -9.09106 | -45.86547 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc0909bc-fa1c-394c-ae63-7d4471136749 | -6.19407 | -44.506 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bb5e9ec-3684-3887-b148-6b81599e94d3 | -6.39024 | -42.94884 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2977db63-91ef-35ac-8dee-e2ef7bb3d354 | -7.16979 | -41.72129 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1df413ea-5538-3dba-9260-602393cfcb76 | -7.76159 | -45.72318 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bbf115d0-bbde-383f-8ea9-98808cb4bdab | -4.91547 | -48.16145 | 2025-09-28 04:04:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 026ba8a1-6c83-36c1-bbf3-d9c101b0f310 | -7.64018 | -45.98019 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dc84da3-2f82-3f5c-8005-688d0fad724f | -8.52829 | -44.63466 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a23e3c6f-9590-358b-bc4c-c57c058d9dc6 | -5.80467 | -42.83775 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 49fe7b09-79c2-3158-bc8d-5296d8aef867 | -5.31953 | -42.76559 | 2025-09-28 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ed026c2a-207f-37a9-ae95-cbaa6a8fc2df | -9.68011 | -44.52327 | 2025-09-28 04:04:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3999ae76-cca5-3b5a-8845-c302262dc4a8 | -3.78979 | -48.86895 | 2025-09-28 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9863e74-461f-3d4e-ad24-ab2ff77db36e | -7.37706 | -47.02959 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| adc4f6f7-2bf8-332f-bdc7-e7bcd3234e42 | -3.78915 | -48.87 | 2025-09-28 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 903f759c-3434-3bd3-aa69-1df1342edc6a | -9.09171 | -45.86174 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a984b15-2097-3397-ae56-4807847cbbf4 | -5.35346 | -45.03747 | 2025-09-28 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09eac670-980a-397c-983e-674d45ceaa8f | -6.18267 | -46.7218 | 2025-09-28 04:04:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffccedea-f772-36d0-bc7d-2361bb70ec8c | -8.17163 | -46.41364 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c7356a92-1826-3fd4-867a-d346c9f650ed | -9.12273 | -46.67158 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d058766b-1122-3d7b-ba5a-036f06a39f6a | -6.48777 | -44.25325 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 403c2ad3-72e6-3353-bcf5-2a40af42541b | -5.0566 | -45.1883 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 796dae35-07df-3d63-b0d0-88034dba4fe1 | -7.86961 | -44.57293 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 641875d8-3caa-36c2-8ae8-ee588a1b9bfc | -7.16921 | -45.50096 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7381020-73eb-359c-8fd0-5debd0b96272 | -8.83797 | -46.20396 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ad8bfa7-b18d-35ca-8db3-e5b951d96c0a | -8.2765 | -45.44962 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce6b5271-2385-3632-b810-bda19cb7163d | -5.75648 | -42.8384 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 343a30af-aa8a-3219-8aac-9e2941dc298b | -7.37626 | -47.0342 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1932d214-ecff-3466-b6e3-55978ab50b5f | -5.90583 | -43.29431 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ecf1c44-615f-3c3a-952b-5949f85a2ec0 | -6.76177 | -45.52859 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a880c35-3028-311b-8e7a-ec74e2c10883 | -6.28888 | -39.82673 | 2025-09-28 04:04:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 36bef272-10d9-352c-9fe4-4a12168f5427 | -6.40935 | -42.90841 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f3dd827c-8238-39e0-b1ae-84b004ceda69 | -5.48161 | -45.38371 | 2025-09-28 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df898fba-8175-302c-a7b2-b8ffcec4b634 | -6.0012 | -43.923 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4761951-f57a-346d-a107-8816c1d106a7 | -5.16607 | -45.01855 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17a15baf-4746-305c-a525-62350f46461e | -3.83749 | -40.33184 | 2025-09-28 04:04:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0097a29c-d453-382b-81f8-46d732c67f0f | -5.80489 | -42.85905 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5caee368-fd9b-3086-8fff-de2248a5dd3e | -6.31007 | -43.45928 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a09311f-078d-3e43-90f5-e4c3ce50ed1d | -5.72487 | -42.66219 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b46e1bec-994b-3a9b-80c1-69ba8db988d7 | -6.65337 | -43.87632 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e940198f-101f-3e26-9103-6ea2832db54d | -5.29226 | -42.77388 | 2025-09-28 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ba5ab17-6906-3b07-8c65-9a629c31fec7 | -5.1479 | -45.70668 | 2025-09-28 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f85d3ad9-0313-329f-b3d4-1dc271cb2817 | -9.10486 | -45.88357 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0429dce0-a221-3366-99f3-8cc6f663fbd1 | -5.74658 | -42.8464 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| e0a4bfa4-70e1-39d5-ace9-2a031b7dcb5c | -8.43174 | -46.86717 | 2025-09-28 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0bd1277-ac92-3c8d-98c5-de3a53b72226 | -2.47716 | -47.65585 | 2025-09-28 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 309cfb8c-0d22-30a4-903f-1d575c6175d1 | -8.48737 | -47.80188 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f85e6f-2d63-3e47-a83e-a8ca297987d9 | -7.09188 | -45.12701 | 2025-09-28 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaaf1d23-f738-3069-925d-d309eccb5ee8 | -6.15983 | -42.80781 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 38367e15-6fc1-3144-8022-080a4c265a20 | -8.83069 | -45.99695 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e3e866f-5d69-3f98-8779-1290cc2dc0b2 | -6.1776 | -46.72313 | 2025-09-28 04:04:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 815f71ec-8eab-3f66-974e-b38b0ca4d639 | -6.11084 | -41.81564 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 73d5a8cc-1374-3e26-b7de-4a0e455ac6f0 | -5.80993 | -42.67103 | 2025-09-28 04:04:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a38a4584-f01a-3568-8631-c8dca1930fa6 | -6.40099 | -43.48352 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9b56c1b-c0a0-32ca-a84c-344118877657 | -9.52817 | -43.50153 | 2025-09-28 04:04:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 482fa65c-2378-3607-b8ab-cd5a111c5658 | -5.84713 | -42.57797 | 2025-09-28 04:04:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4de2f38c-a4c5-31e4-9447-0cfcc0b140ba | -6.25513 | -42.46557 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 983906b2-12b1-3c60-a025-a0cd4d035816 | -5.19654 | -45.02676 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 876ea8c7-b9ea-3de6-9723-3cd07a9104b2 | -5.78244 | -42.77088 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dab1682d-25ed-3906-b634-c46c81e3799c | -4.9206 | -48.1624 | 2025-09-28 04:04:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd15345d-f9a6-3c12-85b9-51dce7f19aca | -7.3725 | -47.02876 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 994b2aba-6318-3b0d-826f-56078632a50e | -7.82518 | -45.14473 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29bb4490-c467-3277-9192-b0b62d119729 | -7.76276 | -45.7223 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef657346-7e24-320f-ae5e-1372d3024aaa | -7.14964 | -40.66918 | 2025-09-28 04:04:00 | NPP-375D | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3cbed52b-08d8-3fd0-9c19-d0207dbefe38 | -6.46172 | -44.219 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a737eb2c-4a38-3853-b37e-b89269136ffe | -6.56381 | -45.10535 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58d39629-b1c8-3da7-81cb-d62b4c2a3028 | -9.28519 | -45.70475 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3319442c-6bc9-3886-a7e3-8c52ae032e05 | -7.7621 | -45.72606 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2cfb2be-55ab-3452-bfc8-56d845edc2c4 | -5.51524 | -42.19975 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3665a92b-d66a-3cc1-8711-23f162829d91 | -7.92403 | -42.67448 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51d3f699-c562-3c84-9d7a-2ba005fa85da | -6.17925 | -42.94548 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 42d51887-8cb3-3976-84ff-897799e74f2b | -6.38764 | -43.47223 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c3ca27a-2f2b-3682-ac93-2d7708f2eebe | -6.25514 | -42.46531 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd6c684b-00ec-35d6-8e97-b5801739b467 | -5.75484 | -42.81802 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4b60973c-4269-3111-9747-aff00ec5d45d | -5.90823 | -43.68843 | 2025-09-28 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3017071f-f7c7-31dd-96eb-1cc29730c817 | -6.05922 | -43.77938 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52d71ab8-5e8c-32b5-8406-5434f39898c3 | -5.90965 | -42.94697 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d936ac60-a3d0-358a-9ac9-e7feca4fc68f | -8.27283 | -45.47094 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3b377a5-bf0e-3cf4-81b7-76f54bdc6786 | -8.20453 | -44.39779 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b176c9f-ba12-3871-b2b5-615e69b93507 | -6.7774 | -41.75266 | 2025-09-28 04:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc9eb8b4-13db-3f29-8503-382603c65ee7 | -8.83004 | -46.00069 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ab3650a-70c6-30f8-9775-2ee63d1149e3 | -4.13056 | -44.22155 | 2025-09-28 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a1f80d5-fa73-35fd-a1ab-a1035522bfbf | -5.47739 | -45.38303 | 2025-09-28 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e577a85d-5dab-3b55-b538-5dc7fd638e97 | -3.59582 | -48.88026 | 2025-09-28 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
