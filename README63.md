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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 829e402c-8eef-3d35-b799-270d02ea728f | -7.47235 | -45.6424 | 2025-09-04 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e5b26d3-e411-33d4-936d-cb7649f45f9e | -6.22319 | -43.37648 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2719276-b197-3d73-9620-b353e8dad35f | -6.21496 | -43.39578 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e14162b-0c98-3b59-a8ee-c3bd89e93b47 | -6.25006 | -43.55162 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eb41455-272a-3ef4-b767-c76d4fc78c54 | -7.70771 | -50.25239 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 730a4915-49d1-3bf3-944e-8318ab0d5072 | -3.73672 | -53.73352 | 2025-09-04 04:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f194408c-c64c-3f49-97e6-2dd1bf3382b9 | -7.68513 | -48.73183 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ac27b315-db35-3ef4-b628-abf20e67f3bf | -10.64742 | -44.84002 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c05453d-cce2-3b26-a324-e29af722fd76 | -6.22961 | -43.40782 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f71f1141-df2d-3509-825b-af2bfa6b5432 | -6.12649 | -42.95104 | 2025-09-04 04:53:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 8f15ff10-35e6-3f5f-b195-a9aa76003280 | -5.028 | -56.10799 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73f9b055-f6d4-390f-93ed-8e7bfc96bb78 | -6.74848 | -58.72949 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cce03909-7467-3762-9de5-f4dd722c6ab4 | -7.79924 | -45.43092 | 2025-09-04 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 928728f5-0629-33ca-b577-15f61a0a6b1b | -4.83241 | -55.79069 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2d580cc-6ca0-37b6-8ed0-d0dd70a7ce6a | -10.49108 | -46.77052 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 69b9489d-6d71-3475-a82d-303985258bb5 | -9.33512 | -55.20753 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 617f44d0-bce8-30d3-b091-a6377fae6fd7 | -6.48732 | -44.10601 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ab2f905-ee2b-37c2-8296-e414b86917b2 | -7.14696 | -46.75461 | 2025-09-04 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de046094-9fab-3b1f-85e7-3a849ce58536 | -6.79045 | -44.48354 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28b3ba18-816f-367a-9f83-9424dc66e4aa | -6.78313 | -44.49912 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 694ffc9e-3a6b-3c2b-aa52-75359b55a2a6 | -8.04496 | -44.13823 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12fe6f3a-bd4f-320f-8aec-64c3e63a714e | -5.80167 | -45.62829 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51af320a-aa01-33f5-8324-5c81fe8f3e34 | -8.82771 | -52.00835 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c193c23-0168-38fe-9155-f7ce0b88f2c8 | -8.03038 | -44.05352 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ad88aee-3f5f-37a9-bba2-ac6399d1dd46 | -7.69655 | -50.25454 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a71a995d-fbee-363e-af01-fd7d7392d5f0 | -8.05019 | -44.13898 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8307677-925a-34b3-baf8-f16359215985 | -6.235 | -43.40834 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cac34d0c-5241-32f3-bb4d-de309cfa88e4 | -6.17704 | -47.28584 | 2025-09-04 04:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcf0de54-0135-3a2e-9897-fc51ef4f2634 | -7.70356 | -50.25589 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d04a4a6-5739-35eb-8e52-9a3a498f6545 | -8.00066 | -50.07642 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee282fb3-6aa3-3d89-b562-686410c10fb7 | -8.0265 | -44.04276 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acd388aa-d9ab-325a-a9eb-3ef4cb421388 | -6.07398 | -53.8199 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf21f9e0-5a70-33c0-9a25-857ab96fba5b | -10.03515 | -46.09765 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fec587c-eda6-387b-bfc9-2b811c6143e6 | -8.01831 | -44.14105 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51a0b604-8f58-3f67-8fc9-d8511bd7d41b | -5.3169 | -55.86075 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a1a3676-3f09-326b-aa44-0287635a7b55 | -8.89261 | -45.82258 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 02eeb82a-3adb-3b0b-a697-6fd4e101035c | -6.73845 | -58.73602 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| fa94e3e7-3b60-3316-b1a8-1903ea66740e | -9.49195 | -47.61872 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87d58e6e-2b25-31cd-8c5c-7b1c44dca46b | -7.93672 | -44.94522 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 33a2b829-542b-3a64-adee-793495c1abea | -6.88647 | -45.56418 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db204ec8-8c7b-36ed-8e62-87a3c5798bb0 | -8.02831 | -44.14576 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f0acf53-2eb6-3089-a5dd-1c2220500416 | -9.56726 | -48.24066 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe479d23-7831-36dc-9eff-31290cbb71a3 | -7.97717 | -46.35823 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8546b290-b756-3e74-93b4-0ae5c6420cd0 | -8.07368 | -45.34808 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5b416f9-fea7-394d-8b93-1c3ce4ece1e4 | -5.48189 | -45.23092 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8a815f6-aa86-366a-8e19-db66dfb3d541 | -6.7829 | -44.46458 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 418e021c-374d-3a33-b8c0-eacb1cc6ff48 | -10.21716 | -51.1333 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aeeb68e-289b-31cc-9dab-f138f0d72c6b | -5.76757 | -44.87311 | 2025-09-04 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cbeb15c-f8c5-3a66-9fe3-436d2dea003d | -6.83306 | -59.36753 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5840cf36-880d-3a97-8cb6-102514bb48fe | -9.43152 | -48.09285 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e07f348a-2cf8-39b1-963e-80a1d89637a5 | -6.83384 | -59.36294 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8f349fb9-9da8-3feb-b524-f3431d16c74b | -5.86124 | -46.12326 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9e2a5d7-4606-31fe-8822-c3da880e4af4 | -7.71589 | -50.31755 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9b81d7d-c40b-388d-bd46-33ac5e8d9009 | -5.70015 | -45.401 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19209e48-c995-3274-b609-80fc852761d9 | -7.70214 | -50.28847 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54f518d6-cc26-3e97-84cf-3e185b4768a7 | -6.49977 | -44.09177 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08b7d1c5-258d-38be-b1d2-cbdc92af5dc9 | -9.64406 | -46.12184 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d6ffaaa-8339-3be5-ab59-b224ae21d96d | -9.60289 | -47.03436 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e4e596b3-03d6-38cd-b7fd-de1952f04cba | -6.78884 | -44.08625 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5c853e2c-9d55-30c1-a135-1dbba3b846fc | -7.60554 | -46.21263 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3543d4e-4338-33c9-bb7a-cf26b12d769c | -9.4307 | -48.09194 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3b76a5d-9c74-337a-b097-7d6d4bc57271 | -8.0868 | -45.35941 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71580f91-9a9b-3fd0-927b-b71ace818cda | -5.7739 | -44.86333 | 2025-09-04 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 588b3014-d1d6-32af-a620-c53b6b22dbb2 | -3.8829 | -54.21364 | 2025-09-04 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38be3f7e-4286-3cab-a3b4-9212eaa9917e | -10.03924 | -48.15145 | 2025-09-04 04:53:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d300455-8a6f-399b-ac3e-7a12ec71d72a | -7.70152 | -50.2925 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e171dc1f-7a86-3db5-92c8-839901dedc05 | -9.43529 | -48.08891 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c356b60c-cd3a-3b54-af91-54133179f8c4 | -7.69417 | -48.72361 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 642342fb-7076-3a08-b10c-2ecfa8d8a7d1 | -7.78313 | -50.95824 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e51cc33-3dd8-315d-8348-dde5f7d53365 | -9.47997 | -47.61431 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7141d5cf-692e-3ad7-bff9-8f099ea5b390 | -8.87442 | -45.85089 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dd7a735-bab1-3174-a443-109b604df5ed | -9.62042 | -47.03698 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff2796ba-4027-3af1-88ae-f9b188d07d7f | -6.78326 | -44.08863 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ce3d92dd-6864-3cfe-aa47-bfa2a3bd4697 | -11.04435 | -45.14703 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff038af9-aa15-3a31-9c83-9c892fa86330 | -6.26092 | -45.09192 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c99c45c6-dcdb-3c2a-aaa0-0b78c5571bf5 | -6.86758 | -45.57586 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cd135950-2276-3f59-845b-27875d7452de | -8.86348 | -47.92645 | 2025-09-04 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d79d912-b06c-332a-afa0-568dd17174e4 | -8.47097 | -45.06148 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4165a163-39e8-3613-98fa-4d1ecb4d2ffd | -7.93658 | -44.95144 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 29223c0c-5f1a-329a-bd63-0ca2227aaf75 | -6.22982 | -43.54152 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67b4b129-6b71-3474-9228-33cece6ce42e | -5.79031 | -43.22822 | 2025-09-04 04:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c03dec45-f6ba-3be5-a250-e7ae3f679979 | -6.68914 | -48.40849 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fd7ba1d-2d6f-3605-a2b3-e22f59677695 | -6.67551 | -58.76381 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dff57bb7-2cb1-3cf3-bcc7-e95a0b4c37ba | -6.76417 | -63.13142 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26c0f6d0-cfee-34c2-b1ad-1d57006680bd | -5.6101 | -57.36176 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 703c6be8-e0cd-377a-879f-55ecb31cbf09 | -6.2326 | -42.4386 | 2025-09-04 04:53:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e62fea4f-af79-3a26-8ed1-609d3146ef24 | -10.45045 | -50.39044 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cf35f86d-515d-365e-87d6-2cd85ce3baae | -8.08529 | -45.36043 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c93c3e32-9c85-366b-8d40-29b87850dbae | -5.18496 | -46.06871 | 2025-09-04 04:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb53cd31-2947-3762-a136-e6bd08407558 | -6.87468 | -45.18969 | 2025-09-04 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50983b56-5006-3070-bf75-95724f8b5549 | -6.8504 | -44.28038 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8822e507-9583-3e60-8650-9a7fd383f0c5 | -6.87296 | -45.57153 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d41897c-ae03-36c5-a4fe-eb15ed0b8d74 | -4.99892 | -56.26365 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3002cd48-e594-323d-88d7-361fa6fcb381 | -5.18871 | -46.07359 | 2025-09-04 04:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1919c309-7ebb-3f61-b6a9-b46eeb78765c | -9.43478 | -48.09257 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a22977c-24ac-3aff-8051-88632a49960a | -7.68693 | -50.2701 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee351fd7-6b5c-3859-b637-8819a9c7bb32 | -11.04906 | -45.1507 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 49f2f176-f56c-3854-91e9-f9911381a6dc | -9.68796 | -49.00676 | 2025-09-04 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44dbb19b-c038-3dde-a4da-6c5834c80b55 | -6.26183 | -44.51812 | 2025-09-04 04:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73505565-de93-3be0-bb5b-2a754bd55f3b | -6.78167 | -44.0902 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README64.md)
