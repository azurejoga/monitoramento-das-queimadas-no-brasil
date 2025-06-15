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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e23a608-883d-3c9f-997f-141d4898d63a | -14.82971 | -48.42971 | 2025-06-15 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cdd449b-ddca-3800-9e64-eab3a3d9b65c | -15.40129 | -47.87934 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0def54cb-0def-3655-af85-25be739eb557 | -15.3954 | -39.33145 | 2025-06-15 03:34:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 65697086-e60a-38f8-bc78-55c5e515928d | -15.40811 | -47.88104 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8e1c96a-24b6-3360-be6e-838727ad58a9 | -14.82808 | -48.43679 | 2025-06-15 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78a8174a-b7ce-356d-97f5-4ea4425bdbf9 | -12.7627 | -44.40765 | 2025-06-15 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5031c4ef-2d7d-3952-8c69-ab06ae13d2e2 | -12.76769 | -44.41323 | 2025-06-15 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0295cee0-b69a-398a-b16a-92bd704e6402 | -15.41115 | -47.8673 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e8fc656-bd4a-3c83-b4ad-e4923ce30ec5 | -12.76856 | -44.4089 | 2025-06-15 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6bc2d0d-2553-3f60-906b-c714d587e5a4 | -15.40588 | -47.85862 | 2025-06-15 03:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6eb915fb-b802-3ded-91cd-fb04ee602ddf | -22.90241 | -43.75519 | 2025-06-15 03:36:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d8e5034-4400-37cc-8cee-e39e3d8664c8 | -13.9059 | -54.6291 | 2025-06-15 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 884c08a4-e6e8-3cb5-b80b-174d6d9591d6 | -13.9062 | -54.6084 | 2025-06-15 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 172.7 |
| cb0b781b-1724-301f-b52f-6dc17c885152 | -13.9254 | -54.6063 | 2025-06-15 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 225.2 |
| ec3c1668-ffa7-32a1-9705-5d469cd779d6 | -9.4158 | -48.4504 | 2025-06-15 03:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| bb662d19-fb9d-396e-9751-0b13bd85ddca | -13.9251 | -54.627 | 2025-06-15 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 145.9 |
| cecfaeb5-b3cb-333b-9642-0e45c9a42a14 | -13.9251 | -54.627 | 2025-06-15 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 3a96641f-4fb8-3244-9bf7-73298be39e6b | -11.0113 | -55.0764 | 2025-06-15 03:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6902326f-ac4e-319f-bd13-f54625706426 | -13.9254 | -54.6063 | 2025-06-15 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 261.1 |
| c886180c-75e1-301a-8608-09eb55c984e2 | -13.9257 | -54.5856 | 2025-06-15 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 1360fbaf-9ded-3543-948e-8244b053247c | -13.9059 | -54.6291 | 2025-06-15 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b3768901-1dc4-3e99-a24e-5a75ac5d94cf | -13.9065 | -54.5878 | 2025-06-15 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 45e06fd1-0c3e-3c71-a37a-88a7f4be01b5 | -13.9062 | -54.6084 | 2025-06-15 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 253.7 |
| d6b0d715-5f4b-3016-a243-dd3b86cc52ab | -5.17004 | -37.84994 | 2025-06-15 03:51:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ec2d069-3765-3d03-a759-b49960287522 | -4.4316 | -46.11274 | 2025-06-15 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7da9aacd-fac3-3ed6-adac-5a04db036a45 | -5.62351 | -43.99854 | 2025-06-15 03:51:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 084ea148-220a-30a0-a86f-141910307eb9 | -5.62213 | -44.00117 | 2025-06-15 03:51:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd86282e-4d93-3a9f-b6db-3c0639c166ce | -4.49385 | -43.77451 | 2025-06-15 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8549f7ed-2c8e-3842-acc1-e1181f4417b0 | -5.63847 | -44.11114 | 2025-06-15 03:51:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f54f15b-315d-3f7a-9814-bb3893bf9cff | -5.20955 | -35.75748 | 2025-06-15 03:51:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd403be4-69e5-3633-a99e-e3ab37dcf9d1 | -5.1728 | -37.85391 | 2025-06-15 03:51:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7931f301-bc7e-39b3-8043-42bb79c77702 | -4.40034 | -42.15545 | 2025-06-15 03:51:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fcb20dfc-1f40-3f23-8d7e-93c7c6c29bb6 | -5.61862 | -44.00171 | 2025-06-15 03:51:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09e49e07-7359-39e6-8b90-13c0beb40d44 | -5.16949 | -37.85339 | 2025-06-15 03:51:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 32eba6ef-b09b-3996-9e54-9f26621389da | -4.3965 | -42.15481 | 2025-06-15 03:51:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 617f3847-e131-3c6b-a9b9-d1ff0b0f3814 | -4.57653 | -37.82375 | 2025-06-15 03:51:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d20c6a75-6b0a-350e-9277-884bd54c7685 | -4.43109 | -46.11576 | 2025-06-15 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94dfcd0d-337d-362a-9ad0-a7914929f6ab | -5.61927 | -43.99778 | 2025-06-15 03:51:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ea5ecf3-b1c3-3f5a-84e7-39685bd461e9 | -5.07048 | -43.72372 | 2025-06-15 03:51:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e69ae883-8c18-358f-af4f-60fc6db2471c | -4.49317 | -43.77855 | 2025-06-15 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b26cfbbc-689a-3e31-a6ad-6438e3cd832f | -4.71927 | -37.77908 | 2025-06-15 03:51:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc64894a-d44d-37aa-b572-ff76c7b63d50 | -5.63916 | -44.10709 | 2025-06-15 03:51:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd9c00f5-83d1-3771-99c9-1774fb888765 | -5.6228 | -43.99726 | 2025-06-15 03:51:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2786832b-3f64-388f-ae0d-b5785612b74f | -8.96261 | -47.97385 | 2025-06-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1987407-f62f-3143-ba73-79c8e6d34a69 | -9.67523 | -48.6089 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f9c6d30-f146-302e-a7e2-08083b72fee5 | -9.40127 | -48.43085 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcc2f262-e86c-3f31-8fad-b4d9f3e13464 | -7.21106 | -43.60256 | 2025-06-15 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48b86e92-6dca-3c1b-8c45-a729d5c2cff8 | -10.63321 | -49.42775 | 2025-06-15 03:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66068ee1-a555-329c-8770-753834e6a35f | -8.96322 | -47.97054 | 2025-06-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02d959fa-b918-39f7-9917-746970cb8834 | -11.1823 | -44.49006 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46c04d3a-fdcb-3ac7-a2f8-cc8be0e62adf | -6.21261 | -43.33138 | 2025-06-15 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b874c3aa-fc65-3198-8410-063e30bc111c | -10.45545 | -47.95146 | 2025-06-15 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c7a7fb2-c350-3d92-a0a7-e231be4dd622 | -9.42017 | -48.44873 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c28ee2a2-93fc-34fa-9ab6-ba34efdaffd9 | -10.08731 | -52.74322 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 25f1af84-cd3c-3362-857c-24df2ef4af85 | -7.10989 | -43.42995 | 2025-06-15 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4db377e5-699c-33ca-8f4a-cdc46046ec3b | -8.36894 | -47.05153 | 2025-06-15 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2962ecf6-2c9f-3c99-bccf-57b54f1335d9 | -7.20822 | -43.10412 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9a6f1df4-6bee-3a85-b565-df28c4ff45ba | -8.30539 | -46.20205 | 2025-06-15 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7411753c-06aa-3408-8c84-3b5aa3ecde41 | -10.74396 | -48.57328 | 2025-06-15 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63567dec-c094-3702-b4ec-7546d6960b89 | -11.57558 | -47.87177 | 2025-06-15 03:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0097e755-0a40-39a1-9e40-087a1e14fcdc | -7.23218 | -44.15794 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a8ea491-d35a-3ac3-b599-2754a466dbac | -10.65699 | -49.36475 | 2025-06-15 03:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0515d68-d482-33fe-90c9-bc08d0f55342 | -10.07905 | -52.74846 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95e8d06c-136e-3e18-b275-3b9b95556dae | -7.23059 | -44.16198 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fa47955-2c05-3533-a0ee-27a2ebb73834 | -10.63247 | -49.43156 | 2025-06-15 03:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4f68fdc-d210-3946-8b61-5c38f6cb6ab6 | -8.31011 | -46.20291 | 2025-06-15 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b9457058-1553-3f39-8ec8-89ecaa69b456 | -11.18813 | -44.48018 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8ccf567-0e49-3d86-babc-074286b36485 | -8.6471 | -48.90007 | 2025-06-15 03:53:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 971ae30e-73a8-3fd2-9c0f-78c3c4a3da9a | -6.83798 | -43.41267 | 2025-06-15 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 20c84109-b137-3ea1-bd50-ba206d0148c5 | -11.57006 | -47.87361 | 2025-06-15 03:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dea85ea4-c687-3adc-820f-8e490e8ca0a4 | -10.62759 | -49.42673 | 2025-06-15 03:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 000cf40a-fc0c-3303-9a81-2f21f7ff66a1 | -10.14665 | -46.70378 | 2025-06-15 03:53:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c430d4e-0f6d-32e8-b677-31a6d9ed55d8 | -11.18814 | -44.48632 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0ea384f1-d5d1-36af-8c51-a92ce76e95e1 | -8.31483 | -46.20376 | 2025-06-15 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3049e286-8bdc-3e5d-942f-704bbb0bdf04 | -10.2779 | -47.60907 | 2025-06-15 03:53:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae1a6cd2-360a-3a7e-8936-b93e89411d49 | -10.16645 | -48.56422 | 2025-06-15 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae213e43-c432-38e6-bf44-b21e9d53cee5 | -10.08807 | -52.74365 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 61324484-7bfd-3ac5-b2c0-a34506fa24ff | -7.96651 | -45.47816 | 2025-06-15 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b08cf8c-fc79-3375-afda-369d222480bd | -11.18691 | -44.48727 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 44939b8e-b3b1-3b0c-8c06-0f7d79fb8890 | -10.14617 | -46.70195 | 2025-06-15 03:53:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbe1b5b1-2c73-3d35-8e36-9c759b9e814e | -9.03947 | -47.02082 | 2025-06-15 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7fb35cf-ba21-3256-a5a2-3f718148ff1e | -9.68065 | -48.60987 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b802d93e-7296-3b82-a588-8ad1d0847da4 | -8.5876 | -45.86245 | 2025-06-15 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3a6d504-660c-30a4-9b22-d9e6312cc06c | -6.83116 | -43.4043 | 2025-06-15 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 3ae588bc-75ea-3d0f-9ea9-16aa1d0ac782 | -9.41609 | -48.44079 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5ceba6b9-ab52-397c-8175-1fddcbcf152b | -10.07213 | -52.74712 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 349edd10-6245-35aa-a95a-ca7dcdd27691 | -9.67914 | -48.60886 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40858387-0b88-300b-81cd-f2d07ab15b02 | -10.50218 | -53.5794 | 2025-06-15 03:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c62d576c-9638-3631-9d3e-97436d2a4b9e | -7.17948 | -43.46663 | 2025-06-15 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0aa6fee5-9e75-3884-b9b2-554706eca3df | -9.41545 | -48.44423 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f120b20c-e451-3cf2-a8a0-0ae4b8a67893 | -10.23885 | -52.23838 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b6d5edd-917d-3cb6-b213-1531aa39a674 | -7.20653 | -43.11409 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cdee8934-5d3b-32f1-bfca-c58706d24af5 | -10.66257 | -49.36583 | 2025-06-15 03:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be5e42f2-ffef-376d-8772-6a99d882300f | -10.45271 | -47.95264 | 2025-06-15 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1979d6e-bcd6-3437-a957-0db82a433461 | -8.3734 | -47.05538 | 2025-06-15 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f76525d9-c36e-3cc6-9e07-3045075490b6 | -11.18752 | -44.48373 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ecf6b32e-3b84-377a-96be-593b3646aa3f | -9.04908 | -47.91515 | 2025-06-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d75fc51d-be38-3338-b135-d42e609c020a | -7.21045 | -43.11474 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6364ed50-78d8-335b-8f99-122b21f7456a | -12.23297 | -44.16528 | 2025-06-15 03:53:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8149f658-b535-3893-8ab0-e63f02d45a56 | -9.41414 | -48.45121 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README6.md)
