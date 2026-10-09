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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd9846ba-07a4-3a13-9fef-ca7f67e7e29f | -4.31503 | -60.87394 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 85dc84fb-757b-39cd-b889-2130a8484d40 | -3.01521 | -57.78198 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8285020b-379f-3e72-9359-3bd589379216 | -3.74566 | -59.46654 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2074bda6-a9f6-3f43-b9db-937d15933cf0 | -1.1039 | -54.16731 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 4dec7888-7631-370d-be42-bdb90078ff05 | -2.50533 | -56.15579 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 155958a1-afb7-32f9-b989-615fb6055471 | -2.93617 | -54.05566 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2cd1b48a-c81d-3a9e-bf07-fe15cb86b682 | -4.05243 | -55.32895 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 00d50f87-b075-3987-a6eb-1223c0b4bdc6 | -3.16878 | -58.62445 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 9c774a45-69fe-39cb-989d-dad24e9dc5b4 | -3.59647 | -61.61499 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 3f321a3d-cd04-34c3-807e-23e7cb4caada | -2.50255 | -58.07338 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| f5f232c4-014b-3dab-b7ac-00996f9ae9c6 | -1.15444 | -54.22489 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4dedce04-8da3-3bd9-97e8-87888cd55537 | 1.31733 | -60.71542 | 2026-10-09 00:37:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ccf01c9d-e1a3-3f8f-a1f3-846036ed2195 | -3.73969 | -59.61972 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 075b9f3e-c86b-3bcf-824f-8484ceb45198 | -3.95105 | -56.10961 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a518ca73-e85c-369d-b432-92a2eea45229 | -4.80514 | -56.14809 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 2efef4be-12c6-3a3d-94ce-625d19cbba7f | -3.64911 | -59.1727 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ecd9c77c-44d4-3b98-a5e2-16176cb588c5 | -3.9101 | -55.89227 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 15f1c536-257c-3272-8c5c-7833a4252fb1 | -3.47452 | -59.50457 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3de36580-1934-3813-a63e-218189192711 | -3.64932 | -59.56642 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| b83584d7-d010-394a-a1a3-5078a212c407 | -3.39438 | -61.08086 | 2026-10-09 00:37:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| a4357635-e3ee-3735-aa93-2f56743c210b | -2.56929 | -56.17664 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 295cbbde-bb70-3e65-9054-9919464b86e7 | -3.18903 | -58.63982 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 134b525d-5fef-3b28-9918-37b6a9aac072 | -3.59864 | -54.67314 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 296e5a01-a9bc-3cc2-834e-349a8fa02f34 | -3.52947 | -59.57747 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| ce3072b1-95d1-3592-a2e0-a41f5e6d8b02 | -4.74809 | -55.66792 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 8681acd9-1aa7-36cb-9510-af459e365324 | -2.9015 | -59.22755 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| abba0788-bccc-3625-874e-2be0db771093 | -3.18153 | -60.39805 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 12cd0266-14a3-3b9d-a196-f09b5001b8e9 | -3.91175 | -55.90392 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 921c38d6-d936-3871-801d-af4c90875dea | -3.94385 | -55.84539 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 14d0ff95-8791-3bf3-b41c-345f12651c46 | -2.47348 | -56.07552 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 148a02cb-ad1f-3932-b023-8536ffb972e9 | -3.57367 | -58.62497 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 41e934b8-5762-3509-9063-a96c25262160 | -2.93834 | -54.15574 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9bcab757-bfc9-3ca7-82e0-4fddf7f83865 | -2.82817 | -54.11171 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| db69c6d6-b635-30ff-a0ea-e3354116554b | -3.70332 | -61.32479 | 2026-10-09 00:37:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2f7c3841-bd9b-35fd-b7bd-30d452752363 | -3.47149 | -60.49621 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5dbcce94-95ec-3c07-b3ae-92bdde62e553 | -3.60058 | -61.64529 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 425ea6d5-e44e-350c-9700-312200aad27c | -3.91982 | -56.0327 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 93ee50d1-4e5e-3f18-8c45-7b14e72ed7dd | -5.23475 | -60.18632 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 21219b3c-308d-32f6-b904-274f57a71620 | -3.11427 | -54.18377 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 2e46fa4d-8b78-32aa-b01c-3db8f626a232 | -3.62881 | -54.23994 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 4408dd0d-abd3-30d5-864b-5aa03b4ab1f9 | -3.70596 | -58.91666 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 916b711d-6679-36cf-a28e-90f8fde68e4b | -1.99505 | -56.96001 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0d36656c-789a-3a4f-97fe-a12670e47ced | -3.19667 | -60.4419 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| af610f6b-586d-3fc1-b8a3-7454d769a540 | -2.88905 | -59.20242 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 32d453fc-f303-3b9e-ac3e-efc153ef5519 | -1.38685 | -55.20283 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bf6508da-df00-35d3-b998-17b9f65e9c78 | -3.83046 | -59.41261 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 45b6f235-e68c-3d72-afa8-787ce3f0e516 | -3.76074 | -58.51365 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 1c50301d-92cd-32b0-952e-48fb517c819b | -3.60274 | -60.5775 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 006def00-3e3c-3ebf-8979-59382b4e9a51 | -2.13191 | -56.6968 | 2026-10-09 00:37:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a6f6069e-f7c1-380f-abfa-d00e1e3749d5 | -3.16498 | -61.08216 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5f9745a3-5479-316d-b9e7-59b0af206162 | -3.89723 | -58.9674 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2aae12e-aaa9-302d-80ce-b715e8228f61 | -3.74808 | -59.48411 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| dff52361-a873-3a14-ae98-a6969865b7db | -5.25471 | -60.33358 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 026da250-82c5-313d-b062-21d19b537ad0 | -3.74446 | -59.45776 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7d3115fc-ad00-39b1-b8ef-55f3a5e9ca79 | -3.20437 | -53.87261 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| ca9b2eeb-7245-3419-8d32-a9e8c88ccd2b | -4.55387 | -54.98225 | 2026-10-09 00:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 9d839097-8cbc-399e-901a-342c407494b1 | -3.84629 | -55.79897 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e85ecddc-2c1e-35ed-91af-0bf20693c226 | -3.98717 | -59.34272 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9bd3f2be-e7c5-3a84-b8e3-2d2bb9d7e1a9 | -4.0271 | -59.8465 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8d264993-7c3a-3040-90fc-41aeb3ce9fdb | -3.28173 | -60.99616 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9b290e99-8b83-39c9-a95f-4e548a939d05 | -1.14728 | -54.21398 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 14087ce9-c668-3598-87ae-c5bef1ff14be | -2.99438 | -53.90474 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 1f0385ac-e0fa-3022-a315-51ec565d27f0 | -3.01889 | -58.9384 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b3b6ef43-9480-33de-9ffa-b8e9a2dccc46 | -3.4541 | -59.55217 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 28e39608-ad0e-3edf-b939-8c859b7027f2 | -3.71554 | -59.65581 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f12677c0-fe43-3f2b-a46b-e7a6ac460283 | -3.69105 | -60.55005 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 72d73917-d6ed-345c-84df-c4d41a674476 | -2.81188 | -59.24636 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b8a7a0c8-b70a-32d7-99ef-94a01015085a | -3.78143 | -58.5867 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1d743281-a4db-32a4-96e6-a4e51770c80b | -3.53642 | -59.48106 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5cb9eef5-4463-3fdb-9da6-7db3860e7e31 | -3.26916 | -54.06687 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 8b4b8a09-554e-33f8-a138-4333046260c1 | -3.90484 | -58.95736 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9731120c-e62f-3422-80e1-6edb231b18b5 | -3.7409 | -59.62852 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 900021be-5256-318e-a6d4-a6cd70a99308 | -3.74325 | -59.44897 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1d60f3c1-04b1-3c3a-a3c1-d0c54783d12a | -2.84921 | -59.10931 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0fa35fb5-b49a-329b-98d4-6b94921d54e0 | -2.51985 | -56.26084 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6dee5122-827f-398a-8d07-5d6c5c6d129b | -3.54004 | -59.50741 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4b5e65f7-446f-3e47-916a-17321d4db424 | -3.48408 | -59.378 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 25d8281c-960c-30ee-a3d8-a710aef7b255 | -3.42861 | -54.06383 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c1f156e9-bbd1-3160-a958-b07d50ba6b85 | -4.12289 | -55.03319 | 2026-10-09 00:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 23b193f3-d57c-3cc4-95a4-a78653d1ccaa | -5.16134 | -60.32449 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 19b5ec4d-b684-3457-859d-a8a7d4eb5eeb | -3.92818 | -56.01977 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c97711f1-60e3-349f-a3dd-9a2343617915 | -4.57136 | -54.95271 | 2026-10-09 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 746765be-324e-36f0-a826-ccd53b69f57c | -3.46718 | -59.25513 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| d06369f5-5178-3852-a081-3f7b8081b827 | -3.6405 | -59.56765 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7f2be687-ef63-32de-a603-ffd67c9cbd53 | -2.73124 | -57.4699 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1ef4a26a-f963-30db-b560-7360a10c28ee | -3.90995 | -59.59867 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 531d84bb-d843-3f3a-9a3a-6219c322959f | -4.30571 | -60.94321 | 2026-10-09 00:37:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2fca1355-3377-3a38-9a2b-e55e80d059a3 | -3.52863 | -59.50597 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 017091a8-0fab-3d84-8766-00c8677918a2 | -2.51714 | -56.17217 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8cf265e7-c3bf-3270-81ec-8229999ebbdb | -3.55597 | -54.69999 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 12145180-2d63-3e0d-b88a-3fbc577b5172 | -3.59921 | -61.63517 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 25bcb409-e865-3826-99da-1d3943fe8088 | -3.56504 | -59.10116 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c3cfe9b0-fb52-3fd7-9d17-2a9d2e3e0de8 | -3.97024 | -59.62919 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d4920f30-7a73-3dfd-82bb-a5305147a9e0 | -2.46498 | -56.08899 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 49e1509d-1b28-31c2-803f-2b28abe7f616 | -4.73794 | -55.6692 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 201783c8-f34a-3a2c-b045-092f99b09ce5 | -3.47274 | -60.50531 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 334415f0-7e20-39bf-b5e7-1f878779f3c1 | -3.71433 | -59.64701 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| debd8b96-d41d-3395-a92e-e4307ed71c40 | -1.1063 | -54.18451 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 45224c93-e80e-322b-a3a1-58f0cf4a1aa5 | -3.5275 | -56.8904 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5ec93d7e-5396-3923-9cc0-24ffa3c3acbd | -3.23053 | -57.87724 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README43.md)
