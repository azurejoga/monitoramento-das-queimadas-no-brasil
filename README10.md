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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bd32e4e-bc71-3525-af9e-0397757eb631 | -14.21232 | -44.39114 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7884c591-603a-34de-b799-97609a381441 | -13.79692 | -47.06201 | 2025-10-31 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78c303c0-ea84-3d40-a891-a0c8a0bd871b | -10.85311 | -44.90642 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d0607f8-1586-3236-8b20-fe01e0efc8c1 | -4.36382 | -45.66014 | 2025-10-31 03:47:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98766eb2-3ccc-3702-89f1-de5ee6a5568d | -5.80044 | -40.82444 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e086d9e8-174e-3ff9-b370-a4501d4a4386 | -14.20769 | -44.39013 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3c5344a-18ab-317f-bd84-d2c3485c12f1 | -5.8879 | -43.19905 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 524a1e98-1267-3074-b251-a8f5412f4dc2 | -10.88807 | -44.36757 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78fdb5dd-33e6-3705-8024-dc827e58fc1a | -4.92019 | -45.32212 | 2025-10-31 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dffb439-d957-3cd3-9080-0d93bc0eb117 | -8.09036 | -45.14477 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 556d64be-1714-357d-a18a-c4b4a8f0cb38 | -5.92441 | -43.3741 | 2025-10-31 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b211d574-973e-3321-9f24-02b6ec648036 | -9.02915 | -47.46176 | 2025-10-31 03:47:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34109735-7807-3b89-9313-797b97f1c173 | -13.68539 | -44.72233 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 51016d81-2ad4-3861-a63a-bacc794c49f9 | -5.25425 | -45.51307 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5964654-ff25-3e8e-a224-7f5a5131d9a5 | -5.42156 | -44.5872 | 2025-10-31 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51d859fd-6abe-3141-ad63-cd4e4657501d | -10.42992 | -40.50418 | 2025-10-31 03:47:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0de91b26-fb9e-3201-9b20-a89e9c3f5177 | -12.93945 | -47.93569 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7875a3a4-4d01-37bb-8dea-e8ef6e9dd1a6 | -9.88446 | -44.86252 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3251fd98-0e26-3631-9b93-c1e7ce10a741 | -7.39216 | -43.01092 | 2025-10-31 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d288daa-bbf1-316a-aad2-36593113ea12 | -5.93111 | -43.33513 | 2025-10-31 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e96616e-3caa-35ed-addc-ba8089b89a7f | -8.04927 | -39.06851 | 2025-10-31 03:47:00 | NPP-375D | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c57dd0c-0f35-3f04-9b41-b0ee0fa9abd9 | -5.69958 | -43.16238 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 13b72ed6-8c7f-36ce-9e92-ee0122cad238 | -5.61594 | -45.98148 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4a1f7d5-f691-3006-9784-e4d08e1e76e0 | -4.78935 | -44.32444 | 2025-10-31 03:47:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9af59110-be6c-3bcd-af6d-4a971cf47b54 | -8.83953 | -40.97397 | 2025-10-31 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc60cbf9-a12e-34d1-a619-5c61168b28ad | -4.91066 | -45.72767 | 2025-10-31 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51fb8e1b-4ef1-311c-a58a-4316950622ae | -8.31817 | -45.38181 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8a5640c-b5d4-3666-9504-2a19dc660eab | -13.39178 | -47.34465 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b79b6dfc-6a2b-34f6-a411-b088f476eef7 | -5.80527 | -40.82162 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 588b3e5c-cb9a-3c0a-91d7-e496178eba59 | -5.65004 | -39.63699 | 2025-10-31 03:47:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d3637b9-ab12-3b7b-b1ba-4c5e453fe78e | -5.88858 | -43.19703 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 26e8551e-766a-37eb-9f46-7a82b96e92cc | -10.8866 | -44.32072 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2717584b-254f-3cc2-a3ac-9e8793603662 | -5.54178 | -38.03597 | 2025-10-31 03:47:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7075622d-a7da-3cb1-8bda-81acb6889588 | -7.07157 | -44.93249 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b626698c-1669-3b82-870f-6fe89f842fa5 | -7.76796 | -46.4735 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1451c56b-c8e2-37a9-9c50-9a1b465e3f56 | -7.9344 | -42.23701 | 2025-10-31 03:47:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed45a98f-1596-3246-a735-68782c813f1d | -6.51337 | -40.79731 | 2025-10-31 03:47:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7bf00c15-a4f9-3eda-a1cd-612d8184e917 | -7.38108 | -39.0431 | 2025-10-31 03:47:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d554eaeb-3855-3a58-806e-4680f5c30308 | -7.39123 | -43.01625 | 2025-10-31 03:47:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f29126cd-fabb-3b75-9420-548f14c0391d | -5.06396 | -45.11398 | 2025-10-31 03:47:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aacf4fcb-ff0b-3c0d-a862-ed8f907ccbc0 | -12.94018 | -47.92533 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00fe75b9-db84-37ec-b3f6-5e67e4653f2e | -9.87867 | -44.86484 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c37779ba-14ed-3650-8a97-7e34ab2bb978 | -7.35214 | -45.00502 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 884c0f16-e3cd-39cb-9e48-923509f8c789 | -10.74933 | -44.73121 | 2025-10-31 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e2d6211-dc92-395e-a404-c55c5fffa99e | -10.93686 | -44.15915 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 97640cdc-8ae8-30f0-9436-c9a8a8ae2f3d | -7.07833 | -44.92616 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 243e6441-9a25-3d94-b3f5-5cda7acd3e97 | -13.68914 | -44.72863 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a335ed00-2a80-3653-ac3c-95177e25dd0b | -6.51394 | -40.79627 | 2025-10-31 03:47:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 572d69fb-5c1f-30ff-81ec-16c2c4035682 | -8.07944 | -45.14275 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3a1b41a-5434-3363-b14e-232b865a622e | -5.28246 | -45.42339 | 2025-10-31 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7aacc33d-c912-3b94-bc9b-375850d5f0fb | -5.70722 | -48.8881 | 2025-10-31 03:47:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 18289d91-b11d-3fad-9c06-ea58059972c1 | -13.94003 | -44.04482 | 2025-10-31 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76655f0b-c301-3c0d-ae27-19a91954715a | -7.78865 | -41.57579 | 2025-10-31 03:47:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2101e49b-7ba8-3403-a08e-c78be083bc32 | -9.88016 | -47.46114 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f464f255-a6e9-3ef8-9ab4-123fcc91c0a5 | -4.83515 | -45.33517 | 2025-10-31 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 337a09cc-493b-386b-a8de-2d64cb4c809c | -7.0777 | -44.92974 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21c4e340-6d02-3e67-ac23-e5eec1c425e9 | -5.03397 | -43.61481 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9cba6d16-79df-39a7-b466-0a67558215d8 | -10.2791 | -44.55453 | 2025-10-31 03:47:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 57df02f1-a0db-3f8b-a4a9-3f5cb860f2e2 | -7.90687 | -43.1762 | 2025-10-31 03:47:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 21545938-a3e4-3538-973b-7c7493e59830 | -6.66755 | -44.69316 | 2025-10-31 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b600d46d-3ae8-35bf-a6d0-c906b421be6f | -6.51295 | -41.34395 | 2025-10-31 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef10ff58-2d3f-3d7c-bb7b-421edd10e5e1 | -8.09102 | -45.14112 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8609ffee-ad6c-3a15-a811-723785e11ebf | -4.78581 | -46.87887 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ec87bb0a-9b03-3bdb-96ff-a7b6fbee9254 | -7.04893 | -41.47324 | 2025-10-31 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fa385941-1e40-3f6c-9b5a-5c51ca819ee0 | -8.08556 | -45.14015 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91d17ebe-2ba2-36f6-81c4-f6896a2982b7 | -4.35682 | -46.78247 | 2025-10-31 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11720a5c-b8e7-3362-a6fd-b2593d31068b | -9.86652 | -44.87251 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa74d25-61d0-3df6-8072-63522b53e4de | -14.39087 | -43.72006 | 2025-10-31 03:47:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3ac46f7-2f0c-30f0-b01a-3a5c5d7fc9b5 | -5.69556 | -43.156 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1815ffaa-8221-33aa-8cbf-60cf352328b8 | -5.74279 | -45.58062 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 025cc6d5-34a2-3523-ad61-4e414c0f3842 | -5.47319 | -44.3179 | 2025-10-31 03:47:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ff01ee1-e22d-31b2-bf4f-c17f1e3dbabf | -3.48048 | -45.86584 | 2025-10-31 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72834eca-56f3-3d61-b937-8fc8d92963f5 | -13.94092 | -44.04002 | 2025-10-31 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cb52705-3e65-3231-a089-1b6c85e2e469 | -7.33198 | -42.73479 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3f2c770c-60ca-324f-8140-9f122d11ca1e | -6.51363 | -41.33987 | 2025-10-31 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2a455aa-f704-3c01-8673-2375debebdf2 | -4.87668 | -47.53095 | 2025-10-31 03:47:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2931a936-f2b9-3784-bf54-605d1d8759ec | -5.62081 | -45.98102 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d110d391-a9b1-3139-b045-09fe13908e8a | -10.85823 | -44.90742 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 873d268f-5561-3e93-9b75-da5d587573c9 | -7.82798 | -40.3649 | 2025-10-31 03:47:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0df3a0ca-9e16-3904-b5b0-bb37a2b6d4b9 | -5.78645 | -43.73842 | 2025-10-31 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe714d37-42a4-3f8e-8eca-e2b1e616bb6d | -4.85442 | -42.74012 | 2025-10-31 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ef3e1a11-8f22-31ba-b27c-95e35850412c | -10.76143 | -44.19735 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c562fae-5d7e-3515-85e7-c9adda4a017b | -15.13442 | -41.83618 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 68963ae1-fb5a-3d43-b9c9-94733b7e2390 | -7.38597 | -42.47721 | 2025-10-31 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 81d98551-68c6-3f57-8f87-9ac3458d6db1 | -8.09455 | -45.15279 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0dce138f-4956-3af0-b471-9cd65488c70f | -5.94964 | -39.83598 | 2025-10-31 03:47:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1423f7d-1869-3db3-ab63-aacc8a91297f | -5.26014 | -45.51393 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93e3768e-4dfe-355b-a90e-6bdf26feee2b | -8.31318 | -45.37797 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c96e2a34-562f-3346-b029-bca5cb35ae1a | -5.42031 | -44.58961 | 2025-10-31 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3f7008b-c976-3a7e-b972-c11886306005 | -4.6692 | -45.09131 | 2025-10-31 03:47:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0e27164-c5b1-3f2e-ac23-b20111c84980 | -5.74786 | -45.58603 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6612aaa1-d0aa-32af-8a13-727eb262527e | -7.79296 | -41.57652 | 2025-10-31 03:47:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4dde3052-d65c-344b-a7eb-d7b71fbd375b | -5.6946 | -43.16148 | 2025-10-31 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9a2274d3-3f6d-37d8-bac8-ad3d73759d16 | -9.34754 | -46.59871 | 2025-10-31 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3a3b21f-d71a-316b-b8d6-0eac19ea7eb0 | -10.50322 | -42.405 | 2025-10-31 03:47:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 4f511f58-bf8b-391e-a6a5-9e6988e619e4 | -8.16954 | -45.49014 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d2b76ac-ed67-34ae-9ba0-29b675e33623 | -10.64362 | -45.24279 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71457442-8993-36e7-8eb1-7393ce631361 | -10.7486 | -44.65028 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04abda34-21dd-3522-ba45-50ecc67a50f4 | -5.80106 | -40.82076 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 084980c9-7b58-3f71-abed-4fcfa6448387 | -3.7771 | -45.16671 | 2025-10-31 03:47:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README11.md)
