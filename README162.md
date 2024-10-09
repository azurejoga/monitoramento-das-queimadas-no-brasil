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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3220d040-e59f-3861-87d5-866cb9453cbc | -8.03715 | -49.70535 | 2024-10-09 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f961fb7-e54a-3f08-8410-64edb9612bcc | -8.52723 | -48.77716 | 2024-10-09 05:01:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abfaafbc-2218-3b65-aa25-d73f39e9ab18 | -8.501 | -48.64714 | 2024-10-09 05:01:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28a5ac45-0f1e-39ee-bbb5-7141fdda61dd | -8.49695 | -48.64116 | 2024-10-09 05:01:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0d9753ef-b5f1-31c2-8014-76641cb2e822 | -8.4962 | -48.64657 | 2024-10-09 05:01:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4fbe7b27-028f-38dd-a322-bf3f53f600f3 | -8.49546 | -48.65189 | 2024-10-09 05:01:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 93ee3de7-4262-3448-adad-024ac4ced18f | -8.49217 | -48.64048 | 2024-10-09 05:01:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b0a2e18a-562f-3bd4-a5cc-48a248286ed9 | -8.49142 | -48.64584 | 2024-10-09 05:01:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 75786acd-72d0-30fd-ad01-e03e18df4810 | -8.49068 | -48.65118 | 2024-10-09 05:01:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9aef34f5-bf12-3e96-b3bc-db3171666711 | -3.50675 | -50.27156 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3f8761d-9442-3de8-ad08-3b2b24a68a19 | -3.50212 | -50.27524 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8171a465-f90e-3ad7-95de-b9013fad2bf1 | -3.43058 | -50.32556 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae3df481-e502-3a30-882a-8a22ddfe4d9f | -3.40923 | -50.33268 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bd28e746-ce16-3353-9012-4eefb3c4907b | -3.40604 | -50.32714 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e48edd5c-6eea-399d-b5f9-8eae8688fff1 | -3.40527 | -50.33212 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5dfcf0b1-7fe7-3206-bb6a-0575dc56291a | -3.33811 | -50.11956 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d7b6407-7980-33fe-b89d-38c5df35026c | -3.33757 | -50.12304 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36514fc9-72a8-3dc0-b7a4-9efba05d53bc | -3.33702 | -50.12653 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be098e97-eea7-386e-900f-c51a9c9a8f90 | -3.33649 | -50.13 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ad9faaf-81f9-3953-aa2e-2e2c4914ec80 | -3.3341 | -50.11898 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 067b3219-01d0-3ab7-9324-7981feac84b6 | -3.33356 | -50.12245 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f470d80-3a31-3b67-ada5-53854a0c923d | -3.33302 | -50.12594 | 2024-10-09 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c5db2f5-2ac3-3015-8956-94a41966fce4 | -3.11202 | -50.38608 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 822d38a1-9091-3cd2-a872-de6d560d2436 | -3.10881 | -50.3807 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 919d90c7-4d5a-3a20-929d-345921239f79 | -3.10808 | -50.38559 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 789f1245-32dd-3e0e-82ed-c5e9ded7f58e | -3.10735 | -50.39048 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 066e4e2f-561b-389a-80aa-fcd6eb86a2f5 | -3.10415 | -50.38504 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47c0ade2-a500-3c28-a735-da6f22a38503 | -3.10342 | -50.38993 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4f01f25-2624-34b2-8b04-207ac81f870e | -3.10007 | -50.4656 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6840b2a-bdae-3739-88eb-d7ae22be1e31 | -3.09616 | -50.46501 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1373e28f-5ecb-369a-8846-ce7d34a42866 | -3.0767 | -50.48516 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 058582b0-e534-3794-8b20-6799ff87e030 | -3.07297 | -50.48668 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e12d7ad5-8b55-3ccc-a1fa-7f6e717ce326 | -3.03599 | -50.43848 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53141e89-c495-37a6-9a81-3a05e0366c10 | -2.89429 | -50.39449 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a48a0d0-1f4a-3ea9-b6e6-bb67a13a2213 | -2.89355 | -50.39942 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67a6028a-ea90-31b6-b383-e8961891b968 | -2.89281 | -50.40434 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4732cc2e-b14a-3924-a966-8f7e4a20de86 | -2.8889 | -50.40374 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59f44497-9a24-310e-bc51-10c05f54bebf | -2.47557 | -50.24669 | 2024-10-09 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f854019-b775-360a-a6c6-31340c4b91c7 | -2.47482 | -50.25167 | 2024-10-09 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cfd24230-7eb3-38f8-bfc5-c8fdf9c0328f | -2.47164 | -50.24609 | 2024-10-09 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcd4fbf9-59de-344f-aeb9-53870b874635 | -2.4714 | -50.24906 | 2024-10-09 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8d26c31-33c7-3c05-9147-727b3f18494b | -2.47089 | -50.25106 | 2024-10-09 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef53145a-7496-3d91-8e18-b456c27c3818 | -2.45416 | -50.25662 | 2024-10-09 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71e1bab2-c3d4-3a94-a38b-bfd3f1c2ac0c | -2.45372 | -50.25862 | 2024-10-09 05:01:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b188e87c-06be-3492-b7b5-7494517c6c25 | -2.3316 | -50.37885 | 2024-10-09 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d3d8b8b-8f5e-305c-b16e-cac28add2888 | -3.6353 | -49.56898 | 2024-10-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22a2873f-f819-3659-b69f-e20136c207ce | -3.63112 | -49.56841 | 2024-10-09 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1345764-d2f9-3fd9-bea0-e079859dff3f | -3.27086 | -49.0982 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 690b7086-711e-3ad5-8c07-07dc71900ecf | -3.26106 | -49.10494 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f332567-3d4d-3858-a963-87f03ae482f0 | -3.26045 | -49.10896 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56ee725d-c3b1-3f96-b9ec-b54d2a9dbc95 | -3.05685 | -49.39563 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fbefd17e-026f-3214-a451-e296f18c1c9b | -2.98387 | -49.52935 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c24c576-e118-37ae-9b45-0d357f6f7d32 | -2.9518 | -49.20322 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44715666-56a4-3a11-9056-470e08a9027e | -2.95178 | -49.2037 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed515215-e7ab-3199-a8df-965bd503b04a | -2.94757 | -49.20258 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5ab8384-b133-3d52-8698-b2f130e0c287 | -2.94755 | -49.20308 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17d6aa18-c94c-3281-8d24-c9eb09ba34e4 | -2.94699 | -49.2065 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 090efb41-0eae-39ad-aaef-990c07602b19 | -2.94694 | -49.20699 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0352cbb-4924-3648-a7c0-e079d83523ba | -2.79786 | -49.59623 | 2024-10-09 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46bd8ee1-28d8-37a9-9da3-0f52319ecafa | -2.79374 | -49.5956 | 2024-10-09 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58df9c6b-55ef-3760-ba8c-0209de422cb3 | -2.62483 | -49.25099 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6e4e087-c4b3-30dc-b66a-4a2598be2b07 | -2.62063 | -49.25037 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1c06373-b57a-3bd6-baad-9e080486ca7e | -2.60641 | -49.78943 | 2024-10-09 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ff99aeaa-0638-3d5f-82e8-deee7228f668 | -2.60586 | -49.79301 | 2024-10-09 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a461ef34-0b2f-39db-b7e8-a3583f96b7dd | -2.60181 | -49.7924 | 2024-10-09 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6a053cfc-d9c3-3822-a6d9-532c7032f79f | -2.47944 | -49.01105 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de342498-9a55-3c5d-9753-77812b2aec5f | -2.40886 | -49.13417 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f2dc89e-dcf1-3c1c-a95a-7d37ebe649a0 | -2.35248 | -48.9929 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aae75ad1-0b7f-33de-a9ed-c2fd2bdb3b02 | -2.35187 | -48.99691 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3d57faf-0374-32b2-9cab-59513cd5e985 | -2.34822 | -48.99225 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9683081-f062-383a-9925-d3ee119bdfa3 | -2.34762 | -48.99624 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 377bfd95-ae74-31ae-b7e9-1b70a3a34235 | -2.31058 | -49.68361 | 2024-10-09 05:01:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7870975a-bdfd-3b22-b3f0-1587b919d573 | -5.09297 | -49.59136 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16a1c65a-b7a2-3342-bec4-74bb1cb2025f | -5.01386 | -49.77338 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c856881a-e172-3c3d-9aee-daff50805dbf | -4.95084 | -49.76406 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 914e5386-d967-3106-8563-f0d5e998c8b6 | -4.94722 | -49.75952 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 614a0b6c-830e-3f2b-8712-2c8ec74d80d3 | -4.94665 | -49.76342 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b15723e-d033-34e6-b021-ec6fbbd1256a | -4.94608 | -49.76728 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edeafa7a-4486-3dcc-b341-eae1eb20fe04 | -4.94303 | -49.7588 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d064d8f-93c4-3eb0-9293-4f08f75e4045 | -4.93884 | -49.75808 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2f31bfc-1d2f-3397-ab19-b00cf3d6c93a | -4.91976 | -50.56935 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 416691dc-1037-3286-b177-17fa6fc20331 | -4.9059 | -49.86682 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae1f5fcc-9c6a-34a0-983a-82df4d264e9b | -4.90431 | -49.93615 | 2024-10-09 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45de7f1f-710e-3a54-9111-48a58f80fe5e | -4.80459 | -49.93837 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 508e6cf5-299b-3414-a918-f2d37cd5555d | -4.80405 | -49.94205 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f40b151-41bb-3437-86da-247525434b0a | -4.72623 | -50.8735 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5387e9b-a1c9-3383-b113-64009da621f1 | -4.72548 | -50.8784 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06a0ea7c-a5e9-33c1-bae8-e3f2b0c4ba2f | -4.72234 | -50.87289 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2247e5b-4a65-3eb1-b609-234a022d7e03 | -4.72159 | -50.87779 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2c3bdb9-e568-3473-979c-83527779c47b | -4.69781 | -50.40201 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46421238-eab9-3d16-84f1-51b480da5364 | -4.38184 | -49.78829 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 279dfd4c-d40c-37f9-bf96-3bc00ec1cc16 | -4.38129 | -49.79204 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63d7920f-7797-3ed1-a901-e9dd851c54a7 | -4.37837 | -50.81473 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff3663d4-b1b6-3ac3-a364-45666e7c61b9 | -4.37768 | -49.78767 | 2024-10-09 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f3251ea-adaa-34c5-94e6-f99e2f095b70 | -4.18476 | -49.39649 | 2024-10-09 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16d2b755-ae32-32aa-9750-ab11983a8798 | -4.18416 | -49.4005 | 2024-10-09 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8716e70-2d73-3710-b2be-1550c39da843 | -4.1805 | -49.39586 | 2024-10-09 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e40120b0-64c7-3f32-ac6e-42985a8b7ff4 | -3.8865 | -49.9917 | 2024-10-09 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7176b971-8b8b-3dee-b1d6-d03336f16ad6 | -3.88595 | -49.99528 | 2024-10-09 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dbcda55-96d8-3b9d-b108-bfb276bde838 | -3.88243 | -49.99106 | 2024-10-09 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README163.md)
