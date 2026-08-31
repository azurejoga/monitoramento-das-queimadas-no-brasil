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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0911848b-34df-37c9-b4c6-b1668992ab8e | -16.21639 | -43.02742 | 2026-08-31 16:48:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2a72e3d4-e4ab-359a-a069-53a67c4ed5d9 | -14.96816 | -54.56843 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f4682f3c-bb93-3229-860d-3f7b74bf2617 | -14.79242 | -48.74751 | 2026-08-31 16:48:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4ed9b78f-50a7-314a-9184-98353f0b32ab | -15.97385 | -55.96196 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 04792209-c34d-3310-9bfe-a6817a73c940 | -18.12636 | -51.6118 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 140d8e8c-6527-39ce-ab35-b44c8a3ef9a8 | -18.26186 | -52.73434 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 12ba2f93-3c1a-3d92-bc4a-3c8a1c7090f9 | -15.6533 | -56.38111 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 490dbf97-1648-34d2-83d4-ac69bb858c23 | -15.58518 | -42.07817 | 2026-08-31 16:48:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec5e33db-ed41-3b0b-a17f-453fac68793d | -14.46699 | -53.3312 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cf8ff4b5-464f-3b4e-b43b-a1507b99546c | -17.53059 | -52.55027 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07e57bf1-8318-3a8c-ad58-dc6d82b627c4 | -14.41508 | -53.0953 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b5c24cb4-c76d-3da8-af6e-92949e2f6750 | -15.04275 | -48.09929 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 3d4832ac-22b8-300b-b2bd-e5567bd28038 | -17.88554 | -52.09003 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 195.1 |
| f3684ab1-0052-3e2e-9289-4cf4f9a8cafa | -14.57894 | -54.10398 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9dec8844-995f-3985-bdf9-962cb0576903 | -19.11355 | -57.37687 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| c9f89deb-1970-3a7d-881c-c178f79c7128 | -16.28327 | -42.5815 | 2026-08-31 16:48:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 55829218-0f5d-3785-9b2f-e2460e411f73 | -15.66397 | -56.3796 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f4e9771f-c11c-360a-ac31-d78c0996dbb4 | -16.54466 | -49.42146 | 2026-08-31 16:48:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b864f672-eafd-3a7b-a07e-d6191034a736 | -17.27726 | -41.75389 | 2026-08-31 16:48:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 27371b65-3079-3b12-ba3b-e549a96f3f19 | -10.1087 | -50.2776 | 2026-08-31 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6c39f46a-9dd7-3893-822c-a7022b51b4f9 | -10.7856 | -50.5066 | 2026-08-31 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f8c54338-f204-3b9c-a3f2-042afa80f657 | -3.9707 | -60.0258 | 2026-08-31 16:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c248795b-7a53-3466-b04d-b0c6974e3954 | -8.574 | -66.9569 | 2026-08-31 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 07671aaa-4b03-3c74-a9ba-42898938ae3f | -6.9872 | -59.2582 | 2026-08-31 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6d132d9f-d862-3935-8b77-8266e339c595 | -10.8617 | -50.4772 | 2026-08-31 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 89b08b34-38a9-31de-b917-04da9f36575f | -9.6939 | -65.1145 | 2026-08-31 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.6 |
| c9e8936a-b681-3572-868c-f986318aab2c | -12.1711 | -50.5432 | 2026-08-31 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c9ecd773-19b3-3991-99c7-4e1ce995b6ce | -6.8386 | -59.4379 | 2026-08-31 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 08217df1-bd67-3486-81ab-c501699180bb | -12.3615 | -50.5632 | 2026-08-31 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| e62a2ac2-0364-34c4-a560-34bf5902ab07 | -3.1998 | -61.161 | 2026-08-31 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c7fa9f24-4244-314e-ab40-f5b1dcc69010 | -6.8599 | -58.9351 | 2026-08-31 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7778ec66-d43d-39b9-94e8-3cfbaf3651b7 | -8.631 | -66.5473 | 2026-08-31 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f29c356e-aa3f-3327-a00b-68051d0e0143 | -10.8025 | -50.6539 | 2026-08-31 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| b23280de-3da5-3c00-9404-9b05a936b98b | -9.4342 | -45.6704 | 2026-08-31 16:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 70088fd4-e893-3a2c-b6bd-81e1ea91192b | -7.2933 | -60.5905 | 2026-08-31 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 62bc0090-e331-3afe-91c8-31d9395278a9 | -9.0057 | -65.456 | 2026-08-31 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 3cd16b48-fa20-36b9-80b4-51e3f1aec326 | -3.6399 | -60.5466 | 2026-08-31 16:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2b1d7746-653b-34c0-9a00-0fe409160059 | -10.1528 | -45.7665 | 2026-08-31 16:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 1e64d9d1-31f2-300a-95ba-e7fc9686b715 | -9.694 | -65.0958 | 2026-08-31 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 00d8f785-1691-3724-a85a-c9b493d229af | -11.1995 | -55.1008 | 2026-08-31 16:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 58bb0ebc-d807-3b53-8950-133df06f41b5 | -8.5555 | -66.9574 | 2026-08-31 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 97175e4c-b109-361f-80bb-114bdff43d59 | -3.4002 | -61.3276 | 2026-08-31 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 4614bfa3-9bf2-32d9-a1ca-63ebd414e2ab | -13.4707 | -57.0574 | 2026-08-31 16:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 153fd2bb-1d62-3413-9892-ec476303405c | -10.7428 | -50.8727 | 2026-08-31 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 50dedb62-b8f5-3583-b057-f8a56ee10e31 | -5.9636 | -57.6704 | 2026-08-31 16:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 43580d60-7c54-3251-9f86-6d9b8a0fc1e0 | -8.87 | -66.8935 | 2026-08-31 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5d434d70-0d46-3b6f-9942-0a3610d2195d | -8.948 | -62.3894 | 2026-08-31 16:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9fa1900a-dac5-38de-a5b8-dcd38ccf8f88 | -3.9708 | -60.0067 | 2026-08-31 16:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e3589a4c-6466-336f-a3a2-20b95a9cad2e | -11.1726 | -51.2728 | 2026-08-31 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f22d925a-6b96-3f23-8635-b4d40714e74b | -10.8614 | -50.4985 | 2026-08-31 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f1529fe9-8699-370c-a222-5aaaeb54a188 | -9.4156 | -45.6499 | 2026-08-31 16:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 291.2 |
| 33b3b8fe-82f0-31ce-8733-20ea6bcd3909 | -10.8212 | -50.6732 | 2026-08-31 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e27fa6c2-92d6-3133-a869-78b1777dd9bb | -10.1538 | -45.6982 | 2026-08-31 16:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 793905f5-07cc-3d0b-8b9f-1b280c0735f6 | -6.1295 | -57.6637 | 2026-08-31 16:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 88eacd52-07c5-302b-82f8-a53ea0d46916 | -10.7644 | -50.6792 | 2026-08-31 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 806a500c-f62a-385e-866b-a63c9af471f1 | -10.8046 | -50.5046 | 2026-08-31 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2bac46d6-08f6-3906-a1ef-fc887075a4e1 | -11.1916 | -51.2708 | 2026-08-31 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d0b39af8-c135-3b3e-8637-db306e0c9e04 | -10.802 | -50.6965 | 2026-08-31 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 7cfb73db-e018-3284-87d1-faa6292aa14a | -8.5739 | -66.9754 | 2026-08-31 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 3886fc74-6201-3f80-b18d-9d574dca9b49 | -10.1531 | -45.7438 | 2026-08-31 16:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| bc10fcdc-b3ba-3269-bbc5-6221402977e6 | -13.4516 | -57.0592 | 2026-08-31 16:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| be1ee5fc-abaa-3acc-8277-550e3268d3d2 | -10.5793 | -50.3789 | 2026-08-31 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 767ee337-fa55-3c8c-8af3-959523d251f2 | -10.783 | -50.6985 | 2026-08-31 16:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 4017ee6e-6ee0-33fc-bddb-256f93eaf6e6 | -9.4345 | -45.6477 | 2026-08-31 16:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 1d4335f4-1b09-3d22-9a4a-736d0bdfa7e6 | -13.62742 | -51.84149 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 88141ad9-f26e-3e1f-a2ef-4c0a505b2c4e | -6.99627 | -43.67534 | 2026-08-31 16:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e25fd877-8158-324f-baee-c5d606c76fa4 | -8.50366 | -55.34734 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0a8e9498-d0a8-3eb1-8581-7124944d5927 | -6.40662 | -49.93018 | 2026-08-31 16:50:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6d4b40cd-fa01-3b3d-a46e-b58c4476a73b | -7.8211 | -35.20687 | 2026-08-31 16:50:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 77420c7c-efa1-388a-87bc-4d36d21a1acd | -9.15823 | -45.80311 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 59bd4b8a-0d27-3ee6-a7d4-2fe78b8d270f | -7.35683 | -45.0878 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ee20d68-c1b2-30a1-a1b8-338348344837 | -11.17856 | -55.08622 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ddb783e4-8e98-3f5b-989e-526dee32331c | -11.23183 | -45.13905 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 1f62b75d-2c81-3f4a-a64f-11ec8363d4a0 | -6.87133 | -47.99657 | 2026-08-31 16:50:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3f2ad31d-5413-3218-8ab4-e180eb42029a | -11.52256 | -46.94927 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ce28426a-3698-36c2-bfcb-a8d8cdd0c8ef | -10.98703 | -49.6895 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05508025-acc2-3817-8c27-b884a1371362 | -11.25091 | -51.25648 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 234c68c8-95ed-3b5d-8afb-250b64d9eed2 | -11.71196 | -47.62606 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fff65ca8-543f-3fe9-8f99-7543c690f098 | -13.54029 | -59.75176 | 2026-08-31 16:50:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 3f9e6b39-cf81-38be-b626-9e089faa9b64 | -9.16815 | -59.36597 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| fed08387-ac39-33f2-ba2d-8a39f8844a96 | -6.81445 | -43.50543 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5074e878-7a2d-36f8-9ad1-e4f6595ebe11 | -11.18379 | -55.09037 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3bf7248f-42e5-3710-9b01-0cc190ea6d1d | -10.31232 | -50.0033 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 255.2 |
| 7953dda5-4d40-3d0b-ac87-b0a2d4d6f0c2 | -9.21353 | -51.56576 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 55dedfef-a554-3caf-9969-db6ca8d48b1b | -11.63611 | -49.42099 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| efd260ed-1876-3503-a01d-55d97f050147 | -8.93211 | -45.02627 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8dab4086-3fed-37d7-877f-deb703b3c460 | -11.65755 | -55.68808 | 2026-08-31 16:50:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3a38a649-e6f2-36fd-bd9b-5a5bf10baa34 | -9.66604 | -47.93806 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 517e3977-483d-330d-bfd8-235d67e6dafe | -11.8176 | -41.3182 | 2026-08-31 16:50:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 2a56efa3-c3e6-3f42-8cea-fee48b85ca06 | -7.25053 | -39.21635 | 2026-08-31 16:50:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| cbf712b7-aca3-3e9e-ae21-b52937d8878c | -7.35153 | -55.18887 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 10ad47f2-70d7-3d66-9d01-387670be8bbd | -6.81179 | -43.54088 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| dc0a090a-7310-3feb-8597-e5468f18ac09 | -9.15182 | -45.80829 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 252b1559-0fe3-315c-ac7c-eff02c9456ef | -11.37624 | -45.20465 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3f0106ae-e64c-30e4-8d1c-f83f76bdf8e6 | -7.53607 | -57.80393 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c480bc2-48e9-396c-8317-2fe134bae50b | -11.1792 | -55.09106 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b8e7ec44-b87b-3359-9c7c-2a47c7e12ebc | -12.75802 | -49.27863 | 2026-08-31 16:50:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 17a2f859-7dd5-3c5d-9654-317dfb6b10ab | -11.79525 | -44.88716 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e72dfd02-1033-3a7c-8ad1-5213f86448b5 | -9.47415 | -57.01297 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a8f1bdba-fbf7-33e2-a800-ff109f434492 | -12.10544 | -45.03074 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README148.md)
