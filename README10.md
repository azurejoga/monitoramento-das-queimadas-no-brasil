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
| 702df95c-daf5-31db-b071-932eb102518f | -14.22159 | -51.91714 | 2026-07-31 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac64e4c5-730d-37ec-920f-098960c4d3ab | -16.40244 | -54.8488 | 2026-07-31 04:42:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9051d15-6d77-345e-b7cd-6e45f5d74396 | -15.88364 | -47.61526 | 2026-07-31 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21d12473-81a2-3211-bfd6-f98db7d91cb0 | -16.75527 | -49.17571 | 2026-07-31 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f8dd31e-105b-37a4-a17f-5ccba192941e | -14.07311 | -46.2275 | 2026-07-31 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8a5e8e6-a8a6-3e2a-930f-0b33065654f0 | -14.37725 | -48.07159 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e06b9b86-08c5-3d0a-b2a4-0b827bdaf523 | -14.36095 | -48.05659 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b05181d9-80cc-3be1-91c2-afbb40051a00 | -14.37843 | -48.06331 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8851b27e-0c89-37ed-96a5-ad3edf3e75cf | -14.83127 | -48.53139 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f59ce32-5683-3c68-ae62-f9b506fa04bd | -15.88267 | -47.61741 | 2026-07-31 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39202a57-b1fd-312f-9232-47a6b4bec4df | -14.37062 | -48.04048 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89a7a6ca-3169-35d5-9d73-666f992f9403 | -16.66876 | -49.12243 | 2026-07-31 04:42:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc63b07b-5413-3e6d-bea7-8eca55457baf | -18.12452 | -44.63699 | 2026-07-31 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d588ad54-9ea0-3548-a587-86469d086bde | -18.11983 | -44.63629 | 2026-07-31 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16deb301-e731-396b-8d99-29bbb66b53e5 | -14.38029 | -48.07607 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd03eaec-8b9c-33c5-9585-4039dbf3f422 | -18.93686 | -47.45616 | 2026-07-31 04:42:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1ddca0b-f563-3274-ae3f-494d05995555 | -18.47433 | -51.72444 | 2026-07-31 04:42:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0d8d0d6-3f67-3379-99ab-5bee93009d4c | -18.11992 | -54.51546 | 2026-07-31 04:42:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| addb63d8-5199-389b-9553-ffeb11e1483c | -14.05806 | -46.21827 | 2026-07-31 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32a34774-b1e2-34d5-b883-7a69126c9b53 | -12.98878 | -53.80202 | 2026-07-31 04:42:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 925f9a65-27d0-312b-8aaf-984d18a79410 | -14.07358 | -46.22406 | 2026-07-31 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e403a98-d8b6-3644-9078-fb2201225fb8 | -16.40306 | -53.33597 | 2026-07-31 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 395dbb83-ed5a-3a27-ba15-07634c8213da | -16.39968 | -53.3354 | 2026-07-31 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ba77441-69bc-380c-95b0-44e22b97499c | -14.21891 | -44.13463 | 2026-07-31 04:42:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adf76806-23d0-3d6e-a1b7-a515caec35d1 | -18.02406 | -44.36839 | 2026-07-31 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2bca5e4b-350c-3939-a38f-0febce9d5197 | -15.54202 | -56.02611 | 2026-07-31 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5025a5b6-773b-3fe2-ad01-9735535060c2 | -14.37125 | -48.03602 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ca93395-1561-3256-a4d9-7d576bc8c1ec | -15.51031 | -47.82248 | 2026-07-31 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 956fb207-f1a0-3b85-88b3-644660c1eaef | -14.40631 | -48.04902 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46a20889-1a7d-3f38-8a7f-8ea5dc823bf5 | -19.16158 | -47.31682 | 2026-07-31 04:42:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 693865a2-75b1-3b17-bb09-e66de1907ba9 | -13.94609 | -46.18805 | 2026-07-31 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 460273e7-7cfd-34fb-a2b0-562ab3d62757 | -14.36701 | -48.03986 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70472a22-55ee-3ebf-b13a-a0703228c09e | -14.06206 | -46.21884 | 2026-07-31 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71c3a93d-cc66-332c-92c7-61facfdbbb75 | -14.36637 | -48.04441 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f24f172-b85e-34fc-9a61-71b4b700a2ed | -14.39299 | -48.06469 | 2026-07-31 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 333e4823-4e19-3a9f-a29f-715039baa0fc | -15.62275 | -55.95007 | 2026-07-31 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5328d4cd-eb1e-3f03-b114-279d261c84f8 | -20.61082 | -57.30115 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ca0960c-4f76-3e90-a2c5-8d76936334ad | -18.81008 | -53.14118 | 2026-07-31 04:44:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f343b3e-c91b-3a5a-9517-733f8df534cc | -22.16043 | -56.0193 | 2026-07-31 04:44:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 16.1 |
| cf5cdd4b-4e88-3762-a193-f8752433f1f9 | -21.38823 | -56.83712 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f83323d-7ba1-3cbd-8444-b46009041326 | -21.73808 | -45.2685 | 2026-07-31 04:44:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 33fcb73c-1053-36dd-9e39-18f43a5908bc | -20.69307 | -45.34242 | 2026-07-31 04:44:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01ebc78d-642e-3724-a8b6-ec3bd52629e7 | -20.11205 | -50.74576 | 2026-07-31 04:44:00 | NOAA-21 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| afdd6923-d40d-36f9-8de1-aae8d854ac16 | -21.04779 | -55.82589 | 2026-07-31 04:44:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f71ace7-4adb-35fe-bc2c-f5f11b9264a1 | -19.01831 | -56.42227 | 2026-07-31 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 01edb1ed-32c8-3034-8533-f541dae1975f | -20.1149 | -50.75026 | 2026-07-31 04:44:00 | NOAA-21 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a15799dd-50d4-3bff-bac3-6eef6c107d31 | -21.75232 | -52.18804 | 2026-07-31 04:44:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 89c7adac-36f9-3335-857c-af7dc3d9b18d | -22.24671 | -56.70911 | 2026-07-31 04:44:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ff84ff3-fdfb-3691-b16e-bce115675b33 | -18.8095 | -53.14484 | 2026-07-31 04:44:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1cebf146-6ffd-3477-ac0f-7c1373d05999 | -18.81341 | -53.14176 | 2026-07-31 04:44:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01dca3e4-1247-3fca-a08a-1d2c156e22e5 | -18.81282 | -53.14542 | 2026-07-31 04:44:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8aa5636-246d-33cc-acae-7df4de8eabf3 | -20.11149 | -50.74968 | 2026-07-31 04:44:00 | NOAA-21 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5f307e42-f8ec-30f1-a644-f054f46444cd | -20.57058 | -57.26173 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b75f4e4-f986-3486-9b8d-11ec97d7d90e | -21.38087 | -56.83561 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d6e6d051-31ab-3ff1-965d-b0b6fa84fff4 | -22.15693 | -56.01853 | 2026-07-31 04:44:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db3ee11c-3697-35f5-978b-f12aff5d3683 | -20.13028 | -44.96062 | 2026-07-31 04:44:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a1ded7a-7464-32eb-bed5-6bb554353258 | -19.02099 | -52.25669 | 2026-07-31 04:44:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b137ea14-de04-3b43-88dc-e89459888184 | -21.37803 | -56.83008 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5310788c-1b23-334e-84d3-ee6ac070eb11 | -22.19592 | -56.02522 | 2026-07-31 04:44:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c54e5c9-a2f4-36db-af31-b12ed1087238 | -22.45783 | -47.10795 | 2026-07-31 04:44:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c7be09a-2c8d-370c-854a-2bdba0c55c76 | -21.38455 | -56.83636 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e18982b2-6b39-3bea-add7-3acc9846628a | -23.03044 | -52.65279 | 2026-07-31 04:44:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 203e4ff8-c0a8-3a54-8561-04275cfcb392 | -22.19551 | -56.02665 | 2026-07-31 04:44:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70941878-2bd8-3012-8bb2-9959100db4b4 | -20.11546 | -50.74633 | 2026-07-31 04:44:00 | NOAA-21 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| f75c86f8-8432-3af9-b41f-3b0b22114cbe | -19.02866 | -57.50266 | 2026-07-31 04:44:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1ad269bc-e92d-38ae-946d-38c071315281 | -22.15765 | -56.01433 | 2026-07-31 04:44:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2e8807f-c7c8-3822-9e8a-a4d99ec3b359 | -22.16392 | -56.02009 | 2026-07-31 04:44:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4ba3aab8-9bf7-38aa-8b15-d602bda712ff | -20.3273 | -58.08717 | 2026-07-31 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f5e11512-1ea9-3ce1-8a8f-a0ab69ad8c64 | -20.51727 | -57.15064 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9ac72fb-90c8-3847-903f-6eebd0ce011e | -23.46068 | -47.38232 | 2026-07-31 04:44:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4a523d53-602d-37f5-b0fe-f51166f4a13d | -22.16669 | -56.02512 | 2026-07-31 04:44:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f003e595-e28e-3946-a35f-db9c38f281e9 | -20.51815 | -57.14577 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1451dbb0-4251-34de-b9be-e9ece64c616c | -21.7375 | -45.27379 | 2026-07-31 04:44:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 92c51386-5b1a-31a7-b9d9-378c1b3c4f3b | -20.32329 | -58.08633 | 2026-07-31 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cfd88e1c-bb86-3fd3-8705-7d38075ee91a | -21.38001 | -56.84043 | 2026-07-31 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2959207-510e-382f-a8c1-ca9f62edf11f | -22.16115 | -56.01511 | 2026-07-31 04:44:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5f26b511-7f3b-3b7e-acf7-4acff52b68e4 | -33.08588 | -53.19269 | 2026-07-31 04:46:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| a0e4f50c-8c59-3418-bbcc-91b82b3c4884 | -14.3855 | -48.071 | 2026-07-31 05:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 715a33a3-cc67-3cca-be9a-f09d65f67e80 | -22.1578 | -56.0217 | 2026-07-31 05:00:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 9e99e5ef-86cc-32b6-8de7-28bde7a5fb6d | -22.1578 | -56.0217 | 2026-07-31 05:10:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b3c07f8b-e43b-3f67-a808-ffc5c09b6c68 | -14.3855 | -48.071 | 2026-07-31 05:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b313a29b-344d-3ab9-b02f-64be5b33b477 | -3.96797 | -48.1285 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 31eb8004-2c71-3538-8573-8bc3e6c0316a | -4.9136 | -43.46714 | 2026-07-31 05:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2ad7406a-1752-3a19-bbc6-972945687b2e | -3.1175 | -47.91427 | 2026-07-31 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6f5bf26b-1da3-3545-baac-ebaab52659ec | -4.36931 | -47.76643 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a611fa5-ac36-3406-b59b-f8415a1fe3d0 | -5.04009 | -43.26408 | 2026-07-31 05:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f0eccfc-f823-357e-909b-27d9c7b2bc9d | -3.96401 | -48.12273 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34f25bfe-faa3-304c-8edc-b9b23d657683 | 1.09899 | -60.51879 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9e25c12-eaf8-3a98-9ae4-8064990351ea | -4.91322 | -43.47203 | 2026-07-31 05:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69af5a43-e75c-3e7c-a6d3-810e36049f6e | -3.0545 | -48.74067 | 2026-07-31 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30d67538-88b9-3124-ac38-951d1a169696 | -2.32679 | -47.20286 | 2026-07-31 05:14:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed45113f-f170-34b2-b3f7-2786a67a2410 | -2.72464 | -54.62822 | 2026-07-31 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 180b9c53-6f37-36e9-949e-3635ebdd3bd6 | -5.71874 | -48.12457 | 2026-07-31 05:14:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc5ce87f-d459-3af0-ac78-236c73fde706 | 1.09768 | -60.51031 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11bcb0af-b1c8-39b2-ae04-03e3d1ac8a43 | -4.37337 | -47.77249 | 2026-07-31 05:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df2d8357-62d0-31d5-9c66-368d889aee19 | 1.10713 | -60.51315 | 2026-07-31 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe22528f-ad35-388e-a57b-0529029b3b75 | -1.73277 | -55.84311 | 2026-07-31 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 333c28de-eed8-3202-bddf-c60975369154 | -0.85674 | -52.71613 | 2026-07-31 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e4206e2-626a-3461-ac7a-e0e84cfabe81 | -2.89857 | -54.55946 | 2026-07-31 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e25fdfac-d8c0-3fb3-9cda-4203e644edec | -2.89203 | -48.01677 | 2026-07-31 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README11.md)
