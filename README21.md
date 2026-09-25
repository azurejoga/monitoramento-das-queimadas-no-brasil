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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 593b5893-15dd-3374-98ba-8b592a661097 | -3.23159 | -46.9373 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 43c03c6f-7189-3ad6-b6b6-2bb1e155eea0 | -3.1992 | -53.41895 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d574d78e-d0d3-3afd-987c-18ab3ea78dcd | 2.11187 | -50.69963 | 2026-09-25 04:44:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b66b4809-5318-3d6e-b393-825a331a78ec | -3.45002 | -50.07988 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e3881c-cce7-3c77-969f-cc1734e0846d | -3.0285 | -50.39753 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b03a4bdb-f3e2-3359-976b-0fd169f696ff | -3.04439 | -46.92513 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1474f80a-0557-3064-9a9f-ae9e7ddcecfb | 2.09937 | -50.9768 | 2026-09-25 04:44:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f922d1ed-47e0-3c5c-80a4-caa31d2d060c | 2.1304 | -50.70092 | 2026-09-25 04:44:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a54fca2b-3e8c-3eff-a731-f3ed92a047e0 | -4.1711 | -53.44875 | 2026-09-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6549765f-3a33-3b6b-8725-0f67ddadd353 | 1.49054 | -56.02114 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd62cf80-1558-3fe8-a699-1303c8312919 | 2.34736 | -50.77023 | 2026-09-25 04:44:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 431bb495-af5e-3270-b9ae-70754ca9df3f | -3.72838 | -49.0537 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f6b4952-06f3-3906-b216-c7d6b05600e6 | -4.16673 | -48.70974 | 2026-09-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee71b4d8-ee7a-31a7-b773-06b886d41024 | -0.50738 | -49.16135 | 2026-09-25 04:44:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c3a6b0c-0c5e-3095-89a2-f56d93e06ffe | -4.45767 | -47.92049 | 2026-09-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2da94b1-41f8-3afe-9e5c-6e50b84499bc | 1.57231 | -55.81702 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98755cb5-a3a2-3581-a8fc-c56d219f9fdd | -0.50127 | -49.15682 | 2026-09-25 04:44:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d157b64-531d-33b8-bc2d-2f668be70844 | -4.28737 | -48.61172 | 2026-09-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75df709a-cbf4-33b3-8b04-dd364a63bd82 | 1.59431 | -50.90829 | 2026-09-25 04:44:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39809428-94f3-3b56-8f88-63ca6927b8d6 | -3.21167 | -53.41607 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 065a711e-e3f5-3e1d-a249-9d5958f917bd | -2.33077 | -48.54724 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d55bb7a7-0078-3cbf-b4c8-4aa1e5862665 | -3.94662 | -42.99064 | 2026-09-25 04:44:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b24ab7dc-029b-3363-bbfc-4065df2d2352 | -3.02908 | -50.39392 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ce17784-2ed0-3c15-8b44-40d269c65d38 | -4.3048 | -48.07091 | 2026-09-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46ae8f35-fb45-339b-90d1-0d614bc6799b | 1.586 | -56.0085 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dd5fefa-a878-3327-8c2d-38bd18d7ac8a | -0.5046 | -49.15734 | 2026-09-25 04:44:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 434f8d86-52e2-352a-bcc3-ebe291e1a4fb | -0.50793 | -49.15786 | 2026-09-25 04:44:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2334d6bd-9c0e-33c2-b047-eae767a8aa1d | -5.37634 | -45.99918 | 2026-09-25 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6002a6b1-4cc5-34d2-97b1-8a2d1dbba13c | 1.29015 | -50.83463 | 2026-09-25 04:44:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feffcf73-f475-393d-9853-43030e3abdfc | 1.48442 | -56.04661 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1c8f9b7-019d-31b2-bfa6-222f61d595bf | -1.14305 | -54.09314 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dc8e91cc-827f-34e3-9e83-6c7c5ec5744e | 1.48445 | -56.0487 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95040a23-4c6c-3db5-9d7f-80c1cb5e8a76 | -1.60232 | -49.81869 | 2026-09-25 04:44:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b32506b5-3a96-3b54-a641-3e3f80bdfe5d | -3.21247 | -53.41116 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b9df88e-1b3b-3b9c-b307-3e7d9fedcad9 | -1.62119 | -54.93037 | 2026-09-25 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dda7fd46-cfcd-3333-a339-7df14c906cd6 | 1.55754 | -55.8197 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2f735d0-f159-365b-b214-022e801a9300 | -2.86487 | -49.63545 | 2026-09-25 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc06c6c6-7f6e-3666-a060-5fbea9814faf | -3.00875 | -51.53331 | 2026-09-25 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92b26c8d-24fa-3c5c-9d18-53caa1efead6 | -1.02676 | -53.7302 | 2026-09-25 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4975391a-e4d2-3818-a2b3-1b5c0ac800fa | 1.55618 | -55.82067 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9c924a6-8c43-31f3-942d-f8f7e05dd687 | -3.20468 | -53.40988 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db44cc6f-0b2f-3c04-95f3-9750f00272d7 | -3.49982 | -50.73887 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11f2cbe1-7044-3968-af06-0028fdc6e6d3 | 1.57321 | -55.82291 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff34b46b-e8b3-3b11-bf1c-7dc2c224567a | -4.11774 | -51.06101 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f40a200e-339c-314b-95f3-e267ff075534 | -1.9095 | -52.09097 | 2026-09-25 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faf07e4d-6440-36ca-a68b-43e9f6e870dc | -1.90651 | -52.08609 | 2026-09-25 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58f1a2af-b4f8-3886-b997-0b3f334fbc77 | -3.79623 | -52.37397 | 2026-09-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a085e207-6f84-3e23-86bf-3dc0948fc3d5 | -3.00522 | -51.53275 | 2026-09-25 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0113bbc6-4a12-355b-ae01-f44cbd1ee143 | -4.11131 | -51.07912 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c255c1e1-3360-3598-9598-6a97f5329645 | 1.48966 | -56.01537 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fa132fc-b25b-39de-a6e3-69c911605576 | -3.20778 | -53.41539 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0dd86f2-37cd-3e0a-b3e0-388736dec359 | -1.53317 | -48.04803 | 2026-09-25 04:44:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d1f8cf4-903b-3f6d-b38b-c373af0617cf | -1.31346 | -54.5732 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 103682f7-ced6-371c-b020-d949e8a8a990 | 2.0984 | -50.97581 | 2026-09-25 04:44:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ec8d3d8-2858-3d09-a3e0-a34981ef8f4c | -3.23274 | -46.92986 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5f8bab72-a6d4-39d8-a489-12cedf947732 | -4.27747 | -48.63147 | 2026-09-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 614915f0-440c-3c8c-ae53-0148c8435a10 | -2.8693 | -49.62901 | 2026-09-25 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a5396ef3-8f21-3c81-b9f4-b403dec1e7f5 | -1.6219 | -54.92604 | 2026-09-25 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a774d51-6b4a-3aaa-bd79-2440ffb963a5 | -3.21325 | -53.40633 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8feab9a-edd0-35ca-93bb-ebb2db0649cc | -3.94167 | -42.99415 | 2026-09-25 04:44:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfc63757-ef8b-34ee-956a-d8d316015f6b | -1.14663 | -54.09769 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bd0c2255-9668-3426-b8c7-423ef198d9ec | 1.49467 | -56.01458 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bddf623-569d-3c04-a5b5-8397ee4a2433 | -3.49864 | -50.74617 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a256187e-ac18-37e1-b9f4-801b254bc42c | -3.94228 | -42.99 | 2026-09-25 04:44:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44921b1d-870e-3344-8436-beb42e973941 | -3.20309 | -53.41959 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 690e7ce9-67cc-3977-b2ba-7f3c35ad140f | -3.24019 | -46.92719 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 73a9643a-1a0a-3544-93e2-1c6a75bded02 | -1.54315 | -54.27118 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63e827c7-5361-3316-a563-7ea5213956fd | -2.31153 | -46.99447 | 2026-09-25 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 635b4cca-11ff-3777-8339-cdd612c8c4da | -3.20857 | -53.41051 | 2026-09-25 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18ad193b-7d8b-3c56-b638-c341eba8525b | -3.18081 | -48.02531 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7d1d4d8-e4c1-3d56-91f7-451c690e28d1 | -3.72453 | -49.05663 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7170e556-174a-3b45-9702-d923ab4fe0d0 | -3.93734 | -42.9935 | 2026-09-25 04:44:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a2e17e0-c53d-3a29-a84d-f5013a992fda | -2.86875 | -49.63249 | 2026-09-25 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 324968e3-1f38-301d-8f00-5c596ce819dd | -3.72508 | -49.05318 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95e26491-b10b-3924-b571-3629df744347 | -0.4996 | -49.14585 | 2026-09-25 04:44:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75f1d833-2f2a-3e15-ba1a-801ef153a123 | -1.9597 | -48.37962 | 2026-09-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9506ef04-5576-3c69-a13c-df6fe4c8856c | -2.06564 | -47.15289 | 2026-09-25 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9c3f451-59c2-3aed-9dc5-4088f92119d3 | -2.60988 | -51.74017 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 174be6b8-9618-3aaa-a253-2f1f377b6c51 | -1.13947 | -54.08856 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6dd95740-048f-3116-bd23-3e12325188dd | -1.14786 | -54.08997 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 70f6f302-27b7-31df-8f1e-a8a34a4de166 | -4.9342 | -45.65878 | 2026-09-25 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab7a3daa-d260-36fc-9153-31bbb08aa926 | -4.28405 | -48.61121 | 2026-09-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b322a6e2-386a-36aa-9b0a-e6337c9d93cb | -1.29541 | -54.22263 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b955035f-af33-31b7-833d-e83caa01209c | -1.02623 | -53.73355 | 2026-09-25 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6eec309-f485-3759-bec1-88f02e4d7ee0 | -3.19615 | -50.75163 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db7d3930-ba61-3288-b5e5-33516c5c2143 | 1.59823 | -55.85411 | 2026-09-25 04:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7481203-8204-3e86-8363-ac7f052dd05e | -4.45711 | -47.92404 | 2026-09-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b1e8d4d-ce56-31c2-ae7e-254a0cd0d073 | -3.26811 | -50.08743 | 2026-09-25 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166fb52b-57c9-36ac-99ae-d06db84b75eb | -3.73142 | -48.9061 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ea1f91b-9938-3ea5-8545-9ad575227c83 | -1.1412 | -54.10467 | 2026-09-25 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38341e3e-af7c-3cc0-b115-73e50ca8f9cb | -3.97129 | -47.20469 | 2026-09-25 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 301791eb-7ee7-394b-9435-32df639c9ec7 | -3.98008 | -48.42828 | 2026-09-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14506c30-82cd-32e5-8778-44702fdcb063 | -3.45058 | -50.07636 | 2026-09-25 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85d50d0f-73f0-39bd-b6eb-f70cc6d874dc | -4.30536 | -48.06737 | 2026-09-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56062667-48f1-3549-ace4-3f505b7d2d46 | -2.93605 | -48.58627 | 2026-09-25 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fded1d3-51ba-3208-a18b-9415cc834a0d | 0.70057 | -51.4377 | 2026-09-25 04:44:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2946b371-8f8f-3161-9ab1-38a94d4f8547 | -2.95324 | -48.58553 | 2026-09-25 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e29e05f-496d-332e-a64f-aec1bda1dfdb | -4.37439 | -46.23816 | 2026-09-25 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 771aaf90-306e-3062-b0a6-828d30b6305b | -3.18191 | -48.01832 | 2026-09-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2afb843c-0f74-3463-b16b-87dc172455ae | -2.17897 | -48.79853 | 2026-09-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README22.md)
