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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e349c812-3913-3351-8afe-5598b4cec938 | -11.62612 | -47.15194 | 2025-09-08 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b08d614d-977a-3fde-8412-bb10280dc0ab | -15.19328 | -47.96143 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd976b51-669e-333d-86ae-61f5dc31282e | -16.2792 | -45.68197 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71f6974c-6d40-3e62-90ec-05f743ad186c | -13.72345 | -46.89826 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c9f7644-8482-39ae-9fbe-b6ca39c210a4 | -14.73664 | -47.77013 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 482a6a32-13a0-341f-aa19-a3497554e3b0 | -13.81339 | -46.28155 | 2025-09-08 03:40:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecbcd6ae-04b4-3273-b9f1-1732286cd357 | -13.82663 | -43.86047 | 2025-09-08 03:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81c634a5-0081-3e9f-90aa-09e5b68f99d2 | -15.35151 | -49.12795 | 2025-09-08 03:40:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b36c366a-0fd8-35a0-a9e8-fef84cbe160e | -12.80824 | -48.0007 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b39d6d01-1f33-39b9-a356-d48bbaa761ce | -12.51851 | -45.26082 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3661dbb0-9a21-32b6-bd1d-e3b7a41da7d3 | -11.5719 | -44.65617 | 2025-09-08 03:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b1e86dc-7620-35ed-b5f9-407a6e34c66c | -11.27588 | -46.47274 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| bd460597-2ae4-3281-bb54-8f7385d5e68d | -11.03392 | -45.949 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11a1714c-9743-367d-9c0a-29ec30faf6ea | -9.15098 | -46.06927 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2765cc78-a398-3bfd-b7f0-b0219b5db73b | -11.61967 | -47.1506 | 2025-09-08 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1afa7ad-668e-39c5-a1e0-d97d62bbb888 | -15.16136 | -47.98262 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccf4196d-1680-3548-898e-b683997c012e | -9.71773 | -43.98346 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e08f929c-a0b1-3a57-9aa4-bd98d19fe060 | -13.03915 | -47.12313 | 2025-09-08 03:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad0ce11c-4942-3544-8b11-43922cc66b8d | -14.51882 | -48.75711 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0edec538-b085-3e05-bcf7-54e88a1f45d3 | -9.33044 | -46.52187 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa060981-b391-3650-a912-383e40803983 | -11.83253 | -46.77099 | 2025-09-08 03:40:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27ad237a-72a5-3cde-9cc4-d05f8fa7590f | -15.02552 | -45.469 | 2025-09-08 03:40:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dd28eb3-ca60-3040-9176-5d7b92c768e7 | -14.52385 | -48.76616 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43e3592a-77c4-3cec-bf44-5531e904ae2b | -13.83297 | -46.24615 | 2025-09-08 03:40:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d10b755-2099-3f01-956b-64a5fb68ea10 | -15.18064 | -47.95834 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 987b8aea-79cf-34ad-a323-0fbbe893c24a | -10.82235 | -47.73862 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f05ad36-562a-36af-9c67-e64c6dd8dcfa | -14.28977 | -44.86689 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ebc606a-a646-358c-b0a2-64459397e5e2 | -12.41199 | -47.4988 | 2025-09-08 03:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85c0b72d-10e6-3b27-b4dc-1bc42385dee5 | -9.33482 | -46.53535 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd3e7297-5188-3a3c-ad58-8529624e0647 | -10.17706 | -46.22986 | 2025-09-08 03:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52e8c89d-346d-3b82-8b0a-f2bfebcb10ba | -9.87615 | -46.53289 | 2025-09-08 03:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 491dc5c4-1903-36fe-8f3c-123b6151ba54 | -9.71841 | -43.97989 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a91ec2e6-176c-39c4-a27d-128612abae0f | -10.1425 | -46.20728 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ccd0544f-cca1-3da9-b692-0859a691128b | -11.4217 | -43.64172 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc6510c3-3cf4-3196-af08-95d3dd238fcd | -13.82302 | -43.86551 | 2025-09-08 03:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1676e4ea-a637-327a-a8e4-3afeaa265012 | -10.13993 | -46.20582 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fe54952-05cf-3a4f-8d42-386ac0df0dd7 | -14.77628 | -48.11631 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfb60f19-74a4-30fd-84aa-9e5538c42b10 | -15.53532 | -48.18292 | 2025-09-08 03:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33845430-7b8f-3d57-a523-43151d863267 | -10.81805 | -47.75291 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c84c60e-0c65-3887-9f93-653573a5f4ea | -14.29846 | -44.87906 | 2025-09-08 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cdf65ba-e34c-36fc-a4d9-0fdc857cbb38 | -12.60629 | -44.64585 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2517df44-7db7-3d6c-9b75-2b60b724c240 | -11.62697 | -47.14778 | 2025-09-08 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 709b461f-0ba2-3a03-8b01-3f32b87757e9 | -10.14673 | -46.21869 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1b34760-d289-3042-853a-521e00fa3bce | -10.14448 | -46.1974 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e260d78-691d-3be8-87cc-b449e7a749d0 | -11.27603 | -46.45282 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eba9b7f8-2167-3385-bd39-efccb0fc08db | -15.52895 | -48.18139 | 2025-09-08 03:40:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e6ad359-05b4-30aa-a4b4-d86579b2679f | -13.01037 | -45.2189 | 2025-09-08 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 862de044-9e31-3a3d-91d7-a70ad18e8fee | -9.32935 | -46.52732 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 316904a6-b453-3730-831b-74dcd8fc6190 | -11.42444 | -43.65563 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00e95aca-1525-3a53-9273-d153e71e4222 | -13.725 | -46.8908 | 2025-09-08 03:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2597232-7ce0-3da3-9f89-1b5dce24c443 | -13.63667 | -43.80721 | 2025-09-08 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa935b94-4f2a-368c-9fca-5f2a5363a0cc | -11.39534 | -43.55158 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76eb81bb-5fc8-355f-a63a-031c84f16c73 | -10.80048 | -47.73499 | 2025-09-08 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 772e1188-7d6e-3c3c-b9e5-20dabb597d47 | -11.60646 | -47.14942 | 2025-09-08 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a029c27e-158e-37a2-8c13-bc83db654821 | -12.86474 | -47.97985 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3132daa7-425d-3d23-8f29-d0e253b9b5f0 | -8.69611 | -45.31998 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 335cc372-ee09-3bc3-a755-39e552eb40e4 | -9.19975 | -46.05385 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1eff274-64df-3dd8-b8a8-b7db9ffdf1d6 | -13.35207 | -44.43047 | 2025-09-08 03:40:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8344efa-61c7-31dd-b406-d0cb4cf6e36f | -10.14422 | -46.21729 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e6ecec7-932b-32ff-9073-b04de70b5929 | -8.92462 | -45.81443 | 2025-09-08 03:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1644e79d-53b7-3efe-b698-8c2a92e22288 | -11.15253 | -45.24565 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41c38a6d-4e63-3271-9edd-8b82886a95ab | -12.1673 | -43.94708 | 2025-09-08 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fd0cc51-b0c4-3708-9904-e364e1766f4c | -9.19345 | -46.03313 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5a3106b-4126-3ab8-970b-500ca2d82154 | -10.28663 | -48.81195 | 2025-09-08 03:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd375837-a305-3464-8521-672d9ccd5fab | -12.8676 | -47.98209 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12cd447e-884d-3a37-adc8-5663273dd975 | -10.14146 | -46.21246 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8a8ab45-4bfe-3dbf-aeca-2d9a4bdaea84 | -12.87424 | -47.98341 | 2025-09-08 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 898a8cd3-e494-3db8-914d-1f726faec7db | -11.41083 | -43.58396 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ec6c849-c45d-3f0a-85cc-6287d149100c | -13.82417 | -43.85949 | 2025-09-08 03:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5c5327d-63d3-3748-bd54-a19446295586 | -11.28408 | -46.46431 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b6b1a2de-4fff-36f1-a0cc-4ebd03123a1e | -16.27872 | -45.68461 | 2025-09-08 03:40:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be928bd9-bdb2-3b30-a4f9-af6f6f5e55ba | -8.69874 | -45.30585 | 2025-09-08 03:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bfb164f5-89a0-3c8f-ab54-dcafdc461af6 | -14.51606 | -48.79626 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e42acccd-eeac-3e3e-bd17-b96bbd624a64 | -15.18993 | -47.97688 | 2025-09-08 03:40:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f18c87ab-8b5e-34d5-8c0c-eaadc9f63917 | -8.8238 | -45.90002 | 2025-09-08 03:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfbdfe41-caac-39a7-afe9-8e0c342fcb98 | -13.6735 | -44.22333 | 2025-09-08 03:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7a5572b-f685-3b2a-9668-d20c966091be | -14.78366 | -48.11539 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60372a29-99ae-372a-8b78-0fd75688e981 | -15.02627 | -45.46536 | 2025-09-08 03:40:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d281483f-69cc-3885-b721-8f013b193e02 | -11.28316 | -46.44948 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fce0a88b-f139-3014-a4b4-e51699094b76 | -9.20076 | -46.04855 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efd38cab-90ce-3b15-a916-9900e214860e | -11.28549 | -46.47066 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b602a78-79af-3cfd-bc15-122c626db3b8 | -15.13505 | -48.07496 | 2025-09-08 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f028125f-c9fb-3c15-8a31-45c8a885bad4 | -11.03489 | -45.94419 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb557f03-d4cb-3095-85aa-c8089aad44de | -11.01709 | -46.03199 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7a75d26-6892-3fea-b023-803f743bf51b | -15.37736 | -46.42516 | 2025-09-08 03:40:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40a5fb1b-bd03-3190-8055-af7e357293ac | -11.28451 | -46.47568 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 22f21ef3-ffe0-351b-a599-9e8f3e9fe4ac | -15.09462 | -48.13835 | 2025-09-08 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e024a6e-f3ca-3d09-9b52-566ae5ee9d80 | -11.41773 | -43.63421 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b7326cd-26a9-3a35-b768-efb330a350fd | -14.80811 | -48.18748 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfd956c0-7263-38d3-932d-3a80f78902e3 | -11.02417 | -45.93511 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ea35aa4-9942-3c86-9647-772d5dbe6a04 | -13.81183 | -46.25934 | 2025-09-08 03:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4490f6a6-493e-311f-968c-d62d1c06effb | -10.14351 | -46.20224 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 38d81294-f590-3e4e-9f02-69b1b11fce04 | -11.15171 | -45.24989 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd4e22b5-c0a5-3cc5-bdb1-5e8520f314ea | -11.03523 | -45.943 | 2025-09-08 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08bbea7e-e2e3-3330-9cfb-61ccb6145f6a | -14.51657 | -48.76146 | 2025-09-08 03:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c89202aa-0eeb-306b-bd79-231a9547d148 | -9.71878 | -43.98143 | 2025-09-08 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 172dbf9c-f28b-3f5b-83af-1758c7094bae | -13.8236 | -43.8625 | 2025-09-08 03:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d5fef1a-9730-3155-ad4e-36cebdf1c6a3 | -15.08931 | -48.13172 | 2025-09-08 03:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c946c31-af8c-3da5-9686-0add53dc547b | -11.41531 | -43.59064 | 2025-09-08 03:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8f2b2cd-a081-347c-b37c-2c81b6bcca99 | -10.13651 | -46.18991 | 2025-09-08 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README24.md)
