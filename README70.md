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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7071a5ef-2529-3ddb-b0b1-6fca3c77bd91 | -17.52766 | -46.74077 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 474a2fdf-68cc-3f7f-9b4f-de70698284e6 | -17.49421 | -47.01876 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6514663c-ee2f-3a3d-98cc-c68eb198dad3 | -17.41361 | -46.31784 | 2024-10-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a54f003-7646-38f6-b3eb-c89a11f9524f | -16.93724 | -47.12565 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3adf2554-7870-3f7b-9a15-455919dcba7b | -16.93651 | -47.12987 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b4ef9a4-b140-343c-b62f-c9d631a61274 | -16.93578 | -47.13409 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb9ff2a9-14a1-3c35-94f7-a16773b17f71 | -16.93505 | -47.13832 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5810371-a229-3ee5-8d24-e53e5cef3abd | -16.93367 | -47.12495 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec62e068-aab4-3354-9e57-af4bf322f7f3 | -16.93295 | -47.12914 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ed1901e-7044-389f-8d62-3d11f5ef4ab9 | -16.92707 | -46.38262 | 2024-10-04 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44aec135-244d-395e-acee-28f88aef5fe0 | -16.92507 | -47.13198 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ba0230b-1efd-3086-b603-5d67e47267f8 | -16.92149 | -47.13132 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48ee44b3-8357-3755-b0a7-628be4aa12ec | -10.73083 | -46.16319 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 47335b14-136e-31c8-81a0-91ac9aaaad3e | -10.72931 | -46.17202 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 485cc07e-8175-3220-a1df-14953acae038 | -10.72804 | -46.16363 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 44a76d8a-f709-32f4-890b-036249b75ff1 | -10.72657 | -46.17244 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0788a6db-8391-39d8-b02e-04207407ef6f | -10.72655 | -46.1498 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e7a2109b-5737-3f52-952f-494df791e019 | -10.72582 | -46.1542 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fc499bec-a81a-3bc2-a31f-e14294e99809 | -10.72509 | -46.15858 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 756a43d1-d28c-3215-b7d6-be01be494428 | -10.72288 | -46.14911 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 35832374-2869-3025-83ee-c04fa63dbce1 | -10.90689 | -46.3061 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 771f1d65-b374-34be-87c2-befd09c2eab3 | -10.86659 | -46.3413 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f3b5c60-2831-3720-ab57-bc64ea91a622 | -10.86288 | -46.34063 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b97c3ea3-d50e-3977-ad6c-296e952c254b | -10.85916 | -46.33998 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8265a10-adac-379c-b38f-68afabf29d48 | -10.85545 | -46.33933 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3136de31-fb4c-34a7-8039-f4282b02acd1 | -10.85174 | -46.33865 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 057d8bb9-3dec-3217-9c4c-5630118ffdbf | -10.84433 | -46.33729 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 144ba803-6846-30db-8c4d-b3af4c30e4b0 | -10.84062 | -46.33662 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37620e7b-bfde-3b94-b24f-2caadc8bd933 | -10.53146 | -46.32136 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a29a25ef-7a72-3311-9528-84b156695dcc | -10.52774 | -46.32071 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 42f64af7-c127-3d22-a3c5-7ae21770f19f | -11.98249 | -47.36619 | 2024-10-04 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 48adab38-ae89-34c6-b172-4d1a1d83e32d | -11.94913 | -47.39643 | 2024-10-04 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ad76a19-0637-3566-9a9a-973ca39eaadc | -11.94824 | -47.40145 | 2024-10-04 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a224fd34-7512-32a6-a27d-9b7ffba2a6d2 | -11.94791 | -47.39917 | 2024-10-04 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8334c82-72d4-3ac5-9552-fa5621878151 | -11.79045 | -47.56599 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 09c69d99-8a1a-3c78-921f-1612e61284ae | -11.78956 | -47.57122 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f66057ab-7ce3-3367-af14-837ac42310d3 | -11.78863 | -47.57663 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a74ea47-2183-35b5-a9e2-0917f01e0a85 | -11.7739 | -47.68634 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c04a18c7-9434-3cc0-9c94-3590aacd5f9d | -11.76993 | -47.68561 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 798ec59d-ff03-3768-9c89-cb72665f24bc | -11.72691 | -47.69748 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5cf36a9-3e46-3a1c-9d8e-a94889abb773 | -11.72295 | -47.69669 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ded6a896-c336-30bc-9137-1160fe73aed0 | -11.7223 | -47.70034 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2b20975a-dfd0-3461-86cf-d9576bf4ae3a | -11.71897 | -47.69595 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8ff7d75b-3409-35ac-91b5-cf25385b56c9 | -11.71832 | -47.69969 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 89d105a0-9add-323c-a02f-1baeada69c4c | -11.71498 | -47.69532 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4565b1b-7ad1-3377-b5b3-3c9f1b89bc1f | -11.71433 | -47.69905 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bdb023ce-0799-3b82-8e1a-be2a65c95243 | -11.71101 | -47.69462 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 888ce84e-099b-310a-9e03-1c2c66fca5b9 | -11.70901 | -47.70595 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d29662c-ab62-3a75-b84f-33a4e28f3182 | -11.7031 | -47.69297 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc212bc5-666c-303e-8f4d-af49cb4d14f7 | -11.69913 | -47.69219 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d356ada4-6d4f-3874-ac12-15588c59e08e | -11.69517 | -47.69143 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08a07e6b-f31d-3dd7-92e3-7c338096b49d | -11.69118 | -47.69077 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18f6c3be-f018-31b5-b563-6ee0e8703764 | -11.67919 | -47.68902 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 547ff1a7-9e91-3523-9f9b-21024b4ccf79 | -11.67517 | -47.68853 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e40cbf7a-8db5-3234-b351-a87648eff897 | -11.67456 | -47.69196 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 659de415-4752-3418-885c-445c7f2593d0 | -11.67219 | -47.69172 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc57e6ea-dddd-3628-8cfd-46e1c0c2d9f1 | -11.67054 | -47.69151 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7945cc67-855a-3648-8837-8b161c83d977 | -11.66992 | -47.69498 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c4b765d-ffef-36a4-a5d9-91cf3c12168c | -11.66756 | -47.69478 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db49c1d9-a743-3a8e-94c7-01dc84760571 | -11.66693 | -47.6985 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6e209148-0042-37ec-85dd-6b6c3330a980 | -11.66411 | -47.691 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3aded507-0ec4-3bb6-aac4-c07d50de57a5 | -11.66352 | -47.69444 | 2024-10-04 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6bff3bf-63e8-371b-8f64-e9608a52dcce | -10.98589 | -47.33924 | 2024-10-04 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e1e90c9-9a92-36f7-b9e4-d8dd38a938d9 | -11.39851 | -47.21661 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0e259de-f319-3646-b26c-4c9b8e4055d9 | -11.39766 | -47.22161 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f2234ab-2b65-311d-b783-0f93ea2e85c3 | -11.39681 | -47.22656 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 002629c7-1866-37b2-9d58-6c6ea34f523d | -11.39208 | -47.23082 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 121a9799-d92f-3856-9d1a-c14a4d5ea4f0 | -11.38904 | -47.22519 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c0e5860-cc31-3bfc-b1d4-bacedd7d21f9 | -11.38819 | -47.23013 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b7f1e969-e2af-3ac8-87a3-a093a80c085e | -11.38773 | -47.20958 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56850a91-6ed0-3bd8-be5b-ca06baafd801 | -11.38385 | -47.20889 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1609649d-f453-3340-affd-ab9664b0fa21 | -11.38299 | -47.21385 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1e0fc4a-4ea9-3184-af1d-cd01f690885f | -11.37911 | -47.21316 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6094a0e4-e82b-3368-bac3-301be7d04df7 | -11.33631 | -46.82745 | 2024-10-04 04:10:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7afe127b-3a17-35b9-bb7d-d5db0eef1d5f | -11.32955 | -46.82132 | 2024-10-04 04:10:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01cb41d2-cada-3b0f-8406-1803a9b44c89 | -11.32576 | -46.82066 | 2024-10-04 04:10:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15bc6637-8b98-3874-bdf4-c7ca688de5e7 | -11.28563 | -46.91682 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1a4bd0f-b72f-330e-9205-993445730f53 | -11.27222 | -46.83615 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1de5f94d-f4c9-3677-aa09-82558497cf00 | -11.23715 | -46.95488 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9d6dd37-04a5-32b0-a6ec-13c7fb034bc9 | -11.22786 | -46.96314 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| eb3e9c81-cd13-3c3d-9ddc-98fd6f5a310c | -11.22485 | -46.95769 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7ef68cd-0528-3b22-b230-c6a68f6b6a31 | -11.22483 | -46.61621 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c1ab5a3-2f69-31cf-ac65-1888f8381a90 | -11.22402 | -46.96252 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2bbf2b70-2d67-3dff-8049-beb7d388417d | -11.22187 | -46.61094 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba22609e-b91b-359a-bdfa-6d307f818c96 | -11.21318 | -46.91064 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3d07ed43-14be-3635-bd7a-39c46afb9fc0 | -11.20935 | -46.91004 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f4cd2f08-2274-3f08-9116-a99a845bac0c | -11.20552 | -46.90944 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e2ab5aa-db23-3675-8bd5-617fbbef6d83 | -11.20087 | -46.9136 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9ed2af93-6338-3de5-8f79-7a706e5beb84 | -11.19704 | -46.91301 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e1d34af-c58d-31c0-91f7-a106cd8d4713 | -11.19622 | -46.91772 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70121ab1-d689-3ff7-b353-e05f50a19f4d | -11.1947 | -46.97237 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b438c2ca-c35c-3f83-bc3e-0f57efec860f | -11.19239 | -46.91712 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4bba790-2a54-37e8-81b0-43cd5d82e35c | -11.19004 | -46.97652 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4ba2050-7c76-3001-aef1-e322d998e37a | -11.18855 | -46.91652 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d57d7c2-f750-3f5e-9aac-630508d46617 | -11.18143 | -46.93493 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 058e544e-b4ea-3960-8be4-b20c8cc3a6a0 | -11.1806 | -46.93975 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 506c58ae-1623-3bb3-aa89-204ba937bbe8 | -11.17508 | -46.94881 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9997cb0e-a5d9-3686-865d-0a199cbb0afa | -11.17425 | -46.95362 | 2024-10-04 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8e37ca8-54f9-33f8-97e2-b797710ebe5f | -11.11366 | -46.49455 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 2ca9ffcc-bda5-3c3b-bc99-4ffedcd4d868 | -11.11206 | -46.4963 | 2024-10-04 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |


[Clique aqui para ver as próximas entradas](README71.md)
