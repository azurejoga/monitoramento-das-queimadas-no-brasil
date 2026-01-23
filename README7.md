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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50c5097c-e735-3d9d-9f76-3d2c73f7e16b | -20.91157 | -56.38683 | 2026-01-23 05:27:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cbc623d-83f9-38b6-a779-089cfe497414 | -19.68011 | -56.86724 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 64bb6afc-72c2-3e9a-bb90-e9ec550e54a4 | -19.1741 | -57.54519 | 2026-01-23 05:27:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 423b4b26-eceb-3d9a-a836-bd27861d844d | -21.78371 | -56.28473 | 2026-01-23 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3d980e2-07ea-3145-b471-36e40b2f797d | -20.36905 | -57.87005 | 2026-01-23 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c3fabb16-9b66-3340-ba12-ab97eef28465 | -19.68255 | -56.86887 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ae6f64ff-4535-37b0-8d13-ba2f983cea6c | -21.53675 | -57.53396 | 2026-01-23 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2831be1f-f620-342c-ac7b-8f8c75dfcee4 | -19.68004 | -56.93045 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6fe9fdd5-1362-3e99-9fa1-a98eff2e45f1 | -19.69044 | -56.87951 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 30f1df98-2e16-3c9b-bd78-6c91518d198c | -19.6899 | -56.88421 | 2026-01-23 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c194db0a-e67a-3c4b-99c6-374de947892f | -21.77891 | -56.28418 | 2026-01-23 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38a11d44-fc5a-339b-bd13-ba3af11ad0b9 | -21.7843 | -56.27906 | 2026-01-23 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24892fa1-8567-3aa7-9e40-9b8b8168b963 | -16.26798 | -58.31628 | 2026-01-23 05:27:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7c251a78-43db-398a-8584-b50eef3f0e02 | -21.78328 | -56.28979 | 2026-01-23 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c22bb2e6-6129-3caf-ae52-01d33caf9e9e | 1.12948 | -60.53087 | 2026-01-23 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed1515ba-cfa3-328a-9909-2a5cc0fd54f2 | 1.28689 | -60.43147 | 2026-01-23 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60446472-9d5e-34fb-9e51-4d39d17b05f8 | 3.35321 | -60.10511 | 2026-01-23 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e09c78f2-0d11-3082-b20a-8fd97bbac7a9 | 3.34925 | -60.10577 | 2026-01-23 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70f09fec-7d64-31b6-b443-743b416a0c28 | 3.34612 | -60.11148 | 2026-01-23 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b0c77486-0754-3c31-b05c-c547cd91eea7 | 1.13181 | -60.52002 | 2026-01-23 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 516662f7-7329-310e-8f5a-881996196487 | 1.28343 | -60.43557 | 2026-01-23 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 524b08e0-a775-39c1-a2dd-e3e4787784cd | 4.27065 | -60.63755 | 2026-01-23 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9ce3977-5ce4-37c7-a787-d051eeb84b0e | 1.28981 | -60.42392 | 2026-01-23 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4f09f2e-146e-3841-bb9e-b40dd0426f7c | 4.2682 | -60.64037 | 2026-01-23 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6200930c-5bf1-3481-873c-42937a9c7645 | 1.29035 | -60.42738 | 2026-01-23 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c536c882-0372-3f91-bdc0-896f3d4c419c | 4.23995 | -60.65788 | 2026-01-23 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fa77ef2-1318-3583-bd52-e42c355259e1 | 0.88541 | -59.33965 | 2026-01-23 05:52:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea004e56-17b6-305a-b53c-e75d32a1d582 | 3.78208 | -60.78872 | 2026-01-23 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 807a6a7b-d228-3ec6-9dd7-58110b8ebeb5 | 2.9014 | -61.47607 | 2026-01-23 05:52:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd5693b4-1c26-39c6-acfb-337eed8a8b8f | 3.35008 | -60.11083 | 2026-01-23 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5beb4506-1a58-3c68-b03b-092fa2ef692c | 1.13264 | -60.52514 | 2026-01-23 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c923ea59-e815-38e2-a420-08f14a943d05 | -14.31071 | -57.5942 | 2026-01-23 05:57:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb31a22b-ce27-3e4d-94d7-0a878c15226c | -14.30466 | -57.5932 | 2026-01-23 05:57:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f663a778-533b-38d2-8e74-8166b62200a4 | -15.59721 | -59.29394 | 2026-01-23 05:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27f1c800-c49a-3d01-b15f-c25f27a19c0d | -15.77457 | -59.14326 | 2026-01-23 05:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94511d67-ac50-3b5d-9e76-e382570df5b3 | -14.3112 | -57.58985 | 2026-01-23 05:57:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7abb51c-da03-3b4b-92b8-03612b0a34f3 | -15.59678 | -59.29771 | 2026-01-23 05:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 628e9874-d581-35b4-b779-8fc88288148b | -19.6685 | -56.86922 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2a20e350-483e-34b6-8609-7e446a415c28 | -20.37519 | -57.87666 | 2026-01-23 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9fbfcf67-28ae-3d30-bed8-5c98c0d65e57 | -19.17576 | -57.54944 | 2026-01-23 05:59:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b61cc85f-03f5-3ca2-af4e-14518d88b400 | -21.53986 | -57.53041 | 2026-01-23 05:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 879270ac-103f-350d-b952-370a2d1c77d3 | -19.17615 | -57.54377 | 2026-01-23 05:59:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 791593b3-289e-3bcc-9532-2dc458d2fce4 | -22.02429 | -56.32852 | 2026-01-23 05:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 644dd9aa-b9de-335d-ad9c-d8c399f6c1e5 | -19.69006 | -56.8769 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 355f8c9b-8967-345d-907c-e2930830bb86 | -21.78446 | -56.28275 | 2026-01-23 05:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5885433-ce35-3d15-9d79-2e42d9739175 | -19.1756 | -57.54964 | 2026-01-23 05:59:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a564ccaf-6fe7-3f04-bc6b-55010a41c3b2 | -19.68871 | -56.87117 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b2e9a0fb-1975-3d4f-9536-e9a2ba696d7d | -19.68333 | -56.87622 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 30476664-9c5a-3695-a113-0ee43eb530ee | -19.67036 | -56.86868 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fc1d0644-97c1-3459-95cf-33466b9585af | -19.68384 | -56.87004 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 29286fa6-c2db-3bfe-a579-66d0215ae3bd | -19.68142 | -56.87671 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 808c3051-6be6-3212-b938-2116d0c2593f | -21.78163 | -56.28273 | 2026-01-23 05:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d5cc957-6369-3f47-8a8a-0de009372204 | -20.38063 | -57.88816 | 2026-01-23 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5156286b-a3d3-3517-8cb6-e713893124bb | -19.17627 | -57.54355 | 2026-01-23 05:59:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 40e8d54f-07d5-3f91-b193-103b4f7c8194 | -19.66362 | -56.868 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a3895172-edb6-3186-8082-839c6557b82d | -19.67524 | -56.86987 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9eeffdc5-d33f-3b77-8732-963142c210e8 | -19.68198 | -56.87052 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9e9d3655-93d7-32ae-9093-1cf63456d81f | -22.02379 | -56.33575 | 2026-01-23 05:59:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f3e9231-76ed-3e42-8b25-af574da508e6 | -20.34413 | -57.86251 | 2026-01-23 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 39d9265b-5659-3235-abe1-42a552736f4c | -20.33726 | -57.86729 | 2026-01-23 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dc0f98c3-f493-38c4-a626-937a9c93fe0d | -21.53327 | -57.52958 | 2026-01-23 05:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fed10bb-4bcc-3f05-953e-5f8472cae677 | -20.38111 | -57.88274 | 2026-01-23 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e6b32803-1629-32a8-820d-449021518956 | -19.68816 | -56.87736 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 025426e2-6efa-3615-ad4d-209b1acc0e07 | -20.36927 | -57.87057 | 2026-01-23 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 760466be-eb11-3e45-8128-80d346c02d40 | -19.6771 | -56.86936 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 71ef0436-d0db-391a-8d64-3a50281b59dd | -20.36287 | -57.86992 | 2026-01-23 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4f907ac3-005c-33c7-842e-1aeff6a9d8c5 | -19.66176 | -56.86856 | 2026-01-23 05:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6741f782-f252-3ec9-9757-5e9b777fa83f | -8.12025 | -48.0197 | 2026-01-23 06:16:00 | AQUA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bf9b117e-492b-3f73-b85b-db91a53a8c78 | -14.31202 | -57.59184 | 2026-01-23 06:18:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3dfb3fb4-f225-32d7-a891-772eecfc7ecf | -20.34204 | -57.85591 | 2026-01-23 06:20:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 6ed7f778-7542-3ba5-b3f2-4bcf60730c65 | -22.73445 | -49.3505 | 2026-01-23 06:22:00 | AQUA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b7f6a53f-d7fc-36ab-9926-449e9da860d1 | -21.78362 | -56.28342 | 2026-01-23 06:22:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1a7109c8-3f21-30c7-9112-4c785f2d7e34 | -22.61287 | -49.56409 | 2026-01-23 06:22:00 | AQUA_M-M | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f5c5f760-4613-32b0-917f-53b211f01935 | -22.61145 | -49.5745 | 2026-01-23 06:22:00 | AQUA_M-M | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e5b558e7-fb41-39f8-85e5-0372edc09529 | -21.78151 | -56.27732 | 2026-01-23 06:22:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bf58eb47-f8a8-35ba-a53a-5bbf4e9a9bac | -6.37139 | -35.52642 | 2026-01-23 11:14:00 | TERRA_M-M | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 14.3 |
| b35b238c-9347-3ec5-b4ae-19d536f2b963 | -6.36999 | -35.53596 | 2026-01-23 11:14:00 | TERRA_M-M | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 9fe96f2b-a71b-34c0-8c95-f56c474fb279 | -4.64192 | -38.56333 | 2026-01-23 11:14:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 20.2 |
| d8f175bd-5bd9-3bf9-92df-a20e01d71d5d | -9.66337 | -37.09795 | 2026-01-23 11:14:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 1869af90-705c-365c-a57f-ff4431796974 | -7.20061 | -35.47006 | 2026-01-23 11:14:00 | TERRA_M-M | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a6881eb8-a399-3c1b-8558-efda1bb6c2cd | -7.89954 | -35.99102 | 2026-01-23 11:14:00 | TERRA_M-M | VERTENTES | PERNAMBUCO | Brasil | 2616209 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d7311cc5-086a-3c16-8194-9406e9c718ed | -9.66495 | -37.08738 | 2026-01-23 11:14:00 | TERRA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 991d5d4a-79f8-3dbe-a599-58969dbc3d49 | -11.92962 | -38.31062 | 2026-01-23 11:17:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 53db4e3f-f610-3fe2-ac89-de5adbd00080 | -10.81549 | -38.08979 | 2026-01-23 11:17:00 | TERRA_M-M | POÇO VERDE | SERGIPE | Brasil | 2805505 | 28 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 850a4c3e-dd7e-360d-b6a7-7572a9ab2b04 | -22.0275 | -56.3434 | 2026-01-23 12:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9eeb0e75-1ef3-3cb7-b11b-d2a1e37bc46a | -22.0275 | -56.3434 | 2026-01-23 12:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 95.6 |
| df00defe-7391-377a-bdda-eaba448f8347 | -22.0275 | -56.3434 | 2026-01-23 12:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 95.1 |
| c1f97deb-cca4-36ae-b72c-af903242c5d5 | -22.0275 | -56.3434 | 2026-01-23 12:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 108.0 |
| adeff2e4-a5e4-3ef4-aeeb-583d2cd355d3 | 3.3485 | -60.1148 | 2026-01-23 12:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 91.3 |
| fba71c60-74ac-3942-a0f0-0a9003de3ddb | -19.6836 | -56.8674 | 2026-01-23 12:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 5aa9c9e1-3f89-30d0-a913-6f639bc13a7a | -22.0275 | -56.3434 | 2026-01-23 12:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 112.1 |
| e1a6906a-40e6-3678-8cb1-1e34805f1c5c | -19.6836 | -56.8674 | 2026-01-23 12:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| a6e36031-fbe5-386b-b406-660cd5f67f6c | -22.0275 | -56.3434 | 2026-01-23 12:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 73af61e2-a99b-39b9-a7f0-c1e04fe89a92 | 3.34296 | -60.09928 | 2026-01-23 12:50:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7b40e8df-8b64-3afe-ade4-72472c4c7a64 | 3.35154 | -60.10397 | 2026-01-23 12:50:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6452fb5e-9604-31f5-a8ed-34a1f3f1b2e0 | 2.05142 | -60.8738 | 2026-01-23 12:53:00 | TERRA_M-T | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| da9ff53b-ede7-30cc-8666-a23b08d70ead | -22.0275 | -56.3434 | 2026-01-23 13:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 417eb9e8-76f6-39c1-a5d7-53bf05f3ad4c | -19.6836 | -56.8674 | 2026-01-23 13:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 08889713-f3a0-3ed6-9940-7be2d82dd6b6 | -7.2597 | -43.0645 | 2026-01-23 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| ed46b9da-42e6-3297-951f-a78f1c9e6f09 | -5.4351 | -39.2303 | 2026-01-23 13:10:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 95.9 |


[Clique aqui para ver as próximas entradas](README8.md)
