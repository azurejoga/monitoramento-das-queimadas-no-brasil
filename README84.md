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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1479011c-a76e-3dd6-82fe-4b75549f4331 | -3.43931 | -54.12974 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5bb63da-de28-3606-ba08-3bd145eefed8 | -2.833 | -49.2413 | 2024-10-26 04:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2a91a46d-8caa-3525-8510-aec3780e5034 | -2.9317 | -52.5713 | 2024-10-26 04:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 2b29825b-92f1-3b33-8252-8ccf3da67797 | -2.9501 | -52.5708 | 2024-10-26 04:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| a7c7d520-7235-3b98-a8fe-51fea9ad1b97 | -2.9501 | -52.5504 | 2024-10-26 04:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 4861e179-92b5-3408-b5a3-d8e9c1a336ba | -2.9945 | -50.4816 | 2024-10-26 04:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 16348bd2-b918-3e05-af07-87aa1246c07d | -3.013 | -50.481 | 2024-10-26 04:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| b65da4b6-91a5-352d-90c5-af074cafd97a | -3.473 | -43.3144 | 2024-10-26 04:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 18a0f8ed-5c04-339d-878d-ab1d78cf58f6 | -3.4729 | -43.3377 | 2024-10-26 04:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5d4a7530-bf4b-393b-bc0b-5decd2904c87 | -3.6084 | -45.8147 | 2024-10-26 04:45:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| feaa4453-ce44-3876-b2ce-f820ce3724a7 | -4.5613 | -48.0358 | 2024-10-26 04:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 136cc915-b691-3d47-a211-e1fc4f318903 | -4.5614 | -48.0141 | 2024-10-26 04:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 28e17319-bd7e-3f6d-8432-5fc5bfeb0225 | -4.5799 | -48.0349 | 2024-10-26 04:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| e915965d-99b7-320b-9f95-960f333095f8 | -4.58 | -48.0132 | 2024-10-26 04:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 8498520e-1a6a-3b66-87bd-d878a688a445 | -7.6474 | -63.4584 | 2024-10-26 04:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| ffacb8f7-03b2-3f38-9fcf-71fe2cb47223 | -10.62124 | -55.90926 | 2024-10-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2088a91-37a7-3c14-a003-712f51ceb4ca | -10.61158 | -55.98777 | 2024-10-26 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50668613-e846-3b7a-8aba-6fc91a70a7ff | -11.27951 | -56.14826 | 2024-10-26 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeaa44a3-052b-3546-802b-0341c28f711b | -11.17011 | -56.28989 | 2024-10-26 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bea24e24-f50e-3e32-9ec4-5db2e3847e90 | -11.16631 | -56.28926 | 2024-10-26 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5ca5eeb-16f7-34ae-875e-e734d32a3523 | -11.16251 | -56.28862 | 2024-10-26 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5899917-abea-3321-adb7-e9614e811273 | -18.11543 | -57.3065 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ec7f534a-d3f5-3c7a-8ea8-545eb35deebc | -18.11258 | -57.30134 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0d43a79b-841c-3f3e-a70a-af82a3e9a735 | -18.11179 | -57.30579 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4ada8ba0-3e00-3367-afee-9748e7410d1f | -18.10821 | -57.2837 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| df8ae02f-1e57-3a31-b5ea-09a586223b9b | -18.10768 | -57.28657 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 9020a719-47d7-3855-a3e8-96f093ce17f7 | -18.10744 | -57.28816 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d7899b33-d679-3349-8ef0-0567698fb140 | -18.10714 | -57.37432 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f2836681-7cec-3c6f-bfa8-c5232ea4f0db | -18.10483 | -57.28142 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 24904767-1678-3d01-aafb-021b74d5b694 | -18.10457 | -57.28299 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 84cc289e-51ac-3794-8d93-afbd3cbea5fd | -18.10404 | -57.28587 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b3f9f371-e97a-3a95-b594-fefb3ec6f0d5 | -18.1038 | -57.28745 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 27381c38-2427-37ae-96fa-ac22275c0fbe | -18.10093 | -57.28229 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0fb10891-e287-38d8-b0e3-7748944045c9 | -18.1004 | -57.28516 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 767759e1-afa3-36c6-a6a6-4233df1c4e47 | -18.10016 | -57.28674 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| bdd6a86c-29cc-3202-9650-21eb1d263b52 | -18.09961 | -57.26823 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c07a4aa4-675e-3073-bd34-6167588569ad | -17.27595 | -57.51065 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| aaa9e1db-a884-301d-8894-78a7b9332b19 | -17.27223 | -57.50993 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 530882ab-8670-39d4-9e00-2a0952a16ac8 | -17.2685 | -57.50921 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 079b8554-b4bc-34e5-9fda-2c76083d4356 | -17.26768 | -57.51387 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 276ede76-f689-336a-8b64-352c52b060df | -17.26686 | -57.51853 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f93e6bb1-3310-3e2f-9a1f-53ba90e4fdac | -17.26396 | -57.51315 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7ceb87a4-41e7-3304-9378-22b4895a2fee | -17.26314 | -57.51781 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 85675fad-cbee-33d5-92cd-30adc81a927e | -17.2627 | -57.49846 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 1d289746-c34f-311c-922e-a97a12540985 | -17.26188 | -57.50312 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 31e5e05d-5d30-3bc0-bd7b-e27251980b86 | -17.25941 | -57.51709 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e1f22ed2-1d0c-31de-81d6-a55e4b8fb1fa | -17.25898 | -57.49773 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| fd1fe3dd-8614-3973-a25b-179f8429278f | -17.25816 | -57.50239 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| fabed97c-34eb-3d44-8dde-3669d259db49 | -17.25525 | -57.49702 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| d7b79093-4416-3dca-b0c4-dd49d0c73c90 | -17.25443 | -57.50167 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6f3673a5-5b47-3e88-8e48-cf7d82d40179 | -17.25236 | -57.49164 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 2c6a5462-81b5-33cf-a8aa-eab39e836b63 | -17.25154 | -57.49629 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 4d1f36b1-78ab-39f8-8ab7-ac5481a05916 | -17.25071 | -57.50095 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e176a335-759c-3c56-87bc-699689cef2a7 | -17.24989 | -57.5056 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 98d5a62c-4b32-32e1-a19e-e15b91ee7762 | -17.24864 | -57.49092 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c7a1cc72-52d2-3f90-a697-b43c8c9fdc8a | -17.24781 | -57.49557 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 79423d22-ca0b-3f5f-bcc9-f236824382e9 | -17.24699 | -57.50023 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 887aac4c-cd64-3724-bab5-7191ddb65e05 | -17.24327 | -57.49951 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1f1dfb4e-cd7f-330f-87f6-39be063851d8 | -17.24121 | -57.53288 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a3138eb9-4c3a-31f4-891d-29b36c1b9e61 | -17.2321 | -57.49735 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 595f69ae-5408-37f0-a19f-20061ec37c0b | -17.22838 | -57.49663 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6cfef4b1-9672-3654-bbee-0fbd48197e10 | -17.22179 | -57.44737 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e7cdc9b9-3ac2-35d5-a59d-2757be09dddf | -17.17653 | -57.4119 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3ce4e0c2-9228-35c5-8be0-0140a55dc800 | -17.14074 | -57.46246 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 64e3138a-b8f4-3159-ac58-951a38e99363 | -17.13702 | -57.46174 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f77c7bca-2628-374f-b9c3-c6fad1178888 | -17.1031 | -57.47925 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 85a430c4-e865-3695-934b-24887db1498e | -17.0857 | -57.39662 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 44108472-bc90-35ea-835c-4bc5b09c5699 | -17.07856 | -57.48166 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 84e235e0-56e5-3d84-b726-3593e0a6fd86 | -17.07827 | -57.39519 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e6b403c0-9a66-3b01-b2b6-f0511f9e0fae | -17.07775 | -57.48633 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 11d5d7ff-0d2e-3535-ace2-bfae6efbdfcb | -17.07666 | -57.40443 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9ef77611-ab86-3688-922b-c99a98da352a | -17.07585 | -57.40906 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fc2cafc1-98fd-327f-9a18-2e6efbd97b86 | -17.07483 | -57.48094 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 16070266-19c0-3fb6-b8de-5e6f7d3040b3 | -17.07402 | -57.4856 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1d73edf2-2e40-3c5f-a0b4-695817279745 | -18.09431 | -57.36427 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 42f70e16-deb2-3927-8d82-24df5e9c9f89 | -17.07214 | -57.40835 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 16312f20-80bc-32fc-85dd-f470b3b04369 | -17.07133 | -57.41297 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7bbc13fb-1c29-3a32-a70d-4bdf83ae2574 | -17.0697 | -57.42223 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3280990c-5de7-3819-9bd8-2afa3605ae79 | -17.06889 | -57.42687 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7971f79b-44e3-3883-bd75-aacc59a58258 | -17.06656 | -57.48416 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 88c612e6-2051-37ea-869b-b90cfc0be939 | -17.06284 | -57.48344 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 114d7263-a53a-3d65-a4fd-db83192fc096 | -17.06238 | -57.46406 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| e8913556-641b-3761-a575-3eb8eaef8fb8 | -17.05911 | -57.48272 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f816c744-9282-382b-b591-089767404378 | -17.05656 | -57.45332 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 06e1c427-d627-3c69-8670-ac0c3928d283 | -17.05575 | -57.45797 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4b5ea516-a936-35fa-a9ab-8a689dde7938 | -17.0552 | -57.39552 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d73e8e59-8364-341e-b1b9-312caea4f779 | -17.05284 | -57.45259 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ec3005d8-11ce-3ef4-9135-82cefb3d5cac | -17.05202 | -57.45725 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4db8544b-4345-3cab-bc74-3ab8d5e7ff65 | -17.05158 | -57.43793 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0bcfebba-686c-37bf-8ad3-6ed947d66320 | -17.05067 | -57.39943 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| bc730b7c-0d4f-34b6-8d4d-fc9667161523 | -17.04912 | -57.45187 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fe4aa6bb-2e3c-3ed0-a9df-73f30c66d747 | -17.04786 | -57.43721 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1575ff39-e879-39b3-a0e4-ddfcc916c26f | -17.04778 | -57.39408 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 12f2a2e1-7c88-3146-8117-fec0373fa9b6 | -17.04696 | -57.39871 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6689ebbf-cc97-31f9-a358-7aa8e69be8e4 | -17.04659 | -57.42259 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a0a0e6cf-908b-3af1-87a3-c734d2d4d64d | -17.04577 | -57.42722 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5a8c9a6d-3d96-3be7-8207-892b5548cc7d | -17.0454 | -57.45115 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c63c6b1d-1ae4-3b34-b8c3-bd6ee0c22404 | -17.04495 | -57.43186 | 2024-10-26 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2de5134e-a1d4-31b4-8fae-c5fd51dcbd7b | -17.04325 | -57.398 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 155879e9-4d31-3da9-af21-0f936bc8d7e0 | -18.09597 | -57.26752 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README85.md)
