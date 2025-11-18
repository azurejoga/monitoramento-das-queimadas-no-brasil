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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ec9707d-d7e1-383f-a116-50273880eb59 | -8.20008 | -49.7924 | 2025-11-18 04:50:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6728c2d-07d2-300b-a973-e42f62f5064b | -10.54071 | -47.99395 | 2025-11-18 04:50:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 977b825c-c5f9-3830-aa44-b822944a65ee | -7.21052 | -46.40058 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82c69838-e34e-3469-8683-af10bbf3c315 | -9.39473 | -48.45651 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5e78298-7951-3b63-8c16-187e2bb42168 | -12.01299 | -46.76387 | 2025-11-18 04:50:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 026d11b2-1a68-3193-bc0a-9bc72e208f92 | -12.23729 | -49.38253 | 2025-11-18 04:50:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c57e257-b154-3ea4-a498-e8cbe5eb6982 | -7.35395 | -46.20985 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06d27ddb-7f6e-32dc-a6a3-f7d7f1861ebf | -7.33886 | -46.17134 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aee9acaf-2b1f-3a34-819d-b09b866b6970 | -10.38385 | -47.28698 | 2025-11-18 04:50:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30605aba-51ad-3fcc-9f84-44701c2e2d1c | -10.72153 | -49.0702 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2975c5d0-4e88-3264-aa04-9a8bc665ee14 | -10.34871 | -48.92176 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c98c545-7dd2-31d4-8106-64044ebb1bfe | -8.31587 | -43.93705 | 2025-11-18 04:50:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4542381f-ae93-3952-9b96-76c49a564ba2 | -11.84399 | -47.60123 | 2025-11-18 04:50:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41223722-3a05-3c37-9d39-39a56050e928 | -7.86793 | -46.86972 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97cb67b1-d925-3d96-93ee-aef438d710a4 | -12.70266 | -46.77331 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88fc5f4e-ecc2-3ea2-8f18-d1ec30aab585 | -10.80364 | -48.09211 | 2025-11-18 04:50:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf8f6585-4af0-3f4b-86d1-c11cc7054a42 | -13.21361 | -53.76605 | 2025-11-18 04:50:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63e03551-5ccb-3210-bd52-da13b6b89aff | -8.47121 | -47.98566 | 2025-11-18 04:50:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebe591ef-8860-3d99-b0af-3adc1421b959 | -12.69941 | -46.79666 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 231b2dcf-3276-394f-b9cc-3ce1055c9161 | -9.02959 | -47.46141 | 2025-11-18 04:50:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07209d50-2610-3184-8fdd-8e3364ffe4d9 | -12.66331 | -46.74747 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8aa20683-2d78-3131-a861-7e3d84272322 | -10.29721 | -57.13884 | 2025-11-18 04:50:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69317190-85f4-393e-8883-687fe10db3ab | -11.20294 | -49.41143 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cbd2532-b2e2-37a2-9800-5d10fca7ac9a | -10.31185 | -54.2089 | 2025-11-18 04:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cee7039f-374d-3521-8771-fcde08a8a3dc | -10.3523 | -48.92232 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba2679c4-363f-33bf-a8fb-2aa9b691b708 | -9.399 | -48.45283 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c6c34dc1-9797-3e11-aac3-60f8126de500 | -10.80788 | -48.0896 | 2025-11-18 04:50:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c39c8e7a-b622-3995-92c1-d73648220329 | -7.92614 | -46.03379 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c168cedd-3571-38eb-9719-47ec4ab0b484 | -8.09557 | -46.05787 | 2025-11-18 04:50:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3782adb-9527-3c1f-a617-528dc7b00505 | -8.31514 | -43.94234 | 2025-11-18 04:50:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 586bcc12-692f-32ad-b099-43dced4136a6 | -9.40389 | -48.44493 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 13666af3-4641-3a52-9811-f3d97916fafc | -10.35947 | -48.92348 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b68cee27-05bf-348f-8149-e0d978131211 | -6.65328 | -51.29583 | 2025-11-18 04:50:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a48dcdde-cd2e-38cd-8a8a-7ef9d4adc55f | -9.72197 | -49.13463 | 2025-11-18 04:50:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25c4b904-5278-36a8-b54c-d60a30badd86 | -10.33727 | -49.63743 | 2025-11-18 04:50:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51d5b82d-befa-32f5-9c28-5670a922e6cc | -11.47885 | -48.55336 | 2025-11-18 04:50:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2713255d-71fd-3247-a064-2e65c8a9ac48 | -11.88542 | -44.20765 | 2025-11-18 04:50:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a61561dc-aaf0-3e24-9874-6a1bde21c14e | -8.54785 | -46.0488 | 2025-11-18 04:50:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5c382e6-c6a0-3741-b300-e4fab20d7b05 | -12.85312 | -41.48875 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f4e5c56f-a02f-3b01-a0be-a16dba34aae4 | -10.52157 | -43.9578 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbf0f866-55ca-3e44-ab00-0c2cf42b3b9d | -10.13314 | -49.15205 | 2025-11-18 04:50:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ac1491c-6bd7-3380-81a3-2626ac48981c | -12.85972 | -41.47136 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3ebf1455-427e-3586-a576-1240893df8a1 | -10.6586 | -49.37093 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15322f40-4bce-385f-a5a8-16d9091bc774 | -6.09583 | -51.27078 | 2025-11-18 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13e33c8e-a01e-3932-96ee-f839cc49e709 | -9.90207 | -58.43667 | 2025-11-18 04:50:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abd631c4-7afa-3d31-af8c-fc92ea15c832 | -8.46879 | -47.97643 | 2025-11-18 04:50:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d37af28-f720-3c96-9271-193fe78fda2a | -9.38871 | -48.4469 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c7cb61a-74fb-3071-934e-a4e37571cc71 | -9.06519 | -45.42243 | 2025-11-18 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42c54dc7-31e7-33e9-92dc-a82c7a8fad7f | -10.61689 | -42.31885 | 2025-11-18 04:50:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09f1c55d-003e-3ddc-8f41-dc3b0a6ae104 | -10.38249 | -47.28834 | 2025-11-18 04:50:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 835b88f2-ad7e-3e8d-9ef3-85aedca28ae4 | -8.30157 | -43.93449 | 2025-11-18 04:50:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12b1c9ba-f542-369e-ba3c-6aa4ac9151ed | -13.89876 | -47.49454 | 2025-11-18 04:50:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7481207-462c-3644-9c07-12582269711d | -12.85743 | -41.49041 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 96e5ec5d-a3e6-36c8-a20a-0ee1fee67d67 | -6.93945 | -49.66431 | 2025-11-18 04:50:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac4ff405-cafc-311f-977d-9c3b066b55c8 | -7.42826 | -45.19944 | 2025-11-18 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ddbcb48-4a94-3c35-850d-7107de3ef952 | -13.20195 | -48.31657 | 2025-11-18 04:50:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34cf320e-c3df-386f-912d-6e6a1b3cf9a1 | -12.41717 | -54.35819 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb89b828-063e-3bef-b34f-0ec1f0724906 | -7.86352 | -46.87071 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f8fe36f-c8e2-3ddd-b572-4c37dbd87444 | -9.44863 | -45.58344 | 2025-11-18 04:50:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae20f7a9-44c3-379b-bcf4-8a19a4eb5e4c | -7.94658 | -46.82221 | 2025-11-18 04:50:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0887a76-2718-3a7e-9ee3-fd2738fa2317 | -6.93306 | -45.34769 | 2025-11-18 04:50:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9dd14e6-2cd9-39a5-bd9e-56496f63ecac | -8.57522 | -46.49249 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2403b60b-a87e-391b-9ef4-7306bc119d55 | -6.92933 | -45.34343 | 2025-11-18 04:50:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fef6455c-1686-3db9-8726-259e1a1be5df | -10.84761 | -44.8825 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e64b144f-038e-3bca-872c-8420dcb97696 | -10.65801 | -49.37491 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f53d742f-71b8-343d-afe6-4f1b8170d495 | -12.69425 | -46.77212 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56c18df2-acef-3b2b-898b-6b1d35235243 | -8.57168 | -46.48837 | 2025-11-18 04:50:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38628ca6-3621-3559-9282-3a635d4b1dbc | -8.53905 | -46.05103 | 2025-11-18 04:50:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ec61141-8c88-32c8-9c8a-46ff7b2ca37c | -11.88023 | -44.20483 | 2025-11-18 04:50:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80b17e4a-5059-3bec-ad8a-67194fca0d0a | -10.34996 | -48.91346 | 2025-11-18 04:50:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ca7a8d-4d16-3ce5-98b6-ffb49102264e | -9.10108 | -47.78307 | 2025-11-18 04:50:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74a1b94d-78e4-3e9e-8add-0c772de4f50a | -12.85923 | -41.47545 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e7546e71-32a4-3f6b-b132-0a20cbeed963 | -7.54246 | -47.04905 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3353fc11-352e-3378-820e-3fc4c51b8ecf | -10.80743 | -48.09249 | 2025-11-18 04:50:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9a58bc0b-6c88-314f-a4fc-cf1c240ef3cd | -9.72963 | -49.1317 | 2025-11-18 04:50:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69af2ac5-ee20-3dc8-8769-9ea8543049e2 | -10.79877 | -47.64203 | 2025-11-18 04:50:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d562ddca-5247-388b-868e-da4ac0ae3245 | -11.663 | -44.7344 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d7ded371-762c-39cb-a015-ec7412ecef90 | -11.21002 | -49.41254 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f92bda5b-a748-3140-909a-aed2a06ecb9d | -12.06566 | -48.19822 | 2025-11-18 04:50:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e5803df-90dc-31ca-81ec-a1a27caa3964 | -12.23519 | -49.38058 | 2025-11-18 04:50:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa4bf8a8-d910-3940-9bc2-27c1f01664ef | -9.05967 | -45.43006 | 2025-11-18 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bccea9bf-8ed9-3770-83b8-d52edfbbf888 | -10.51901 | -43.96657 | 2025-11-18 04:50:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3af6ea4c-fabe-3708-b6ca-d15e49ea5a63 | -10.74695 | -45.14753 | 2025-11-18 04:50:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d67aefba-6030-3de1-b7d3-c99cf04834c2 | -7.41488 | -42.75804 | 2025-11-18 04:50:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16ee3e98-1ac0-3045-a7b0-47280183f2ac | -7.43563 | -48.93836 | 2025-11-18 04:50:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9021fce-4d8c-3507-9381-d3e112316c8a | -7.68034 | -47.52454 | 2025-11-18 04:50:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35de9538-bb7e-3544-95f0-775b460da77a | -12.66277 | -46.75143 | 2025-11-18 04:50:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cb3eebf-9bfa-35be-8e14-65f73647b8fb | -11.21296 | -49.41713 | 2025-11-18 04:50:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faa22627-1dff-3b74-899e-2c901be1e03c | -12.73263 | -45.43205 | 2025-11-18 04:50:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4310419a-117b-3e84-a3d3-459ef3fc320d | -7.08059 | -52.61817 | 2025-11-18 04:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e3cbf45-d0ba-35de-a0aa-14fc6b05e6e1 | -9.39536 | -48.45226 | 2025-11-18 04:50:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 29063c37-87eb-3f18-9cdc-263d0a9ba0d6 | -8.29533 | -49.3064 | 2025-11-18 04:50:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 517e1f15-40fe-350a-83ef-e1f89095f129 | -11.88047 | -44.207 | 2025-11-18 04:50:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 975c02bd-49ab-3335-ad97-0d1410e458e6 | -7.42885 | -45.19536 | 2025-11-18 04:50:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31e220d2-ba0b-369c-8df1-bc495a13c06c | -10.91899 | -49.41237 | 2025-11-18 04:50:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0722fbe4-6d92-3370-b018-7129dc181baf | -12.85167 | -41.48761 | 2025-11-18 04:50:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 604d5485-81e7-3b37-aa21-3c9fac83c3f5 | -7.54631 | -47.04963 | 2025-11-18 04:50:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57c94668-5aef-3a3b-b754-826ad414b4e3 | -12.89944 | -54.72169 | 2025-11-18 04:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12278995-b22c-36b7-b30e-65a0f6a51848 | -8.8623 | -47.32065 | 2025-11-18 04:50:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd51edf6-3a8f-38d5-a5dd-d6ea94fd78ae | -6.93362 | -45.34379 | 2025-11-18 04:50:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README45.md)
