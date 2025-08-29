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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4611481-2482-35bc-95ec-3008cf7c46b2 | -11.36457 | -43.54898 | 2025-08-29 11:36:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e8776813-8b1f-3b63-92c6-65615dad58cc | -11.62207 | -47.30702 | 2025-08-29 11:36:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 44cccdd5-08d4-3c5b-a9ff-58ce9a894f45 | -11.88016 | -46.41223 | 2025-08-29 11:36:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 07162322-d165-39ea-b6e4-6a56421e8568 | -13.5479 | -46.87816 | 2025-08-29 11:36:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 1475e983-c410-374c-b28d-99e656680af1 | -13.56384 | -46.88165 | 2025-08-29 11:36:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 7a948f0c-3b0c-3964-9576-54ae1d34b04d | -11.3482 | -43.56723 | 2025-08-29 11:36:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 708.6 |
| 9053e37f-f56c-3919-872c-e31d819d52bd | -11.58945 | -46.26154 | 2025-08-29 11:36:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 1e74a1b9-eab1-3a26-bc7f-6344f3087b7b | -11.42422 | -38.39735 | 2025-08-29 11:36:00 | TERRA_M-M | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b9bf720e-9b98-3657-8293-9c0a56ec9779 | -9.55331 | -45.88504 | 2025-08-29 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 3ce022f6-c470-3d6f-8fc7-f17f66b5bbfd | -11.58348 | -46.29487 | 2025-08-29 11:36:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 87dab72e-6dac-3ff1-906e-676cca3a1cfe | -11.3516 | -43.5468 | 2025-08-29 11:36:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5bc47171-38e2-33fb-b015-a01b8c453781 | -11.56571 | -46.39388 | 2025-08-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f9c7784d-d66c-35d6-82d6-23cb04fd8c8a | -8.08995 | -45.02713 | 2025-08-29 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 71d94286-f3e3-3fe4-809b-a35c5b0991e8 | -11.57554 | -46.28613 | 2025-08-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 536.6 |
| 17d95dbb-a0d5-3b57-b859-b3a22c7c7e6a | -14.03651 | -44.47679 | 2025-08-29 11:36:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ad3dc1b0-d53b-30cc-8931-f4be60860a8e | -9.56108 | -45.89218 | 2025-08-29 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| d42a272c-dd3a-3f81-aea0-a1d3358417c3 | -8.10043 | -45.03592 | 2025-08-29 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 8bf9c431-17e8-334b-afe9-0ec036a3b533 | -9.55876 | -45.85219 | 2025-08-29 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 96d8e8d1-d72f-39e0-888d-ac96e0c6000c | -13.40358 | -46.9844 | 2025-08-29 11:36:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d2658ae3-0de1-3f73-90f9-99f15deeac6a | -11.56971 | -46.31987 | 2025-08-29 11:36:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| d4b8f39e-1207-33b0-b227-20268abb88d2 | -11.3448 | -43.58768 | 2025-08-29 11:36:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 40b5ce27-b08c-3a5b-a223-e678f6886a9b | -16.04464 | -43.82524 | 2025-08-29 11:38:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a3f66468-32dc-3123-b6f7-7bd8d3dd11d1 | -20.86424 | -42.9747 | 2025-08-29 11:38:00 | TERRA_M-M | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.6 |
| 37b1e042-b050-32ce-bf1f-dc46b5917295 | -20.60205 | -41.75214 | 2025-08-29 11:38:00 | TERRA_M-M | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 70fd2268-ff8d-39ca-9d63-059f955dbb7d | -20.85388 | -42.97278 | 2025-08-29 11:38:00 | TERRA_M-M | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c930fdfd-e572-34a0-8f69-655e5c816fd8 | -19.54372 | -40.43456 | 2025-08-29 11:38:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 1a26daad-c11b-3c8a-b37b-04db5c622e84 | -18.98178 | -40.24109 | 2025-08-29 11:38:00 | TERRA_M-M | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 34cc0ea0-1792-3404-b6ce-188a4d61b41d | -11.5722 | -46.2844 | 2025-08-29 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 309.5 |
| d8d4af79-764e-36c5-aedc-6f122941e203 | -11.3517 | -43.566 | 2025-08-29 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.6 |
| 7b02430a-e1a6-3fa3-9698-bd3be12fe4ed | -10.867 | -47.4967 | 2025-08-29 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| fd569f6d-7ecb-3649-bcba-04d843f2a5b9 | -10.8483 | -47.4768 | 2025-08-29 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| ba03d944-895d-3f1e-b593-3dfb98cd13db | -12.9186 | -48.1354 | 2025-08-29 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| df5909f8-51f8-30ed-a088-7bc57bc45d21 | -13.558 | -46.8745 | 2025-08-29 11:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| b931cf80-0325-3e61-ba82-31a2ef7ccf55 | -10.848 | -47.4991 | 2025-08-29 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 20dbb47e-30ad-3ddc-8205-83ca773189a2 | -11.876 | -46.4007 | 2025-08-29 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a4563b57-014b-3ec4-8cb9-e48c2e76c765 | -11.3521 | -43.5423 | 2025-08-29 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0195e2b3-98a5-3518-bcb2-347907b322c9 | -11.5707 | -46.3751 | 2025-08-29 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| f848f777-44f8-395e-a4e8-9923648c41b8 | -12.8994 | -48.1381 | 2025-08-29 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 12abb492-bc6e-3eca-a0c0-9d7cb034820a | -11.5726 | -46.2617 | 2025-08-29 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4f0f2060-676b-3960-b96b-c8ab37ea1014 | -10.867 | -47.4967 | 2025-08-29 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| f31f113d-70fa-379a-a603-119526cc18b1 | -11.5707 | -46.3751 | 2025-08-29 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a41c9eb7-1e90-3ed5-a1e9-621c6017d580 | -9.564 | -45.8594 | 2025-08-29 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 63e96e2b-c609-3fae-a48e-e252d2e8dbfc | -12.8994 | -48.1381 | 2025-08-29 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 082eef52-0e8e-36da-87db-a8b5d6096c2c | -11.3325 | -43.5689 | 2025-08-29 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 7c55c043-a6e6-319e-8e40-27768211ae7b | -12.9186 | -48.1354 | 2025-08-29 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 1c846a12-cbb6-39a6-a2db-76c2e6e41efd | -11.5722 | -46.2844 | 2025-08-29 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 381.5 |
| 82df473e-f1c8-35f2-8e34-d1aa6d9d8f64 | -6.3883 | -45.5793 | 2025-08-29 11:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d7865ea1-db32-360f-9448-3fa2f901373f | -9.5637 | -45.882 | 2025-08-29 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| b99d259a-5f38-3e15-b610-87ef53572e40 | -11.876 | -46.4007 | 2025-08-29 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| d72b2a4a-a7b9-3b73-a3b3-34122dd8c857 | -11.3517 | -43.566 | 2025-08-29 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| 0bd8b082-a5dd-3698-8492-f8392ff0fb2b | -10.848 | -47.4991 | 2025-08-29 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c2ccec2f-3763-343d-a931-9b814ff6b654 | -11.3521 | -43.5423 | 2025-08-29 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| dae29bf4-9800-3a2b-a658-dca3a6d0becf | -11.876 | -46.4007 | 2025-08-29 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 1c2a4748-9a5f-3841-ad0e-ec228ad574c8 | -11.553 | -46.287 | 2025-08-29 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 77f9a152-435c-3916-a3ce-51acae1fd53e | -11.3521 | -43.5423 | 2025-08-29 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 91652906-35c1-3f68-8a9a-6f3cbcb3a4f9 | -11.5722 | -46.2844 | 2025-08-29 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 361.8 |
| 93fa110d-fc1d-3f9c-ab9f-e1b320bd20ee | -12.6875 | -48.1899 | 2025-08-29 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 40200c75-83ac-386c-a4e6-b1a11e0442c5 | -11.5527 | -46.3097 | 2025-08-29 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e04007a1-ca21-3bdc-ad4b-c44c150010dd | -12.9186 | -48.1354 | 2025-08-29 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4e36ac03-7299-38b8-8167-8a1243987d2b | -13.558 | -46.8745 | 2025-08-29 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 71f2c093-d255-3671-a99f-ded603dd4bec | -11.3517 | -43.566 | 2025-08-29 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 228.1 |
| 62b9e981-751c-31dc-a6e5-9dc139a419ba | -12.8994 | -48.1381 | 2025-08-29 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1ee35c90-6f82-34cd-9887-51ea113d740c | -12.6875 | -48.1899 | 2025-08-29 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 55de818f-cf05-34c1-8dcd-b22653cebe20 | -11.3521 | -43.5423 | 2025-08-29 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ed9719e5-a260-3de5-ab78-ab3453ff434d | -12.9186 | -48.1354 | 2025-08-29 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| bad88c26-6580-3c6b-a9b3-4012cd22218a | -9.5447 | -45.8842 | 2025-08-29 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 323525e1-f3dc-3f67-82eb-c92f58e61092 | -9.5637 | -45.882 | 2025-08-29 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 315.1 |
| ca51674b-d102-3235-9ec8-6f9069e0183e | -11.876 | -46.4007 | 2025-08-29 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e12c5f67-f286-3c65-baa1-8b5cb336b399 | -13.558 | -46.8745 | 2025-08-29 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 868d3a5c-2497-3aed-9ca9-fbc049ba1ff4 | -11.5722 | -46.2844 | 2025-08-29 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 262.1 |
| e3715bbb-1732-3857-98b9-2b93f9c98c8f | -12.8994 | -48.1381 | 2025-08-29 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| aeaf1a0f-9275-3182-ad8b-196998f6abfe | -10.8483 | -47.4768 | 2025-08-29 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 24bae70d-afa8-3bb6-9f16-416fdc3761f1 | -11.3517 | -43.566 | 2025-08-29 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 255.5 |
| bc0f6d2b-f1cd-3fd9-ab31-bd82a54cadc8 | -9.545 | -45.8616 | 2025-08-29 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e205aeff-683d-3aec-8f36-9eff4eec45f5 | -11.5707 | -46.3751 | 2025-08-29 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5dbf040b-f509-3342-b120-7903bc10dbda | -11.3325 | -43.5689 | 2025-08-29 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| a414f7fc-7ed2-30e8-92c5-725b2d434b28 | -9.564 | -45.8594 | 2025-08-29 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.6 |
| ea0e53be-c688-31d0-a5bc-67d7f1490d29 | -11.553 | -46.287 | 2025-08-29 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fcae2276-e9d8-3f65-a4b0-8a1f3e2178a9 | -10.848 | -47.4991 | 2025-08-29 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b206d201-40f1-3d92-bd47-b569edf151df | -9.545 | -45.8616 | 2025-08-29 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d3a6b907-b58a-3dc9-8a92-fe50ce4a4e16 | -11.3325 | -43.5689 | 2025-08-29 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 21d920fe-dbf5-3bb2-b925-298ab61901c1 | -12.0365 | -50.6233 | 2025-08-29 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 42a7787b-3bb2-352d-93bd-082b333ba41f | -11.6315 | -47.3105 | 2025-08-29 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| f67217b2-f93f-3181-b374-51d56bac40bc | -9.5637 | -45.882 | 2025-08-29 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 063a346e-7a03-3f6f-9819-70ab420b3c99 | -9.5447 | -45.8842 | 2025-08-29 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 283.5 |
| 64baa574-dd7e-3142-ace0-c57429cd0af3 | -15.0835 | -48.1367 | 2025-08-29 12:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 635e93df-9ed6-3dfd-9814-ff4900d2c896 | -11.5722 | -46.2844 | 2025-08-29 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 634fc118-b780-3d72-a7ed-57c172a6d8ea | -13.5774 | -46.8714 | 2025-08-29 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 253eae8d-4cc8-3896-bce2-4a98eaf0ca76 | -11.553 | -46.287 | 2025-08-29 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 183.6 |
| b1d46bbf-351a-382a-9b93-8c52e64f7795 | -12.9186 | -48.1354 | 2025-08-29 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 6eef33c5-7f57-3955-a4ee-cde55ea416f7 | -13.3543 | -54.38 | 2025-08-29 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| de56e6c4-4c42-336a-952f-ba1359f91c6d | -12.0362 | -50.6448 | 2025-08-29 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 01d8ae7f-9036-3a51-abe4-ffb85caff30f | -13.354 | -54.4006 | 2025-08-29 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c20cf38f-65ba-32c4-83f8-f27c3e14b580 | -10.848 | -47.4991 | 2025-08-29 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 4fda3d7f-b40e-3ee2-b17b-a8e62bb53e9f | -11.3517 | -43.566 | 2025-08-29 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 404.7 |
| cd4f999f-11cd-37b4-89b1-060b73079c46 | -11.5527 | -46.3097 | 2025-08-29 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 8deaa67d-2391-3eda-a07d-19f54edbeac2 | -12.9182 | -48.1576 | 2025-08-29 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 906bd4be-1a68-39f0-ae1e-f3970ecf9e25 | -11.3521 | -43.5423 | 2025-08-29 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| f334bcf5-8213-3389-8dca-ca4a83cedccc | -10.8483 | -47.4768 | 2025-08-29 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 2cd90ca5-a0d9-38db-9277-c576f193d5a6 | -12.8994 | -48.1381 | 2025-08-29 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |


[Clique aqui para ver as próximas entradas](README93.md)
