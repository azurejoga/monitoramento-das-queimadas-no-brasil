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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb714950-28e6-3523-815a-d2d248969e04 | -7.3406 | -72.90264 | 2024-10-13 06:44:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ffb8132-9f70-34dc-8170-3fced41fb80d | -7.34101 | -72.89967 | 2024-10-13 06:44:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd85ad8d-3993-35d4-a078-f6f8ddd222dc | -7.41441 | -72.81907 | 2024-10-13 06:44:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15c278bf-57d2-3aee-8e2e-702146654021 | -7.41952 | -72.81979 | 2024-10-13 06:44:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32d95635-11d4-3ac0-94ae-e357be22d150 | -7.42462 | -72.82053 | 2024-10-13 06:44:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10cce6fe-e0fd-3aae-b580-6554a027374e | -8.00584 | -72.32258 | 2024-10-13 06:44:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f61e65f-4615-380a-9ade-023a79c710f4 | -8.0063 | -72.31924 | 2024-10-13 06:44:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20af1d95-5a7d-365e-b809-e8f5242166c9 | -8.00799 | -71.38778 | 2024-10-13 06:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d87fbda-f8cd-38b4-ae65-59817805faa0 | -8.01367 | -71.38858 | 2024-10-13 06:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 711c7f5b-dff7-3136-b616-c6773fdbbb88 | -8.02396 | -71.39803 | 2024-10-13 06:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24961b43-afbb-3777-b18d-e54fd4c7875a | -8.02448 | -71.39411 | 2024-10-13 06:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddebb2ba-26f4-3ee9-90a3-cbcd4ca64ab8 | -8.03015 | -71.39491 | 2024-10-13 06:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5fd5a38-10c6-3cde-8cd4-abbec45d5591 | -8.10972 | -71.33684 | 2024-10-13 06:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aed396f8-5c6a-328e-9df3-010c28151386 | -10.46115 | -69.69652 | 2024-10-13 06:46:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e030afd-b028-3161-ba11-e5e403b0ea28 | -17.6474 | -56.2876 | 2024-10-13 06:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| dfc832a5-6728-3e48-a350-5226279ffc80 | -9.7359 | -64.2295 | 2024-10-13 06:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4fddc542-3c69-3a67-8402-4bad418bef34 | -17.964 | -57.3843 | 2024-10-13 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 76026493-f603-38a7-8f20-4265decc4c94 | -18.2155 | -56.5457 | 2024-10-13 06:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.9 |
| f2ea68ee-e699-3eef-a44b-49c09c2f917d | -9.7359 | -64.2295 | 2024-10-13 07:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2b03c307-c5c2-347f-87fd-4c314725ae6e | -15.6419 | -59.9767 | 2024-10-13 07:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9803a783-f771-3ad7-928d-dac7fe05d77f | -17.02 | -57.4153 | 2024-10-13 07:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 8fe91c96-2a86-332d-8c6e-33e72143f8c8 | -17.0197 | -57.4358 | 2024-10-13 07:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 14eae435-2ae7-3760-ad57-541ccc849d5f | -17.0004 | -57.4176 | 2024-10-13 07:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| ddef8249-b71b-3415-b970-a038885448f5 | -17.0001 | -57.4381 | 2024-10-13 07:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 5a7b8dd7-4e40-30de-b610-a61d32dc2a07 | -17.1954 | -57.4767 | 2024-10-13 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 2ac12195-65ca-3278-bc77-e606e0122725 | -17.1957 | -57.4562 | 2024-10-13 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 29d4f877-b8ee-3dcd-b9d3-4605143199d5 | -18.2364 | -56.4806 | 2024-10-13 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 41c1374c-1358-3715-b345-ca3395f39b4a | -18.2166 | -56.4832 | 2024-10-13 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 692b16ba-b27d-3e26-8ea3-b64fa66c0eac | -18.2155 | -56.5457 | 2024-10-13 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 935137a0-10ec-3912-99d0-07ac7b443f3c | -18.2151 | -56.5665 | 2024-10-13 07:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 3ff81b98-cf2d-33b1-a39e-53f3a3a4ec39 | -7.34953 | -72.90092 | 2024-10-13 07:14:00 | AQUA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc5fa647-aea4-38ac-a7a4-8d128cc4736a | -9.7359 | -64.2295 | 2024-10-13 07:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f093095c-c6bf-3550-9bbd-f73dfda21c02 | -17.9057 | -57.3297 | 2024-10-13 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 3f3f794e-5e51-375d-95d5-661e195095c4 | -17.9248 | -57.3685 | 2024-10-13 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| c96d3db2-011b-3743-bb5b-daa0bec44df0 | -17.9251 | -57.3479 | 2024-10-13 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.8 |
| d0727bb2-fce1-388e-b219-f66244e95ca3 | -17.9254 | -57.3273 | 2024-10-13 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.8 |
| a46449c4-519b-35ce-aa65-5d43201b6d3d | -17.964 | -57.3843 | 2024-10-13 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.9 |
| fe44c893-bf9e-3e0d-a66a-3ed6f0bf7248 | -17.9053 | -57.3503 | 2024-10-13 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.7 |
| 87f13559-40ef-381d-b669-3c710433f985 | -17.905 | -57.371 | 2024-10-13 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 46ecc88b-ca4e-3a9e-854a-efdc615071d0 | -9.7359 | -64.2295 | 2024-10-13 07:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b687152a-c4a6-31cb-9c10-7033544626c6 | -17.196 | -57.4357 | 2024-10-13 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 0bb5deef-be34-3b31-a713-83c1cb537ba4 | -17.1957 | -57.4562 | 2024-10-13 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 152.5 |
| 287e3a57-81c6-3329-8efc-a6f58bb777cb | -17.1954 | -57.4767 | 2024-10-13 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 60c14d80-46b5-32e0-b985-3582073034d1 | -17.1764 | -57.438 | 2024-10-13 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 50781544-3915-3868-9e29-e1407a4491ab | -17.1761 | -57.4585 | 2024-10-13 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| f2fc8018-ab2d-3951-b2b1-b7f8801d559a | -17.1758 | -57.479 | 2024-10-13 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| dcda6b33-0f9c-301a-86a0-6990bf16bd22 | -17.6672 | -56.2851 | 2024-10-13 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 5c4efa08-395c-370a-90f9-67a983ff5aa4 | -17.6478 | -56.2668 | 2024-10-13 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 36cdff6f-40ac-3d5f-b4bd-20895eb40f80 | -17.6474 | -56.2876 | 2024-10-13 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.5 |
| c5394bde-4e0a-37c0-affe-9ec859a87c7d | -17.6471 | -56.3084 | 2024-10-13 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 98c8ff14-e4be-3f7c-999c-9d9af798ecd1 | -17.906 | -57.3091 | 2024-10-13 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 4c7ab169-46ad-3d9a-9b32-70ec137f51f6 | -17.9057 | -57.3297 | 2024-10-13 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.2 |
| 7d7cb471-179d-39f6-a901-b6749ee892f1 | -17.9053 | -57.3503 | 2024-10-13 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| eb60694e-536b-3b39-904a-af92f9aed89a | -17.905 | -57.371 | 2024-10-13 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 4ac20f03-8b0b-3e43-9ba5-c9f26f282894 | -17.8863 | -57.3115 | 2024-10-13 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 2d850180-d3b0-3535-abc4-571d6ede097b | -9.7359 | -64.2295 | 2024-10-13 07:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9a9a6476-6ec2-3168-830a-3cfc59de0d67 | -9.8551 | -60.3159 | 2024-10-13 07:36:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 5b831e8d-17fc-3647-9c8e-c2923cea84ae | -12.4792 | -63.0159 | 2024-10-13 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 59fcd0a2-7559-3b49-a05b-df61e9c4e3d5 | -12.4794 | -62.9967 | 2024-10-13 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 167e4622-f671-3f89-9a67-df5128ddd587 | -12.4981 | -63.0148 | 2024-10-13 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| de45db8b-a280-3f2d-9968-5eaabb4c942b | -12.4983 | -62.9956 | 2024-10-13 07:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 78091022-7078-3c9a-9cd9-5ea117a6c608 | -16.9995 | -57.4791 | 2024-10-13 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 5d49ed2f-915a-3e04-a7d5-f983d85dcf5c | -16.9998 | -57.4586 | 2024-10-13 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 48bf53a5-a333-3d5c-9b13-35655283ffe8 | -17.0001 | -57.4381 | 2024-10-13 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 6c5df8f2-0da8-388d-91d5-0ff21b1d2334 | -17.0197 | -57.4358 | 2024-10-13 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 124436dd-0e47-37c0-b364-1f76e770d4a2 | -17.1758 | -57.479 | 2024-10-13 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 7ac1c69c-74cc-37fa-93af-a0d9bc6bb3b0 | -17.1761 | -57.4585 | 2024-10-13 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 05398131-6549-3aa7-8dc7-cc83e5311116 | -17.1764 | -57.438 | 2024-10-13 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 43bd5045-7c33-3689-99ce-a09edf036d54 | -17.1954 | -57.4767 | 2024-10-13 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 4c817737-0d2a-397e-a447-9f16cc031408 | -17.1957 | -57.4562 | 2024-10-13 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 095e30d8-97f4-37a7-a38e-dff32f0d0d59 | -17.6474 | -56.2876 | 2024-10-13 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| c5fccf6e-ee3b-3bb1-9959-a2be5d59c5c3 | -9.8364 | -60.3169 | 2024-10-13 07:46:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b5d086c3-9dd7-3d43-b0e3-a1b392e6ab0f | -9.8551 | -60.3159 | 2024-10-13 07:46:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9144b0d1-66d0-3964-9965-cef181ece381 | -12.4792 | -63.0159 | 2024-10-13 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| bf9c7d36-3305-3b5f-a0cc-e21a51e19baf | -12.4794 | -62.9967 | 2024-10-13 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 87570e9e-c131-3ed5-b922-9cb3087be8b6 | -12.4981 | -63.0148 | 2024-10-13 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 93017143-7d4a-3ddc-b650-c10670073132 | -12.4983 | -62.9956 | 2024-10-13 07:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 16ac79c9-64f4-3863-9816-b092f8adfc94 | -15.1817 | -59.7396 | 2024-10-13 07:46:32 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f6f973f3-25b3-3217-9d4f-d8925f448f46 | -15.1819 | -59.7197 | 2024-10-13 07:46:32 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 6b79c004-f083-3bb3-a775-92ca47af2a4f | -16.9995 | -57.4791 | 2024-10-13 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| b8980fbb-000f-386f-8613-b038e4e50a3d | -16.9998 | -57.4586 | 2024-10-13 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 819989be-7925-349a-8a73-c4a79deff49e | -17.0001 | -57.4381 | 2024-10-13 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 170.7 |
| d78d41ec-e456-3454-94c7-f30a785a48b9 | -17.0004 | -57.4176 | 2024-10-13 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 37749b2f-abef-3e60-8388-53af1cc70e8b | -17.0194 | -57.4563 | 2024-10-13 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 82f40680-8593-3b23-b6f0-d0dd474de059 | -17.0197 | -57.4358 | 2024-10-13 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 144.9 |
| 610a9461-8ec3-39e9-954b-025831cf981c | -17.1758 | -57.479 | 2024-10-13 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 35d1e913-c522-347c-8931-55eabb444b1f | -17.1761 | -57.4585 | 2024-10-13 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 060d8274-41db-35d3-bb31-4d46dd5193b4 | -17.1954 | -57.4767 | 2024-10-13 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.9 |
| 9a7db575-29ac-3d36-958f-d79f5acbbff8 | -17.1957 | -57.4562 | 2024-10-13 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.4 |
| 2c79505e-3d13-333c-860a-08f716c29f5a | -17.196 | -57.4357 | 2024-10-13 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 3126346c-0768-3b48-a494-04ba280648a0 | -17.6471 | -56.3084 | 2024-10-13 07:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 8ca52d25-afd6-3e33-817f-d62890085497 | -17.6474 | -56.2876 | 2024-10-13 07:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 187.6 |
| d6f300ef-fd4a-3bfb-801e-ad52b8c243f8 | -17.6478 | -56.2668 | 2024-10-13 07:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 5318f69b-d890-3e9d-b18d-02ca2f9dfbb3 | -17.6672 | -56.2851 | 2024-10-13 07:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| dee643f1-726c-3e02-b289-3605eee66dc9 | -18.2357 | -56.5222 | 2024-10-13 07:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| cea301a6-4f64-35fb-b2ba-7f8b1165b383 | -12.4794 | -62.9967 | 2024-10-13 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 4e3315cc-e9f6-37c9-8136-1f2ba0734667 | -12.4981 | -63.0148 | 2024-10-13 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 0b050f0d-55d6-3014-a8a1-44ca3faedd67 | -12.4983 | -62.9956 | 2024-10-13 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 0d7e9256-f77e-351b-b9ce-9f2ee093e838 | -12.4792 | -63.0159 | 2024-10-13 07:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 17f5d955-2d44-38a4-ac73-12ada9199a62 | -16.9995 | -57.4791 | 2024-10-13 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |


[Clique aqui para ver as próximas entradas](README115.md)
