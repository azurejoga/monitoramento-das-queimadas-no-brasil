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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 086828bf-538a-30c8-8e4d-1f2c94f629f7 | -3.5269 | -43.6828 | 2025-11-28 08:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| e130325c-3f13-30f5-bbeb-d7090f8df85b | -3.5269 | -43.6828 | 2025-11-28 08:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 2adfcfa5-e3d3-35ef-b1ee-a2202356b340 | -3.5269 | -43.6828 | 2025-11-28 09:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d3910d24-1a05-3138-b977-8b5a589b8b19 | -3.5269 | -43.6828 | 2025-11-28 09:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 89b28754-d09c-3b05-b188-1161c1c4d8e7 | -3.5269 | -43.6828 | 2025-11-28 09:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| b4e9fcdc-384f-30c9-8ccc-18810e0e021a | -3.5269 | -43.6828 | 2025-11-28 09:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| e6e3daf0-f481-37d7-8cf1-393883b68510 | -3.8029 | -44.3136 | 2025-11-28 09:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 7578d117-59ee-3db5-9064-9a7c0fce1eea | -3.5269 | -43.6828 | 2025-11-28 09:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 2b2c86c7-4e03-382e-9763-f43f0c8ba3ee | -3.5269 | -43.6828 | 2025-11-28 09:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 851275f1-1116-353f-b2ca-6050c39670ac | -3.5271 | -43.6597 | 2025-11-28 09:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 65989c36-1171-302f-848b-2f31604c30be | -3.8029 | -44.3136 | 2025-11-28 09:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| ecdd39e8-9b14-335f-8140-7d811ea5edf0 | -3.5269 | -43.6828 | 2025-11-28 10:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 975686d9-47b0-36b5-a6ee-a8fae48c7c2d | -3.5269 | -43.6828 | 2025-11-28 10:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 6cdbb035-7e4a-31af-9d4a-f556e190d09f | -3.5271 | -43.6597 | 2025-11-28 10:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 6c98dfe6-af76-3b36-b97a-27a334ea6fbf | -3.5084 | -43.6606 | 2025-11-28 10:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 3afebec3-7add-333a-a50c-dfbc3e53d234 | -2.9788 | -45.3467 | 2025-11-28 10:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 5beb2319-f39e-3030-8c93-0e6937a9223e | -3.5083 | -43.6837 | 2025-11-28 10:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| f6386ca6-5f3c-3457-9a51-80eed360fb29 | -2.9789 | -45.3242 | 2025-11-28 10:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 6f8f0496-8329-341c-b505-0fc663cf1526 | -3.5083 | -43.6837 | 2025-11-28 11:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 0fad9eb0-8bda-34f2-8201-66d2d4d578a4 | -3.5083 | -43.6837 | 2025-11-28 11:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 279.5 |
| b5928753-d5a2-38ce-9378-7ff183834e4d | -3.1089 | -45.3419 | 2025-11-28 11:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 5b59c0bc-76be-35f3-a553-edce0b3fef9a | -3.1089 | -45.3419 | 2025-11-28 11:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 145.7 |
| ff4f6396-4deb-3ad6-bba2-e321253cf906 | -3.5083 | -43.6837 | 2025-11-28 11:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 517abe12-b3a5-33cd-b561-4e2e4e48031a | -3.1878 | -44.4096 | 2025-11-28 11:30:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f5755f38-fa31-33e1-8413-2cbaee04eb2d | -3.2065 | -44.386 | 2025-11-28 11:30:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a6efaafe-c09a-30e6-897d-6158c6ff6a30 | -3.1878 | -44.4096 | 2025-11-28 11:40:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 6c07c75c-5bae-392f-a082-acdc25566f0e | -3.1878 | -44.4096 | 2025-11-28 11:50:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| a9a37f53-fc7f-3505-afb5-0877505246ce | -3.2064 | -44.4089 | 2025-11-28 11:50:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| eef82d92-6308-34db-b45d-31290fffc082 | -3.5083 | -43.6837 | 2025-11-28 12:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 4b71a7fc-069e-303e-8653-86901d1ab4a6 | -3.1878 | -44.4096 | 2025-11-28 12:00:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 957cc3cc-a831-3b1e-b11f-a7fe3fb4b893 | -3.1878 | -44.4096 | 2025-11-28 12:10:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 39e75770-62db-3045-8b57-eee1989040b2 | -1.68773 | -47.01255 | 2025-11-28 12:14:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bd9cc17b-009f-3a82-8ec6-c2883d4d3074 | -3.37429 | -42.08262 | 2025-11-28 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 1e71b818-10cd-3154-93d0-4fc098bad9d7 | -2.24369 | -46.14953 | 2025-11-28 12:14:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c51e0feb-ad62-3b9d-9953-946b916357df | -2.90922 | -42.03877 | 2025-11-28 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 05b1db30-fdd5-3d2b-80ec-77ac8acbc888 | -3.04082 | -42.06901 | 2025-11-28 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 0d5ae2d9-84f8-3f76-87be-c582484411f8 | -3.07349 | -42.41828 | 2025-11-28 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6277d4da-2261-37fd-837d-477a4e133e8e | -2.02721 | -45.46915 | 2025-11-28 12:14:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e13a8730-76a1-3718-959c-5f58fb54d00c | -2.50164 | -45.76711 | 2025-11-28 12:14:00 | TERRA_M-T | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 95c1c54c-f663-3962-a90f-7fd0ffe0216e | -1.49375 | -45.78308 | 2025-11-28 12:14:00 | TERRA_M-T | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6645857f-0c70-3a29-8080-0219748e5583 | -0.87735 | -47.24468 | 2025-11-28 12:14:00 | TERRA_M-T | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a57a12dc-4df1-3adf-a3b4-f10a2a8e1a3f | -3.25402 | -41.26145 | 2025-11-28 12:14:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 17.9 |
| ee241a70-5a13-35c1-87af-7ba1c2eef161 | -3.38329 | -42.0728 | 2025-11-28 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 101644ca-b24c-3a0e-a7ea-6d8e279d7823 | -2.42112 | -47.23531 | 2025-11-28 12:14:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 9d6d6c9c-b9e5-3b39-b73b-987c5e2f8a12 | -3.12563 | -42.37803 | 2025-11-28 12:14:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a4b98bfb-4dc9-3434-83ed-f1f3cfe3bf4e | -2.42238 | -47.22657 | 2025-11-28 12:14:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 13a6fab2-0819-3ecc-b981-e6000edf9801 | -2.56647 | -47.50854 | 2025-11-28 12:14:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a5e6f3f6-8bfb-393d-891c-9c84d25a1f96 | -2.99371 | -42.2426 | 2025-11-28 12:14:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e301761a-8c6c-353a-819d-fe088534f722 | -2.99696 | -42.23722 | 2025-11-28 12:14:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 45f86b6b-921d-3f70-960d-34564baf5206 | -3.38839 | -42.06783 | 2025-11-28 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e5319bdd-17c0-32fc-bc0f-9b28303a598b | -2.90693 | -42.05515 | 2025-11-28 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 1faff8de-eba3-3df7-b75a-30fe55845f1c | -1.90724 | -46.12103 | 2025-11-28 12:14:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 5f2694cf-ca2b-37d2-b273-db83f3be9ba5 | -2.99472 | -42.25298 | 2025-11-28 12:14:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| bfae801b-bf09-315a-b037-6a26accb8c04 | -0.8572 | -47.57315 | 2025-11-28 12:14:00 | TERRA_M-T | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7798632a-e75c-312b-a5a8-3a9565dafff6 | -0.88311 | -47.9735 | 2025-11-28 12:14:00 | TERRA_M-T | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c9408582-b753-35f3-bff3-d3f300b42fd9 | -3.42954 | -41.31958 | 2025-11-28 12:14:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 6339708f-5054-3799-a07c-e6f202b98de7 | -3.03144 | -42.07836 | 2025-11-28 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 3db7e883-d09c-39c0-bae6-63a32465fd09 | -3.03861 | -42.08529 | 2025-11-28 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 2ccbcdf7-343c-3235-bc8c-d480504dd545 | -3.0757 | -42.41211 | 2025-11-28 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5653c293-1ee1-32aa-bd5a-5794856339dd | -0.8673 | -47.25221 | 2025-11-28 12:14:00 | TERRA_M-T | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 53ccee7b-e92c-32ab-9346-473f9362bd03 | -2.67697 | -45.19045 | 2025-11-28 12:14:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6712558f-140e-3b8a-a380-ad3281870bf3 | -3.37658 | -42.06622 | 2025-11-28 12:14:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 080da4d6-542d-3c1c-bce7-7c51e3011d0a | -2.27453 | -47.09558 | 2025-11-28 12:14:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| adeaeaf5-f296-3f70-ba77-d247c81c0e93 | -1.49245 | -45.79225 | 2025-11-28 12:14:00 | TERRA_M-T | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8d432f3a-7c76-364e-914b-358d8c15327e | -0.8761 | -47.25343 | 2025-11-28 12:14:00 | TERRA_M-T | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e1e6a339-b9d1-3bc0-8463-2277a676ae8f | -1.89321 | -46.28374 | 2025-11-28 12:14:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1db49b6a-ad7a-3a2a-9708-8800af54d0ba | -1.44812 | -47.45698 | 2025-11-28 12:14:00 | TERRA_M-T | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6fbad7d9-afbf-3a7e-a4ec-9903d5f53407 | -3.03376 | -42.06211 | 2025-11-28 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 944fd313-e3a9-3ea2-bcff-196751cda3a8 | -3.12349 | -42.39347 | 2025-11-28 12:14:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 70dcd813-96eb-39f6-8071-aa3460db52a0 | -2.02856 | -45.45965 | 2025-11-28 12:14:00 | TERRA_M-T | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 37754390-64c3-36c5-bd6a-a7e673bbb813 | -1.90597 | -46.13004 | 2025-11-28 12:14:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 2ccf28e6-d4e9-325d-bd7a-770287ac59f9 | -6.47567 | -38.86298 | 2025-11-28 12:16:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 1ad920b0-a833-3e78-b3b3-3c75955c236e | -7.4582 | -44.75129 | 2025-11-28 12:16:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ea4be2ec-06d1-3fde-bc97-23ccd93ae8dc | -3.43058 | -42.07897 | 2025-11-28 12:16:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 5e0f142f-02e8-33d4-9511-00eddae3b859 | -3.71122 | -41.85913 | 2025-11-28 12:16:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| baa9af0b-a050-3a9e-91e4-3bd942143b50 | -3.19199 | -44.3955 | 2025-11-28 12:16:00 | TERRA_M-T | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 173.9 |
| ba9a40dc-42a4-3692-9417-df1625f1edef | -3.70911 | -41.83461 | 2025-11-28 12:16:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 42.8 |
| b90b3a11-e3d0-355f-989c-5151c0a75ddc | -4.09882 | -48.01542 | 2025-11-28 12:16:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eb9cb5a7-d9a0-35d6-9313-0ea9c2448035 | -3.73775 | -40.48841 | 2025-11-28 12:16:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 90eddc10-c2f1-3048-a7db-5f1571cbac28 | -4.10982 | -47.29602 | 2025-11-28 12:16:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e92c70c2-a6c3-3eb5-aaee-b321ad837fdf | -3.8059 | -44.32005 | 2025-11-28 12:16:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 970589be-ac78-38d3-bbd3-1520424d9ab8 | -4.17925 | -43.75752 | 2025-11-28 12:16:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 12e7372c-c3a3-34cc-ba2a-fba45133ec5c | -3.3179 | -44.44113 | 2025-11-28 12:16:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 623e2586-edfd-3b22-af61-d66e7517361f | -3.79283 | -42.20247 | 2025-11-28 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 95a0a58a-99bb-3ac3-a2c8-d9f6c3647abd | -8.16763 | -43.1917 | 2025-11-28 12:16:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 095033c8-feed-3f69-9930-aec1de344975 | -8.36747 | -41.84277 | 2025-11-28 12:16:00 | TERRA_M-T | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 1391f6dd-0ab2-3119-aa64-6e21597bdd00 | -8.41273 | -44.03054 | 2025-11-28 12:16:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 160.6 |
| d06e8934-8319-3f97-8473-0d35063915ef | -3.56937 | -42.14329 | 2025-11-28 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| c40d6860-055b-307a-8824-027758b6bc69 | -8.17375 | -39.68175 | 2025-11-28 12:16:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 88c91ec8-652d-3044-8472-1f44511edfc2 | -8.16934 | -39.688 | 2025-11-28 12:16:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 005e3b4f-52ae-3b23-82dd-c395f5508ecb | -3.78106 | -42.20087 | 2025-11-28 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| b054ffbc-bd1f-3017-aac3-783de5b155b6 | -3.56243 | -42.1365 | 2025-11-28 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 5d9909c6-fa8d-3be3-8ebe-9fe51c4e9340 | -8.42371 | -44.03181 | 2025-11-28 12:16:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a56a21f6-5e61-3e3d-9deb-74d884ab25e2 | -3.38452 | -42.4151 | 2025-11-28 12:16:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 37.4 |
| 2346f56f-2ec7-3bf4-b3ec-fd813f0018e1 | -3.51904 | -43.67048 | 2025-11-28 12:16:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 5231309b-a962-312b-b7ff-a741fbe4da5e | -3.71356 | -41.84163 | 2025-11-28 12:16:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 7df3ab1f-7a92-3171-88a7-c21f3915e9ce | -8.41462 | -44.01621 | 2025-11-28 12:16:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b55999cf-9d71-3602-a8be-781c2a84acb9 | -3.39735 | -44.16965 | 2025-11-28 12:16:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 209078c4-e210-3a75-a752-a0b5adf40c0c | -4.87071 | -45.05193 | 2025-11-28 12:16:00 | TERRA_M-T | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 327259d3-aa81-3607-8ff1-94b524265ff3 | -3.53559 | -43.67867 | 2025-11-28 12:16:00 | TERRA_M-T | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |


[Clique aqui para ver as próximas entradas](README24.md)
