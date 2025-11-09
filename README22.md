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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 825ccff3-3ba0-315b-8d18-adbaddcdfb0f | -3.0849 | -52.92508 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 510b637c-59b6-3ebe-a720-b49c745ff0f1 | -5.30431 | -47.28508 | 2025-11-09 04:38:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 031a1735-c6bc-3982-9e28-5f7c3ab1fc66 | -3.47018 | -39.57368 | 2025-11-09 04:38:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1082c015-ecb4-3477-9579-9620de78c5df | -6.11765 | -43.76277 | 2025-11-09 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4b25c45-2d97-38a5-897b-5df60d2db613 | -6.88044 | -49.2497 | 2025-11-09 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e040913-e741-33f9-838c-e56a39738d8c | -3.33647 | -50.07912 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d28ef134-5c92-36ea-a297-76d21d4c247c | -2.63598 | -49.20752 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16b995e4-aa29-388e-9bcd-b49bfc85a5da | -4.3961 | -45.96609 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e83b63c-fa28-32a1-af8c-d020809be59c | -3.79919 | -48.90042 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94b2a5c5-fda1-379e-af3b-1674bade7b6b | -3.91371 | -50.04262 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 005251a4-b127-3a33-be46-00a16d34c0e0 | -3.33961 | -44.36974 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 65cd9b0e-3341-3f9e-a7c7-915920d67ba1 | -4.29173 | -49.73874 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21acf4e7-0ed1-3332-9a57-2aafbe02739a | -6.14315 | -39.90957 | 2025-11-09 04:38:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b59bdb73-8582-31e7-a9a9-6d104a2c544a | -4.64197 | -49.54573 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32c50701-94b5-3f80-b8e4-2da20e6dffea | -3.6648 | -51.75059 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2670e39c-f4c1-3f8a-abcb-87e08b01c2d3 | -7.9463 | -46.77289 | 2025-11-09 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2af30b0-9383-3e07-a693-74eaf4aa2f1b | -7.9867 | -46.81125 | 2025-11-09 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dedff28-4043-3216-a7f6-8acb4699bf62 | -1.85761 | -54.35934 | 2025-11-09 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47d9e0a6-482f-31d9-b572-7cf1b06dc653 | -6.41248 | -43.75815 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a633fbf6-0184-3f8e-8595-f48c451567c0 | -4.40617 | -49.76781 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2b6febc-9ca4-374a-84ed-2fda41cf138e | -7.17348 | -44.95213 | 2025-11-09 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 22dabad2-6249-347b-b84c-6618337932c6 | -3.08106 | -52.9245 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb0edc87-9f1b-3e26-9919-524e72d57b87 | -3.9634 | -49.96726 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ee01c6e-ddaa-3f04-9e5f-910ef607c981 | -3.15504 | -50.59696 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9946a9f5-43e8-3750-8980-6a8e904342d8 | -2.4853 | -54.19822 | 2025-11-09 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34a4ac41-cc32-36e4-bdd5-b79a33dba8c3 | -5.20186 | -44.41513 | 2025-11-09 04:38:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13a6633b-f969-339d-a09b-21c5a96b5885 | -5.43606 | -47.56357 | 2025-11-09 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1310066-d5eb-30e2-97b3-ab2f597f0744 | -6.99779 | -42.79092 | 2025-11-09 04:38:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ba6d3c9-3acf-3025-a4f4-f6603aa83fa2 | -2.83226 | -50.44186 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e95d16e-684a-30b7-b3f4-8f5c24918006 | -3.31874 | -49.12368 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 449cc449-3524-33b6-b240-3142018c6f90 | -3.2487 | -50.14236 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11451240-8821-3aa1-ab81-abfd62390a18 | -4.64794 | -46.86311 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75af7e4e-02ab-32ea-b3cc-c3ffadb41d7f | -4.5234 | -48.83481 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a8b86b6-343e-3139-b046-8afb9436e3cc | -3.79588 | -48.8999 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfc5d091-ee01-3061-8f38-507c27e46fe4 | -3.09567 | -49.22316 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6173441e-ba7f-3ef0-9003-838c95283876 | -3.50261 | -50.04356 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b997918e-c1ac-303f-abea-9ebd4feaec19 | -6.01629 | -43.77593 | 2025-11-09 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9225d084-78a9-3e9d-80dc-049711e266cf | -5.15808 | -46.13164 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c8e733e-01fc-3bec-88fa-4d889c7d9e99 | -4.82549 | -45.61086 | 2025-11-09 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a064332-0448-3360-a9fa-d1ce55568b6d | -3.25798 | -50.01947 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82575825-4583-337f-b752-0653cd32a936 | -6.88374 | -49.25023 | 2025-11-09 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ead24e5c-9cbf-3b45-86d6-1975fb184be1 | -6.85845 | -44.83662 | 2025-11-09 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0226bf04-c3ff-327f-9a4a-012ea0bceb6a | -3.42299 | -52.8939 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5129619-8824-3a2a-a4d6-e985e7f56b62 | -7.56274 | -45.87741 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 600730ca-e36b-3314-8888-e2c05c031379 | -4.10106 | -48.94801 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81e2b930-0b6b-3658-9295-6cf4513e6898 | -3.28788 | -50.20006 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed2acabe-9feb-3e04-b6e7-8c3ec3bf449e | -6.08092 | -42.69485 | 2025-11-09 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ec6fc51d-2afd-3abb-82a1-6cff48e6ad49 | -3.29126 | -50.20059 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef3eb339-cacf-36df-a73b-75c86d379fa3 | -3.31819 | -49.12713 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d301fa04-775d-3ac4-aca5-0e3cc1a43e69 | -3.30647 | -50.16986 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc708d30-9113-30d3-8804-24951a37a5ad | -4.89039 | -48.59608 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d85899b9-96fe-3177-acc8-dfde2b5356f0 | -4.58037 | -45.62506 | 2025-11-09 04:38:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 816ba884-cd63-3d39-9487-3934036e3c01 | -3.31045 | -50.12279 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c236b79a-a179-346c-b33c-4116a1babd10 | -3.80954 | -45.98905 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92b40d6d-3258-35a2-bebe-222eee956872 | -3.34788 | -50.20189 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8973b48f-f396-364b-9260-3d9c0fec5e8d | -4.20765 | -44.75941 | 2025-11-09 04:38:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84a52fd0-3049-329e-957e-b23a09439e4f | -3.31605 | -50.13101 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37d058e7-1560-3104-baba-bea4eb497a72 | -8.18811 | -46.20805 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 217d8460-0376-3c0c-ac89-85cb2b4ac209 | -5.9751 | -53.53121 | 2025-11-09 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4359f2d0-294d-3955-9023-be23f727c227 | -4.46092 | -45.57434 | 2025-11-09 04:38:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 027947d1-b1ad-3e02-8bed-291f1797c612 | -4.63703 | -46.39331 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4c180937-d36e-386b-bf19-7c25d87ee586 | -3.03482 | -50.27179 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0874655e-35b5-3533-a62d-56e2748032f2 | -4.70522 | -48.79995 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae1ca831-c92c-33f9-8a65-139d2b8e2f3d | -6.62075 | -55.02118 | 2025-11-09 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80944a58-edad-36e4-90a8-4edeee3811ec | -3.43377 | -51.45242 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a2d725c-68cb-36e1-9086-99b6f4e9fb86 | -5.48987 | -45.86319 | 2025-11-09 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a76ef6f-1d10-31bf-ae66-c291deb9851c | -6.87653 | -47.24156 | 2025-11-09 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50ca8860-dee4-3553-a32e-5ef73f7fe37f | -6.64213 | -47.28521 | 2025-11-09 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 881d8d5f-1a0a-3721-a376-6c2e59f18879 | -3.41495 | -51.56781 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a15e65d-327f-3551-a3f7-4249134e8d44 | -4.58807 | -49.39174 | 2025-11-09 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41d7daaa-7218-3e0d-8519-5023b9fd1b56 | -2.74314 | -45.16763 | 2025-11-09 04:38:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cae8fd3e-54df-321e-bc00-8310c67d036d | -2.74014 | -45.16277 | 2025-11-09 04:38:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e211b32d-b820-3e3e-aa95-9888531e9484 | -4.81885 | -46.80304 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef803a75-d58f-310c-be64-e2177df06f96 | -3.31543 | -49.12317 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acc0c988-a17e-3d37-ae01-78325276b6d7 | -3.61406 | -49.27687 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32b7257e-80fb-3014-9c54-3ee7e3f44793 | -4.2069 | -47.77828 | 2025-11-09 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3abc95c3-4dc9-380d-a3ad-239f77e5efe4 | -3.23138 | -51.38192 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fd9c883-9f82-35f4-9843-8f37c2f06116 | -2.97132 | -49.12936 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 674808df-c665-3ab7-acee-4cc574933f4d | -4.39677 | -49.65582 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bddcb23a-b595-3749-8be0-96cc67f1e7d4 | -3.86888 | -49.384 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c59ca70-114a-30dc-a172-065bb64fa903 | -6.41191 | -43.762 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47cfc37c-800b-3d03-b590-71a2756bffa9 | -3.12533 | -48.11044 | 2025-11-09 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4be49a9e-4e3d-3c08-9ee0-99f173f57a90 | -3.35776 | -49.2433 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47857001-38ca-3cba-9b9c-2521fc9c55be | -5.50307 | -47.20101 | 2025-11-09 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82eb1cb2-da8f-3da7-910c-53727870f836 | -4.75846 | -38.6854 | 2025-11-09 04:38:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6198ed96-0ac3-3491-8328-a0b722f05094 | -3.10016 | -50.19606 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 579f79c5-5de6-37ea-a957-03c5205d8ebb | -3.65551 | -50.27571 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56863f6e-e2ff-32ce-b110-ae4de5a51123 | -3.45394 | -45.64805 | 2025-11-09 04:38:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 24b5f314-9278-3be3-a1b5-9dbb07f00b7e | -4.40439 | -45.97432 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e687e70-7c68-3f56-ace7-c8439eba2a56 | -2.94232 | -49.35517 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 8d9bc5dd-956a-35ab-95dc-fbd40198e94c | -3.83321 | -51.9859 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb4aff15-f076-3001-bd8d-24d5c43fc21a | -4.26444 | -48.55775 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07018cff-20ca-3e8f-93e0-0b60309510c3 | -4.41424 | -48.94423 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 894a2fe7-8713-36a1-b939-91fd71fab263 | -3.67237 | -50.45243 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08d0b8fe-9a0d-39a3-9dc9-47d213386dba | -3.13963 | -50.16544 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b8064503-1439-3797-896c-c5af67b09aa6 | -5.09816 | -37.78443 | 2025-11-09 04:38:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 88aaf588-4766-319f-874a-1a89985c8bc6 | -4.25197 | -48.63699 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b9ed4ad-09de-3448-8e8f-0281cb8a1f27 | -6.04062 | -57.96511 | 2025-11-09 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d0e257e-62b0-300f-8952-aab9286a7c9b | -3.82595 | -51.35574 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7201573b-a15c-332c-8a52-d8a9e6cf3857 | -5.48489 | -46.09646 | 2025-11-09 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
