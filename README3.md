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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bdc98db-4b97-37df-8857-fe7a1e1e3dad | -15.88428 | -51.82263 | 2025-09-10 00:28:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 411c49e4-5818-36a8-bf3e-4b0520008468 | -16.7044 | -48.53403 | 2025-09-10 00:28:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3ec94301-6975-3105-b0d0-073f5d11e9f1 | -16.8432 | -49.17078 | 2025-09-10 00:28:00 | TERRA_M-M | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f2322ad4-0f3f-38cc-bd18-3b7049648eb0 | -18.14532 | -51.74386 | 2025-09-10 00:28:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ec93eef9-41d0-3faa-9299-bc56107fd9f4 | -15.473 | -49.37995 | 2025-09-10 00:28:00 | TERRA_M-M | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b1c76901-aab2-38ec-a9ec-a49352972e0e | -19.85221 | -48.09909 | 2025-09-10 00:28:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 14f115a6-fa2f-36ba-becb-07ebf05504a9 | -15.48415 | -49.38972 | 2025-09-10 00:28:00 | TERRA_M-M | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| abcbd46d-4b78-3a0a-87ca-52e6c9a5f8fe | -16.45769 | -51.98764 | 2025-09-10 00:28:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 29.6 |
| c2b65b54-0728-3703-85c7-5241c703af9d | -21.00619 | -46.06024 | 2025-09-10 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 6e9d5290-7694-3bef-85e4-ebf246577d3c | -16.62394 | -49.78297 | 2025-09-10 00:28:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2c17f788-b5cb-3422-9335-db3139a572eb | -20.94238 | -46.27213 | 2025-09-10 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 1409bc39-b757-395c-9fae-4b344c559046 | -19.60268 | -46.0883 | 2025-09-10 00:28:00 | TERRA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 56455063-026e-3c3f-807c-c9661c3431de | -18.00967 | -47.11095 | 2025-09-10 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a55974de-9e1f-3f78-9389-b0db4c36fd89 | -21.02036 | -48.41981 | 2025-09-10 00:28:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 0be07192-04e1-3acc-ad8f-96b8c458fdfa | -16.28545 | -45.68825 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e33c594f-1252-360b-93e8-8e3cc0ddf6e4 | -19.85355 | -48.11012 | 2025-09-10 00:28:00 | TERRA_M-M | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4eae756d-5001-3542-b241-1dee9080b323 | -15.51933 | -48.38362 | 2025-09-10 00:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 678e754c-88b9-3810-8a4d-a7ae82c7a0aa | -16.62838 | -51.83531 | 2025-09-10 00:28:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0e96e9b6-813b-3f43-b95f-27b20720a514 | -17.71902 | -44.49956 | 2025-09-10 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 97d1f802-d135-3423-add8-9430acb2b5b5 | -19.51825 | -45.02296 | 2025-09-10 00:28:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7ffbad33-dc79-3a6b-8857-6cbd48207283 | -20.86815 | -43.70761 | 2025-09-10 00:28:00 | TERRA_M-M | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 3112e64f-64d6-3e79-ae47-1484a4cbd98c | -18.43954 | -45.93849 | 2025-09-10 00:28:00 | TERRA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6153f402-97c1-3fec-a835-a65036fb6393 | -17.71957 | -44.44039 | 2025-09-10 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4ddc5fa7-794d-3075-9baf-03fe7dfd3a8c | -20.54349 | -47.67572 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6e13202a-0e1d-3485-bebc-f74accb92ba7 | -19.54635 | -44.0646 | 2025-09-10 00:28:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 8c5a9061-ee35-3dad-ac19-29b7a4516f38 | -16.45753 | -50.67854 | 2025-09-10 00:28:00 | TERRA_M-M | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 4e4d0903-fc4c-36a9-8cfb-63f73f8fef92 | -19.54492 | -44.05481 | 2025-09-10 00:28:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf4d84a1-8e45-3cd8-8b3d-8e26a3cb05d6 | -18.76007 | -49.61252 | 2025-09-10 00:28:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 405cfb10-7890-3ab1-a4e1-7a3604e3ccbc | -19.84874 | -48.10533 | 2025-09-10 00:28:00 | TERRA_M-M | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 51a4a042-b357-31a5-8534-ea68ccf1535d | -17.70907 | -44.43213 | 2025-09-10 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 54efecd8-d81c-3cb5-9505-f7913f8e6909 | -16.67676 | -48.51234 | 2025-09-10 00:28:00 | TERRA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 30def542-25ca-31e2-8fcb-1314533a69c8 | -17.71052 | -44.44191 | 2025-09-10 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 313aa5c6-97aa-36d9-9b9e-734a8d3513b5 | -18.35364 | -49.35 | 2025-09-10 00:28:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3a4ced3d-d7c0-3ce0-8366-3be9037457c8 | -16.27249 | -49.16928 | 2025-09-10 00:28:00 | TERRA_M-M | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 2d63380e-9c5d-3eef-8c3a-d34d4bd07f54 | -19.93852 | -49.24681 | 2025-09-10 00:28:00 | TERRA_M-M | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 759cfb7a-2e83-3039-bad8-ebd8a3243ad3 | -16.68889 | -48.53196 | 2025-09-10 00:28:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1ad9b892-1b48-3b2b-bf06-51bb74ab6722 | -18.45879 | -46.47646 | 2025-09-10 00:28:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0bcbd351-185d-30cb-883f-28110a0f0ea3 | -20.06637 | -47.52818 | 2025-09-10 00:28:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c5224549-323c-34b5-a911-b470c156377a | -15.87062 | -51.80727 | 2025-09-10 00:28:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 1c910053-d3cd-30b9-8417-074b7ec1959d | -17.29934 | -46.68367 | 2025-09-10 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92b8ea37-96e8-3bf1-9101-d792f6c056bf | -15.22508 | -48.24168 | 2025-09-10 00:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 530984d1-d1f2-39b3-9b9d-03fc24ad90a6 | -19.77344 | -45.79144 | 2025-09-10 00:28:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c3f6c915-bec1-3432-81c5-c6faf0eee6f3 | -16.46211 | -51.97497 | 2025-09-10 00:28:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 7ebd65e2-d1b1-33ff-a1ee-cea32533fea6 | -15.48271 | -49.37838 | 2025-09-10 00:28:00 | TERRA_M-M | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 460daffd-f506-3926-a317-c26371a321a8 | -15.8823 | -51.80581 | 2025-09-10 00:28:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| bab55e37-7c18-379a-baab-d87621738621 | -15.10357 | -48.01779 | 2025-09-10 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b1354226-5aae-3137-a097-7ffaa7dc89ed | -16.57476 | -49.22581 | 2025-09-10 00:28:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9aaad235-4209-3f21-ad3f-a9249d8444d3 | -15.84509 | -52.27043 | 2025-09-10 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5c5e31a9-b712-3049-9ed9-424947837211 | -18.12936 | -51.70987 | 2025-09-10 00:28:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d3800779-6ff8-3b2d-a5c3-aab3bae2d1cb | -18.35365 | -49.35696 | 2025-09-10 00:28:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0330f554-5493-3068-9ee1-d3bcc85b8cf3 | -17.40977 | -49.89452 | 2025-09-10 00:28:00 | TERRA_M-M | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2e7f7a89-a175-3269-87da-828d8a4c5df5 | -15.84623 | -48.0002 | 2025-09-10 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c95859de-8374-3aef-942f-2dcffffd430c | -20.07699 | -47.53736 | 2025-09-10 00:28:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 59eacfca-e8b3-30e8-8a9d-6e7438eec340 | -15.80471 | -52.23927 | 2025-09-10 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2f897a23-fed6-3e0b-8ea5-d09a9d32076a | -18.52592 | -43.27907 | 2025-09-10 00:28:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 1a7671ca-d970-3f95-bff9-17be334df1e6 | -18.77192 | -49.62397 | 2025-09-10 00:28:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 544e1842-bb64-348d-b80f-90aa9cf3a4e8 | -19.2125 | -43.06586 | 2025-09-10 00:28:00 | TERRA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 9ac46bb1-1e24-3fd3-b6ae-a22847f79725 | -17.20934 | -50.16496 | 2025-09-10 00:28:00 | TERRA_M-M | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| adca3f9a-3fb5-3c61-823a-eefc32574c8d | -18.03145 | -47.13703 | 2025-09-10 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 26e27bfe-3c66-3627-9c71-8a7d7d01c181 | -20.47161 | -43.95922 | 2025-09-10 00:28:00 | TERRA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 34fedca6-d1b7-3aa2-b77a-37434c615e8d | -17.30814 | -46.74875 | 2025-09-10 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ba20a70e-7345-3d9d-a339-ffcdf78bed8a | -15.10486 | -48.02749 | 2025-09-10 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 072ecc35-ca34-31cb-b082-6d028f7e7859 | -17.24371 | -46.08023 | 2025-09-10 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| dadd0acd-7f35-3c69-ac56-427676fb1ac2 | -16.11902 | -48.33798 | 2025-09-10 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 01ab818a-43a6-3511-a499-744e9d947039 | -16.41203 | -50.87848 | 2025-09-10 00:28:00 | TERRA_M-M | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5c6bbe8c-3432-37e8-8f79-9c95b4395878 | -21.03165 | -48.43031 | 2025-09-10 00:28:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2b5dc9ca-f594-3a90-aac5-3b2d96c303b0 | -19.9151 | -46.15608 | 2025-09-10 00:28:00 | TERRA_M-M | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bad48cff-7dc5-3727-afe0-d5df56ed2f09 | -20.15428 | -47.69687 | 2025-09-10 00:28:00 | TERRA_M-M | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b7b93d7f-cf7e-39b5-95fe-c4b4613aa61a | -20.1636 | -47.69523 | 2025-09-10 00:28:00 | TERRA_M-M | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 556c99e6-ebd6-3dfb-809c-b87bca9d089e | -15.86087 | -51.82552 | 2025-09-10 00:28:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3fed0fbc-3721-3c48-9917-80ef0c751dac | -17.27689 | -49.21064 | 2025-09-10 00:28:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 373a57a0-1de8-39b1-8fdd-17228dc4535e | -20.52394 | -47.64087 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3f217450-8340-3e68-9d8f-0a97e4271b76 | -18.11734 | -51.7112 | 2025-09-10 00:28:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 824cb10a-55a4-30dd-b6ff-0da004c536f2 | -19.667 | -44.90009 | 2025-09-10 00:28:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 0bfab2ed-45fb-3576-bb3e-92ef816ea2ce | -17.30688 | -46.73943 | 2025-09-10 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c0fe2016-7167-35d9-9eb7-28c6514cef1a | -17.73711 | -44.49655 | 2025-09-10 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56a8c8aa-998b-31dc-884d-51280034a2be | -18.7704 | -49.61102 | 2025-09-10 00:28:00 | TERRA_M-M | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 800441c5-6464-3bc7-b89e-ef53df811c44 | -15.95251 | -48.10891 | 2025-09-10 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ee118e34-90a1-37bc-9172-df2d567bc299 | -16.62251 | -49.77125 | 2025-09-10 00:28:00 | TERRA_M-M | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 9f34fab9-6a41-3f84-a944-538700704e4c | -19.75433 | -45.71805 | 2025-09-10 00:28:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 96af267f-a211-3d78-95fe-61cb15935bb9 | -20.33857 | -42.24914 | 2025-09-10 00:28:00 | TERRA_M-M | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 6f0720ae-7c85-30d3-97d6-8185fa828876 | -14.75919 | -45.3281 | 2025-09-10 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f2b86140-ca90-3356-8397-93294027a082 | -15.95119 | -48.0988 | 2025-09-10 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62668bda-7160-3295-bea0-31bdffb0c972 | -18.13132 | -51.7276 | 2025-09-10 00:28:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 179.5 |
| e3e8ad03-9ca1-306a-b00a-155a8c0af451 | -18.34206 | -49.33934 | 2025-09-10 00:28:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2c12d342-8740-3749-9826-e38ce6a83d45 | -20.16091 | -43.66327 | 2025-09-10 00:28:00 | TERRA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 9ddab03a-14d1-3759-8909-7da35b65246f | -20.13834 | -47.874 | 2025-09-10 00:28:00 | TERRA_M-M | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0508ea7f-0b55-3d92-bcd4-0652198c9d98 | -19.73158 | -47.90698 | 2025-09-10 00:28:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7a2be080-9a95-364a-ae69-0b00e6b6cfd3 | -15.93517 | -50.23159 | 2025-09-10 00:28:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 8b57fa85-9f10-3a6c-97a4-4b0b8c9acf59 | -15.81669 | -52.23691 | 2025-09-10 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 865c38c0-6990-3e02-be23-78289e810510 | -15.87258 | -51.82411 | 2025-09-10 00:28:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 54bef0c7-08c6-3c14-ae58-073affe5c227 | -19.29705 | -47.98169 | 2025-09-10 00:28:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5a7b0b04-b5ca-3ba3-ac83-833c88ed7f54 | -20.13421 | -47.68919 | 2025-09-10 00:28:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6d676e23-cbbd-3bdd-b5fa-7b24122ce11f | -17.74479 | -44.4857 | 2025-09-10 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| cfd908a8-9d3f-379c-9c7a-4c1e8439acb4 | -19.51692 | -45.01358 | 2025-09-10 00:28:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 0ed32b32-bc31-30c1-95a8-8cc8b16c5cc9 | -15.47159 | -49.3688 | 2025-09-10 00:28:00 | TERRA_M-M | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 92f9cc31-3db6-3a1f-8432-c54cea4843ed | -15.87454 | -51.84093 | 2025-09-10 00:28:00 | TERRA_M-M | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0b7997b6-7205-354b-b331-75ab46184239 | -21.55068 | -46.85038 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| e7d8f601-e98d-3ce0-817b-fe1af2a635c6 | -15.52853 | -48.38209 | 2025-09-10 00:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 10878525-4f6e-3c78-b39c-cb31fa9c1b6f | -14.75019 | -45.32956 | 2025-09-10 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |


[Clique aqui para ver as próximas entradas](README4.md)
