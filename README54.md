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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bff340f2-2642-39d7-b071-6017dc53b4b8 | -16.29199 | -57.66696 | 2026-08-22 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 48eb5230-bfe1-3dc2-96a9-68e6dd49ee7f | -15.21409 | -52.77419 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69e585da-5b8e-3ac3-8f6d-a5debc1a669f | -16.95445 | -46.11732 | 2026-08-22 05:06:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec8c3c7a-b323-3f51-b540-b454e3c98a81 | -13.83783 | -54.00428 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b40a2e2e-b8b5-3798-9003-5928b3b5de52 | -13.69542 | -51.84771 | 2026-08-22 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9273c942-f594-36f6-b416-570f48c0d414 | -13.40688 | -54.36 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 643be381-fcab-39d8-9788-7d630355cf27 | -15.21814 | -52.79443 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53fd01b3-5f84-3223-b760-f01c2301004d | -13.403 | -54.363 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dec907b2-f556-3905-91a6-b90bbe546452 | -14.54611 | -53.00251 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 273e6b3f-7692-328a-aa3d-9ac5de9ae521 | -16.28849 | -57.66625 | 2026-08-22 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 42cebe50-6141-32e8-b0da-ca01fdbeb41d | -17.95398 | -42.7298 | 2026-08-22 05:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a32ffdd-516b-35e4-ab7f-fab2a61f5b35 | -14.40254 | -51.80346 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50eaedc0-c9f4-3896-a116-dd212b28d216 | -14.38834 | -51.80126 | 2026-08-22 05:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f08f685a-bb1f-32f9-98e4-8623de89e599 | -15.67951 | -53.77547 | 2026-08-22 05:06:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72cdbab9-bf96-331e-91b4-54b547593499 | -15.20805 | -52.79749 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65dd434f-fbf2-32de-8d5e-5b44c15caa71 | -13.87779 | -53.98884 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d31341c-bec7-3d63-836b-0b715d7c9f64 | -13.69804 | -51.95043 | 2026-08-22 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96ca3ccc-c855-3a34-8c94-1950d8423f39 | -13.38582 | -54.3638 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1c4ceb9-1b43-30ad-9b60-9ad8b0bbe334 | -16.95393 | -46.12111 | 2026-08-22 05:06:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b0f547e-0e0c-34dd-b575-16f6b00bcb72 | -17.56803 | -47.88539 | 2026-08-22 05:06:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b56a391-6b3b-37b6-9c80-3e70bba3a014 | -18.0903 | -46.94921 | 2026-08-22 05:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61c249ff-22c4-3f65-8606-7ac0a5864e89 | -12.94086 | -56.62169 | 2026-08-22 05:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5e41b14-5658-37a2-b864-5f181b3f229f | -16.71767 | -47.70562 | 2026-08-22 05:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ed572ff-b257-3747-bb66-deb4aca3f896 | -13.82912 | -54.00264 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c090b7b-dae9-3c62-8793-4bf6d1a169aa | -16.71297 | -47.70506 | 2026-08-22 05:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a5cedc9-838a-317f-9a14-0e4f7254d45a | -19.74667 | -45.10088 | 2026-08-22 05:06:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f35efff2-6e36-3e90-a612-2fa741c83f02 | -18.52819 | -48.25245 | 2026-08-22 05:06:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38ceae91-521a-3d40-b740-b320c13c75d6 | -15.23767 | -52.8288 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6569f51e-8a1b-3017-8df5-e0b8ba607d84 | -17.91585 | -44.39592 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6642bab3-0b43-362c-9c6e-087e2033f0e6 | -16.036 | -52.17084 | 2026-08-22 05:06:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e773394-2a54-3207-ad16-b3cbf990df1e | -15.44149 | -41.38398 | 2026-08-22 05:06:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ae031380-e836-3d6f-a990-5c031f093fcf | -14.00195 | -53.66733 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8eea8c9-6ada-305d-8d97-5292d20aea91 | -16.61406 | -49.39735 | 2026-08-22 05:06:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ad23b0b-1904-3aeb-9e3f-ace6e0fbe19c | -14.56427 | -53.04373 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95d67f0e-dbba-3616-830a-785259699f40 | -13.40243 | -54.36655 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a845534-5d74-3397-83cc-e07aeaef35bf | -17.97289 | -44.3665 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24728346-36b9-38ab-950f-a4a46d3d374d | -17.69432 | -44.44379 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5de8922-c433-3de2-a6a7-cd1567ed175c | -16.48776 | -47.95279 | 2026-08-22 05:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1724a073-73e9-344c-848e-4d128dd850c4 | -18.10383 | -47.17973 | 2026-08-22 05:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d05bc8b3-e476-3711-9a4d-e6e2e226a146 | -16.79057 | -49.35899 | 2026-08-22 05:06:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07be3119-5e26-34b2-86b7-6792451506d2 | -15.34137 | -52.92648 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 179f4d04-172c-346c-a614-ba6d23b576f8 | -14.31913 | -53.00499 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61272dd0-fded-39bc-96b2-3ee7aeb02fae | -18.27302 | -43.31168 | 2026-08-22 05:06:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e72ea245-b7a2-366a-b861-797c10bb0053 | -16.50358 | -55.18571 | 2026-08-22 05:06:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 79452880-37de-33e6-a745-92d89030de9a | -16.70886 | -47.69967 | 2026-08-22 05:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b7bf113-4d25-345f-860e-9443a3eed884 | -17.96958 | -44.37503 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 917fd294-00fd-39f7-bfa5-a7355cd66aee | -14.55858 | -53.01222 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2a4e7ab-8a0f-3ffa-863b-2491c362f714 | -13.92111 | -58.26236 | 2026-08-22 05:06:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| caa0c36a-e63a-3649-a786-5396822b592b | -15.2187 | -52.79065 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4223657-03d3-3758-9042-b79620d83075 | -14.55178 | -53.01112 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47c482e4-2fd9-367b-b04c-91468b73376e | -13.98923 | -53.66927 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f022e12-beea-3780-911f-374026aeebb7 | -14.56142 | -53.01648 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bad2d57-9ebc-3a38-976f-b4b906dd87d1 | -18.75775 | -43.80603 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b64e6d2-e51e-38c0-8cce-490e6a965d91 | -18.27715 | -43.31017 | 2026-08-22 05:06:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0ef06db-2e2a-36f3-92ed-7e13b224fde0 | -13.69303 | -51.86376 | 2026-08-22 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64413d97-2b24-383a-bb77-27e50342cc39 | -16.95409 | -46.1206 | 2026-08-22 05:06:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7be7501-dc3b-3b4b-aa88-5253b5e8b2c0 | -14.50072 | -59.82664 | 2026-08-22 05:06:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c13697c-1f04-325f-88bb-6a27cdbdbd70 | -15.20727 | -52.79651 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8abd9d7-7f75-35d3-bf53-9b78b799d98f | -15.20405 | -52.77734 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9211807f-c5bd-3da2-aae3-6a5f49f967ad | -15.8647 | -55.55848 | 2026-08-22 05:06:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 157a7a72-e89b-3996-b92a-aaaf0b2f1bd4 | -14.55411 | -53.08787 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2af1af54-4013-33ae-a8c0-dffaee05134a | -12.95501 | -56.64444 | 2026-08-22 05:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c670511a-1694-34da-981d-7608bff27f1c | -14.54555 | -53.00624 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24859f44-cd5a-3f18-bb50-353fab1e5180 | -18.91676 | -43.59355 | 2026-08-22 05:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a4be9cf1-f5ec-3549-9d4a-a7cea4693a51 | -14.72289 | -47.14167 | 2026-08-22 05:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d06fba34-a7b4-33bb-90db-c61bba632596 | -12.95349 | -56.63203 | 2026-08-22 05:06:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2181fde7-4117-3a2e-89d1-2cf9129fc87d | -14.55799 | -52.99303 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7ec8f10-f941-3120-96dc-2348368c57cf | -13.99083 | -53.69495 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5b168d3-d667-385f-b387-7b3f8ceaa6a7 | -16.2955 | -57.66768 | 2026-08-22 05:06:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6c9a3331-d583-3e85-b69a-821573a8c4b5 | -13.69044 | -51.95331 | 2026-08-22 05:06:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a22f2d9a-30c3-36ad-9bc0-8e8e5dfde560 | -14.01088 | -53.69822 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ab4c9d4-c181-3591-a90a-fe9239c04063 | -14.14273 | -48.06501 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88ba5c75-7b28-3c7d-8e38-41c1f5a96e7d | -17.92093 | -44.40489 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ac2d474-5441-35ee-ab37-6ee8157a347f | -15.31321 | -53.8032 | 2026-08-22 05:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83e0bd13-3c5b-3abb-8e4d-c5ffdb193f24 | -17.968 | -44.35579 | 2026-08-22 05:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0933a54a-6764-33f1-affa-6d9c0ef60f93 | -18.79151 | -43.77999 | 2026-08-22 05:06:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01bd229c-5617-3931-86a0-4df99fda59b3 | -14.1298 | -48.06585 | 2026-08-22 05:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99877851-f082-3fda-9897-e4a45df68b62 | -13.99417 | -53.6955 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2c9aa14-2567-3082-89af-da82eba434fa | -17.91627 | -44.39183 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 932f87ef-6828-3a9f-8776-16c2e0688b53 | -13.82415 | -53.99083 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9f9778e-9937-3c5f-8695-89c138425274 | -13.82026 | -53.99385 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f767be4-9ae8-3b65-8f4e-427bdec73ef1 | -15.63788 | -47.73196 | 2026-08-22 05:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9043b8c-05b5-3e21-9f02-4d0dd26f34e4 | -17.92253 | -44.38918 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 32365c5e-1a00-3a60-82f2-2486e2d19883 | -17.84565 | -44.46508 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2c1adde-b6f0-3943-b858-8eca58a0d881 | -13.98756 | -53.68004 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ab5d3872-428b-3552-be13-49568d77ea14 | -15.18269 | -48.74492 | 2026-08-22 05:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 416f7eee-601c-3252-a380-a7b9f1b4e2b1 | -15.24856 | -52.85012 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48b50c4b-4020-3959-9e14-c0f5ced71e63 | -16.95431 | -46.11786 | 2026-08-22 05:06:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0fb6aea-5feb-3f59-9910-70ae90bb4248 | -13.88223 | -53.98226 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06c83a04-5992-38ff-8749-f320ea568231 | -16.03184 | -52.17442 | 2026-08-22 05:06:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f549221-2bd7-324b-84d9-bf90acf86f49 | -14.04612 | -54.09992 | 2026-08-22 05:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f2873f01-f688-3b61-b9de-f8306d499ded | -17.92051 | -44.40903 | 2026-08-22 05:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2461e458-d159-38d3-a934-53fc86018223 | -14.72763 | -47.14234 | 2026-08-22 05:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bcef80c-9761-3af1-a5c4-05b26f6eca6c | -15.00739 | -52.69589 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c1f2776-b3b3-3ea9-80db-bda0b72425d3 | -13.52365 | -58.1186 | 2026-08-22 05:06:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 896d63f9-3f11-36a2-aa88-c4a553f5bceb | -19.74625 | -45.10509 | 2026-08-22 05:06:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e85d37e4-7df3-3776-a43d-7eeed99d9eba | -15.20521 | -52.76966 | 2026-08-22 05:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 957c3448-7e1b-304f-9083-80e36270afc9 | -14.19047 | -53.02394 | 2026-08-22 05:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6b16d67-cf89-30f8-aa0f-36022e6c6cdf | -17.9602 | -42.72492 | 2026-08-22 05:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e0a3698d-39f2-3869-bdaa-2ff7c547e165 | -16.71355 | -47.70026 | 2026-08-22 05:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README55.md)
