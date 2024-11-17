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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5e2dbb0-f081-3767-b3aa-a974d095d139 | -2.5945 | -47.543499 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55a895fd-b863-3c39-b783-1f8f0beb7c83 | -2.6733 | -46.849998 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8148684d-10b6-3d8a-bbb1-2307cd4694a5 | -2.6676 | -46.193901 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94f1f3e8-9a21-34f4-985c-a3c78d863cd4 | -2.638 | -46.560101 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6632d73-83da-3d2a-884d-ecc2fa80d8d8 | -8.4345 | -44.215199 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db4367b0-2838-3643-a33f-bff9c458629d | -4.4712 | -48.098099 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaf7e5d9-6ff2-35d5-ae04-7865ee6ec08e | -1.1404 | -51.686401 | 2024-11-17 00:28:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bea0c82-238a-3b84-a4a8-7da4a0da1eb5 | -3.407 | -45.864201 | 2024-11-17 00:28:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2eff19e6-0f2e-3a53-84f0-12fdb1834347 | -0.1016 | -51.5924 | 2024-11-17 00:28:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 701b104b-844f-3000-b3d2-d6a8107cb483 | -2.8461 | -46.6586 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7575a665-f5b8-3eb3-b8fe-5f251a8ac7ce | -3.0137 | -45.408298 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 70b28c93-9560-3982-9402-4a979a48260c | -5.1111 | -45.153099 | 2024-11-17 00:28:00 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54ae4556-8c96-35a5-9be8-d6abaa4c8046 | -2.4644 | -45.667198 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4159ff-6df4-3cee-924e-b51954207cd5 | -3.838 | -45.9902 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 371659e4-87a8-3107-b167-aa69083c3af9 | -2.6359 | -46.8218 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05deed0a-d2a5-3877-8c8e-5f0172247c5a | -1.4878 | -47.3927 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c52bd757-efb6-3e4e-b4cb-4afeabf5e7aa | -2.6266 | -46.555401 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf75d152-c83a-3ba4-83af-6d39f05ccfe0 | -1.2459 | -47.101898 | 2024-11-17 00:28:00 | METOP-C | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb751b41-8699-3b74-bdc8-5bc5b64e3e62 | -2.5782 | -47.562401 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 036f3982-3a1e-3802-85a6-f899721350ed | -1.7539 | -46.3475 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa25f77c-64d9-3905-90af-f6e33dd65dee | -8.4412 | -44.1992 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8cd1620a-fa06-3e6d-b81d-3587a2eb247e | -2.8477 | -46.665501 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eef0d3b-aa27-3dd2-ba37-f4ae9567dcbc | -3.572 | -45.684101 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2b4b0aa-1073-31d2-b10f-a5434d1cf3d7 | -3.302 | -48.844799 | 2024-11-17 00:28:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0dc3a29-a9ec-3969-a094-cc27bd377176 | -4.0943 | -46.8881 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9e78b1d-876f-34d3-9b47-e97ac9ece5fd | -2.6391 | -46.835701 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af2f1e1c-9ffd-3ec0-af5f-ff594f1fd09d | -6.1956 | -39.779099 | 2024-11-17 00:28:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b5ff4c29-4677-3850-aa3f-f63fe23f656d | -3.5705 | -45.677299 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d33faa7d-1f30-3c74-947b-68ca79760aeb | -9.4047 | -40.330002 | 2024-11-17 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9b012c8c-78ec-347b-ac91-2a12b61c9d58 | -2.588 | -47.5602 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac31488-491e-3c72-846a-594b12f77656 | -8.4396 | -44.192299 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5278648a-3d84-3248-88e2-872d6b13e2a7 | -4.4779 | -44.015598 | 2024-11-17 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 319979d6-a862-39d8-80c8-7538560e6be4 | -4.5275 | -43.294498 | 2024-11-17 00:28:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7cce42f-a5a7-34b4-9bb9-bb248a478eaf | -3.6191 | -43.159401 | 2024-11-17 00:28:00 | METOP-C | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 597636ef-8da7-3e70-b6c5-ed4e9c8026d5 | -3.9349 | -49.005402 | 2024-11-17 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4fe8a7-29c3-3f45-9dc4-c71ce3800de5 | -5.5852 | -44.881302 | 2024-11-17 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91b0e098-64e3-37fb-becc-d3e6de5aaf73 | -8.438 | -44.185398 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9f1dbefc-298b-3ebb-8d4e-a593c4c93463 | -2.6496 | -46.205101 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b60938b-d1a5-3012-897f-8099c1b0db81 | -2.6099 | -46.256901 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 724cac69-b4a5-36d0-934f-b089edf78239 | -3.5689 | -45.670502 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57a5377b-5b01-3ed6-94b6-b9a7afc74411 | -1.8684 | -50.054501 | 2024-11-17 00:28:00 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcd57bca-8e9b-305c-80e1-522efa6c7bb0 | -5.6901 | -46.5639 | 2024-11-17 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4eb61d-fd85-3ff4-9e38-977ff30a93de | -2.9476 | -45.795101 | 2024-11-17 00:28:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44d1d192-c7dd-3e7d-a89e-fa2cdaf4e73e | -1.5023 | -47.4561 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cbffb20-b360-3ed3-a5ff-1aeae0716db0 | -3.1113 | -45.070301 | 2024-11-17 00:28:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5632ace-feac-3b52-aec6-b973d61c434c | -0.3214 | -48.6922 | 2024-11-17 00:28:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eccfa43b-9880-3f82-8a5d-3a188346c191 | -1.2819 | -51.946499 | 2024-11-17 00:28:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7ccd8cc-f8b0-30e3-b592-2b030b0d782e | -2.9507 | -45.808701 | 2024-11-17 00:28:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffeb4b22-97f2-30ac-b618-e18c080a8f18 | -5.5901 | -45.217701 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 878342f0-9421-3f28-80a0-ca1533a7914d | -2.2358 | -46.8307 | 2024-11-17 00:28:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0dce818-01ec-3d71-bda6-47e8c2b251f4 | -4.6821 | -49.633801 | 2024-11-17 00:28:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 896d3a57-9398-3aa5-a4db-cda03dcefc06 | -2.6594 | -46.2029 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d611dbf9-b88d-3c72-8ca8-590602a92ee7 | -2.8588 | -46.713902 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9924210b-6c41-3035-ac31-7932bd45cc47 | -5.2717 | -44.908798 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7861e93d-6de5-3426-956b-b79a4255587f | -2.5074 | -45.450001 | 2024-11-17 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed3bb91-bafb-3b2e-a83e-21892172bf4d | -4.5373 | -43.292198 | 2024-11-17 00:28:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 196596c8-c97a-39ab-a3db-c80f1fac6e73 | -4.4891 | -43.885799 | 2024-11-17 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 563eecc1-9e6e-3b0a-af9b-25aad0a4e4c0 | -4.4872 | -43.7882 | 2024-11-17 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04f62160-de71-3a55-adf1-72dc10e57957 | -2.9044 | -45.0228 | 2024-11-17 00:28:00 | METOP-C | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9b9a112-22cf-321f-bc65-c47ee5769f39 | -2.6625 | -46.216499 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e524735-0569-3e8d-bd3a-1c54157d8fff | -3.5581 | -50.2551 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c245bcad-22f9-34d1-8a6c-bee5c68d2653 | -4.3927 | -45.529202 | 2024-11-17 00:28:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5a9a9d-a24b-3195-a25d-2eb0d1d10964 | -3.5559 | -50.245201 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32e1ed1b-c505-36f8-92b5-71ae5f9203b2 | -3.5078 | -49.939602 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8cf7204-c9b0-3a6c-bb3e-d00e5169c4f2 | -2.6001 | -46.259102 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3807d831-4bde-3629-a2bd-11faa4a203f5 | -3.2667 | -44.177101 | 2024-11-17 00:28:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b189aff-768c-3622-bc56-e50a3c5b7c97 | -2.1105 | -46.4184 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08b9536f-ae39-351f-9fa2-1e6b2bcc71e1 | -2.7114 | -46.069599 | 2024-11-17 00:28:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9607b0d0-fcf6-3dbe-a72c-214f31ede0e9 | -12.4345 | -43.803101 | 2024-11-17 00:28:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bfcca7be-82d2-3797-b4d4-418b63a79812 | -1.8573 | -47.836399 | 2024-11-17 00:28:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d299fb2-a38d-30e1-9327-b3f0fbebf6b3 | -4.465 | -48.115898 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac8e33c-d136-3440-8772-ad2e3fec0a9a | -1.2003 | -51.768902 | 2024-11-17 00:28:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff3ce535-0042-3c06-b9df-43dd33117f93 | -2.6666 | -46.866001 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ce478a5-c91a-3c31-aae1-5d1713599f8d | -3.7886 | -46.0443 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6a02390-1e74-3824-a743-1139e5412da5 | -1.2557 | -47.099701 | 2024-11-17 00:28:00 | METOP-C | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fec8582e-5606-3362-85ca-d7824fb1d65c | -2.6282 | -46.562199 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2637d5b9-8429-318d-84db-91e99cd0b328 | -3.2842 | -45.598301 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb3249f8-d330-31b6-a102-6e4dcfaad001 | -2.4732 | -45.4361 | 2024-11-17 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e22cdf21-7201-3473-9628-c4d948cdd8a5 | -2.3275 | -53.577099 | 2024-11-17 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 517d13a7-8ec7-3779-b408-51ab8ee99ecd | -4.8181 | -42.902302 | 2024-11-17 00:28:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ab190ba5-c4e9-39f2-8b3e-7eca8a10c01a | -2.65 | -46.161999 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef4523de-c006-3381-afbc-241e944b25af | -2.9224 | -46.7216 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c31bcac7-7494-3891-9c6e-d775a13ec71e | -3.5246 | -50.517502 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a59838c-e927-3009-a093-fd2dbef7bdad | -2.8833 | -45.380199 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29b0f6b9-efb1-3bde-85b4-e2119eba24d4 | -2.3508 | -47.469299 | 2024-11-17 00:28:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5ed41cc-cd84-3c14-9dbf-5e1ce8bce50f | -6.8195 | -46.777 | 2024-11-17 00:28:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1a0a3dc-6779-31a8-a72e-35ef0226d983 | -2.8267 | -45.493198 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3c7f5f-87d5-33b8-9155-260b02f8804c | -2.156 | -46.121899 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 970b0425-500f-326f-851f-2da91a2e87da | -5.5886 | -45.210899 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3d9c134-3eb0-3492-9e09-62a367f81e69 | -5.4224 | -45.341499 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61566e9d-7bcc-3e2a-b6a2-002440ea9a5e | -4.2414 | -41.935398 | 2024-11-17 00:28:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b7bde70-47d8-3f92-8bca-139d04e85fb7 | -2.6749 | -46.856899 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc00f68d-0abd-375b-8623-4263ea6231bd | -6.4856 | -47.491798 | 2024-11-17 00:28:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fca6e85b-d147-33cd-95f7-8e05aeadcaed | -2.9179 | -45.171299 | 2024-11-17 00:28:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11bd1199-04fe-3008-b97f-efee95ba9891 | -3.0411 | -45.7528 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41b3022f-d76e-348c-92cf-f8e099aece9c | -2.1963 | -49.550598 | 2024-11-17 00:28:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b015b81c-c5ba-3935-9ccb-7a3d1251aa6e | -3.5243 | -50.241699 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e0731ea-34d1-3954-9d49-d69bd17fa8d7 | -2.4301 | -46.2827 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22b79d35-a136-3c4c-a505-1357955d62cd | -2.5554 | -47.2817 | 2024-11-17 00:28:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dc648ef-62ac-33bd-aca8-d833ae012e53 | -3.612 | -47.532001 | 2024-11-17 00:28:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
