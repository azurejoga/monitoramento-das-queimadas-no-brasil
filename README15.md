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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 661fa81f-3c1f-3705-a133-c4c550adfffc | -7.22658 | -45.17639 | 2025-08-22 03:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaec4637-3953-340b-92d9-a202b15c201a | -6.43319 | -44.51538 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0556bb49-f711-360b-a637-793e6ac0596b | -3.8173 | -41.57294 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 175b4697-770a-33c6-b12d-1b9392cdecea | -2.45259 | -47.74818 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9125f24b-e49f-3864-b4e8-5b4f33e35fda | -5.6986 | -43.53483 | 2025-08-22 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f27a82e-00df-36af-983a-21b95a6ecd20 | -6.63306 | -47.9063 | 2025-08-22 03:55:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 173e50f2-6ad6-37a7-aeff-bd2275c9a97e | -6.28857 | -43.70271 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe6c3d32-9ed9-31d9-a1d0-6024a96195bd | -2.47379 | -47.76482 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b3b7ee6-8628-370a-9ddc-b3429df6de6b | -6.41299 | -35.02467 | 2025-08-22 03:55:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d0aa4d3b-1ba1-3e53-be33-0c14eb6331f7 | -9.71612 | -45.63038 | 2025-08-22 03:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 887997e0-68a9-34b8-8b62-d6437be82662 | -7.81136 | -46.8872 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a72c56ee-4751-3aea-8e18-bef75f3ef811 | -11.00487 | -45.63886 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aa5a802-356f-3860-a289-4f7f04faffb9 | -12.97276 | -42.53271 | 2025-08-22 03:57:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 539c1f39-7a5d-3021-bd9c-64043e14009a | -7.8573 | -46.99901 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6046a549-79fa-3b0b-93d6-8d770ae73f39 | -13.36763 | -46.26022 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6a02015-d99c-313f-b874-ea5dacb3e845 | -14.76423 | -45.41815 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07798165-b541-3dde-9035-b621a30941ae | -15.89101 | -43.45785 | 2025-08-22 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 92b08b84-e1a0-3fa7-942d-c3d172ba4766 | -7.86161 | -46.98756 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f7cd541-3811-3102-9575-e51a318232f1 | -12.96167 | -46.25568 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1396c0b7-67d3-3faf-84a0-53a4b367b141 | -7.85491 | -46.9959 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1946643d-ed8b-333a-8e69-fe13aaa7220a | -13.46299 | -47.05278 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd290bc3-b959-3a37-b193-2373f065cf79 | -13.02884 | -46.31409 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d5d0f55-abee-3625-aba3-8c3601413ff5 | -13.00231 | -45.23146 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a35e3b99-74a4-3aa0-b704-74ca4cb967e5 | -13.58037 | -47.0452 | 2025-08-22 03:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62680db8-ae22-3ac0-881d-ed8b77a2a919 | -10.72897 | -48.25292 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89caacc9-5d55-3df9-b070-7a402b7c8b33 | -12.95822 | -46.25683 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed70c47f-1e1f-371e-8b69-3d1f48d29cee | -8.21298 | -44.42879 | 2025-08-22 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be09fe90-ef31-386d-88ff-8c3fdc19cdff | -13.03021 | -45.17017 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81991a39-d78c-3ea8-90d7-e418013afa3d | -13.03776 | -45.1756 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7363423c-c648-3a10-a0e8-784fd77d09fc | -12.6031 | -47.0865 | 2025-08-22 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7858a8ba-15ef-35a1-843a-d0e914c880db | -12.92004 | -46.16518 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fceec04-5a6c-3df7-8a62-a2404dfdd98a | -14.88277 | -48.04904 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 053e9927-96f6-342c-9474-9952ba1650d7 | -10.18885 | -47.5605 | 2025-08-22 03:57:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04a11170-b952-30eb-ad4b-59d9b0553aef | -12.95359 | -46.28264 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6abd9934-12b9-3783-8ee4-5dbb5f9bacd2 | -8.90511 | -47.33647 | 2025-08-22 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2aa4343b-e6e2-3e14-bc98-f1d7aa6a6b48 | -11.81269 | -44.25624 | 2025-08-22 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c5fddea5-84b2-37e4-b14a-9fced53c3629 | -11.32787 | -48.3339 | 2025-08-22 03:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82b5cf23-136e-3643-92ef-d3f63c552874 | -14.88175 | -48.05416 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86381920-bfc0-36df-af77-add7765af9f9 | -11.44674 | -47.31081 | 2025-08-22 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5831bd91-acc2-3993-9e69-635f2a5a9865 | -14.76627 | -45.43001 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 389a52d6-ce9e-39f3-b145-1550638a0bcf | -13.64351 | -45.7135 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 681879ee-ed45-3fb2-bc90-a6b568a21108 | -8.79389 | -45.42594 | 2025-08-22 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e082398a-2ad1-3b5d-9233-6b7c8b05f532 | -13.46091 | -47.05457 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fba09ee-6c75-3308-9119-41e5dd489035 | -14.89617 | -48.0571 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 337fbd65-e746-3ebb-8cf5-ad0f9f2de9b0 | -13.02887 | -45.17776 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4c4577c-1580-39a5-ac87-8893c8e36439 | -13.02034 | -46.33563 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5eeb94e-de06-3053-b3ff-19aa44114eeb | -7.86181 | -47.00305 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4eed66a-40d9-3014-92e3-63e556d473f4 | -10.97486 | -45.60361 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4649b92a-b309-3173-a79f-b9e3c520e3b1 | -13.02409 | -45.18073 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d64e68e-9230-32ad-a54a-f80933a00310 | -13.03005 | -46.33275 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39192fb4-d80f-3d72-b59e-1a583ccb5b4f | -12.95921 | -46.26884 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fde2f63-3838-3b52-968c-47464c1c2fb8 | -7.85674 | -47.00206 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76294ab0-e676-34d9-97bd-ac7d158cc420 | -10.27647 | -46.75421 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31503953-4ae6-3a5c-8f53-79616343f66f | -11.1228 | -44.71837 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 216db80b-d917-3726-b361-7907dcd7dafa | -13.02807 | -46.31833 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcb9aa49-2817-33b2-9b4b-8a27476c8af4 | -13.00299 | -45.22766 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 67feb832-8b7b-30ba-b03b-1c4b2f8623df | -12.92438 | -46.16636 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0e7bd3f-64fe-37d3-aaf3-cf3ac65689f8 | -13.90411 | -43.88464 | 2025-08-22 03:57:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3724bf0a-b3e3-39da-9b8e-8481fba315d0 | -13.63987 | -46.88105 | 2025-08-22 03:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 448b41bf-31cc-3b71-a09b-30d47fec35aa | -9.64052 | -44.60683 | 2025-08-22 03:57:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a59b364e-ff5a-3c33-ac0c-fe00ebc64e7f | -13.35891 | -46.25814 | 2025-08-22 03:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aff9ff8d-af96-373b-99db-da2bd5de264c | -7.85333 | -46.99196 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a73c19e-ba46-36b7-a31b-58c293b64d10 | -8.11918 | -47.15058 | 2025-08-22 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b92d4e53-34ac-3c68-a2b2-fc028352f35d | -15.15104 | -48.11743 | 2025-08-22 03:57:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f662d992-1f0d-31df-9ad2-8de7af11ecc6 | -13.03432 | -45.17098 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf7f646c-3658-3391-a51d-9e649c7fd617 | -11.00419 | -45.63764 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a0ceb1f-9bf0-32e3-9c55-76efe84b836a | -14.46485 | -48.36096 | 2025-08-22 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 588c9c52-2e3a-38ad-8ab7-e7ec7152aab4 | -14.89244 | -48.0605 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2dd739d-8b97-393e-8bba-808d76dd2071 | -12.43747 | -44.70346 | 2025-08-22 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b03b8fc-cf13-37de-ac82-dbf4196ac472 | -13.6437 | -46.8858 | 2025-08-22 03:57:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74c71c1b-8592-356b-b4b8-0cd85a6a9368 | -15.5141 | -42.2112 | 2025-08-22 03:57:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79f14d63-73b1-311b-acb9-e70a1a39712e | -7.81453 | -46.86946 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe430413-d2ba-317a-aa36-713b44f76801 | -12.92361 | -46.17055 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a75d2ec1-9eb2-3031-95f4-ade7f4344c33 | -12.98646 | -45.22455 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec4c973e-3ca6-3b6d-9b38-d4375dbe7d21 | -7.86859 | -46.99466 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a794d7c9-eeb9-3488-9b10-8540bd23c759 | -11.28119 | -44.95016 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37c59b8b-4cd9-341b-9596-a2165637216b | -15.15279 | -47.95493 | 2025-08-22 03:57:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31364c4c-d414-30c0-979e-aac4834cc9b1 | -13.03498 | -45.16721 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9351b6e6-8ef5-3f75-a0ec-cbed3c9ec9d1 | -8.5792 | -48.54925 | 2025-08-22 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 509b573f-da70-35cc-93ee-724ec29bb829 | -13.38054 | -47.50148 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98739039-47e4-30f8-ad29-d9c37e648d8d | -14.97081 | -47.14085 | 2025-08-22 03:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e1ce5f52-879c-33e6-a344-474cc3f2f2e7 | -13.02117 | -46.33104 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0300d789-a907-3f69-b30c-d226cfbedd9f | -9.13686 | -46.38595 | 2025-08-22 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ebee574-f19d-3f9c-b07e-de7d18890c59 | -8.21227 | -44.43282 | 2025-08-22 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7535853b-9fef-3507-a8a3-3c8bb22b3f9d | -11.44087 | -47.31529 | 2025-08-22 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4ed77ce-31e4-303b-97da-fe139b4dcf47 | -11.29355 | -44.92911 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e257c10-a623-38ab-88d2-5941bf54cc73 | -13.03962 | -45.17498 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f6715c7-118f-351d-9c95-d50d7374b630 | -12.5871 | -47.09373 | 2025-08-22 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21381a30-72b5-3003-b9fb-7d32d7bd3659 | -14.49736 | -48.83298 | 2025-08-22 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ee21579-c13e-3cff-93dd-58680057034f | -10.28181 | -46.757 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bce3db32-92ee-3f4a-9a8d-3d95e5580ed6 | -14.86436 | -48.32164 | 2025-08-22 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dc179ec-16e5-3cae-bd60-fbdd75cd2d23 | -13.03842 | -45.17181 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f26bbe2-7e08-3f3c-a8aa-9c8f97d90a47 | -13.50154 | -47.06783 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2068a84d-05fc-3b06-8e8d-dfe7a0c28983 | -13.49971 | -47.05211 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86c0f9e1-1268-349b-90a9-425314f3a8aa | -9.13685 | -46.3817 | 2025-08-22 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65c4b03b-f138-3865-9438-996f0c45e996 | -13.14217 | -46.90372 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8bcdcf3-908d-3e2b-8159-ac4e3ff197e1 | -7.85786 | -46.99594 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58c1db9e-b8ca-344d-afb5-0f7b776cdc14 | -9.71531 | -45.63484 | 2025-08-22 03:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69db515b-6cb2-3c79-a389-b1a84308a81f | -12.99818 | -45.23068 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5fe221f8-5ab1-3aa9-a803-c2db3018e13c | -12.95205 | -46.25813 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
