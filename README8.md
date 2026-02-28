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
| 6ff75402-7887-3dc3-9ae6-afbb142838dd | 1.4682 | -59.9119 | 2026-02-28 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 2265f482-5b7a-3c21-bd52-d7a69d766f6b | 1.4681 | -59.9309 | 2026-02-28 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 188.4 |
| 29cb1d48-d039-36f8-bd5e-711aeb10c368 | 1.4682 | -59.9119 | 2026-02-28 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d6e7a19d-cedc-371c-ad9c-5fe080b5c84f | 1.5046 | -59.9306 | 2026-02-28 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 235e569a-182a-3866-abc6-948eeb1fac6e | 1.5047 | -59.9116 | 2026-02-28 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| eca902ff-bf37-3518-9b01-692a7ba85e65 | 1.4864 | -59.9117 | 2026-02-28 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 06e63198-7415-34fc-bf6f-ea745060331c | -21.7001 | -56.3109 | 2026-02-28 13:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 101.9 |
| c65de6a3-8e38-3495-a528-dca23e81d65e | 1.4864 | -59.9308 | 2026-02-28 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 285.6 |
| 4b3321ef-5adb-3e40-a749-55a025b36355 | 1.4681 | -59.9309 | 2026-02-28 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 188.4 |
| 0245d114-7675-3e0a-8592-20634f18f662 | 1.4682 | -59.9119 | 2026-02-28 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 621f6f08-8f71-3606-9a8a-e7fce76653d6 | 1.4681 | -59.9309 | 2026-02-28 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 189.5 |
| 850f268e-cd1b-37f5-b987-f5ab0750cc3b | -21.7001 | -56.3109 | 2026-02-28 13:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e520d50b-940c-3afd-a838-4d59876b2197 | 1.4864 | -59.9117 | 2026-02-28 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 5bcb2ff3-6fb3-39bb-9cbc-1fd0d653da79 | 1.4864 | -59.9308 | 2026-02-28 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 304.1 |
| db07ff97-e308-35ba-8a77-c1923e380aab | 1.5046 | -59.9306 | 2026-02-28 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 220be228-14ad-360b-af68-08a154bc77d9 | 1.5047 | -59.9116 | 2026-02-28 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| efe776d5-af41-358c-9592-710986379d63 | 1.4681 | -59.9309 | 2026-02-28 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 187.7 |
| fe72e56e-dcb7-34fd-81f4-5c3f0bc3e916 | 1.4682 | -59.9119 | 2026-02-28 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 853397c3-f1ff-3b7d-a579-1b7a20612a35 | -21.7001 | -56.3109 | 2026-02-28 13:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| b2a711e9-353c-3a15-833e-08bfbdeffb0f | 1.5047 | -59.9116 | 2026-02-28 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 48a38c1a-9807-324d-ad3d-566b273dc2a4 | -21.6795 | -56.3142 | 2026-02-28 13:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 91.3 |
| e452fc55-ae96-3736-a463-5005baf2e576 | 1.4864 | -59.9308 | 2026-02-28 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 348.8 |
| e5f58b7f-d026-3bc2-9051-79eb5b9cbb16 | 1.4864 | -59.9117 | 2026-02-28 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 220.7 |
| cb6e4537-9b22-32aa-af19-263295f21b6c | 1.5046 | -59.9306 | 2026-02-28 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 8797f979-132a-3970-9137-0fcb59a4125a | -21.6795 | -56.3142 | 2026-02-28 14:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5d540019-94ce-353c-b24c-4cdce8baf5e8 | -21.7001 | -56.3109 | 2026-02-28 14:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a65b1b27-1cc8-3e9a-a847-f586d788e826 | -21.7001 | -56.3109 | 2026-02-28 14:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 5905696f-3538-3b01-a2b8-3a5c6e633fe8 | -21.6795 | -56.3142 | 2026-02-28 14:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 75.8 |
| aee68322-caf9-3468-bf93-cb6bad1ba6db | -21.6795 | -56.3142 | 2026-02-28 14:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 6548fdc8-abe6-3e88-95dd-ffe95a049d7f | -21.7001 | -56.3109 | 2026-02-28 14:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 109.1 |
| b0b842d3-9619-3777-a48a-b93fde4a5352 | 1.5046 | -59.9306 | 2026-02-28 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 145.1 |
| cda22fb0-7684-3a34-ad90-c5e486c2fa18 | 1.4682 | -59.9119 | 2026-02-28 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 4402744b-5982-307e-ad18-ecea9752839b | -21.7001 | -56.3109 | 2026-02-28 14:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b2fe14c3-abb0-39f6-856d-2af8579e5399 | -21.6795 | -56.3142 | 2026-02-28 14:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f10ee328-d758-3460-bab9-063586d00449 | 1.4864 | -59.9498 | 2026-02-28 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 32bde53b-85d3-34a2-bee7-4487d8ee2ede | 1.4681 | -59.9309 | 2026-02-28 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 212.9 |
| 93da72ab-ded7-3975-b422-7472995cba32 | 1.5047 | -59.9116 | 2026-02-28 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 6d2b3927-9c1a-39b0-8eb8-370dea4788a7 | 1.4864 | -59.9117 | 2026-02-28 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 231.7 |


