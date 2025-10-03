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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c10f5b61-5bab-3b2d-8aad-54443ef1f5fc | -7.9137 | -43.5369 | 2025-10-03 00:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| d22f8e51-b341-3215-b751-d35d2ef0a97e | -4.669 | -45.8066 | 2025-10-03 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 387.6 |
| 1a5e9cda-4cd1-32b5-983a-55146bcf84b7 | -7.2576 | -48.4915 | 2025-10-03 00:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f99929cb-386d-3d57-8f4f-0fd796fbe0c8 | -5.3665 | -47.2063 | 2025-10-03 00:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 15a04fdb-a6e5-3347-bef0-cef73f216a0d | -17.5956 | -46.6648 | 2025-10-03 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 186.7 |
| d9c2c8eb-4251-338c-a349-10f4878bce88 | -11.1631 | -43.4054 | 2025-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 27cc238d-e635-36f6-ab52-f177b96bd1ca | -4.6504 | -45.8077 | 2025-10-03 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 201.1 |
| 9e195499-def4-35f7-93f5-9dfac1d13829 | -3.9331 | -47.5655 | 2025-10-03 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7166cbf1-1509-3695-a956-8992819777e4 | -8.6138 | -54.976 | 2025-10-03 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 69d46c73-f949-3791-8b32-ee119bf218fc | -11.1444 | -43.3845 | 2025-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 0178c5dc-1f85-3141-81c6-55d2c87fe38b | -9.9182 | -43.7212 | 2025-10-03 00:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 7ad86984-ec76-3cc7-b0d8-c568e1edde5a | -12.6131 | -46.9725 | 2025-10-03 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 630b2a57-f8f1-398e-958a-2d95ea2e1931 | -9.8991 | -43.7237 | 2025-10-03 00:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 65d973d8-ac28-3ea5-ae84-259b587c2daf | -9.8772 | -47.8103 | 2025-10-03 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| f5530053-92c1-35bb-8670-720fdd088500 | -5.6361 | -43.9258 | 2025-10-03 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 5398124a-c34b-3745-9da3-45cc7a93c5e3 | -7.7743 | -42.6103 | 2025-10-03 00:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| f7e1d758-41f5-3673-8591-cb29e9c2699a | -5.3849 | -47.2271 | 2025-10-03 00:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 155.2 |
| d3588f8e-5718-3f77-b44f-0230f4bd4ddf | -14.7083 | -43.8869 | 2025-10-03 00:40:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 68.4 |
| cc63991e-9958-34a7-989a-d1c2cd408737 | -7.7557 | -42.5885 | 2025-10-03 00:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 152.1 |
| cab9bdff-97d5-3b90-9d12-0b2648236df8 | -14.8961 | -46.8575 | 2025-10-03 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 8413c1cd-1c38-3dc7-8c85-9a173c5d77d1 | -3.9517 | -47.5647 | 2025-10-03 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1024f9f5-2714-35a7-8881-09f10bfe7922 | -5.6363 | -43.9027 | 2025-10-03 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 44ef5371-b5f1-3a48-8c11-0e1cc2c1e3b3 | -5.655 | -43.9013 | 2025-10-03 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| caa89186-a938-398f-b655-578d92917e25 | -14.8966 | -46.8346 | 2025-10-03 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 30a703e4-dd70-3029-bf99-b20769b8e606 | -12.6323 | -46.9697 | 2025-10-03 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 78bdd67b-1042-3b83-a9b2-3b15d826a39a | -6.2406 | -45.365 | 2025-10-03 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 316516f0-fde0-35be-97ca-126482336a03 | -10.948 | -51.0846 | 2025-10-03 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 1c698888-cae0-3dde-ac72-de72702b1186 | -5.3851 | -47.2052 | 2025-10-03 00:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 7ccc79f0-7f47-379c-a3d1-11bead535914 | -5.6363 | -43.9027 | 2025-10-03 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 216.9 |
| e252ef9a-5d0a-342d-843a-a839a7caa020 | -5.8657 | -43.3981 | 2025-10-03 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 03b883a1-0e04-3cce-b333-643de9aeed9c | -14.9538 | -46.8931 | 2025-10-03 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3bd6c391-a3a5-36ab-9c44-4cf0949d3820 | -13.1349 | -47.8597 | 2025-10-03 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8ead1c0f-cd63-3e17-9d6d-7e4a2d362d5a | -14.7083 | -43.8869 | 2025-10-03 00:50:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 406d3c08-964a-3ce8-8d3b-88e691f6d3fb | -7.8948 | -43.5389 | 2025-10-03 00:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2e137b93-3d35-35c4-bc5c-66d00b767c87 | -6.0605 | -44.6061 | 2025-10-03 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| fc69d07c-8a81-3cd4-9936-9f49780b4cf2 | -13.1345 | -47.882 | 2025-10-03 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f247d539-4f93-3787-852a-f92566e9c44d | -10.2587 | -50.3478 | 2025-10-03 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| ec346a2f-51c9-31aa-be59-4a7ef4d5c5e5 | -5.3849 | -47.2271 | 2025-10-03 00:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 09d08d1c-1f78-3f8e-80c2-b907a0b70a2c | -9.9365 | -43.7657 | 2025-10-03 00:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 219e584e-0149-3cc8-aef7-a861138b60d2 | -14.8961 | -46.8575 | 2025-10-03 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 133.1 |
| b3480f33-d42d-383f-aed9-6a6d1afe19c9 | -3.9517 | -47.5647 | 2025-10-03 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 660baf41-8b46-349c-adae-40f3fc1b83e2 | -6.2406 | -45.365 | 2025-10-03 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 191.6 |
| f39b8584-c2ff-3a5d-9273-ec4cd2ec9da6 | -12.6323 | -46.9697 | 2025-10-03 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 67a13ba5-5d55-3432-8661-78cc0ec07dcd | -13.7764 | -47.5617 | 2025-10-03 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 42f5935f-0fc7-3183-8f1c-1b3d57a24351 | -4.669 | -45.8066 | 2025-10-03 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 394.6 |
| 1ab0a60d-db48-3acf-b5e3-74e5625fa660 | -4.6505 | -45.7853 | 2025-10-03 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 249.1 |
| b5d61f56-00b6-39b5-9424-a6ece6e7abee | -4.6692 | -45.7842 | 2025-10-03 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 344.4 |
| 2205f427-ee57-3ecd-8ce7-92fbcffb121e | -10.2584 | -50.3692 | 2025-10-03 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 2095303e-1862-3e26-bb19-dbf6bae2867f | -9.8991 | -43.7237 | 2025-10-03 00:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| d8972a73-5607-32f2-aa91-754c75bc83ca | -6.0418 | -44.6076 | 2025-10-03 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c1553ed3-647b-31b1-9db9-d4c5812ba7a8 | -7.2578 | -48.4699 | 2025-10-03 00:50:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a18f333b-c6dc-3048-8451-5a895059a98a | -6.0416 | -44.6304 | 2025-10-03 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 779e723d-f18c-39a4-a9c0-eb02030530c3 | -7.9137 | -43.5369 | 2025-10-03 00:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fe16f875-69b7-3ddc-85d5-bfc71e740e89 | -11.9163 | -46.2817 | 2025-10-03 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4570485b-e15b-334c-80ae-2ff4eddd7398 | -12.6135 | -46.9499 | 2025-10-03 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 67e40da4-bcd4-32d4-a96e-ba300f9f6f88 | -11.1444 | -43.3845 | 2025-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 99.6 |
| d578a6bf-16b0-3f7c-b9ce-d89c82ce44d2 | -9.9369 | -43.7422 | 2025-10-03 00:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 3f3701db-f3db-37d0-bcf4-de03bd8ce885 | -4.6504 | -45.8077 | 2025-10-03 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 738be099-bb85-326d-bedf-6787d794b4bf | -5.8655 | -43.4214 | 2025-10-03 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 44745700-51e4-3471-b98b-d2bbafcf4c93 | -3.9331 | -47.5655 | 2025-10-03 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ee818136-9867-3534-811c-11cc88aaa175 | -8.6324 | -54.9747 | 2025-10-03 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4f991929-ff39-376a-ae18-9a2bf7a97f1f | -14.9342 | -46.8965 | 2025-10-03 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 80958e5d-7708-37e2-8e33-2bead2f15998 | -5.3665 | -47.2063 | 2025-10-03 00:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f3f69d99-b3a1-3eac-b190-73d9860b42fe | -17.5756 | -46.669 | 2025-10-03 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 1c9a53dc-f7c5-3521-8f14-5bb2aaaba2a0 | -19.7244 | -45.8804 | 2025-10-03 00:50:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0185b781-3d8e-30eb-a802-7994d983718e | -5.8469 | -43.3995 | 2025-10-03 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ab11d249-1c90-3fb7-b7ac-30047e63b1cd | -5.655 | -43.9013 | 2025-10-03 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 720bb50f-99df-3b3f-8354-a8d804d2bbfc | -6.2408 | -45.3424 | 2025-10-03 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 507017e6-9f9b-3f86-99a3-345d647f9bb6 | -17.595 | -46.6882 | 2025-10-03 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 78ff5073-186a-3491-84a9-e6f76df6a673 | -14.8966 | -46.8346 | 2025-10-03 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 190.8 |
| ba62e58e-8496-39ca-8cb3-3aa87758f1cf | -17.5956 | -46.6648 | 2025-10-03 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 438d32ea-89d8-3e20-a4b5-012140ef0e49 | -12.6131 | -46.9725 | 2025-10-03 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| b3b7f8fa-0f09-38ce-a43e-6a0a619edd31 | -5.6361 | -43.9258 | 2025-10-03 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 6273949b-14c0-3c67-84e8-796409db4484 | -11.144 | -43.4082 | 2025-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 149.5 |
| c4f0f45b-80fa-359c-9106-0a178589d29c | -8.6138 | -54.976 | 2025-10-03 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5b6030f6-3420-3cc8-978c-fce6c538745f | -14.6886 | -43.8907 | 2025-10-03 00:50:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 84.5 |
| a439789c-1bb8-3285-9519-ec12fdf2164d | -6.0603 | -44.629 | 2025-10-03 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| ed63b5f9-f840-3b4c-8c37-588b53999cb7 | -12.6327 | -46.9471 | 2025-10-03 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 893d1fc8-b032-3e05-ac43-6b29431cda56 | -9.9182 | -43.7212 | 2025-10-03 00:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| f2eefa9d-1c2e-3c17-9809-20b6d5920ae9 | -13.7769 | -47.5392 | 2025-10-03 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e0dd438a-2557-338e-bc1f-db1261b964a3 | -21.59035 | -45.29136 | 2025-10-03 00:50:00 | TERRA_M-M | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 9e43d645-d3e9-3703-b244-c54ed5610621 | -22.14117 | -51.33595 | 2025-10-03 00:50:00 | TERRA_M-M | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ae9b88e0-4c82-37a9-aae7-3aa4650079d1 | -19.72809 | -45.89411 | 2025-10-03 00:50:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| af75c88b-cfef-3116-8b8c-453c601d05b2 | -19.5915 | -45.8995 | 2025-10-03 00:50:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 29957d03-e1c3-3047-8f62-1606f5e0e36c | -18.68278 | -47.83067 | 2025-10-03 00:50:00 | TERRA_M-M | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 66.5 |
| fc5170ba-9834-39e8-b84a-24d36f58f10d | -20.38196 | -44.13196 | 2025-10-03 00:50:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 8a19bc72-409d-3133-9cdc-790297272805 | -19.8942 | -44.50379 | 2025-10-03 00:50:00 | TERRA_M-M | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.3 |
| 4c070fab-4bff-38df-a2fa-9167eaa14932 | -21.58753 | -45.27507 | 2025-10-03 00:50:00 | TERRA_M-M | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| c9a5e9b2-788f-3811-a605-8be7e64609df | -19.72528 | -45.87767 | 2025-10-03 00:50:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 52.7 |
| d43a1b4a-317e-37fa-a576-837f9c5d24b7 | -19.89475 | -44.51014 | 2025-10-03 00:50:00 | TERRA_M-M | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.7 |
| 6a61b9ec-20d9-3aca-826f-56e0a1ab3067 | -20.37984 | -44.12577 | 2025-10-03 00:50:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.1 |
| 62874c42-9557-37a9-8c88-3af1d73a35bd | -18.77519 | -43.57613 | 2025-10-03 00:50:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| c5f2c21a-50cc-3001-a48b-9fbbf91eab72 | -19.89786 | -44.5237 | 2025-10-03 00:50:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 4e427663-95d0-3005-8a12-cac135fbc757 | -20.38393 | -44.14771 | 2025-10-03 00:50:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 8693f4f3-06e0-34f3-91ab-c05f5c067a65 | -18.68478 | -47.84328 | 2025-10-03 00:50:00 | TERRA_M-M | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9a765cb7-ea98-304b-ba23-b325db4f6772 | -20.13566 | -44.01582 | 2025-10-03 00:50:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.9 |
| 7ff3bd3c-8ed4-3466-88a2-41bbaba47732 | -19.71956 | -45.91326 | 2025-10-03 00:50:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 97d96fe2-a3f0-330a-91cb-c78149db075e | -15.24644 | -49.29254 | 2025-10-03 00:50:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| bf26870e-5ef0-3696-8a3a-2c579fa8009a | -16.32791 | -49.93606 | 2025-10-03 00:50:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b87b7707-ff48-3031-a637-d1f3df704b4b | -16.77099 | -43.9609 | 2025-10-03 00:50:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 46.4 |


[Clique aqui para ver as próximas entradas](README5.md)
