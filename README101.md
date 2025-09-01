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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f58aaf5a-97a7-3c53-904c-62ba8b7dd9d7 | -15.7116 | -48.8809 | 2025-09-01 11:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 40afed4f-b107-38f7-a51c-b32fef382e88 | -7.0948 | -44.3358 | 2025-09-01 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 007948b9-e469-3c9e-aa77-d12f92dec2da | -11.0472 | -46.9169 | 2025-09-01 11:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a9fc3706-fd20-332e-94aa-0e08b4f02f5b | -12.591 | -48.2254 | 2025-09-01 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ecd2a672-a923-384c-8701-cf75606f12a1 | -12.5526 | -48.2307 | 2025-09-01 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 329.8 |
| bf45736c-5e11-339d-b47e-5c4d651a50f3 | -11.0568 | -45.146 | 2025-09-01 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.7 |
| a9f0650e-410a-3fef-ad10-22080ecb2908 | -12.9768 | -48.1049 | 2025-09-01 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 0b32f7df-f35a-3250-8b94-fd6fb2253e36 | -12.5722 | -48.2059 | 2025-09-01 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6348a054-afb8-3fba-be27-418aaa139ea5 | -7.0572 | -44.3393 | 2025-09-01 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3dc05568-d95d-3591-9969-346638da07e1 | -7.0757 | -44.3606 | 2025-09-01 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 466fb271-b657-3fc4-9744-a60c7aa8e963 | -6.744 | -43.7666 | 2025-09-01 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 8badeaef-68a7-3fe1-b76e-5fb94a8e24b4 | -15.7116 | -48.8809 | 2025-09-01 11:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 7acc6879-f10f-3b42-83ab-be9268ce7d7b | -7.9539 | -46.4542 | 2025-09-01 11:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c77d9dc1-d0fa-3ea9-ba12-d3f2c06c5fff | -12.9768 | -48.1049 | 2025-09-01 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 5e27f2fb-683b-3ba3-bfbb-d1c4de334998 | -15.5862 | -48.3435 | 2025-09-01 11:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 760b36d4-5d7a-326d-a42d-a705624ce800 | -7.0946 | -44.3589 | 2025-09-01 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 04048a4b-5f8c-3f5d-813a-519fd8866079 | -11.0377 | -45.1487 | 2025-09-01 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| c01b1c97-654f-334c-a8fa-03f2ce5c30e9 | -8.8437 | -47.5217 | 2025-09-01 11:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 51dbbd44-ab74-3291-bd00-448090da8dbd | -11.0457 | -47.0066 | 2025-09-01 11:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| f419afce-5e4a-3cb8-b8be-bd2466d9253f | -11.0568 | -45.146 | 2025-09-01 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 2707eded-41fd-3e82-bcc3-91d9540ce2c7 | -6.7438 | -43.7898 | 2025-09-01 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 7eb9510e-c2c8-31ed-a613-52513999187a | -12.9764 | -48.1272 | 2025-09-01 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 47fdd0d6-2f5f-39df-a977-1f36855a8426 | -6.7626 | -43.7881 | 2025-09-01 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 619c7d58-3c81-3aea-b71f-0555ca3f167f | -12.591 | -48.2254 | 2025-09-01 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| c0ad6a3a-e0de-38b4-9729-bad87fae9cd4 | -6.7628 | -43.7649 | 2025-09-01 11:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 03a589e8-9326-3d86-bb91-e768d6ca84ec | -6.8426 | -43.3385 | 2025-09-01 11:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| f6eecac8-77a2-3bd0-b32d-fe81a931e601 | -19.5016 | -46.5957 | 2025-09-01 11:40:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 76f719ae-cb16-3327-abf3-97ed36ce3ac0 | -11.3705 | -43.5868 | 2025-09-01 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 40f9ed09-6d25-3a88-9ed4-063a07f01ff4 | -7.0757 | -44.3606 | 2025-09-01 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 63821549-8606-3c17-bdf2-ecf79a916401 | -12.5718 | -48.228 | 2025-09-01 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 364.1 |
| 638a29e9-ea99-3192-96d7-f2caf11cf942 | -7.076 | -44.3376 | 2025-09-01 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 76dade28-864c-3129-8974-803b1c82a71c | -12.5722 | -48.2059 | 2025-09-01 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 310b5937-e896-31d2-80ff-f9ba13260c1c | -7.0948 | -44.3358 | 2025-09-01 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4feaa11e-babe-38e3-b98c-8ec279822f23 | -6.8428 | -43.3151 | 2025-09-01 11:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 74d254e7-b4a6-3039-abbb-5a1f17edfb14 | -12.5526 | -48.2307 | 2025-09-01 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 359.1 |
| 9240af7a-0682-3bb4-905f-3248d61b0480 | -12.9575 | -48.1076 | 2025-09-01 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 64186086-3a87-3f50-be50-099fea0acfb2 | -6.8426 | -43.3385 | 2025-09-01 11:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| d04558fd-ebc7-3c1a-ade3-5df9b5197030 | -11.8527 | -51.4742 | 2025-09-01 11:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| aec5f5b3-e7f1-33e0-9e8c-e35f7b56fe19 | -12.9768 | -48.1049 | 2025-09-01 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 44ae79a5-4ef9-3141-96c6-fb3711c13231 | -6.8428 | -43.3151 | 2025-09-01 11:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| befc7579-bb93-3118-bc9a-6988d763471a | -7.0946 | -44.3589 | 2025-09-01 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 76a6c5de-837a-3a1a-9cde-e17045fe26c7 | -6.7626 | -43.7881 | 2025-09-01 11:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 624a0d50-5d71-30ee-8237-f249397e0795 | -11.0568 | -45.146 | 2025-09-01 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 2eb2ddcf-ac3d-3250-9ec2-5f2b2ba3d8a3 | -6.824 | -43.3168 | 2025-09-01 11:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 45574110-e869-31d1-8707-290c59345e47 | -7.9539 | -46.4542 | 2025-09-01 11:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 2f70a963-0c54-31fc-a961-cb281025afdb | -15.7116 | -48.8809 | 2025-09-01 11:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 0ec14861-08a7-3d89-ae0e-d4a5e0eeef49 | -7.0948 | -44.3358 | 2025-09-01 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ea096139-d125-3749-8ac6-74bc0556f737 | -6.744 | -43.7666 | 2025-09-01 11:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 90275706-d521-38e4-a7b7-64e675960470 | -7.076 | -44.3376 | 2025-09-01 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 34c657e7-533e-3104-b85f-2ffe4af33555 | -11.3696 | -43.6341 | 2025-09-01 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0041e3c1-a2b5-37c4-88e3-414c86a8cced | -11.0662 | -46.9145 | 2025-09-01 11:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 21928263-16b0-3b2f-9dae-9d508f577892 | -11.0377 | -45.1487 | 2025-09-01 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| aa6ddb18-9ba7-3f05-90f2-8eb3a283d60d | -8.8437 | -47.5217 | 2025-09-01 11:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 9b027083-a16a-3fc6-8ed4-ab25e88370f2 | -7.0757 | -44.3606 | 2025-09-01 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 36751ba4-c675-307a-8f18-c9ce4319ef5e | -11.3705 | -43.5868 | 2025-09-01 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 07eda800-075f-3910-97fc-3556aeee4aae | -6.7438 | -43.7898 | 2025-09-01 11:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 27a47c3f-f6be-3559-9682-28ab75386410 | -3.46095 | -39.59784 | 2025-09-01 11:53:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 0d849901-d9f5-368e-a34c-fdabde6332c2 | -4.44372 | -38.04969 | 2025-09-01 11:53:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |
| e9487ec5-7fbe-3ae4-a170-149da3796155 | -3.42424 | -43.33269 | 2025-09-01 11:53:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a9db920d-d52c-3414-9f18-9ac131da7c24 | -7.09582 | -44.33494 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| dd905113-620f-3334-9cb9-e0a7f6c69c25 | -6.19352 | -42.52034 | 2025-09-01 11:55:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| cc5cd636-fe45-3e96-8b89-ad949fa4a40e | -6.74904 | -43.78714 | 2025-09-01 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 90527a9a-9a1b-36b3-b0cf-b8ac92a6fe41 | -7.46154 | -44.82687 | 2025-09-01 11:55:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e30a6dc8-6eb1-3732-9ff4-3b85d65c7a58 | -6.71124 | -42.25778 | 2025-09-01 11:55:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 705e964e-77ac-30b1-a6a1-60f0c01e61d6 | -5.88784 | -44.32874 | 2025-09-01 11:55:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba530c6c-7680-362b-97c3-e687e91e87c8 | -7.06572 | -44.3301 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5884af95-e81c-3d9f-870d-c2fd74ef3d76 | -6.7507 | -43.77626 | 2025-09-01 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c43dfbb5-5faf-3d55-9e8c-7f8bf735bcfe | -6.83846 | -43.32599 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 75c91cf8-5cb6-30d8-86d6-cb77c77b6b7b | -7.21849 | -44.74566 | 2025-09-01 11:55:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a15f1235-450b-3c1b-8cde-2d43bae4a7be | -6.1846 | -43.31324 | 2025-09-01 11:55:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e2425b0f-b1b3-34aa-8cb0-981153af6a18 | -5.86235 | -43.001 | 2025-09-01 11:55:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ebc78307-36dc-3f5d-898f-d9b26aa51830 | -7.09407 | -44.34659 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3bbc3947-9c96-3582-aa71-79511df65fa4 | -7.06395 | -44.34175 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 079b5379-223b-32e5-9b90-cfce9ceec31a | -6.299 | -43.62691 | 2025-09-01 11:55:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 73e9f8b2-dd56-3a54-8651-d47e1e533690 | -6.83052 | -43.31441 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| c116ea40-b938-3a04-9504-6c556da7b406 | -6.74737 | -43.79807 | 2025-09-01 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| dfe47dd5-6c32-3c2d-bcbb-b9676c8829c9 | -7.49304 | -40.54745 | 2025-09-01 11:55:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 18ef5675-fb03-3be3-b3d5-1a1de0b8086f | -5.79861 | -43.62363 | 2025-09-01 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0fbb1bb9-ac07-327a-8f1b-af451f7a5e64 | -7.07221 | -44.35514 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3ee078df-cdcc-3b1a-9972-0365a1685789 | -4.82197 | -43.23663 | 2025-09-01 11:55:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ccf7fd4f-20a6-3554-a54d-28af8e025c52 | -6.776 | -44.62252 | 2025-09-01 11:55:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 46eddc2a-09c5-32eb-bb66-5ce53ca03b27 | -7.08226 | -44.35677 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 4c4ab8c0-1065-3212-b1e9-9f496e344ac4 | -7.11221 | -44.5616 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9433d119-a3c4-309b-bc25-01b901b85447 | -6.83693 | -43.33619 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a6989829-ea84-3dfc-8f96-c846dacf0a10 | -5.1839 | -38.09449 | 2025-09-01 11:55:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 3f59833a-5edf-3aae-bf2e-187cc680365f | -6.76044 | -43.77764 | 2025-09-01 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 873c1057-cc08-32d3-a748-2b60305a4c86 | -6.84793 | -43.32733 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| e4763029-391b-35aa-990d-6d5b8ed92c2b | -6.8464 | -43.33757 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| b0cb592c-f754-3aef-8345-b54ec451669d | -7.46348 | -44.81418 | 2025-09-01 11:55:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| a0044c5a-b4f2-3741-a1d3-8c53a340f380 | -7.09231 | -44.3584 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| f0494250-5d74-367d-befe-ff5be877f4da | -6.2803 | -43.29083 | 2025-09-01 11:55:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a6bd2169-8744-3450-8dbd-436f1d233493 | -6.64784 | -37.84689 | 2025-09-01 11:55:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 11.4 |
| fd58f1db-0cfd-3292-99ca-e47c8ad31968 | -6.26411 | -42.60498 | 2025-09-01 11:55:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5bebc68a-a93c-34ba-9e89-1f5f7d0c68c9 | -6.92088 | -45.56934 | 2025-09-01 11:55:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75162630-5817-3434-b89d-b4b7960eb068 | -6.4538 | -43.97297 | 2025-09-01 11:55:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7554ff27-f5b8-390b-8223-a395bd41b544 | -5.88962 | -44.31683 | 2025-09-01 11:55:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| c796c097-6347-31be-9de1-52c27cbf1555 | -7.11126 | -44.7749 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a7117eda-0abf-3376-9afc-ed7a53e8dfe5 | -6.71261 | -42.24852 | 2025-09-01 11:55:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ab0322df-e70f-36a9-8353-26ba03470dcf | -7.2393 | -44.05902 | 2025-09-01 11:55:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| a6cf7673-096c-3bcd-8288-fba0a115be33 | -6.7456 | -43.79171 | 2025-09-01 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |


[Clique aqui para ver as próximas entradas](README102.md)
