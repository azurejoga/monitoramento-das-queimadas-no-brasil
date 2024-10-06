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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 929f0662-6a68-338d-b0f8-57281b282aa6 | -13.8749 | -44.6093 | 2024-10-06 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 9acb1a28-9600-36e5-b172-11530633e685 | -13.8943 | -44.6058 | 2024-10-06 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 64dda9a4-c43b-3b0c-8c62-167bd556136a | -18.659 | -57.2552 | 2024-10-06 12:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 102f1586-ebf0-335b-8782-dcbe6013215c | -10.443 | -50.691 | 2024-10-06 12:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 2c052fa4-86aa-39c7-a1c2-c65abaf81c02 | -10.4238 | -50.7142 | 2024-10-06 12:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 356.5 |
| a95adbbc-da72-3a65-b9cc-233365eb0ba3 | -10.4241 | -50.6929 | 2024-10-06 12:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 162.8 |
| b4b545da-6ed9-36ca-ae89-abb7e733445e | -10.4235 | -50.7355 | 2024-10-06 12:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 140.3 |
| d1cf342b-fde8-3119-928c-73f1d74d6928 | -10.4049 | -50.7161 | 2024-10-06 12:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| dd9e3a10-5b31-3453-ad48-f9690a7bae6e | -11.4238 | -47.1815 | 2024-10-06 12:26:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 8b730cd5-e2a1-311d-a8ea-e2e0cb31480c | -12.42 | -47.0453 | 2024-10-06 12:26:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 8f888ab2-de1f-3a0f-87c1-397bd610dcd0 | -12.4689 | -47.5312 | 2024-10-06 12:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b5f29be5-b589-3eea-b00a-882349a26b62 | -12.4878 | -47.5509 | 2024-10-06 12:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 78c1b0e9-79b9-39ca-934e-9d286690383e | -12.4874 | -47.5732 | 2024-10-06 12:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| fbc23add-8be9-385e-98cc-74295fa72073 | -12.5066 | -47.5705 | 2024-10-06 12:26:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 288d9dbf-8f92-35fc-910f-9a4965d76b38 | -13.8943 | -44.6058 | 2024-10-06 12:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 7b6d5a01-b2d0-30c1-a66c-16fba199b3d9 | -14.0689 | -45.5308 | 2024-10-06 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a4ec9dcf-0c24-3257-bc5b-d92566383d85 | -14.0883 | -45.5274 | 2024-10-06 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 250.3 |
| 95b90ec4-79cd-361d-8c95-5ba44f2e77bf | -14.0888 | -45.5042 | 2024-10-06 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d1a893f3-3454-3664-a102-19ac31ba6c60 | -14.0879 | -45.5507 | 2024-10-06 12:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 1f04685b-b744-35be-b2d8-ff4769151215 | -15.163 | -48.0561 | 2024-10-06 12:26:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c8550a6b-f827-3550-aadd-377bca60a499 | -15.1635 | -48.0336 | 2024-10-06 12:26:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 226.6 |
| 27807f43-678f-3869-80ad-73d9969dc299 | -18.6387 | -57.2785 | 2024-10-06 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 562622e4-b51d-3edf-b960-069ecdfbb93b | -18.6785 | -57.2734 | 2024-10-06 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 061cca9d-a45d-3bbe-adc2-63125b736d31 | -18.659 | -57.2552 | 2024-10-06 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 190.7 |
| 3f04825c-9246-3556-86d1-a8c2191fc4ed | -18.6789 | -57.2526 | 2024-10-06 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 48b98205-a812-3c40-b11c-2cbd2fb31aa9 | -18.6586 | -57.2759 | 2024-10-06 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.8 |
| 0dfb0b66-97ec-349f-b14d-24f3b139cf09 | -10.4235 | -50.7355 | 2024-10-06 12:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 769c4d3d-8dd2-376f-b224-344dacb8c453 | -10.4241 | -50.6929 | 2024-10-06 12:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 035ccd94-2d40-30e2-b140-ab8c8f7a63b1 | -10.4238 | -50.7142 | 2024-10-06 12:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 387.4 |
| 3f0e2b8a-ce44-3b49-a61a-9a15971e63cc | -11.4238 | -47.1815 | 2024-10-06 12:36:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 0c9c49f6-f563-3a22-99ed-8202e837cac0 | -12.4874 | -47.5732 | 2024-10-06 12:36:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 1003b24f-4cab-30bb-9b1c-34f91173c8bc | -12.5093 | -45.3017 | 2024-10-06 12:36:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| a295597d-4d8e-3fa4-93a3-ac9fe4dd8fb4 | -12.4878 | -47.5509 | 2024-10-06 12:36:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 7beae9d4-3b5a-35ed-acb8-47a15a53059b | -12.4686 | -47.5536 | 2024-10-06 12:36:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 8b3fa07b-2ef7-330c-80e3-ca92e48aebb8 | -12.4689 | -47.5312 | 2024-10-06 12:36:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 83e15e6e-bd9c-3ae3-abdf-de23b545053f | -12.42 | -47.0453 | 2024-10-06 12:36:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 8a02be5f-637e-3258-8e5c-cb445fc963be | -12.5066 | -47.5705 | 2024-10-06 12:36:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 8e322d1f-5549-3169-a7fa-365b1b26e81c | -13.8943 | -44.6058 | 2024-10-06 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| c58d3955-86bc-34e9-a3d5-88c2b74c21dd | -13.8749 | -44.6093 | 2024-10-06 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 9d8a9b18-7b9d-375d-8e02-db81825b10d9 | -15.1635 | -48.0336 | 2024-10-06 12:36:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| f65e39c6-013d-3848-93a2-b6c6e85f455c | -16.9092 | -47.1724 | 2024-10-06 12:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 3cc53a87-1572-320c-bb79-e126e296d11f | -6.9514 | -59.0666 | 2024-10-06 12:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 85342938-0e45-32c8-af94-6438308e4ef5 | -9.9355 | -47.6937 | 2024-10-06 12:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| a8647793-346b-3779-bf79-3d2bf3266c0b | -10.4235 | -50.7355 | 2024-10-06 12:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 172.7 |
| babbeba1-4dac-3085-8caa-a0097dde50c6 | -10.4049 | -50.7161 | 2024-10-06 12:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| dfe1ccdc-8110-3a6b-b2d5-d82e8078ac1b | -10.4241 | -50.6929 | 2024-10-06 12:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 156.5 |
| e513e44c-0ac9-35c3-ac1f-535d5be55fc8 | -10.4238 | -50.7142 | 2024-10-06 12:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 412.6 |
| e82f95f2-17f3-3687-a284-2b6cdb80e3b7 | -11.4238 | -47.1815 | 2024-10-06 12:46:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 35c039a5-627e-306a-b8a3-d8c3f80549ad | -11.6857 | -45.2411 | 2024-10-06 12:46:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ae94366b-e490-39e5-a5e2-bd0ea61ed468 | -11.7187 | -47.8107 | 2024-10-06 12:46:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 7232dfa4-0558-338c-9bd0-b3a3b30bd092 | -11.6665 | -45.2439 | 2024-10-06 12:46:12 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| cbb9d36a-85f1-3285-8cf0-9fa9ff1ca386 | -11.7378 | -47.8082 | 2024-10-06 12:46:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| c9f90ab4-28d9-35ab-8696-4dae34376afa | -12.2543 | -45.5937 | 2024-10-06 12:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e7877286-528e-390a-8411-aee194556363 | -12.4686 | -47.5536 | 2024-10-06 12:46:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 4c996b4b-4bb8-3349-bbcd-b388f07f0b91 | -12.5093 | -45.3017 | 2024-10-06 12:46:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2954deb6-f979-3800-81c2-c72445a2b1aa | -12.4689 | -47.5312 | 2024-10-06 12:46:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 8e2a839a-07cd-30c1-b6fb-93e83f0434e3 | -12.42 | -47.0453 | 2024-10-06 12:46:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 655f64d6-7bf7-3441-a815-82c0946e106d | -12.4878 | -47.5509 | 2024-10-06 12:46:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 6a741e60-2dc5-3815-88d2-2c626e288d00 | -12.4874 | -47.5732 | 2024-10-06 12:46:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 36706056-aa85-30e5-8f6a-addd63aa5788 | -12.5066 | -47.5705 | 2024-10-06 12:46:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 208.8 |
| a4d18cc9-a235-3ef6-9b65-e176ae99e7b9 | -13.8943 | -44.6058 | 2024-10-06 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 9509ac39-d4d5-3f0a-a6fa-fc7d3d54a147 | -13.8749 | -44.6093 | 2024-10-06 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 5a890d8a-8f2b-347b-936b-86d5db24a841 | -14.0879 | -45.5507 | 2024-10-06 12:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 287.6 |
| 5c732440-60b1-32e6-9f0a-a73da8a4cd60 | -15.1635 | -48.0336 | 2024-10-06 12:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 168.9 |
| b42db8e4-cac3-312f-9050-276e1d072c29 | -15.1435 | -48.0594 | 2024-10-06 12:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| f0f15001-2635-31a6-8f4c-f26023f159b6 | -15.163 | -48.0561 | 2024-10-06 12:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cafc0973-6661-3f2e-97be-51225af30944 | -16.9092 | -47.1724 | 2024-10-06 12:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 940e862d-9ed5-3ee8-8ea7-7804bdc191c9 | -16.9098 | -47.1493 | 2024-10-06 12:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| bf12d3d0-8ee5-34dc-ab31-b897fc4253ac | -6.9514 | -59.0666 | 2024-10-06 12:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 94cbab6b-7824-356f-9276-719af70cccc5 | -8.1478 | -44.4171 | 2024-10-06 12:55:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d508cee3-cf72-3bae-bf41-8b8dbb2b6c7c | -10.4235 | -50.7355 | 2024-10-06 12:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 2af1ef73-76cf-3834-aed1-529f0e0f2260 | -10.4049 | -50.7161 | 2024-10-06 12:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 179.8 |
| ee7163aa-81b0-3bcb-b1ee-351e150dddba | -10.443 | -50.691 | 2024-10-06 12:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| aab7226a-9b3b-3f63-8c18-560c4b5f3997 | -10.4238 | -50.7142 | 2024-10-06 12:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 343.9 |
| b46a3774-8446-3010-ac4e-e2fa96c8ad2b | -10.4241 | -50.6929 | 2024-10-06 12:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| beb1c0a5-a4f1-32d1-bc7e-2e90a814c5b2 | -10.9044 | -50.1304 | 2024-10-06 12:56:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| abbc597e-7227-35d7-8148-80eb34f4af2b | -11.297 | -46.7724 | 2024-10-06 12:56:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 4f9a6d01-18b5-3c09-a066-858cef0bfd5a | -11.4238 | -47.1815 | 2024-10-06 12:56:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| e2df7fa0-a6a7-3d85-aa79-a6dd7d16148b | -11.7378 | -47.8082 | 2024-10-06 12:56:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 56ed85fe-9416-36eb-afb7-543051cb2f6f | -11.7187 | -47.8107 | 2024-10-06 12:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| dbc481a2-f384-3d0d-ad13-7b11950964d2 | -12.4689 | -47.5312 | 2024-10-06 12:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| bfd46b92-628f-397c-bca3-df696077dd21 | -12.4686 | -47.5536 | 2024-10-06 12:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 91cb4615-c0e3-3061-8c64-541aeb8b4bf4 | -12.4878 | -47.5509 | 2024-10-06 12:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| c11fbef3-704e-3521-aab5-dbcf459d59fd | -12.5093 | -45.3017 | 2024-10-06 12:56:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 1193dc07-ad1e-3505-9a0e-5162dd719db3 | -12.4874 | -47.5732 | 2024-10-06 12:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 2904eb31-c47f-3ac3-b66d-42a0de718de3 | -12.4497 | -47.5339 | 2024-10-06 12:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4278f959-61a6-35d7-8f45-c1bb63849f5d | -12.42 | -47.0453 | 2024-10-06 12:56:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 356e9f6a-9d50-3f82-bdef-fec7f5d06ad4 | -12.5066 | -47.5705 | 2024-10-06 12:56:17 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 5f8b99da-17cf-3381-903d-ea7e69399d2c | -13.8948 | -44.5823 | 2024-10-06 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4f877bab-783d-3c4f-8748-d6e11eaead5f | -13.8749 | -44.6093 | 2024-10-06 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 61d8b92f-e35d-309e-b25e-d863a647d135 | -13.8943 | -44.6058 | 2024-10-06 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 7d1f470c-6ce8-3879-975d-f4845c7fb7fa | -15.1635 | -48.0336 | 2024-10-06 12:56:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 2dbbe4ca-5725-3b22-adbf-1ccf18895069 | -15.163 | -48.0561 | 2024-10-06 12:56:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e5122800-f5f1-38a7-b5f5-7e6123726dbb | -15.1435 | -48.0594 | 2024-10-06 12:56:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 65e5ce05-f66b-3b3c-aec8-d3a327cf070a | -16.5474 | -49.2058 | 2024-10-06 12:56:39 | GOES-16 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 27a2c882-86e7-3517-80cf-f4c1cec05a73 | -17.6545 | -44.4097 | 2024-10-06 12:56:44 | GOES-16 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 949fc9f4-6fda-3d0a-855b-983f4e17e390 | -14.09 | -45.58 | 2024-10-06 13:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37c9750f-1991-3cb2-9594-da0d09365df1 | -14.09 | -45.53 | 2024-10-06 13:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02ea6274-4b5d-3c13-993d-6096951e54de | -14.12 | -45.54 | 2024-10-06 13:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ce647d9-c56b-31a0-bb08-35722c917a3e | -6.9699 | -59.0658 | 2024-10-06 13:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |


[Clique aqui para ver as próximas entradas](README161.md)
