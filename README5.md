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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ca5ab18-95e9-39db-9c12-1836b2e9d873 | -7.69606 | -50.28225 | 2025-09-02 00:11:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 7634c317-e3b9-3fe1-90d2-ae3b460f8f9f | -6.54618 | -43.10321 | 2025-09-02 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68096560-be5f-31ef-bb65-530049370423 | -7.06637 | -44.33957 | 2025-09-02 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0d430303-9654-3806-bdae-14c22dcfa6ce | -8.19757 | -46.79064 | 2025-09-02 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 81709cd1-c18c-3ac4-aebb-4a34fd87ab6b | -8.87257 | -45.76931 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5e10629f-3213-3888-855a-da994c4a7e83 | -6.24906 | -42.61671 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 04d9e23d-7674-3802-8675-3ce66e833fcf | -7.85629 | -46.74285 | 2025-09-02 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a80914f3-9dd7-3955-91b0-fc6bad07476c | -7.49003 | -45.36462 | 2025-09-02 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 6e21fa57-0681-321c-925c-06e1e21a3e65 | -5.78386 | -42.58681 | 2025-09-02 00:11:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 2031d314-9d12-3044-98d8-b902d11aa590 | -7.84582 | -46.74423 | 2025-09-02 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5db01144-8040-3001-a598-a0458dd14b1c | -5.91766 | -44.97123 | 2025-09-02 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bd6cf3d7-d9bc-31ae-9a63-3899b5bb1051 | -4.30561 | -48.10427 | 2025-09-02 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 76477691-6e92-3218-8fa2-306f9f804504 | -6.33363 | -43.56567 | 2025-09-02 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c86345d8-30f4-3a2c-8e25-bf77591e819e | -6.8396 | -52.82059 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b5af43e5-f5f4-3322-b344-77923bed074c | -6.53859 | -43.11328 | 2025-09-02 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e89ff81d-7b77-3f97-bda7-e42e2c41bd77 | -7.06729 | -45.5694 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3014f56a-a3d9-3cf5-8b3e-52b7681dd56a | -7.17565 | -45.7652 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c2790b4-8bb7-3bef-8f47-9d30592d940f | -7.70986 | -45.01571 | 2025-09-02 00:11:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 46660388-443b-354a-a66f-81bd5da3f1a9 | -9.16978 | -45.22317 | 2025-09-02 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f5701390-d1d1-382c-8f0b-4979d46ffdff | -5.85897 | -46.61657 | 2025-09-02 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 8f1991cd-ac89-3d7a-b442-2b7985e861c3 | -8.18211 | -46.79852 | 2025-09-02 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| a8595b9e-57ce-3394-9447-e74b15628b0a | -5.73571 | -45.5333 | 2025-09-02 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe893f4a-6a2d-30ce-8085-810d51a6193e | -6.97951 | -44.31091 | 2025-09-02 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 895f4050-3d72-3e83-a200-031e5defadbb | -6.1955 | -45.38857 | 2025-09-02 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 38e7f55b-5f8b-3ff2-9be8-c18c6ffb265e | -6.27951 | -44.51322 | 2025-09-02 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 85bd5eec-a726-3665-accd-96e2e7cb4ecb | -5.8708 | -46.47378 | 2025-09-02 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| be9150ea-36fd-3501-879d-92de1ecdcefc | -6.98977 | -44.31885 | 2025-09-02 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3cb7f188-5604-30f9-9320-20cfdad74722 | -6.6281 | -43.96017 | 2025-09-02 00:11:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d313f0d8-a506-3d87-83e1-515b90c8c113 | -9.48168 | -47.60762 | 2025-09-02 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 59c332a1-12a3-3188-8f0f-c7d4ea8d9e7d | -7.9804 | -46.44702 | 2025-09-02 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d5c89e05-b9e8-3163-989d-eba0091097b5 | -5.69286 | -45.90184 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 36dba23b-7796-39ac-831e-c8ef19b2ba23 | -7.06319 | -45.98539 | 2025-09-02 00:11:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 02d5a7db-f45b-3532-8090-7b0246638867 | -6.06654 | -45.58348 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7739db1e-ab31-3325-9ca6-edf40c160283 | -7.38298 | -47.04676 | 2025-09-02 00:11:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 10000c6e-6495-3116-be94-90e5d0b751e6 | -10.05801 | -48.10059 | 2025-09-02 00:11:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 54c39274-cf31-3aeb-8656-863252406c56 | -5.85848 | -46.611 | 2025-09-02 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 8db4159c-871e-3e24-94d0-76dea40a6ec6 | -5.15495 | -44.84338 | 2025-09-02 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 623ad8ff-6538-3019-921a-d79329325394 | -6.83462 | -52.82789 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 52c33bc2-c6f2-31ad-8000-e1657feabd7d | -3.79518 | -49.42725 | 2025-09-02 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c1018fa5-3b89-37fc-a75a-bf2e9ada54ab | -6.71487 | -42.26432 | 2025-09-02 00:11:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 989d3153-d728-3d58-b608-dac0f44dd389 | -10.25768 | -51.13087 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 8acc8f3f-6730-352e-b201-95848f26ac35 | -4.92258 | -46.87011 | 2025-09-02 00:11:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e8ab0bc9-cd05-3437-8ef1-1dba650817fd | -9.83464 | -48.61188 | 2025-09-02 00:11:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 92198699-3de3-33b8-bb41-288a2a4def0b | -7.87915 | -47.97148 | 2025-09-02 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 0eafa3b4-f930-3490-bfb2-bcef859d8940 | -10.06446 | -48.15236 | 2025-09-02 00:11:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2aaaeacf-af58-3664-b370-91683f6e49e2 | -8.01575 | -44.07407 | 2025-09-02 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fca66278-5a31-3a86-88d0-743518301eac | -5.16763 | -37.97213 | 2025-09-02 00:11:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| cbc9bac5-5355-3a61-8d1f-a96026629ab1 | -5.54761 | -43.74918 | 2025-09-02 00:11:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff696caf-472c-3bfc-888d-4d6c86c0158a | -8.87401 | -45.78055 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 04e62269-e416-3e68-ad70-6c67bd40fca5 | -6.54546 | -42.9684 | 2025-09-02 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3753710-8f5e-3aea-a774-a7f20d8bd7d1 | -6.53737 | -43.10446 | 2025-09-02 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 02370c80-cf2d-3b28-ab10-da99ad79d4d6 | -6.85127 | -52.82546 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a13fdbe4-e79a-3125-9c42-433129d5fe4c | -6.86797 | -52.82331 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3e0d245f-0f6a-3c68-b4e1-afa32e40f298 | -8.18701 | -46.79211 | 2025-09-02 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ea948b54-5f10-3323-8504-0d27fddaf3f3 | -9.48107 | -47.61724 | 2025-09-02 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6d39fed6-d820-3fab-a376-c44ac09dd651 | -6.30926 | -43.65025 | 2025-09-02 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b22045b-7eec-391d-a46c-2f9e61ba8d22 | -6.5342 | -42.952 | 2025-09-02 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7f0aa5e9-e4f8-37f4-8300-94efbb4e834a | -6.01112 | -43.83445 | 2025-09-02 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f8ea588f-8d5c-3ff6-89f6-9717cae1adbf | -9.73463 | -48.96941 | 2025-09-02 00:11:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 29e426f2-1416-3fe7-867b-179c52f01655 | -5.24888 | -44.45327 | 2025-09-02 00:11:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f0788db0-b1a5-3806-97aa-ea9cf04cbce7 | -6.29799 | -43.63376 | 2025-09-02 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f55974ec-4b3d-3193-8c82-28fd0aca16b5 | -8.17645 | -46.79349 | 2025-09-02 00:11:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 5739a3cc-158c-3b14-8236-44754eeb1e7a | -6.17689 | -42.75997 | 2025-09-02 00:11:00 | TERRA_M-M | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6ffa9d0b-d557-31e3-8e97-241c0baab7e8 | -6.3412 | -42.55231 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bbf88156-28d5-349f-a126-dd529d91505b | -5.68887 | -45.94542 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ffab731f-9a25-3afb-99e6-0bfa46f6e9ac | -7.06194 | -45.99194 | 2025-09-02 00:11:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8c551315-06f9-31ff-b2fe-861cbe9d2e2f | -5.85745 | -46.60488 | 2025-09-02 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6807d710-b117-37c4-8292-797d16909e88 | -9.1118 | -46.045 | 2025-09-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 147f391d-62c3-36d5-a6ab-aa3deee84265 | -6.39822 | -43.49617 | 2025-09-02 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9f457a13-4a4f-3c81-a084-13e582de77b2 | -10.04809 | -48.11953 | 2025-09-02 00:11:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 80b8ea07-0b61-38ad-b531-413ee3127791 | -2.4482 | -49.37163 | 2025-09-02 00:13:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 077fff51-a598-39c5-839f-aefd0806b8c6 | -6.2861 | -44.5198 | 2025-09-02 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c0c100c0-1211-3402-94b8-7d1c1c1f7328 | -6.2674 | -44.5213 | 2025-09-02 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 902c91d9-ecdd-392a-a192-e2727d1108d6 | -7.5476 | -61.3437 | 2025-09-02 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 99e0c31b-0999-3155-ba6b-ab68232595db | -9.7485 | -48.9598 | 2025-09-02 00:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 734d5678-9599-3c2a-915b-eae9b0eeef3d | -11.6647 | -57.3533 | 2025-09-02 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 775381e3-c3b1-388e-837b-50ffb6c1d83f | -10.4314 | -54.7597 | 2025-09-02 00:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0dd3a193-c4da-3b2f-a9be-0282b1096321 | -8.6674 | -62.8179 | 2025-09-02 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2c6cc27b-aff0-35ac-9651-7727831a624e | -3.2305 | -47.135 | 2025-09-02 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| a660080f-fb85-3d6a-9b9f-5aa67b14f437 | -6.2863 | -44.4969 | 2025-09-02 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b2449c63-7016-36c1-8d4a-5bfd15c358d7 | -12.938 | -57.0057 | 2025-09-02 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c87472e4-468d-3b01-baa8-8a7b4374e29a | -6.4029 | -58.2173 | 2025-09-02 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 1bfdcdfb-ff7f-39b2-96f4-cf8610356418 | -10.4312 | -54.78 | 2025-09-02 00:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 19d1967f-14b7-3c70-8568-e903d7bbd530 | -6.2676 | -44.4984 | 2025-09-02 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 85a0b566-45fb-328d-b76c-ddb04d981a2d | -9.1267 | -46.044 | 2025-09-02 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 409d290c-d20b-3073-a110-127ac7ad4645 | -8.6487 | -62.8376 | 2025-09-02 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 47f10555-120f-3a05-99c3-3ff5d5130986 | -8.8467 | -45.8034 | 2025-09-02 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 048cf86c-9b53-3a64-b09e-420e976cecb7 | -9.8805 | -64.9951 | 2025-09-02 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| ac6ee511-b9ad-3686-bcde-b42c47944767 | -14.2887 | -45.2368 | 2025-09-02 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 48832e2a-bdaf-3e3f-a6c3-59c65147b83e | -12.9382 | -56.9856 | 2025-09-02 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 2613af52-f00b-3cd2-b449-02871486d2a2 | -12.8625 | -48.0545 | 2025-09-02 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0684958a-51c2-3f4c-b185-d968b5cb6455 | -8.6673 | -62.8369 | 2025-09-02 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 68c5d81f-e64d-3a0a-a90b-3644166a85e7 | -8.7154 | -50.4492 | 2025-09-02 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 60791795-84cd-38f8-a727-fe034d0d08af | -10.4502 | -54.7581 | 2025-09-02 00:20:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 89a1ceaa-388b-3539-bbc1-01ce929f86e5 | -10.2786 | -47.5223 | 2025-09-02 00:20:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| abe65065-8db2-3db4-896a-29c180ddef02 | -10.0623 | -48.0978 | 2025-09-02 00:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| a7e57021-74a6-3cfb-9ab6-edb7198bef01 | -12.9385 | -56.9655 | 2025-09-02 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5d4cb122-03d1-30ea-95cb-9104ac355e14 | -7.5477 | -61.3247 | 2025-09-02 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 90e1e2a4-b182-316d-afde-b5d9aaf42870 | -7.5291 | -61.3444 | 2025-09-02 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 237a461d-2ef3-3106-b13c-d626637cccb7 | -7.5292 | -61.3254 | 2025-09-02 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |


[Clique aqui para ver as próximas entradas](README6.md)
