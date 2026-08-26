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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8961d304-7a48-38c4-b743-8e5ea7a3b170 | -7.39052 | -55.16843 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb9ed1cd-1b63-3978-8d38-7ec7d288a46d | -6.61613 | -58.37811 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc1c2e4a-563b-3d87-92e5-0ddf9ea433f9 | -6.99038 | -59.27828 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4f02a58-fcab-37a3-b64e-bb4ec997c37d | -6.14516 | -57.70103 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2b14f38-3547-3f44-8d0c-52b63ff8e313 | -7.00554 | -59.23769 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b66f62e-ec6b-3864-9cf7-29b044afcab1 | -7.01917 | -59.2339 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0df8a509-65f6-3177-99d7-ebd976e23ffa | -6.99935 | -59.31042 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68d8fda5-ec9d-32b6-9767-eb708bfab566 | -5.94067 | -57.73344 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f6ef499-0de5-3335-877a-d096faf1513f | -9.46422 | -60.53873 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 707efe2b-571a-302f-8427-a449d4d65f9a | -7.21513 | -60.61481 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf06804a-3570-3e46-ba20-cba485a5adb5 | -8.82402 | -62.33427 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f996249d-ef19-34ec-8889-3715dadff6bf | -9.59661 | -61.00611 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd330059-79d8-3086-b7cc-26dc0959ee8d | -6.27921 | -53.36083 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51853380-167e-33ed-9034-9f9d1fdc84ec | -9.60265 | -55.11514 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 909f5259-db5e-3224-93f1-035d91de0be1 | -6.72752 | -59.44704 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42e9464d-846e-3117-bf3d-36de11c19214 | -6.92109 | -60.07026 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42215de2-56b6-370f-bb7b-ab349ae27ec7 | -7.00032 | -59.30304 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70417b3b-0465-395f-ad52-12bb4a429d1e | -6.12732 | -57.8287 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f87000c7-d498-3e57-bb77-9ce86c3c1d76 | -6.96778 | -62.86633 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86fc1639-50f8-33b1-a509-bbc2a7b27c6f | -6.51236 | -55.23071 | 2026-08-26 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2904e2d6-ce94-3f32-a9d3-4c37f1590ea5 | -9.39304 | -60.58011 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fed6a4b-8788-38a7-9455-d0aa81885152 | -7.01475 | -59.23325 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 729b944c-4b6e-31cf-8cb5-72845659810e | -7.5432 | -61.36594 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c185035c-7818-38b1-b87a-5d7a239a0bbf | -8.8203 | -62.33372 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f7b72a23-5b21-3a4e-9ae7-542753074cb6 | -6.15 | -57.70184 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bc32dd8-2e93-3415-af57-b69712756f3a | -6.64054 | -58.50536 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fbdc0812-263f-3f18-9305-c238db4158ca | -6.15671 | -53.68969 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88a5fa0a-3452-3b69-8041-dd5268b0da4e | -6.13052 | -59.91954 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5e70b36-f3f2-344d-8577-4e1ebeed1e1d | -6.27202 | -53.3652 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea1a1408-328c-39f8-9b59-008a2161b9d9 | -6.31086 | -53.57267 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c72f667-e59d-341b-b072-7159546f583b | -6.84796 | -58.98679 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08189a4e-7595-3c28-845e-e54b34845a54 | -6.13284 | -57.82729 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 58e5f9a2-5873-3193-880f-81d910b74cb1 | -6.12247 | -57.831 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03322641-9d46-3a35-853f-57319d7c7fa8 | -6.60614 | -58.38142 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a416b1d-7252-3a58-8b11-81080183a3e0 | -6.15022 | -59.93002 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| afff3551-a574-3476-85eb-8b0b53a1d378 | -7.02298 | -59.23891 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7af13747-84a0-3429-83aa-b415c102b985 | -7.02421 | -59.2302 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65557a73-9f12-323b-b458-45488feb48e8 | -6.11845 | -57.82494 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 46ce2717-3c53-33b5-9599-911c901688db | -7.37986 | -55.15883 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f61096c4-8eb0-3e29-9a4e-e15609262b6f | -6.54339 | -55.08949 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ba0c075-2d45-37e0-9b29-8d5fd0f318af | -6.12884 | -57.82116 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b02d53ad-4a9b-35e0-8b51-0b342a38e7f9 | -6.99968 | -59.30732 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fc78cbc-8c0d-3167-8546-4077eee90a59 | -6.84201 | -59.43305 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a65732bb-ed7b-34ba-a8c3-138d648594b1 | -7.54465 | -61.35633 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c20c1bc5-96e2-3450-86d5-5526cce384d4 | -9.60473 | -55.10825 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 434a01cf-09d1-367e-b4d9-a81983b6f273 | -6.14817 | -59.92522 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33faa940-0bdf-3f69-b3b0-0a315cd59ea4 | -6.77438 | -59.44013 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9db28d8a-7161-3a7a-ac9e-12fd932d7936 | -5.9455 | -57.73416 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9879c4e-649b-35c1-8582-581d4d1afc8c | -6.61078 | -58.38225 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6af47343-9e03-3877-9ef1-e498504190fd | -6.12252 | -57.8279 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1e87df17-8b1f-33ea-8c93-72ff7f82630d | -6.14028 | -57.84122 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 543b365f-7c40-35bc-aa90-8c75b06e967e | -6.33742 | -54.74456 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d6454a-820a-3e5e-a081-6e15f488eeb7 | -6.33208 | -54.73949 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56c0604f-e962-3551-bdcc-2ea8d24e7896 | -7.55521 | -61.41718 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 190de045-94df-3120-9700-0ae332982021 | -7.62182 | -63.36679 | 2026-08-26 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f74d80a-304f-30ff-8889-b9a2ef74b0ac | -3.77686 | -59.28001 | 2026-08-26 05:48:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38e29d94-12dc-3294-991e-07ffa86d9f50 | -6.99159 | -59.26968 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c20b06ec-b030-3b80-a3a5-45d71cffac7d | -6.68957 | -58.71755 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e640fcf5-3883-3e75-94a6-18593565dcfc | -7.54248 | -61.37076 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f13a35d-973a-3520-a4fb-5672377607fd | -9.16624 | -58.33592 | 2026-08-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 29f1eaa6-3302-3d17-a61f-7a7f5c583027 | -6.5376 | -55.08844 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92ba2238-f82e-319c-911b-56bf6c9cc80f | -6.65049 | -58.5019 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9e67c851-48f0-367a-be3b-dd30e271a1d5 | -9.60812 | -55.12041 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1f3759c1-3963-316f-bc82-94a596872cb6 | -6.63386 | -58.5189 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c62d964e-5c04-3b11-bebf-d373256a47a3 | -8.63928 | -54.74751 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f498c109-4650-364d-8dd2-25571053b7c0 | -9.16698 | -58.33064 | 2026-08-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d23d9aad-4bf8-3f9c-b3b6-578fcee23339 | -6.98404 | -59.26101 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc1acd4a-dfa1-3fb2-92ea-8bfe25091713 | -6.86004 | -59.40142 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cae4f6c6-5bda-3599-b144-7cc1a4b086e7 | -6.63455 | -58.51413 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 81957c94-59b4-3009-ba90-5f6944aa8242 | -6.61543 | -58.383 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db7f033c-781f-3894-b74d-d9b64e5e1f00 | -6.88768 | -59.02881 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da648a81-536b-3bac-b51c-9622c081fc5f | -6.62649 | -53.19348 | 2026-08-26 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a50a7515-bc84-390e-b7a0-4261e0b527ef | -6.73306 | -59.66803 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dae54284-fa6c-3266-bb4e-64382d40d115 | -9.09921 | -59.40651 | 2026-08-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5348788-0fe9-30a6-8f3e-b33a55a3be3b | -6.14302 | -59.92135 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e9c4869-a6d3-3c4a-a2bf-c6c50e9883f2 | -6.98527 | -59.28322 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2097e017-90e9-3483-a1a4-d0c806f49831 | -7.3764 | -55.18485 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78194f91-7f1e-3e3d-b5a9-982cf7b9c0e1 | -6.15429 | -53.68774 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41320711-148d-35c3-a444-3cd4887cc4bd | -6.16067 | -57.80134 | 2026-08-26 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5cf47755-aba0-3e37-aff2-de2b41560713 | -6.78673 | -59.65947 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f8f60c0-864d-3ea2-984d-8da98937f1a1 | -6.6195 | -58.48749 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2d1ac1b-fdc2-3f4d-8557-b9683a56dafd | -6.77378 | -59.44436 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 361a289a-7da7-3ffa-821a-b2da753ee803 | -9.60417 | -55.11281 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 7074288a-d439-3bf8-9c53-60b721afea22 | -6.86419 | -59.40907 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b0f0591-6b32-349a-9f3e-92a109aea509 | -8.82335 | -62.33872 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2bb78f1-2b36-3de6-bc00-bcd32e393c22 | -7.52094 | -61.3825 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| be54f7d3-87dc-3368-ad84-e0b67e761d3d | -9.39248 | -60.58396 | 2026-08-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbd31148-5361-36f3-a460-2d002212326a | -9.66941 | -55.08441 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0b75da2-e444-3d4b-ba30-e5aea36e7fe2 | -6.73149 | -59.14283 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f64eac6-9ec6-3c7a-96e7-e04a251a1298 | -6.97588 | -59.2552 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 666b1a53-b491-3029-9961-9a7258bba908 | -7.01033 | -59.23257 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8822fe7-05e0-37c6-b8f6-bd64b606420e | -7.48121 | -55.28501 | 2026-08-26 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1895f98-9042-3da3-bf96-b0f47f932f2f | -8.80745 | -62.31805 | 2026-08-26 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ee6964b-5124-3c57-acd1-b6c725366d02 | -6.50482 | -53.25962 | 2026-08-26 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 233c1023-fc10-3de4-b43d-8572ae0e52d0 | -6.13451 | -59.89296 | 2026-08-26 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b727fb44-3d6f-3a6c-a5c7-e7036faa1064 | -7.51393 | -61.37649 | 2026-08-26 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3dc38bd4-9c79-3da4-a936-edaea09d1e40 | -6.62924 | -58.51821 | 2026-08-26 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec1fe07a-837c-3f69-980f-012cdb9058b3 | -7.38175 | -55.18937 | 2026-08-26 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66b12898-63e8-3f6f-8c3e-10635f37512e | -6.72642 | -59.14664 | 2026-08-26 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b068d99-d464-3219-9b0b-9aa07e02b975 | -9.60361 | -55.1173 | 2026-08-26 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |


[Clique aqui para ver as próximas entradas](README70.md)
