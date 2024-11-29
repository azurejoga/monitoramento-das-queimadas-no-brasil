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
| 58fa43be-0c3e-3e1c-a771-eed810f5d1f8 | -17.5805 | -42.7483 | 2024-11-29 02:50:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f766fb4d-c466-3934-820d-dcf230de765b | -1.9726 | -46.4467 | 2024-11-29 02:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| eacb98ae-1315-3ae3-9035-39541f5fc40b | -2.8665 | -45.5304 | 2024-11-29 02:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1f3f7648-282c-3b15-8457-2a2ebc0ae262 | -2.6498 | -48.7986 | 2024-11-29 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 3ab177bb-465c-367e-9283-bdd029376354 | -2.8425 | -46.8193 | 2024-11-29 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e7649d62-29a3-376f-97de-a0391ead5770 | -2.6684 | -48.7767 | 2024-11-29 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 361.5 |
| cc6c882a-7299-34f2-8694-836456846c73 | 1.8399 | -55.8218 | 2024-11-29 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ed242d5f-faff-324d-838f-716f1fe88a02 | -2.9844 | -53.2819 | 2024-11-29 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 245.7 |
| 389c1d46-47fc-30c0-8f8e-8830a19ef093 | -3.0028 | -53.2815 | 2024-11-29 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| fadedce9-b61a-3908-8d6a-b7a9ca256889 | -2.9844 | -53.3022 | 2024-11-29 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| c2823aba-134d-34b0-bbc7-9b263250d9e6 | -17.6007 | -42.7434 | 2024-11-29 02:50:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6dba2c21-ce25-3cd3-8e97-9f250528af57 | 1.2171 | -55.9667 | 2024-11-29 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1f7303b5-ee29-3547-82a7-27d95f4ff6aa | -3.3439 | -46.6912 | 2024-11-29 02:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3ff2d384-2c6d-3890-ba3d-15c3caa7b4a3 | -2.966 | -53.3027 | 2024-11-29 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 427d0422-efbb-3518-bd68-8557c8b0efb4 | -2.3419 | -46.8781 | 2024-11-29 02:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| afee7ba0-de33-310b-a8dc-e63bdf171dd1 | -1.6997 | -52.4535 | 2024-11-29 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 780c303e-5ea6-3251-af20-051ffedf742d | -2.6499 | -48.7772 | 2024-11-29 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 208.9 |
| ce50aada-6a07-36b2-8551-370c2cce3a20 | 1.1988 | -55.9669 | 2024-11-29 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 055d6ec6-b9dc-3224-8d31-9ec6cc627043 | -4.4404 | -46.5975 | 2024-11-29 02:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 283e92dc-c43d-3d94-84c9-f74bcdba4192 | 1.2171 | -55.9471 | 2024-11-29 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| d2174e76-4022-363e-a2ca-3963d9b2f9f7 | -1.092 | -53.3954 | 2024-11-29 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9f04d7bd-ab43-31e5-a158-755d4f08d375 | 1.1988 | -55.9472 | 2024-11-29 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 136f4c54-9052-3484-81c3-727f1ae1dd63 | -2.6683 | -48.7981 | 2024-11-29 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 355.9 |
| 896d340b-125b-39d7-8af1-3bd47b48d0c3 | -1.6997 | -52.4535 | 2024-11-29 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 694b9fc2-1850-3457-810d-1fb1fe951210 | -4.4404 | -46.5975 | 2024-11-29 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 310c28c3-cb10-3b0a-ac31-07c507ae6fd2 | -4.4405 | -46.5754 | 2024-11-29 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 99.3 |
| c20aaeec-d5cc-3a30-a517-78ab6cc8cce5 | 1.2171 | -55.9471 | 2024-11-29 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b393107e-4431-32b8-8102-c4b9bc439933 | 1.8399 | -55.8218 | 2024-11-29 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 7c0f27ad-90ec-3f4b-98cd-2eb414e7885b | 1.2171 | -55.9667 | 2024-11-29 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 46614e9b-4cd4-37a0-a780-7097604a87cb | -2.9844 | -53.2819 | 2024-11-29 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 291.0 |
| ce581005-3250-3dd0-bafb-499d6588b848 | -2.8425 | -46.8193 | 2024-11-29 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| b9ebb913-eeb2-3e4a-b47c-0932cc9a2e20 | -4.4219 | -46.5764 | 2024-11-29 03:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 67d3f231-f3f1-338b-86b6-b3df97cd7c5b | -2.9844 | -53.3022 | 2024-11-29 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 1da6f40d-e397-370e-b349-b9b0ff367df4 | -17.5805 | -42.7483 | 2024-11-29 03:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 71ba6778-7bbb-3779-8177-726e651085ed | -1.092 | -53.3954 | 2024-11-29 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b25d0b87-284f-38ae-81a0-f158cca4557e | -1.9726 | -46.4467 | 2024-11-29 03:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 464ddc77-c6f8-35b7-829b-4a8d53f2c639 | -2.3419 | -46.8781 | 2024-11-29 03:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ffb29b38-23e1-34ad-8d13-f3c9ba594d66 | -3.3253 | -46.692 | 2024-11-29 03:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 084e50d7-3558-3982-9087-42f4e0cf05ff | -2.966 | -53.2824 | 2024-11-29 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 7afedaf3-0888-39dc-ac5a-be414104007e | 1.84 | -55.8021 | 2024-11-29 03:00:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 73d04677-436a-3af6-b70b-cc4a87dd294b | -4.2225 | -45.7634 | 2024-11-29 03:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 7e2f5760-dc02-3686-bd3d-12afdcceb117 | -2.966 | -53.3027 | 2024-11-29 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b2002309-3733-37c4-a58d-9232e1c66030 | -1.5869 | -53.8336 | 2024-11-29 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 425420fc-93ab-3abf-895e-d442c9a204d5 | -2.67 | -48.74 | 2024-11-29 03:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 641704bb-79cf-375b-9cc3-28a190b6cc16 | -2.69 | -48.8 | 2024-11-29 03:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd9ae2f-4c9e-3dc6-84b7-2c4a12c8d68c | -2.67 | -48.79 | 2024-11-29 03:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca9748b-f3e5-3700-bb2d-6e173f8e046a | -2.64 | -48.79 | 2024-11-29 03:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d20a21e4-811b-33b8-9ae9-61228f4129ab | 1.1988 | -55.9669 | 2024-11-29 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2c2d3258-fbc1-3b6d-94a5-d6980e8b83b2 | -2.9844 | -53.2819 | 2024-11-29 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 252.1 |
| 0917faec-7f93-32b3-ad30-2b121400f17c | 1.2171 | -55.9471 | 2024-11-29 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 1906d4a9-af32-32d3-8770-07af898d40a4 | -4.2223 | -45.7858 | 2024-11-29 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d4695e08-445c-30a8-a05e-270b0afea242 | -17.5805 | -42.7483 | 2024-11-29 03:10:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 19a6210b-b07f-325d-8bac-69c40a3e2353 | 1.2171 | -55.9667 | 2024-11-29 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 16637c77-a77e-3068-8bc4-06a96783de27 | -1.9726 | -46.4467 | 2024-11-29 03:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9bc8985d-2ebb-3e72-b1fd-90e947e16edb | -2.6498 | -48.7986 | 2024-11-29 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 191.5 |
| 199f5264-afe2-3cd5-b4b9-43e8c274ffda | -2.966 | -53.2824 | 2024-11-29 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e6e3b436-eb38-3e42-9b6e-72dee4a96706 | -2.966 | -53.3027 | 2024-11-29 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f2b12552-d236-304f-957b-bd666bfbabab | -4.2411 | -45.7625 | 2024-11-29 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 114430b4-866e-382e-877c-e3b1cb5ff749 | -1.5869 | -53.8336 | 2024-11-29 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 129bed4d-b209-375c-9dae-43ddbb1f5cc0 | -2.3419 | -46.8781 | 2024-11-29 03:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 4eb20d7d-c95b-3360-97cb-878709c76cf6 | 1.8399 | -55.8218 | 2024-11-29 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1a6353e3-2216-34c3-a570-c0239a28a3ec | -1.092 | -53.3954 | 2024-11-29 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 45b105cc-57e1-33c6-9ff6-945b08d46214 | -4.4405 | -46.5754 | 2024-11-29 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 019d3986-2f68-3852-86e1-a30746c4b9d7 | -4.2225 | -45.7634 | 2024-11-29 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 467dfd2c-eae1-3b01-8f4d-a90897a6d366 | -1.6997 | -52.4535 | 2024-11-29 03:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 8d4eb6fe-27fe-347b-b394-5f4458a02ea9 | -1.9541 | -46.4471 | 2024-11-29 03:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| cd932dff-9f7d-3268-a7f6-76c003a41a99 | -2.9844 | -53.3022 | 2024-11-29 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 169.6 |
| e0e9efa3-45b0-38bb-9b6c-0c57c3fe74ce | -2.3419 | -46.8562 | 2024-11-29 03:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8b5e4bd5-1182-333c-9dd9-a57de58d1f44 | -2.6684 | -48.7767 | 2024-11-29 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 237.8 |
| 290a8f93-df43-31d8-8bc6-1f28890a554b | -2.6499 | -48.7772 | 2024-11-29 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 1585948f-191e-3e9f-b68e-9d065c54c626 | -2.6683 | -48.7981 | 2024-11-29 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 321.9 |
| c0eb8c75-f7e8-3543-b0c4-c6345e946acd | -4.4219 | -46.5764 | 2024-11-29 03:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 48b25d1e-b7bd-384a-87fc-9cf3670eace8 | -4.84194 | -41.25328 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8982ef2a-ff0e-34e4-8cc3-7c9530ad175a | -4.85624 | -41.25929 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f213280d-54c4-3eeb-8af9-5dea9d210d1e | -4.50646 | -42.07434 | 2024-11-29 03:17:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b5d23a37-9290-3723-9cfe-efa40ab6ce03 | -4.86742 | -41.273 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| cb5a6ca0-866f-321d-a167-89bf65d2a7c9 | -7.27258 | -39.28667 | 2024-11-29 03:17:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf099917-0670-3439-8901-0ee73c1af6b9 | -4.86185 | -41.26603 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f2868ac4-8293-36f8-9062-b47522d68386 | -7.27624 | -39.28704 | 2024-11-29 03:17:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7ea65b2a-c911-32f3-970f-0057ebfa331f | -4.93919 | -38.11826 | 2024-11-29 03:17:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f292321a-8d55-3c55-98c5-2b576f879e58 | -5.14886 | -37.74313 | 2024-11-29 03:17:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 79205365-b0ef-3f64-907f-875fe4735931 | -4.67331 | -42.38291 | 2024-11-29 03:17:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9997e6d6-6be7-377f-a858-4b22bf95588f | -5.14874 | -37.74368 | 2024-11-29 03:17:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7807db28-c237-3565-8ac7-226ae7c38361 | -5.82809 | -39.20682 | 2024-11-29 03:17:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 284764a1-d1b5-38a0-ace0-10565b44203f | -6.82557 | -35.06452 | 2024-11-29 03:17:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b96cc895-5a3c-3c15-a327-f7b6417bec66 | -6.91508 | -37.84003 | 2024-11-29 03:17:00 | NOAA-21 | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3d28cd7b-df2d-31ce-9132-032d6f52256c | -4.67065 | -42.38299 | 2024-11-29 03:17:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 98c11fef-302e-3230-a36b-36c0bddc432d | -4.84082 | -41.2594 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ead0ba08-6ba9-362b-a86c-6d14526d7a32 | -4.84656 | -41.2652 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e8defbf4-f693-318e-b553-ba70c458afbd | -4.86825 | -41.26826 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 470cb96f-46a7-39bd-9e86-b4150bd0b60c | -7.025 | -39.3699 | 2024-11-29 03:17:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3138d433-fb7f-3e34-8ab6-4cb2c09482fa | -4.86663 | -41.27758 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 565ba5ad-1e4b-3ba2-ab73-54a7612a0498 | -4.84299 | -41.25738 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ba42812d-df10-3c3a-8037-4bad0eaaacc2 | -7.06067 | -38.97281 | 2024-11-29 03:17:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e5b0aeab-7921-357a-aa65-1ac20753230a | -4.85423 | -41.26038 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| eafb875b-5c1f-3f0c-9ad7-22e99f3ab420 | -5.56186 | -35.52529 | 2024-11-29 03:17:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b54659c2-d067-36cf-8958-6478129cadf2 | -6.91562 | -37.83694 | 2024-11-29 03:17:00 | NOAA-21 | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7cff5990-0346-3e07-a07f-55d1658759b8 | -7.22143 | -39.05785 | 2024-11-29 03:17:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 00e4cb5a-5af3-3a29-beda-bb56a84af263 | -4.84401 | -41.25159 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d89feb59-89e5-3fc6-a9e0-b60fb471f0ed | -5.1493 | -37.74048 | 2024-11-29 03:17:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
