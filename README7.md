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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee68a01-482a-3696-a452-5e168d6672cf | -18.26947 | -52.88329 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9e67c807-a237-3c89-9191-5293499f59fa | -18.28905 | -52.90041 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 393.4 |
| e53988a3-581c-3942-84b2-e86fdc6a5a82 | -18.29796 | -52.91582 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1a29ebde-52b6-3fde-a1e9-f8549d1998eb | -18.27493 | -52.89152 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.7 |
| f17cebab-b5fc-3841-9eab-6304ff1355c9 | -18.27839 | -52.89888 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 341.8 |
| 98e5bcf9-6a85-371a-ad97-8a48d8c6b622 | -18.29447 | -52.94349 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3c0c715e-afd3-3dd5-b5a7-006b3db13563 | -18.28731 | -52.91431 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 468.0 |
| 57428508-420c-320d-bd2e-39cc9b4f3675 | -18.27666 | -52.9128 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 55a7caa3-089f-3372-a781-00fcf65abbfc | -18.2731 | -52.90546 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 48f3b54f-cf8a-3085-ad8b-bff0ce2a8067 | -19.45166 | -56.6199 | 2026-04-24 06:59:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 29303a0d-8a72-373e-8a33-bffbb9fb0622 | -18.26774 | -52.89728 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 28acce16-83be-3f3e-9f46-4a28fd42c6d1 | -18.29447 | -52.94347 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b32bed29-c8d7-351d-b955-166ef26363df | -18.28905 | -52.90039 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 393.4 |
| 5d779f38-d03d-358b-85df-1c30bd34d4ed | -18.2731 | -52.90545 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| c92a5c7c-22f9-3310-b144-ec3434b767cd | -18.26947 | -52.88327 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e5beae9b-b484-3f73-a234-e2fb22e5ad2f | -19.45166 | -56.61988 | 2026-04-24 06:59:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 9d3ef506-4f62-34f5-b267-8c30b8235f8c | -18.27666 | -52.91278 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a482efb0-b4da-3ddd-84fb-1aee7e2e0fea | -18.26774 | -52.89727 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| d01e65d7-3dbc-3fab-b13d-0a8137588dfe | -18.27839 | -52.89887 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 341.8 |
| 5b8760ef-51ad-3e80-a71a-e7f8246ea21e | -18.27493 | -52.89151 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.7 |
| f3578353-9e04-3093-b1ab-aa84f5bfc60e | -18.29796 | -52.91581 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8c1d9e2b-24fa-38ec-b5a3-d1644d32d9b9 | -18.28731 | -52.9143 | 2026-04-24 06:59:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 468.0 |
| 15ff3148-f874-349b-847a-87f71e107057 | -18.2858 | -52.8983 | 2026-04-24 07:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 278.3 |
| 481c7111-73f7-3016-86de-3a34a7a53dc9 | -18.2659 | -52.9016 | 2026-04-24 07:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 629001f5-54cb-3359-9196-3b8828384458 | -18.2863 | -52.8767 | 2026-04-24 07:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| b917979d-d283-319c-940e-413a5861800b | -18.3053 | -52.9167 | 2026-04-24 07:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 2d53f8ff-3022-31dd-a618-d068d51ccafe | -18.3058 | -52.8951 | 2026-04-24 07:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 184.1 |
| b3f9d14e-72d8-34f3-a5c7-67d1fda07835 | -18.2854 | -52.92 | 2026-04-24 07:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 257.2 |
| 9f05bee1-4dfd-36d2-86c0-a562dc55174c | -18.3053 | -52.9167 | 2026-04-24 07:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 86370abd-1458-34a2-b5f7-d70b72b2ee48 | -18.2858 | -52.8983 | 2026-04-24 07:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| abcdb9f7-a5ca-34a0-b160-14c646d8a8be | -18.2854 | -52.92 | 2026-04-24 07:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5bb428ab-44ba-36e6-ad2e-f8db57545585 | -18.3058 | -52.8951 | 2026-04-24 07:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 2abdbeba-dd29-365a-b590-da6ecc515a88 | -18.3058 | -52.8951 | 2026-04-24 07:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 148.9 |
| b4143185-6a49-39f7-80e4-6ada9d8bef67 | -18.2854 | -52.92 | 2026-04-24 07:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 27ff90ed-53cc-32cc-817b-695bbe48b677 | -18.2858 | -52.8983 | 2026-04-24 07:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 4c888132-3aff-3efa-8ad9-bc62a4c43980 | -18.3053 | -52.9167 | 2026-04-24 07:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 142.5 |
| ba8d8295-4bf9-39c8-a895-1304a0bc63f8 | -18.2854 | -52.92 | 2026-04-24 07:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 97f82dd1-0816-3623-8f18-c574960e725d | -18.3058 | -52.8951 | 2026-04-24 07:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 127.7 |
| f5815f6e-3d66-35b2-bc7e-c45b937fe171 | -18.3053 | -52.9167 | 2026-04-24 07:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 194.1 |
| c04dab1f-797e-3868-b5e2-fe0797fa4d24 | -18.2858 | -52.8983 | 2026-04-24 07:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 9af7b11b-3e48-3cb8-ac95-55aa3762f48e | -18.3058 | -52.8951 | 2026-04-24 07:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 87443c1e-250a-35e1-8562-49b6e652f621 | -18.3053 | -52.9167 | 2026-04-24 07:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 0f7b0bd1-f4f5-3f96-a171-384dbddc2955 | -18.2858 | -52.8983 | 2026-04-24 07:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| b2f97dad-ac6d-3f95-bbf5-751577884342 | -18.2854 | -52.92 | 2026-04-24 07:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2a3eebaa-da34-319b-92ef-e296c48fc9e7 | -18.3053 | -52.9167 | 2026-04-24 07:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 256.1 |
| e41a8db4-e7fd-3dac-a4bb-e6d1a9ccfbfa | -18.3058 | -52.8951 | 2026-04-24 07:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 129.0 |
| dd76580f-5371-3411-8d90-ef67c3f23d00 | -18.2854 | -52.92 | 2026-04-24 07:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 12572fb3-865b-37f4-bf73-ec7194be9a8b | -18.2858 | -52.8983 | 2026-04-24 07:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| ef2bd6a4-390e-384c-9352-0bdeafa92774 | -18.3058 | -52.8951 | 2026-04-24 08:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b343fd17-c3da-31de-b9ba-a425e29bf6af | -18.3053 | -52.9167 | 2026-04-24 08:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 2d64c8f0-9058-3bf4-ab60-2c446a9f6b04 | -18.2858 | -52.8983 | 2026-04-24 08:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| bcee4061-fd5e-3b92-96fa-e0e8267ad392 | -18.2854 | -52.92 | 2026-04-24 08:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 4519db9c-becb-341f-b9d2-8518eb556717 | -18.3053 | -52.9167 | 2026-04-24 08:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 138.5 |
| cf8d71f3-3cd6-3b08-902b-19c7b6e5ce60 | -18.3058 | -52.8951 | 2026-04-24 08:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| a8590c60-77f7-36f5-8e7b-7f790e9db532 | -18.2854 | -52.92 | 2026-04-24 08:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 3f18768c-087e-3a5c-a41e-dd2ee17e7b7e | -18.3053 | -52.9167 | 2026-04-24 08:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 141.5 |
| f98747bc-da22-3eab-9311-2fc359aa42c1 | -18.3053 | -52.9167 | 2026-04-24 08:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 20b530da-c456-3adc-8e24-d62fedced92e | -18.3053 | -52.9167 | 2026-04-24 08:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4769dd3f-2c54-3790-b7e8-208165738e3e | -18.3053 | -52.9167 | 2026-04-24 08:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.6 |
| de332674-b92c-3234-84a8-bda0fff8905b | -18.3053 | -52.9167 | 2026-04-24 09:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.3 |
| faae2fb7-175e-3edc-a8d8-97c4d5405269 | -13.3766 | -45.301 | 2026-04-24 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 4678d55b-185a-3224-9ebf-8d9dd3870191 | -11.77779 | -43.65446 | 2026-04-24 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92221625-14fc-3a2e-b4c6-e624f6f59814 | -11.76922 | -43.63758 | 2026-04-24 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 17abe12f-0b74-38fd-9994-c51b8ac83827 | -8.6932 | -39.4068 | 2026-04-24 11:42:00 | TERRA_M-M | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6053040a-0189-30ac-80d6-17119c1898c5 | -11.76922 | -43.6376 | 2026-04-24 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6f3dccfd-c0f0-36c2-ba0a-de1a49cee1f0 | -10.55633 | -42.43995 | 2026-04-24 11:42:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1d2cd76e-b9c3-34a5-95d4-75d5c95c6ec3 | -10.55633 | -42.43993 | 2026-04-24 11:42:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7c6c3992-cc61-3b8a-b791-67e65fc26ba3 | -11.77779 | -43.65445 | 2026-04-24 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3868f43f-e142-3a5f-b68e-15664ec3ac95 | -11.76794 | -43.64657 | 2026-04-24 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 466060d6-81dc-38fd-9f40-26dccb93fd6c | -8.6932 | -39.40678 | 2026-04-24 11:42:00 | TERRA_M-M | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5a839f9e-6bb8-3a84-8648-28f44170d876 | -11.76794 | -43.64655 | 2026-04-24 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dc843123-d874-3dab-950b-a687ac420014 | -20.20546 | -46.88227 | 2026-04-24 11:45:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4bed50b7-5006-35fd-86fa-567384237e35 | -13.38107 | -45.31276 | 2026-04-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 758711a7-570e-3484-b67a-9d93ca2389ff | -13.37261 | -45.30492 | 2026-04-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7b611ae8-6f30-3f43-b69a-73f7e00de9a1 | -17.37627 | -42.61813 | 2026-04-24 11:45:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d314679-1c43-3c77-aad3-fafb9665069d | -18.3013 | -52.92726 | 2026-04-24 11:45:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 421356cb-3fb9-3f6d-9abb-81f995863865 | -17.60356 | -44.60711 | 2026-04-24 11:45:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 109c3a3d-e493-365b-83b2-b4688f623440 | -17.38575 | -42.61941 | 2026-04-24 11:45:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c7401f0d-4705-3701-8b0b-f8382e9192a5 | -19.16306 | -40.45188 | 2026-04-24 11:45:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 93619939-822b-3bd3-8cbf-b0d1c151345e | -17.38575 | -42.61942 | 2026-04-24 11:45:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 442d2643-8a23-3c3d-80a2-7b0e5225594a | -12.05806 | -45.33684 | 2026-04-24 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b75b1cff-e85a-3852-b824-348960afe7f7 | -21.02344 | -45.5731 | 2026-04-24 11:45:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbe638dd-827c-35ea-ab3e-cfbb9e78ff5f | -14.87749 | -46.84275 | 2026-04-24 11:45:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 56c2dc2c-0235-3e36-ad81-ccbec4e76f40 | -12.05806 | -45.33683 | 2026-04-24 11:45:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ddc02d24-8bae-3ecf-9b88-08f2a503ab54 | -13.37261 | -45.30494 | 2026-04-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e2fda594-e94d-3479-b496-7a6eea17f81f | -18.2783 | -52.89792 | 2026-04-24 11:45:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 126.2 |
| bda97f37-fcaf-32aa-a636-0889d51a697d | -13.37124 | -45.31427 | 2026-04-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2291aa07-edb6-3b7b-9a7b-0ef33bf9a510 | -21.03229 | -45.57449 | 2026-04-24 11:45:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa63150b-c521-3908-afb0-3ba979acc327 | -19.16377 | -40.44548 | 2026-04-24 11:45:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 20dff484-9d0f-3234-ae53-6b10a9b4cffb | -13.37124 | -45.31425 | 2026-04-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5a3c245c-989c-305b-8edc-f418ea8beff3 | -13.00734 | -42.56521 | 2026-04-24 11:45:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| da4d8733-bd14-3263-ae33-b433aa97f339 | -14.87749 | -46.84274 | 2026-04-24 11:45:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 573b5839-1844-3a8e-b1c9-185f0236936b | -13.00602 | -42.57479 | 2026-04-24 11:45:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 81fda719-b09c-353d-ae9e-eb31ad55741e | -17.37627 | -42.61815 | 2026-04-24 11:45:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f878a8cb-e47b-3579-90f6-169fb0d29602 | -12.99692 | -42.57354 | 2026-04-24 11:45:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| ceaf0f5d-fba5-3ea1-b04b-afd64a453eb2 | -15.93081 | -43.73004 | 2026-04-24 11:45:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69f374f3-e53d-3b59-83db-447675345cf3 | -17.60356 | -44.60712 | 2026-04-24 11:45:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c291d426-0076-3568-bd39-9aa8d01ddd12 | -12.99824 | -42.56395 | 2026-04-24 11:45:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| f8896490-29bc-3ccd-8ae6-971db4db05d6 | -13.52857 | -42.9911 | 2026-04-24 11:45:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 0336dee2-51c1-322b-aa40-528ab883b97b | -13.38107 | -45.31274 | 2026-04-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |


[Clique aqui para ver as próximas entradas](README8.md)
