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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c57e7ad5-b26f-3209-96d7-db0ed20f597b | -5.80952 | -43.23764 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ea1c443-f2f0-3fa5-b6c2-6e364e7852d4 | -6.43808 | -58.12195 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8efe9c75-a763-306c-b555-caddfafc3ac5 | -3.47884 | -59.25493 | 2025-09-03 05:12:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be892392-b671-3482-9435-2ebbce704b90 | -7.71333 | -48.75168 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a55cc051-5ba5-360c-b184-917fa0719723 | -5.92862 | -57.71445 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c191d77c-23fc-32d3-bebd-82687c354055 | -7.48301 | -44.8396 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dda37aa0-8fe3-3533-9b30-fd30f584f346 | -6.80327 | -52.81272 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12944df1-b72c-336b-aa3e-400a3c59e213 | -2.88151 | -59.22659 | 2025-09-03 05:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c27351ff-b031-3178-9e86-419342b9887d | -5.92418 | -57.72089 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 5affdde5-a59f-33c2-8cf1-a181bc52b8c2 | -3.22336 | -47.12968 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a68a7423-928d-38f0-889f-81a448f0c9f5 | -7.47539 | -44.81429 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0af4c5d1-1b04-3eb9-934a-eb998cbe8956 | -6.77648 | -52.80357 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6925f726-a87c-3598-8636-91663fd11f7a | -6.78752 | -52.81044 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b1c360f-e8de-3a4e-8a4e-4f4b197fb869 | -3.22885 | -47.13054 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf3890df-1bf0-3f4c-bca8-6a52727fada2 | -7.14768 | -48.20461 | 2025-09-03 05:12:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6ab2bc3-3cda-3272-9331-7d94f414f3b9 | -2.28153 | -56.12958 | 2025-09-03 05:12:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3a74b91-d1e9-3d6a-9c15-bc0c6e272f68 | -5.91918 | -57.7094 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0743186-c5c6-3da2-bcfe-a1b18e893e0a | -4.14972 | -46.79188 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97cb8031-e170-35df-8e87-b2ad64f1a4ec | -8.20919 | -44.81295 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 84d413ab-c8cc-38c7-8ecf-e474fafd485a | -3.2239 | -47.12613 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c09e964-2288-3945-9b22-a8086f8ae860 | -6.27486 | -44.50384 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc6f2509-f1ec-3c57-a578-35c7e6175983 | -6.82782 | -52.83319 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3745cc22-c985-3b83-b143-9ea038479ebb | -7.72345 | -48.7246 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dea318b4-b368-3eb2-a8c7-e81f6d0080b2 | -6.85038 | -52.81638 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1b41e4ed-e540-3f3c-90d7-2474770ee981 | -7.48456 | -44.82796 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95297f48-8075-3242-965f-8b59cc057625 | -7.96878 | -46.50604 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 194a8108-2d94-313a-9325-7b97b236b874 | -7.92867 | -46.43159 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08a80bd6-5a16-3e03-877e-26f035f8810e | -6.79098 | -44.09027 | 2025-09-03 05:12:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0cc972f-c16a-3d29-adc0-33aab3ada172 | -5.10877 | -56.96982 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62db785c-515b-3062-98e9-3f617c091419 | -5.90199 | -57.75313 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a46ade5-dd28-3555-9e41-9900a7c805ce | -6.34777 | -45.66828 | 2025-09-03 05:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5b1d9d5-79f8-3cba-9a9c-517d4ceac5c8 | -3.48174 | -59.25946 | 2025-09-03 05:12:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff7d26ef-370f-39b7-95c8-ead5f9d56973 | -5.90863 | -57.71132 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4979ef8-30d8-3eab-b5ed-cf457f2562c9 | -6.05593 | -57.99609 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5c9fb2a-52df-3aee-b9e1-e20d235a51b1 | -3.32553 | -54.91044 | 2025-09-03 05:12:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a46697fa-31b6-3475-a0e3-3f9bfb3a25fd | -6.79616 | -52.80647 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be08626a-f864-3995-a0cf-a31ad3df6c0f | -5.59924 | -51.94921 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a79eea6-24f0-3295-9379-72f480a7247f | -5.87088 | -57.75537 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 714f2777-69af-359c-9a72-3ecce754f434 | -6.83538 | -52.8089 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfab83be-ae1f-384e-9528-b680785d1836 | -5.80453 | -43.23489 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a4dfcc5b-b6bc-37f0-b386-7816071cfe33 | -5.54763 | -51.33996 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 547daa94-7bbe-3824-8594-a55bf962313f | -6.83567 | -52.8344 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aae67402-32a2-3f64-9bf2-8e404df6e0f8 | -3.88487 | -54.21419 | 2025-09-03 05:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db1e4150-55ab-34fc-b7cd-cbef812f6151 | -8.05921 | -45.361 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d9d7f083-d12e-3e0a-a66b-f4155cef32f0 | -5.54338 | -51.33934 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 234b0e51-523e-3e33-ad03-a96e89bc67d9 | -5.92752 | -57.72141 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e81f361-288d-3566-b9c8-548b25021a15 | -7.60147 | -46.22839 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76b56abe-9932-3df9-a7d6-b43104b42919 | -7.50122 | -45.34711 | 2025-09-03 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd5679fa-11fe-363d-9c71-9603b66ed12c | -6.82677 | -52.81276 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50bd3d6a-bb41-3fd9-928b-749f6d053417 | -6.53003 | -56.20701 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b22b07b8-5ef8-3717-82fe-d4bf9951e26f | -3.48382 | -48.44543 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 918a9f66-45b6-3ef3-86d7-4eebda6b3fef | -6.27747 | -43.50775 | 2025-09-03 05:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e5576fe-6377-3f0d-bdad-53bd55c08953 | -6.85328 | -52.7966 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f5ffb2b-00cb-3560-9ab4-500b54659ccf | -6.03677 | -46.01483 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c35d3fd1-ff6b-3ff3-8df0-9d241014771b | -6.77574 | -52.80854 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35faccc6-458c-3b00-b68c-49891afadbe3 | -6.70312 | -48.39868 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a2f40286-b753-3405-b417-c4846f4e104a | -7.9232 | -46.42503 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5f1c423-aa87-3ebd-9604-5af2f54d02b2 | -5.86922 | -57.76583 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fe0eb426-98ec-3148-9bd8-e62e47a00459 | -7.93106 | -46.55693 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 129463f8-cbbb-3f9d-b8a3-99dc8742eb88 | -5.86422 | -57.77576 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 348d8d69-5d18-3c9c-8d86-c0e34b2875ee | -6.58103 | -44.56975 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc48aded-b737-3c8d-8c40-7e814e20780b | -3.22497 | -47.11901 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 876cc163-a11b-360e-8dc4-77604b374010 | -7.92321 | -46.42572 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24dcbd6b-af71-3dce-be5c-c7bd973e789c | -6.81422 | -52.8161 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c78ead0-fb65-36fd-acc7-840447be5321 | -4.16108 | -46.7936 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 664c8fa5-5294-324d-9c74-1169693400e9 | -2.89884 | -48.29311 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bb280e16-4e76-37df-87b6-91144f416980 | -5.8731 | -57.76287 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55e8e8e5-8d08-3e3d-9932-9daa5f4c2109 | -5.69057 | -45.95205 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c3e701d-1e7f-36d8-af10-dc4562a9b142 | -5.10545 | -56.9693 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 782ced0a-1404-3dd9-8da1-9a11871c0f2b | -6.34196 | -58.32377 | 2025-09-03 05:12:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f009c4f-ec74-3527-9169-db010fb85ab4 | -2.13258 | -48.00572 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfc66925-1d26-30b4-866d-ad6524e7a2a0 | -3.81157 | -52.2672 | 2025-09-03 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 56037fdd-0724-325b-9df2-7dc44276547b | -6.43304 | -58.13197 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe78a4d7-9844-3a85-a1f9-efc603a3424b | -7.49355 | -44.81192 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c241e82c-1f84-34c3-ae69-613ed74a3d7c | -6.85505 | -52.81197 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15cf95a2-1f8e-3ac7-aeb6-5b2e54b64b5d | -6.34842 | -45.66365 | 2025-09-03 05:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2904cd92-0f1a-340a-afce-2061d80a2a37 | -6.53058 | -56.20345 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b088e58-49f7-3926-b413-59085de67264 | -6.84892 | -52.82629 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eebe0c22-31b9-3a64-87ef-fccc9ffec94f | -6.47805 | -45.40623 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec113494-b1f0-33bf-923b-47d867ae877d | -7.72019 | -48.74043 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 884ba1d9-83e4-3261-9744-17cc13d641f3 | -5.8931 | -57.74458 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe7415a6-843c-3873-bb4e-e81d5c247692 | -7.69803 | -48.75285 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9bff7621-5296-3532-8cbd-23f46b5ddade | -5.10932 | -56.96635 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edb03d45-323a-3ccc-b99a-2df9127caf64 | -7.15311 | -48.20529 | 2025-09-03 05:12:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7dcf45f4-9fda-3e21-bab9-068ecf8e7fd3 | -4.52624 | -54.97501 | 2025-09-03 05:12:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64029045-c85c-3733-82b6-b5804d291d89 | -5.70971 | -53.69284 | 2025-09-03 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59a412b5-df73-3e10-a56b-31c0e673849b | -2.58583 | -51.9245 | 2025-09-03 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77b11315-4976-3461-bd3b-13a2f6dbabbd | -7.50918 | -45.3372 | 2025-09-03 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6d92880-9dd9-3dcd-be3d-c31726d5c121 | -7.91579 | -46.43447 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65dd5623-c010-3e97-8b27-560547f9f379 | -5.92085 | -57.72037 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 820cb245-d16f-391b-9f0d-570b8aae95f6 | -5.91363 | -57.72282 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46ea518a-6e17-30a8-97e4-1610accc0173 | -6.69502 | -44.17966 | 2025-09-03 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7b7a921-c8f6-3ea2-be34-941647dc241a | -8.0202 | -44.11031 | 2025-09-03 05:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 201b0e29-37b3-30f0-a37b-9dbc90d55022 | -5.31741 | -55.87821 | 2025-09-03 05:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9116d6b0-48bc-35f3-a2ac-857293d14b32 | -4.15651 | -46.78531 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9431c02f-fd50-3c3d-88e3-cf796b1ef01e | -6.43639 | -58.1325 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dc4cec8-c023-3a89-81b3-035450cbc88e | -5.90032 | -57.74214 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| e543b905-825f-3146-af38-aa4c2405ebf2 | -5.91919 | -57.73084 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d27a676b-1d12-3fa1-aa9e-4f2583cf465f | -6.46012 | -49.52296 | 2025-09-03 05:12:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3eda739b-7db2-3a72-93d2-699544525b89 | -6.34055 | -58.18213 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README81.md)
