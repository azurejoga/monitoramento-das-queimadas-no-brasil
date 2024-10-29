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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a7029ec-cccb-31fc-b8d0-7c0880ce5a51 | -1.3716 | -55.86303 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e17415dd-d22f-3a28-bba2-1a6c4c88214a | -1.37098 | -55.86601 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7448efc0-01ef-3991-a5a3-98dfc203fb62 | -1.36679 | -55.86233 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10036f4c-296a-3bdc-8b92-aa4741aa9fc2 | -1.36042 | -55.68725 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75b29477-9f87-3690-8ea3-bfe41d6db62d | -1.3596 | -55.6924 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41f863cc-230d-3e45-b218-9f77d127a67f | -1.34343 | -55.14795 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 911ea63b-f5b7-3baf-8252-cc17408c08fd | -1.34268 | -55.15266 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 1ce7102c-5f3e-3d58-a177-51a7f9a0eac4 | -1.33888 | -55.14712 | 2024-10-29 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47c07687-c090-3606-96c1-f784d8d3d29a | -1.32806 | -55.45398 | 2024-10-29 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b80f17f1-76c9-3a9b-82e6-a9c0dac16798 | -1.32297 | -55.82881 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b298c7e1-5478-3fca-be16-720d88e77499 | -1.31817 | -55.82809 | 2024-10-29 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1c81a68-a32d-306a-9a36-bd64d595dee6 | -2.27882 | -56.42945 | 2024-10-29 04:38:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd2e94e6-8db8-3035-8c6d-066ea55c0997 | -2.46654 | -55.62462 | 2024-10-29 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa3e143d-c2d8-358e-bceb-a0f31e2dc1a1 | -2.10109 | -56.86122 | 2024-10-29 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7cca772-007d-3387-a8d5-daba66a6b516 | -2.06022 | -56.86547 | 2024-10-29 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1c2cf02-2b57-3ad1-a842-b60566e0a2fa | -2.05972 | -56.86853 | 2024-10-29 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca96032b-5985-3d47-848b-a40219a924b4 | -2.05513 | -56.86465 | 2024-10-29 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a684db0-e5cb-344c-8226-d4655019d885 | -2.05464 | -56.8677 | 2024-10-29 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbcbde13-bf46-3034-a3d3-0d480dfce40b | -2.3433 | -57.14938 | 2024-10-29 04:38:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04a4ec88-fb89-371d-88a2-8ecef9ccd26c | -2.3428 | -57.15247 | 2024-10-29 04:38:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fdfeaf9-9792-3d8e-ac30-ece15cb3c9ce | -2.34231 | -57.15554 | 2024-10-29 04:38:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88ad6a8a-7002-3638-8549-a23a2214e012 | -2.33712 | -57.15484 | 2024-10-29 04:38:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d966069-a31c-3bc6-906f-2d67ecfd99d2 | -2.32732 | -57.14993 | 2024-10-29 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f060aafc-f590-3fc2-b0ff-2b69a6f584fa | -2.32215 | -57.14912 | 2024-10-29 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09729f04-d8a5-3a66-8bff-bcf64779ebb5 | -2.32164 | -57.15228 | 2024-10-29 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 157357f0-33ee-3528-906b-a0555d2bb31c | 2.55227 | -59.97123 | 2024-10-29 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60a3ff51-f28d-35e7-8181-0c6b0d4f038c | -1.71943 | -60.13151 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fc854e4c-21bf-31f8-8a03-73a622e40fa2 | -1.4276 | -60.28659 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cfb0e96-8087-3a8c-a066-2676eae10072 | -1.42671 | -60.29192 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3527fa0a-2e68-3ba3-8f5e-192b388afd05 | -1.42566 | -60.28942 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b61c3b17-7ff1-31f3-b2da-7bc7fa3f27ab | -1.42207 | -60.28033 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57c19765-a65b-3664-8b12-8b29bfe715d0 | -1.4201 | -60.28308 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93327504-0d94-374c-9137-cb4981d7fb11 | -1.30439 | -60.22696 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da484383-ee96-3ce3-b09e-4385a927156b | -1.30247 | -60.22762 | 2024-10-29 04:38:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7b45b2f-8498-3849-a680-8807a6017d5e | -6.67385 | -37.4719 | 2024-10-29 04:40:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ac85109-6345-351e-afef-ecb70e475d92 | -9.09786 | -40.36391 | 2024-10-29 04:40:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb7805c8-5a97-3b05-aab4-30ccd66bc7b3 | -9.09738 | -40.36758 | 2024-10-29 04:40:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 89e3c26c-fe35-3cee-9d6b-34c186d75864 | -8.80524 | -40.96471 | 2024-10-29 04:40:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d46c4553-c682-32fb-982a-a00b37af9564 | -8.29791 | -40.46475 | 2024-10-29 04:40:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94992eb5-45cb-3980-9779-0eebe822a8e2 | -9.38443 | -40.7952 | 2024-10-29 04:40:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d8b71115-ca91-3cab-8506-e1d25f6adecd | -9.38397 | -40.79873 | 2024-10-29 04:40:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a6595528-748a-3f45-ae68-088a2e2e0f75 | -6.28571 | -41.93193 | 2024-10-29 04:40:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5a91ee37-7a43-32d4-b1b7-0546bdfbba48 | -6.15937 | -41.78735 | 2024-10-29 04:40:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c7bfbdb0-c5a6-3074-9b08-cfac572bbf02 | -6.1583 | -41.86572 | 2024-10-29 04:40:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5e5b42ce-8452-38d9-ada6-d1453065f9ff | -6.15768 | -41.86349 | 2024-10-29 04:40:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1b1c4dc8-35e0-3633-aa2f-d201097f5cf5 | -6.15692 | -41.86868 | 2024-10-29 04:40:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e80418a5-35e6-37e6-af87-547959883fb2 | -6.15347 | -41.86556 | 2024-10-29 04:40:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 88d9fab1-b621-3bb1-95ea-63b37ce53703 | -6.15286 | -41.86328 | 2024-10-29 04:40:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5d761f71-a728-3d96-8b5e-efca7cb8331c | -5.62319 | -41.73487 | 2024-10-29 04:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 59586387-96b3-3554-a5cb-4eefbc504922 | -5.61915 | -41.72919 | 2024-10-29 04:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b9ef0cb6-7fad-3627-978c-5f2b12a5f159 | -7.33599 | -41.87428 | 2024-10-29 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| aa9b0abe-f86a-3bba-9689-9ee43a2069f3 | -7.00867 | -41.2957 | 2024-10-29 04:40:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2cb10146-3319-3b2a-a3e3-5a8166bde792 | -7.00828 | -41.29855 | 2024-10-29 04:40:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 98c3f710-5ce9-3444-92b1-65d9c2228f71 | -6.99862 | -41.33203 | 2024-10-29 04:40:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c07c6d8b-4720-38a6-bf62-95444607bf65 | -6.99824 | -41.33485 | 2024-10-29 04:40:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46ed75eb-5b50-3369-b6f5-917392efbf45 | -6.99786 | -41.33765 | 2024-10-29 04:40:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d62ee49-1d82-3d35-bf3c-66c21b47f9a3 | -6.99748 | -41.34044 | 2024-10-29 04:40:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 81cc4191-792a-39f4-a4d6-dae5975e083f | -6.9971 | -41.34321 | 2024-10-29 04:40:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 272094ae-1bf0-357d-88bb-3f6b66e1ad47 | -6.99325 | -41.3341 | 2024-10-29 04:40:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1f907ebd-f2c4-3610-833d-914464719c8c | -6.99295 | -41.3338 | 2024-10-29 04:40:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0d54fd8-4c40-3ab3-b035-eb6d36cc84cb | -6.99287 | -41.33688 | 2024-10-29 04:40:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed5d8257-69c0-3cba-a3cf-bbb8d9101802 | -6.99255 | -41.33659 | 2024-10-29 04:40:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eee92fec-cd4c-3998-9a1b-842e5290027e | -6.99215 | -41.33936 | 2024-10-29 04:40:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7c7205f-b674-3e20-8466-5cee55c9a523 | -6.98788 | -41.33608 | 2024-10-29 04:40:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28fbb64e-7f1c-344e-bcb9-7b2447f57271 | -6.98756 | -41.33579 | 2024-10-29 04:40:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e770c098-cfb7-3c33-8afd-8b1388d5f91c | -6.67617 | -40.89231 | 2024-10-29 04:40:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 02fa36e3-0ae2-3ea7-aa54-82ec1063ead5 | -6.67574 | -40.89543 | 2024-10-29 04:40:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 270ea735-806d-3d29-b393-ca72bb3e3970 | -6.5176 | -41.57689 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9dd36107-8332-31f2-9c13-0f5017dda443 | -6.51534 | -41.57851 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 86fb9b78-dcc6-36a9-a8fb-9ba5a3488941 | -12.0111 | -42.95085 | 2024-10-29 04:40:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 308aa12a-3ae4-3029-b790-9ddcc8e50bea | -12.0063 | -42.95016 | 2024-10-29 04:40:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 899a3ba0-315c-3158-87ee-a0654e2e3e17 | -11.28974 | -41.86197 | 2024-10-29 04:40:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d24d948a-9eb3-325d-8737-ae80b725dccc | -6.51659 | -42.35897 | 2024-10-29 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 82309798-cf27-3e93-805b-8b75322d0759 | -6.51643 | -42.35542 | 2024-10-29 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 68f91121-ab8d-3e88-8b61-a3f5549357ac | -6.51578 | -42.36006 | 2024-10-29 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8ac3f96f-4ca0-3ebf-b202-6848a34ffabe | -6.48376 | -42.19141 | 2024-10-29 04:40:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a9636b34-b90d-35c1-8497-377f40e1650c | -6.44097 | -42.23653 | 2024-10-29 04:40:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 77edc966-f06b-36ad-9803-d749ec68870e | -6.43902 | -42.23891 | 2024-10-29 04:40:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8da8b674-895c-33b2-81fb-afd75223320c | -6.13713 | -42.51819 | 2024-10-29 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8b68a5f7-713c-3e3d-889a-b271dc9e2c45 | -6.13324 | -42.51299 | 2024-10-29 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3bc6dab1-ebfd-370c-89c3-3e954d3336c4 | -6.13258 | -42.51751 | 2024-10-29 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 19fee5c7-6fd9-3662-b04d-3256072d4574 | -6.12804 | -42.51685 | 2024-10-29 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d0042763-5bca-3596-9d8c-18fe655e2c50 | -5.88409 | -42.3232 | 2024-10-29 04:40:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b9784615-75f0-3a84-aa97-f8ccf49a8641 | -5.62128 | -42.48164 | 2024-10-29 04:40:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 99a319e7-485f-3263-902b-96d400dc5b7c | -5.62061 | -42.48619 | 2024-10-29 04:40:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e7f4f453-f4d4-346c-a0ee-a3bec23efc35 | -5.61173 | -42.45227 | 2024-10-29 04:40:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 26eeacae-1cb1-306a-a88f-e2c2a791936b | -5.24031 | -42.46388 | 2024-10-29 04:40:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f66a14d3-70d7-399f-a537-2c20daf4813b | -5.8333 | -42.84396 | 2024-10-29 04:40:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3b43fb7-1d12-35f2-957d-1ae64ba176a7 | -5.55309 | -43.22941 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c168acd-33e3-34f7-ae9c-f2a7e90e6f99 | -5.537 | -42.99159 | 2024-10-29 04:40:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b1d2095f-94f8-35c1-b907-40a2e82ca4ad | -5.52305 | -43.32129 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eded803a-3c12-368e-a9b8-1d6b7c157ef9 | -5.52273 | -43.31934 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 869c1eee-55e3-3064-ba6b-426f39c7023e | -5.5194 | -43.31658 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9588da74-95a8-3d6e-9f48-049d3f28b4a0 | -5.51848 | -43.31863 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9c468a3-5af1-3179-851c-a21302a54736 | -5.35051 | -43.13594 | 2024-10-29 04:40:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ace6b69-9d3b-3d9d-8733-1b196254d468 | -7.27328 | -42.57088 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 220b400d-9c9f-3193-97e2-2ab360fface6 | -7.88022 | -42.95558 | 2024-10-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f6d04523-4724-3461-ac10-12f3fc8b44c8 | -7.80452 | -43.1812 | 2024-10-29 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 18217336-553e-31da-82ba-710533b27d55 | -7.80368 | -43.1784 | 2024-10-29 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 64435c53-29d4-322d-8ffc-150a12224d7e | -7.34408 | -43.57478 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README56.md)
