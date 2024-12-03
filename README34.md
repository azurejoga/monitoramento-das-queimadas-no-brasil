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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6803387e-7415-352f-96fe-5b9df3085012 | -2.21911 | -45.56247 | 2024-12-03 04:27:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87332924-355f-3a6f-96db-3c30458bbb8a | -0.59243 | -51.68725 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb000395-dd55-3a4b-ac2c-48f8d9c63412 | -1.6105 | -45.54825 | 2024-12-03 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dac99835-5271-31d5-9537-d5a6aee10699 | -1.73019 | -47.05668 | 2024-12-03 04:27:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97528166-bbc4-3771-a620-6952d33717f5 | -2.09741 | -46.57964 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e586ae4d-d10a-306e-9cae-bec9f21c6b45 | -0.73092 | -47.53339 | 2024-12-03 04:27:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d6b6a16-85f9-37b9-8755-775c556a8529 | -2.22998 | -46.38512 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60545a33-199a-3bbf-a87b-e78c2aacffdc | -1.94284 | -45.55244 | 2024-12-03 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9f7f3d4-902d-3c60-871b-f8ef219a6ee3 | -0.82218 | -53.05659 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99f9f673-81e3-3c42-a864-73310aac9348 | -1.82346 | -46.59278 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb66e34-707a-3382-950d-784851539c72 | -2.12497 | -45.34727 | 2024-12-03 04:27:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f5bf15fd-ef34-35a5-bf22-89d63d4483c5 | -0.6123 | -51.69415 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6201025-372e-3157-a4e6-8da07325794d | -0.25995 | -51.49905 | 2024-12-03 04:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f79a080f-24bb-3cc8-a78d-b00dfbd136e9 | -1.96075 | -46.45623 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3b1183e-7ceb-327b-9299-60bd3f93c3f0 | -1.80268 | -45.55586 | 2024-12-03 04:27:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5726eb46-9a4a-3c95-9efd-0728e95b8e4a | -1.42369 | -47.29895 | 2024-12-03 04:27:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3575c47c-8e51-3b15-9a39-c710e952818f | -3.61848 | -54.57725 | 2024-12-03 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0c86429-796c-3617-8171-9555728bcb43 | -2.65467 | -46.57892 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 207bd321-6064-371a-9bf3-bca86f3b17dd | -2.62741 | -46.12473 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03f925e7-9c91-359a-8812-50cf0dc6191a | -4.80727 | -44.99453 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c302359-308c-3f39-a3c4-4707809d279e | -1.70039 | -52.60903 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b3e284b-ef12-3ad1-97b3-895b2a3b9932 | -2.97531 | -46.93905 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf54a3bf-0fdf-3a53-9a72-aaf39e3065ad | -2.66911 | -46.6164 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0606b445-d8fd-3f0a-8844-2edf1a123f79 | -2.4762 | -46.56834 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 773942e8-a54a-3e1c-adae-19eef3fdc2da | -2.82593 | -52.58533 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4eb76a97-466c-3600-8514-1b174c9fb29f | -2.67518 | -46.62086 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0dd097f-1bb7-3ae6-8391-eb78a63ae2ec | -1.3856 | -52.43688 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb49afd5-a30a-38f8-ab2c-6175c04f4023 | -3.55077 | -51.45975 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ccc5a16-c4b3-399c-aed2-745c47824887 | -3.36441 | -50.05807 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5a1f13c-87dc-36cc-a2e5-adf437ffe08e | -2.66152 | -46.12322 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f8a761a-ae9a-3ddb-af04-71d5e81368f2 | -4.48162 | -46.36191 | 2024-12-03 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36a0c08f-4a8f-3331-b851-bd5b087f49d9 | -2.54854 | -46.56205 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4107cb3c-38be-3d6c-a171-c4e2a4d43c4d | -4.03977 | -48.2664 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49802df5-4a99-3731-b89d-fa77c8d2b5b3 | -3.92754 | -47.98702 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2da2fbf7-3b37-31c5-857f-5dfa5e84ec0d | -4.20787 | -44.37286 | 2024-12-03 04:29:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5506ccf3-536f-3754-a64a-ca63f2dad5e5 | -3.26375 | -45.37663 | 2024-12-03 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c8a580e-6a76-3a29-9ca8-ed130d10a865 | -1.72551 | -52.47835 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbd3e001-6cc9-3925-a50b-c0ed502873b7 | -3.2793 | -53.25169 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37e82692-ec95-3544-ad7e-b395b8bcb14a | -2.72509 | -46.30358 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e3bfcae-032b-3d4d-a90d-9282eb1fbdc7 | -2.35685 | -45.70637 | 2024-12-03 04:29:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7971d74b-daac-39af-ad77-40fbe8eb1163 | -3.46972 | -45.13285 | 2024-12-03 04:29:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22c7a693-aa29-3384-8797-2f5140adccb1 | -1.74464 | -52.65105 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04df9def-f8f8-3528-91e9-e2bc9f714fac | -3.8139 | -46.55067 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8a0616a-ab7e-394c-9f34-9a5e32e3e14a | -3.07921 | -53.91771 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32876716-5938-3023-b022-4dfc5f74dc16 | -3.08212 | -53.38091 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5b27b01b-10b0-375d-a11c-7c26112c3a2d | -4.04255 | -48.27045 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a2148c6-ea04-3753-be88-1bac53948cca | -4.75111 | -45.11582 | 2024-12-03 04:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab3d5b27-dcad-3f18-b5b8-95018d9ca978 | -4.30696 | -48.22914 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd2ed509-ff73-3ba9-8843-0258918eeb79 | -3.25952 | -46.44698 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8591f754-eb76-30f5-84f0-75f37c82ba1a | -2.65744 | -46.58287 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 575dc442-9cab-3253-b938-835f616dd3b1 | -4.48635 | -46.02998 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf8b0c4b-f6c8-31fd-8dad-0b6d2c09b06c | -4.06884 | -46.67937 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 354e2442-03fa-3986-972d-38089843d26f | -2.68065 | -46.60762 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ca4adf1-ba5c-3dc4-bba5-91786c305d4e | -4.1493 | -48.24002 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59a0c21f-680c-338d-9177-ea8aeff6b057 | -4.05707 | -46.8191 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfac0393-662e-33c5-8431-dd3eeeba727e | -7.48459 | -47.48731 | 2024-12-03 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7812201-b825-325a-9fcd-eab3f4427e12 | -3.12024 | -45.9901 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa740207-fa32-3228-8cea-28f1e357a92f | -3.31538 | -51.26859 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb350a3c-7bcd-3b42-9dd6-4ef35eaf241c | -3.52172 | -46.1812 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b3865de-9bd7-30b1-990f-255958b33ae8 | -3.54146 | -50.18166 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ae324b3-6c1f-30d0-864f-7128ea74724b | -3.33922 | -46.04518 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cc3458f1-ab97-303c-90fc-86a06a82064f | -5.81075 | -46.48413 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c26501d-bc46-33aa-885d-59343006d7bc | -3.93596 | -46.92021 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0839167-0495-3a37-bf2c-efbf3220bbbd | -3.88428 | -46.40511 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 272f117b-f71a-32de-96ac-d8a6b4c0379c | -2.56073 | -46.39804 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cc7072b-4666-3d81-b18c-8cbd08138c04 | -3.98304 | -48.1927 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9b826ac-76b8-3770-8bf6-e3553fca2522 | -2.65509 | -46.1219 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92bacbcd-bf7e-3c69-b512-1b1db76afc3d | -4.31918 | -48.2167 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 602a6270-c5f7-3797-a3b9-c2383ff601c0 | -8.13675 | -44.46597 | 2024-12-03 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31376429-2e99-3e27-bc99-9e0c01027dbe | -2.82353 | -53.0556 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e65be6b6-e289-39cf-8a2a-71dfc90ef299 | -7.16906 | -48.77644 | 2024-12-03 04:29:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e002635-4982-34d2-a28d-29731aef7039 | -6.67804 | -46.38305 | 2024-12-03 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61d44c6a-e854-361c-afda-e356a28463b1 | -3.25723 | -53.63414 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 455cdcde-3558-3a2f-b420-08cd3be37093 | -4.13295 | -45.82957 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 520c5e6c-ed31-3db2-8b3a-4d56b47511b7 | -8.1374 | -44.46151 | 2024-12-03 04:29:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 355c2921-759d-3fe3-9f83-c083cbd6fe51 | -3.34125 | -51.20501 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11f8e34a-28b4-3e31-95f4-4ef5768192ca | -2.65028 | -46.58529 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8f0aa7a-0e21-34c6-aa95-a22ea3449b01 | -3.49692 | -53.83958 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61954dcc-f26a-3d15-8754-69f4d8b2daa6 | -1.78548 | -52.75363 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 638b34e0-7072-3faf-b32b-2cc1470be66d | -2.8262 | -51.84187 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08e35cfd-c4f7-33a6-b4b5-aa82a76b7087 | -3.25212 | -53.66545 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 42801ad7-5d6c-3ed2-9f0a-a0e5f69652c9 | -5.45055 | -44.8283 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a7ae5799-65ea-30b4-afd0-f5b3c2cbcfe0 | -7.48128 | -47.4868 | 2024-12-03 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e261d474-0c66-3bb4-85a3-7d76651ac3d0 | -5.54488 | -43.89458 | 2024-12-03 04:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea65ce9f-28d8-3f13-9a31-43690ef27f62 | -2.77042 | -45.23499 | 2024-12-03 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2dd494d3-a11f-3845-ad61-f0bb87233ea3 | -5.79846 | -46.47499 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 4f0f82c8-8944-3607-9043-679af26fba19 | -4.5322 | -45.73571 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d13ed2c3-0f68-34bf-8e74-6751cd7fb201 | -3.17096 | -46.31958 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebd36a59-335f-3af2-a8fa-8b7cc4732355 | -6.44801 | -46.12249 | 2024-12-03 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c20187e4-4506-3fca-891b-e307ae33d2fc | -3.28245 | -51.0647 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4747fe6-082a-3890-9921-050839ed103f | -3.86315 | -46.88769 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 764b439c-a7ce-3df8-9cc6-6e0df379b473 | -2.66586 | -46.09535 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a587f4c8-672a-3c1f-a9cc-c3adf3e30a6f | -3.09764 | -53.23027 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06ee1ba4-2264-3dc9-ae35-dd6ae94edeaa | -2.71765 | -46.19949 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 025f41f2-8c1e-3904-b540-21c82b67ce79 | -3.36522 | -54.0649 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8069f3aa-76bb-365a-865e-1b9f7c6d1e15 | -5.8046 | -46.47958 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4924ac20-bc90-3bc7-b91f-342432e99e5e | -6.11823 | -43.96264 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bea36787-e956-3a50-8c53-eba0e1b3698a | -3.22527 | -46.44877 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e90ae4da-43aa-3b71-8379-24095c2df818 | -4.16401 | -48.59434 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b7b3850-52dc-32f3-9e7a-d52cf45ba9ea | -2.55184 | -46.56256 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README35.md)
