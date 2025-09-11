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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c94af79b-3bf1-385b-a514-5be13c7a8cae | -12.39799 | -63.79453 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71c8488d-0797-3fd8-9890-5a66bd09c17d | -11.8803 | -58.80524 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b2d4c5d-64b6-393f-8aa3-e07d8ca41322 | -11.21975 | -54.99308 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a086439-0c1c-3a57-ae3e-86d62dab4114 | -12.92853 | -54.75889 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc41809f-c9df-324a-93af-6a818bc220b5 | -11.78498 | -64.92638 | 2025-09-11 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13ade0fd-cf9a-39ce-9ee3-4472c9967e16 | -9.9841 | -64.97936 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77daf376-f3bf-3561-8cca-5d7ad1db8dd5 | -11.79319 | -62.73914 | 2025-09-11 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 52f1ee7f-8287-3154-b109-b2d1b8f21d86 | -14.51708 | -53.92458 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3874e03f-da8b-37b0-be35-8ccecd3453af | -15.79796 | -52.24479 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2d231bad-d971-3028-a2f1-b1441aeaef94 | -11.23002 | -55.00191 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7dbb191-f4ae-3b46-9ba8-954b2707e7b6 | -12.96441 | -54.75475 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5fda4a5-7fd4-3b3d-9fdd-0849dcaa0adf | -12.35273 | -63.63717 | 2025-09-11 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58afec16-90d4-3941-b1c3-a5ff6e4c6fec | -12.40963 | -63.82194 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cd9a431-f4c8-3c9e-8332-b7db7c575e81 | -9.80337 | -61.52238 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7de2e405-4831-36d9-a4b9-96dfa01d08c9 | -15.56896 | -54.75869 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6e7f2b56-5492-3e88-9f84-61100a558a1d | -11.88349 | -58.81465 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15ecba3f-9b76-3c03-a8c1-9d01f149d108 | -12.96984 | -54.76033 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52d46ad1-d54c-3601-8885-81a054869388 | -12.3842 | -54.17085 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f84d0727-5bff-38b9-9b98-7882a28929f5 | -12.60987 | -56.96896 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 607ac9d2-244a-3efc-bcd2-0a00c71e26b7 | -12.40136 | -63.79504 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d84a49d-763b-3203-a4e5-f288c4bcee2e | -14.91018 | -55.8772 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d17b5037-d892-3d49-8199-bc55a82da181 | -12.86989 | -62.12424 | 2025-09-11 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68b941a1-2e54-37fe-ae41-8b228a33426b | -10.02472 | -51.73404 | 2025-09-11 05:38:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 533406c7-acf2-302a-8a46-2866b04fbece | -12.39021 | -54.17144 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3eb954e5-8fa2-3593-b89a-a040480328bf | -12.4029 | -63.8209 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e74686b-f63f-34dd-a576-54c27e8ad91d | -13.14065 | -54.91375 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 717e88d6-a546-3408-b483-2d6bbba2ebf2 | -12.97076 | -54.75106 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35b42eac-d87d-33f1-8bbb-fdd20d175444 | -10.73063 | -69.34251 | 2025-09-11 05:38:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48fffbc2-79fc-3f30-b7d6-f6541eb070e2 | -12.94637 | -54.81237 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab1eb044-6162-3c6f-a397-81013a806e97 | -12.39858 | -63.81332 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebacef76-a412-3260-90bc-239f2850c42e | -11.22945 | -54.99549 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6081294a-e548-3e84-89e0-8c44722d28fa | -12.41658 | -63.89016 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37e473f7-9fee-3f85-8ef6-ee6fd3baf860 | -12.93093 | -54.78873 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b9f4170-8687-36cf-b823-98046a036c46 | -9.71535 | -62.4074 | 2025-09-11 05:38:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8152d727-a8c3-341b-b614-c70ffff41418 | -11.22899 | -54.99934 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acefeaec-f1a4-3698-9ba3-7826fe0ff98f | -17.37647 | -52.92733 | 2025-09-11 05:38:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 577e7cf4-4851-3930-9d7d-f5a21a22447d | -11.05198 | -51.34076 | 2025-09-11 05:38:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e104ce2d-60ee-334a-9dfc-e705e1ed25d5 | -15.79669 | -52.25856 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 703a0766-6e03-3f50-b864-6d78275cc2c1 | -10.16696 | -68.15304 | 2025-09-11 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c3d3b78-0c20-3198-ba31-397797c6b0a3 | -11.20905 | -54.98764 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15c2a314-8ef8-32d4-9a6c-4f678efda455 | -14.93607 | -55.94565 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c34b912-b813-3823-b5d3-edd6bf8a9365 | -12.97025 | -54.75532 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a26a6c72-905a-3f88-afca-f323644a40c5 | -15.14218 | -52.45497 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1617324a-30ca-3eeb-9625-3f5efd9efdcd | -15.56345 | -54.75337 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e3f8856-6700-3d0c-895c-bd1bcbe69ac8 | -15.79614 | -52.26444 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8514056e-9ca1-379c-8a7a-f78fe2931df8 | -12.39802 | -63.81696 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b31be88-e68d-3c53-b6ce-fc124273df59 | -15.12372 | -52.4217 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd6b4da6-2f5a-3c52-b17e-59bd38d3fec6 | -15.13592 | -52.43835 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 530c76c7-92ee-3957-8f36-05ea84ce36d4 | -12.06768 | -64.17525 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df875cc3-67ba-3508-a272-0f75bcc2da1b | -13.14017 | -54.91775 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2eec736b-28d4-3db1-9e1c-bdf6a28865f6 | -12.41518 | -63.80785 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11040ad4-004a-3de8-86c1-063847faf187 | -14.88763 | -55.8778 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f11c50c-e320-3800-9524-ef22a8379294 | -9.75193 | -65.07047 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a2ef407e-2dd9-3f1e-87cf-8eba8ce32c61 | -14.30966 | -54.75343 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c55f843d-729c-37bc-aaba-601a0d458b15 | -11.77564 | -64.94285 | 2025-09-11 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 776ee03f-72e5-3db6-ab87-35527e35ff7b | -11.21927 | -54.99691 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 312e3a9c-6971-38ea-982e-06860e0d3f83 | -9.79619 | -61.52129 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5a7fbbe-8972-3e72-8a2e-5d0cab60c45f | -12.07156 | -64.17221 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1aaafdec-f5be-3796-84cf-078a38caf3cc | -9.74862 | -65.06994 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ffe40735-45f8-343c-8610-a210482f3fa3 | -11.79666 | -62.73967 | 2025-09-11 05:38:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3b1fb440-6e4f-3f70-941c-93f180273e99 | -14.50464 | -53.93781 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8448d322-cca4-3f9e-bcc0-2ee01ebfb262 | -11.77674 | -64.93584 | 2025-09-11 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9517ece5-8c0b-3cec-9028-19f7d56fd9fb | -15.14948 | -52.45134 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fccf7303-2a25-38b9-bc49-841052fefb55 | -14.92076 | -55.83325 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0256150-c1e4-3f80-84b6-19636a8a9e68 | -9.98245 | -64.98982 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ac71577-96ba-3f28-9365-2fa8a1e0950d | -11.78774 | -64.93041 | 2025-09-11 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7230e5c0-d2a4-3734-a1a3-0a989a204af9 | -9.98355 | -64.98284 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c2c9766-0c0e-3d43-bef3-0901c038e8ea | -12.96496 | -54.75126 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f09cb25-5a0e-3d28-9792-f610c4d2aa81 | -15.1536 | -52.40844 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cbe09068-ddbb-32f5-9763-6560efc65b6f | -10.00043 | -67.59699 | 2025-09-11 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abe068d1-ca04-3d83-99a3-4b921e41425b | -9.98439 | -63.66369 | 2025-09-11 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f7d3ffe-a83a-3858-a82e-5dc3e440a34e | -15.56944 | -54.75414 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 744a3788-69f6-311a-989d-41ccb89d3520 | -9.15727 | -60.25754 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2287d36c-7241-312e-a3f7-48865ab2a4c2 | -12.3998 | -54.16605 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f0a69aa-d3cf-3945-9dcf-f0190c9a2a1d | -13.13488 | -54.91301 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a11a63fd-43f1-3415-bbee-57f95977b564 | -15.60288 | -52.74454 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10c9a16e-d9f6-3a7b-b77d-2ec7a38dcef4 | -15.13467 | -52.45069 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| db81638f-2771-3cb6-957a-3fa76509012d | -12.46219 | -57.1992 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c84b1ee0-289f-3546-8cdd-b12d99ad80ef | -15.14755 | -52.39894 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| edec693d-62ce-3689-a8e5-5d8da366134b | -8.94423 | -63.99282 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b59e5785-215f-3fc0-a9f1-de07087d6d97 | -12.3973 | -54.16298 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78b954bb-6b17-353b-8286-83ba08ad6805 | -12.41181 | -63.80733 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f433ef5b-cdb6-321f-bc3d-5a0fbc3f0389 | -15.55201 | -54.7464 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1a620d7-f839-30ad-88eb-a5cdca0200e4 | -10.15569 | -64.2496 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd1c190c-e698-3eab-bc26-cf0fe3374d97 | -14.91614 | -55.87423 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94abd002-a0c3-381c-b460-78200093de5d | -9.46381 | -63.37814 | 2025-09-11 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b82f4aa3-73d8-3f19-92f7-b52ef14c4a98 | -12.61023 | -56.966 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10e896ad-b936-3eeb-91cd-a65c7d974259 | -13.25208 | -51.77039 | 2025-09-11 05:38:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f21aabc-2f44-3d10-a927-0e486d0045a6 | -12.93484 | -54.75539 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32ca5f62-c3e5-31d5-a2df-26894b47c76b | -12.94748 | -54.74826 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 907397fe-f068-3744-9ba4-45bf57d6d58b | -12.96391 | -54.75898 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8df5da7-cd52-38e7-a617-6713d10dc91b | -12.42048 | -63.88705 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cd219b6-6806-3b63-82c2-5f07bb4c5cac | -12.95961 | -54.74631 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1cf58496-779f-3fce-822e-bc934f13194e | -10.6412 | -69.30683 | 2025-09-11 05:38:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2416a238-098d-3d08-be3f-0c5cdfe2a6ff | -11.87911 | -58.81417 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 547d82ab-abab-3acb-ab96-f498d28c8c17 | -15.55851 | -54.7424 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 624d3283-785c-31c8-a3ca-094d02def65c | -14.51443 | -53.96415 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f564aeec-a37e-3a3b-bb84-04268876c7ae | -12.92562 | -54.78381 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1adbf0bb-0d96-3b82-8789-67e99b3b78d1 | -10.9307 | -69.3064 | 2025-09-11 05:38:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61cc6780-ab11-340f-a3e7-081d9e9dbc04 | -12.93576 | -54.79769 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README128.md)
