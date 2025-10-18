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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d655e812-6b8b-3803-8817-10779b3fd098 | -10.69546 | -44.56807 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| efbf3ef6-0a24-3e78-8a2b-9fa664643281 | -12.39296 | -47.21344 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 4a8e2c0f-22d2-35a7-ae1f-3920df8046e7 | -10.09678 | -47.66672 | 2025-10-18 00:52:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 7dd32c70-c0a6-3a9a-9747-9790e33acc10 | -12.38981 | -47.1947 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 45250851-5a6d-3fa1-b185-f352e730a0b6 | -10.24842 | -44.05081 | 2025-10-18 00:52:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 10986647-62a2-39fc-aa34-b8c9fa419d7f | -13.52945 | -48.00449 | 2025-10-18 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ae235442-f8f0-3e38-bd2e-50d46b9e3a08 | -13.45515 | -48.11874 | 2025-10-18 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 899bd172-f4b4-3ecf-8fa6-a96b460e8204 | -14.26754 | -51.87541 | 2025-10-18 00:52:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7314ca55-6f51-33b7-b5e7-a5c1badd308e | -11.60731 | -44.06351 | 2025-10-18 00:52:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 196.2 |
| e725aad5-12da-39f9-8b9e-bc54ceaecd16 | -13.76394 | -48.24418 | 2025-10-18 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 56b738a8-b5ff-35ad-94a5-e89f679e700c | -13.22369 | -43.98493 | 2025-10-18 00:52:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| fc2545f4-348d-30d2-9bd1-d851e6c3642e | -12.91837 | -48.58416 | 2025-10-18 00:52:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1c5e997a-cfd9-3c05-be6c-22464955b878 | -11.63963 | -47.86231 | 2025-10-18 00:52:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e47a2f8a-5ace-3562-b295-12f037f3b73a | -13.42202 | -47.98292 | 2025-10-18 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 831c3284-7d83-390b-9b75-98c8bc629075 | -9.74999 | -43.97419 | 2025-10-18 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a5056ae1-8d33-3a6a-8182-a188e497d618 | -14.39906 | -47.89243 | 2025-10-18 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e5c2e0c1-b09b-3944-9a1e-0f0eca6a11a0 | -13.19887 | -48.3202 | 2025-10-18 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| de1d9703-1396-390b-bfdc-a00beb1d23c9 | -13.45728 | -43.75289 | 2025-10-18 00:52:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 80481803-5944-3163-beb8-ad5e6b5e46dc | -8.71844 | -49.60087 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c5d2b335-924e-3215-82b5-bc350b3f50c9 | -9.91178 | -47.67717 | 2025-10-18 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 47905186-81ba-3681-bfd1-354cfd094bc9 | -14.55605 | -47.93835 | 2025-10-18 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f9b54686-9086-3bbc-925d-df68402e8e75 | -9.90887 | -47.65826 | 2025-10-18 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0edd0b6f-fa2e-3c47-b88c-ae21d9ee384c | -14.5554 | -47.93217 | 2025-10-18 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c139fad2-be71-3760-ad17-cc97d21c539a | -14.44715 | -52.89482 | 2025-10-18 00:52:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e0029a64-d4ef-3a61-b774-c19217e0e55b | -12.31262 | -47.83863 | 2025-10-18 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8d5d0d0c-73bd-3f10-9fdb-17b2fb3c015f | -11.08937 | -44.70365 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 72623ea3-6c9f-3c32-ba42-b434b973f5b9 | -9.76203 | -43.97697 | 2025-10-18 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 848525e5-e2c8-3268-bd0f-797860a15135 | -12.64083 | -44.14193 | 2025-10-18 00:52:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| f23f1b52-76ec-31e1-a516-d370ec51cd82 | -11.61305 | -44.09722 | 2025-10-18 00:52:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| e03e6b05-587f-3899-a27a-b863d4c63b82 | -14.3221 | -53.7904 | 2025-10-18 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c322e124-371a-3305-93c5-166679c060dc | -12.38774 | -47.20161 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 3668a66e-2929-348c-be09-99272221af9a | -13.77268 | -48.23339 | 2025-10-18 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 905af0bd-80c3-3a58-9910-cd57089e40f4 | -12.08142 | -47.40527 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| b172d6a5-9e42-3f17-a56e-941cd84107a7 | -9.56121 | -47.77229 | 2025-10-18 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 072bd4d0-c718-32fe-ba0d-16b3d050bf08 | -13.51811 | -48.00654 | 2025-10-18 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 11f1269f-87c7-3595-8445-22ce4af07bea | -12.98845 | -48.44516 | 2025-10-18 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a96d32da-6508-3470-9330-877a5038aa5f | -12.07818 | -47.41248 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| db0f8a10-da94-3621-b45d-d7ce6abb8273 | -10.0843 | -47.6686 | 2025-10-18 00:52:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c3629040-8c2b-3a61-98b5-f0c78042c269 | -9.22291 | -48.58816 | 2025-10-18 00:52:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0527ee41-97d9-3e54-ae73-3bfc7542afcb | -10.42383 | -47.74639 | 2025-10-18 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 86dc0143-c6c0-38c2-9e3d-1a1184436133 | -10.49547 | -47.53667 | 2025-10-18 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| be3a2721-4a73-38cd-983e-ff8d00dc983e | -10.53368 | -44.5072 | 2025-10-18 00:52:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 19dfe1ee-cffd-3477-bc9b-6f3dbe4de068 | -10.9922 | -44.35209 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5194c7e9-0121-39a0-9f8e-0c4467e392d0 | -10.81452 | -54.61224 | 2025-10-18 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 181b9041-2f75-356e-977b-036f55f0229f | -14.2841 | -51.86332 | 2025-10-18 00:52:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 38aee174-065f-3271-bcf2-bf54b0664602 | -14.45723 | -52.90257 | 2025-10-18 00:52:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e18177a4-3602-3fd0-837e-58a2ac27e243 | -8.36072 | -46.2496 | 2025-10-18 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 1675a323-be16-315f-a360-ab0e97f7b4f0 | -10.54034 | -43.38158 | 2025-10-18 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8e10a23e-7d07-38da-9760-c449a92be8ce | -11.60506 | -44.09351 | 2025-10-18 00:52:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 6bb640c7-7aa3-3aef-b5d7-7a0dbb0ca8d0 | -8.82411 | -49.69233 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 29a3bacd-d5f1-3064-84db-df4093e080f4 | -10.74648 | -47.29817 | 2025-10-18 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9545b77f-40ed-3133-9ee8-270f746cdb27 | -8.82205 | -49.67845 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 97dee162-df81-396c-8ae3-fafa5a3045a4 | -10.09368 | -47.64759 | 2025-10-18 00:52:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e0fe9027-3ffd-3bc3-be16-4832f9fd2bbd | -13.46417 | -43.75836 | 2025-10-18 00:52:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7fe11989-9af8-3d91-8723-ecd8b653bcc5 | -13.76149 | -48.23472 | 2025-10-18 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 24924135-3e97-375d-9ead-796900c84447 | -9.5074 | -47.27493 | 2025-10-18 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 9dedf6f8-d00f-3d58-a102-2ec658b2c895 | -10.09527 | -47.6735 | 2025-10-18 00:52:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 78e5c18c-2b97-3f59-b390-a20765ce6e83 | -10.50221 | -43.46549 | 2025-10-18 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 07e23817-73b1-3e02-8309-a26810f808a8 | -8.44732 | -44.18153 | 2025-10-18 00:52:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 1b2ece3a-8430-366d-96ba-23744ff07ff4 | -14.32086 | -53.78118 | 2025-10-18 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b16c2208-5a43-30ee-b4cb-16e539fbe941 | -14.44841 | -52.90388 | 2025-10-18 00:52:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| da8d13ed-ad95-3a23-ae64-9cca7be238e9 | -13.77507 | -48.24255 | 2025-10-18 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| c96f960f-a76f-33a1-be85-a50d45c9b47a | -9.54879 | -47.77467 | 2025-10-18 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 3796fd91-e5d4-3eae-856c-11bf001d68da | -13.04086 | -48.19771 | 2025-10-18 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e7531e49-1ec1-3bdd-940c-4bd7957a359f | -8.38572 | -46.22062 | 2025-10-18 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f2e83c69-fa4d-328f-8714-efbe18b10eda | -10.09234 | -47.65448 | 2025-10-18 00:52:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5e0349c6-a578-3958-9577-b2b20ca0be52 | -8.54102 | -50.08644 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b52c9c14-16e4-3bb9-8634-5fa0a6ff4629 | -10.70131 | -44.57359 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7ea31fa5-718d-33a3-a621-4bebd9317558 | -12.3052 | -47.26019 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c7b6fec3-a45b-3f28-9f9a-a5b6e56c1148 | -10.23768 | -44.04526 | 2025-10-18 00:52:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| c1d58523-fa6b-3874-a471-285a42784139 | -12.99098 | -48.46087 | 2025-10-18 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 65cd5bee-beea-349f-8124-185cce6cc292 | -13.73143 | -48.11619 | 2025-10-18 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3cadfa58-6e58-3a2b-a2cf-34c96b88abcc | -14.45598 | -52.89351 | 2025-10-18 00:52:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dbaf76f6-40d1-3515-9006-e52d69535890 | -14.2662 | -51.86608 | 2025-10-18 00:52:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fbefd41e-ea3f-382a-9353-4960998cbe24 | -8.39176 | -46.23954 | 2025-10-18 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| ac9e03f6-e1f0-37bf-92f1-aa782af92865 | -10.57895 | -47.39284 | 2025-10-18 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2285a8a5-9e7f-3166-9097-fafcd3e7aa6a | -10.54206 | -43.37577 | 2025-10-18 00:52:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 57d1261c-3d28-36a8-834c-21ec2c734a36 | -8.55159 | -50.08479 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1197ffb9-5712-31f7-ba05-27f16a8a4d6e | -11.58307 | -44.06276 | 2025-10-18 00:52:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c5cf71b3-76bb-3936-b2da-43323cc345eb | -13.44882 | -47.92983 | 2025-10-18 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4c060dc4-10ea-39d7-a6b1-5f70397c65cd | -9.98906 | -47.00629 | 2025-10-18 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 55b3192e-46e8-31a1-b815-2971cf62cb63 | -10.97775 | -44.32763 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 775981ec-492a-382a-bcd0-ede6d4161da8 | -12.39073 | -47.22025 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9c8b6382-a8c3-3190-abb7-27d4d75177d8 | -11.94106 | -44.25059 | 2025-10-18 00:52:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 16c001d1-2c5e-326e-981e-c0260f9bb2a7 | -13.73752 | -46.82845 | 2025-10-18 00:52:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6f8589ac-27d7-3af1-872c-0fb431a9e6c8 | -10.95921 | -45.48388 | 2025-10-18 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| df000244-2bcd-31fb-9eb8-1a10694ef694 | -10.98636 | -44.31915 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 3727a555-ef03-32a8-bcf5-a7136e7ae595 | -13.77495 | -48.24805 | 2025-10-18 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f9973e1e-0aee-304d-a3c6-be813aa1ad0c | -11.9756 | -47.88585 | 2025-10-18 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5755eefc-c5b6-33c4-9c41-71e0157d5daf | -10.57852 | -47.39942 | 2025-10-18 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 871550a1-93ec-3a1d-a663-557991308d8e | -11.65154 | -47.86037 | 2025-10-18 00:52:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5c4acd19-2060-3407-ba17-24daa86c7ad6 | -10.95038 | -45.43164 | 2025-10-18 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| dbd797cb-72fa-3933-814d-425d64a888c6 | -12.08442 | -47.4235 | 2025-10-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 99ef9c1f-a430-3e10-a663-96f2282584f7 | -8.53903 | -50.07336 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 746dc352-1490-303b-a2d1-00892a4368b4 | -10.47831 | -43.43012 | 2025-10-18 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 3ed91316-55ae-3b07-b9ed-2087028b4346 | -10.49954 | -43.47276 | 2025-10-18 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 1e1ab66d-591c-34f0-a7df-48b90136b741 | -10.4683 | -55.59354 | 2025-10-18 00:52:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 63ca7acf-609a-3ac2-be20-6f3bb0d2b227 | -11.59906 | -44.05984 | 2025-10-18 00:52:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| e735a4ef-9da1-3abd-bb3a-62ebb10bea7a | -8.82639 | -49.68618 | 2025-10-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| d8d0da62-0ff1-3b16-aa50-dbb9bd434b95 | -14.55784 | -47.94703 | 2025-10-18 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |


[Clique aqui para ver as próximas entradas](README5.md)
