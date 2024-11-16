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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0cecedd-a55c-370a-8129-5b87a8f6f7cd | -16.0466 | -60.119 | 2024-11-16 14:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 57fc1283-4429-3bf9-bb86-fc060c4ca2ba | -4.0244 | -44.6677 | 2024-11-16 14:00:00 | GOES-16 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 3ae03cca-c9cb-3e82-91ce-5d65ace68bd1 | -3.6659 | -42.2492 | 2024-11-16 14:00:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 268.7 |
| 82f8e1a6-63ac-339c-9da7-ad3e30a8759e | -3.0161 | -45.3004 | 2024-11-16 14:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 0b51abb2-38fe-3aef-814f-b0f0e944d119 | -16.9381 | -57.6495 | 2024-11-16 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| dac46e55-1ce5-3385-b2d1-652820fc3f01 | -16.9773 | -57.6451 | 2024-11-16 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 1e119212-26d8-3bf2-94dd-2fd7c4d31e73 | -16.9384 | -57.6291 | 2024-11-16 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 234.8 |
| 81979445-2687-3f56-b896-6feaade92fa5 | -18.317 | -57.5465 | 2024-11-16 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| a7ee61d9-4ac6-39b2-88f0-e663a02e9eed | -16.9388 | -57.6086 | 2024-11-16 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 91b355db-cfee-3d44-9d5f-b394e4df90d2 | -19.5426 | -56.908 | 2024-11-16 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 95fe6b13-ae31-37e0-a9c0-c744e27c5740 | -4.8209 | -42.9122 | 2024-11-16 14:00:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 178.7 |
| f66dc6c7-9396-38aa-a09c-1cb2361ecdc6 | -2.2813 | -48.4223 | 2024-11-16 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 4cdab0a1-ff87-39d9-a5aa-ae684e053773 | -2.2814 | -48.4008 | 2024-11-16 14:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e52fd40f-1a3a-33b5-bd76-5508b12f4cac | -0.7837 | -49.4704 | 2024-11-16 14:00:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f0d0d769-a2b2-3332-83d5-962c4b2b3e37 | -3.66 | -42.24 | 2024-11-16 14:00:00 | MSG-03 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ddf10210-dbc5-327f-965d-5c0519e10b18 | -3.66 | -42.29 | 2024-11-16 14:00:00 | MSG-03 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9615fcb-1d0d-3ccd-83bf-d6067b8a6f63 | -3.6659 | -42.2492 | 2024-11-16 14:20:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 160.0 |
| d2beed6f-069f-3526-a335-23a9308b867b | -1.0258 | -47.7541 | 2024-11-16 14:20:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d1732d63-d90b-3b28-adcf-473a7eba6970 | -16.9388 | -57.6086 | 2024-11-16 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| a5dc6d5b-bc1d-378a-9ec9-0d2139363fc8 | -2.1021 | -46.532 | 2024-11-16 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 321f2992-bc82-360c-bb05-d4bacb0a9e44 | -23.9306 | -54.0564 | 2024-11-16 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 106.7 |
| 8ba548ec-7417-3860-871d-bff2005d35c9 | -4.8209 | -42.9122 | 2024-11-16 14:20:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 3f06c71a-9695-3964-8987-623ba8da791e | -17.5685 | -57.4735 | 2024-11-16 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 2bbb2230-dab0-354a-9c60-1e82f7c10df7 | -19.5225 | -56.9108 | 2024-11-16 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 2557911c-38f6-3fdb-b02b-5820f831aca1 | -15.9028 | -59.254 | 2024-11-16 14:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 85c071c8-c42c-30b2-acd8-3d5b0a715f36 | -3.7867 | -43.9011 | 2024-11-16 14:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 1f323a04-205e-3b07-b3c7-7059e84f20ad | -16.9384 | -57.6291 | 2024-11-16 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 233.0 |
| d080fd8b-5cbe-3cb1-8df9-fc4ff7d31ba4 | -19.5426 | -56.908 | 2024-11-16 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 9ca2c255-1e45-3f1b-9918-7a2355499644 | -4.0244 | -44.6677 | 2024-11-16 14:20:00 | GOES-16 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 75fbebf0-8d76-38d8-b7d5-e1c784d9a33c | -23.9512 | -54.0744 | 2024-11-16 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 12c58534-6b76-3999-827c-63c8024a1331 | -3.7468 | -44.362 | 2024-11-16 14:20:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 687a60b2-4abb-3fad-85df-8339092f6055 | -16.9381 | -57.6495 | 2024-11-16 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| cb7953bc-9ac0-3199-9be9-9c5ece425578 | -17.5692 | -57.4324 | 2024-11-16 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| aeffd93a-8abd-3aa0-9690-645a4f0e1e7b | -15.9222 | -59.2521 | 2024-11-16 14:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 2460e670-e325-329c-b02d-24058fb936ee | -3.7597 | -42.1969 | 2024-11-16 14:20:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| ecda7751-8431-3727-89ae-327211e87fdd | -2.5119 | -45.9888 | 2024-11-16 14:20:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c87e28e5-29d7-3c86-9713-c08b954c281f | -16.0466 | -60.119 | 2024-11-16 14:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8b929592-8844-3456-b0ee-7e2b1d41d21b | -2.2814 | -48.4008 | 2024-11-16 14:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 49b3d34d-ab4e-3a04-91cb-ac6a5e310dc9 | -3.6391 | -43.6313 | 2024-11-16 14:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 16bfeccf-a686-342c-9446-20cd866d693c | -18.317 | -57.5465 | 2024-11-16 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 3f606552-44a4-38db-8eb3-498902b366ef | -0.7837 | -49.4916 | 2024-11-16 14:20:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 95663c23-06d6-39d5-9249-f6585986daec | -3.6472 | -42.2501 | 2024-11-16 14:20:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 169.0 |
| 90290150-ca84-3252-87dd-e32a88d26f8b | -4.8022 | -42.9134 | 2024-11-16 14:20:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b9d173e2-b881-3a70-9523-36a76dc411f4 | -0.7468 | -49.4707 | 2024-11-16 14:20:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c7c2d6f7-383c-3488-b552-cf29ab5ed155 | -3.6392 | -43.6081 | 2024-11-16 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c2c7ed30-9d88-356d-a948-cb7a6df438e0 | -0.6547 | -49.3866 | 2024-11-16 14:20:00 | GOES-16 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 585750cf-afc1-38b0-ba8a-83d357975b2e | -17.647 | -57.4846 | 2024-11-16 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| c0198e3a-3338-3bfa-9df6-ee6399dbb1d1 | -16.9577 | -57.6473 | 2024-11-16 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.2 |
| 2ffd1883-95b1-379d-8bf6-e44c23de48c0 | -0.6547 | -49.4078 | 2024-11-16 14:20:00 | GOES-16 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 59fb1a24-31e1-3a5a-9069-a3ed6780b5ea | -0.7837 | -49.4704 | 2024-11-16 14:20:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 9cb30bb7-72aa-3de4-a50a-07bc5e6b4cec | -0.2493 | -48.5142 | 2024-11-16 14:20:00 | GOES-16 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 7c70efdd-c2fd-3085-97f7-c547d68ba542 | -17.2353 | -57.4311 | 2024-11-16 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 2fa91fc0-c2a9-3ba5-8a82-bedcc3991d7e | -16.9388 | -57.6086 | 2024-11-16 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 54be751b-b1f8-3596-bcf8-841f920a5583 | -23.93 | -54.0787 | 2024-11-16 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 73.3 |
| fa433266-1d46-3eb9-8538-37f5183c4ca3 | -3.7867 | -43.9011 | 2024-11-16 14:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d6984646-5817-37c3-ba65-394d9eb490e0 | -4.8022 | -42.9134 | 2024-11-16 14:30:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 849b02ac-6b34-33b4-93bb-a0a0483a87c3 | -19.5426 | -56.908 | 2024-11-16 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 658c77f0-6b7c-3d62-a58b-076dfedafb70 | -17.5678 | -57.5146 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 79fdb85a-08c0-3fcd-8b9a-cc2ca3783073 | -3.6233 | -43.1443 | 2024-11-16 14:30:00 | GOES-16 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 804b141c-f8be-3325-92ae-e3c8d0483771 | -19.5422 | -56.9289 | 2024-11-16 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 9e8b4e0e-1619-3b9c-9593-a291ad60fca7 | -0.7837 | -49.4704 | 2024-11-16 14:30:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 4e9a80cd-804f-39f2-81da-fa0647f5f259 | -2.6781 | -46.1837 | 2024-11-16 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| d8d84dde-bb71-3f26-8210-33ba70050b79 | -17.5869 | -57.5533 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| a4344db5-1ae6-3d11-9ca4-c32aa5b47297 | -17.5675 | -57.5351 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| 0184edd4-c275-3d04-89d9-dfb157086426 | -17.5672 | -57.5557 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 53cf3ff8-92fb-3196-89a4-f5438dba46b9 | -17.293 | -57.5062 | 2024-11-16 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 4130e601-5d2a-3043-9492-3c9d027b7283 | -16.9577 | -57.6473 | 2024-11-16 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| c915152b-b041-37f3-a065-5d283ec736d4 | -17.5879 | -57.4917 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 360144ee-d17d-33b7-b626-05400ed59fa2 | -23.9306 | -54.0564 | 2024-11-16 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 117.2 |
| b7f7d32a-5c10-3fa1-9411-140c3a768a85 | -0.6547 | -49.3866 | 2024-11-16 14:30:00 | GOES-16 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 26c6ffa8-0158-3426-abc1-138009541203 | -0.7837 | -49.4916 | 2024-11-16 14:30:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| c907d240-f9da-3649-8f63-346e1471332f | -4.8209 | -42.9122 | 2024-11-16 14:30:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 9512758a-3193-3edd-bfb4-b963d50b005d | -17.5685 | -57.4735 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 931cc2a2-5579-3a3d-bddf-78a50acefb82 | -16.9413 | -57.4449 | 2024-11-16 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 0da741ed-ba5f-32bb-bc43-f1f0f1b991bc | -17.5481 | -57.517 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 46159f48-f66c-35c1-aba3-f286262ddd7b | -0.2493 | -48.5142 | 2024-11-16 14:30:00 | GOES-16 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 2569fd9a-805a-3157-9a58-c56a7d2f8813 | -1.5629 | -47.3768 | 2024-11-16 14:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9343de9c-cff3-3733-b466-fe8ce9f6ddb0 | -16.9384 | -57.6291 | 2024-11-16 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 225.7 |
| 7e752024-edb8-3a85-a901-14b668a2016e | -23.9729 | -54.0478 | 2024-11-16 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 985e6baf-c402-3dff-ab0a-b7a3f9890140 | -17.5478 | -57.5375 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 50e6a268-5d95-30e5-8335-ddf12bfbab3f | -16.9773 | -57.6451 | 2024-11-16 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 82157a97-cf21-3d9a-976a-cff929214858 | -3.7654 | -44.3611 | 2024-11-16 14:30:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 895734ad-d8a6-36c9-87e3-4d9f7d088dd2 | -23.9517 | -54.0521 | 2024-11-16 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 106.3 |
| a3d1ecda-7d8e-3bcb-8650-f96914853076 | -3.7597 | -42.1969 | 2024-11-16 14:30:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 994c3868-354c-3573-8299-4a5e1f25d35b | -16.9381 | -57.6495 | 2024-11-16 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 6a1e9e16-3128-3d70-a251-1149bba6a549 | -17.5862 | -57.5944 | 2024-11-16 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 264.1 |
| 16ccc086-78ed-3710-91f7-8dce27a0896b | -3.7468 | -44.362 | 2024-11-16 14:30:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 221d6620-d349-326c-843f-fa71ca622e92 | -1.0074 | -47.7543 | 2024-11-16 14:30:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |


