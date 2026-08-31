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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54e18c21-e3c3-38d1-948d-abb41ebdf358 | -6.9177 | -55.6967 | 2026-08-31 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 52a4f50a-ca37-376c-82c4-ae994446752b | -14.3807 | -52.5675 | 2026-08-31 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c7239805-0c31-3ed8-bcf6-324a57d5415b | -7.6149 | -44.8833 | 2026-08-31 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 87f10a40-9b78-3e4a-945f-650ac0d1cb66 | -3.6216 | -60.547 | 2026-08-31 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 0df63e09-8015-3c53-b6c2-24c788d55fec | -10.8617 | -50.4772 | 2026-08-31 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 53cadde1-c75c-329e-bd2c-77d67890eb84 | -8.799 | -62.4905 | 2026-08-31 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.0 |
| bdeed586-7c70-3d35-aed2-befd6b7df141 | -11.3423 | -45.1982 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f3f9306f-b86e-3153-8a55-1800a0832bb3 | -10.3205 | -49.9567 | 2026-08-31 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5bba2a39-25fd-3f1e-bcf2-5ba7fef34966 | -9.4342 | -45.6704 | 2026-08-31 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 0e186d18-d996-31df-906d-4b8297be7cf6 | -14.1263 | -52.8106 | 2026-08-31 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 6434b8e9-f6a5-30a2-adf4-2aa03715214d | -5.2548 | -55.8907 | 2026-08-31 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 6c209efa-1c6b-3f86-a68e-6528b65e0771 | -10.7407 | -54.0401 | 2026-08-31 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 191.8 |
| 84b576ac-af33-36f6-9145-b30b1928f4b5 | -3.4167 | -43.3867 | 2026-08-31 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| db9e0cc2-5063-37ad-8ce6-e3f3bd36c95c | -15.8844 | -56.4819 | 2026-08-31 14:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9fb59308-019e-356c-a2cc-7efd69684248 | -8.7439 | -46.4661 | 2026-08-31 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 98bf23c7-3d06-3ad2-b422-d5b0f2c109b6 | -9.2092 | -51.5654 | 2026-08-31 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 145.8 |
| 73803aff-a391-3694-ac53-303d9bb671e0 | -5.2362 | -55.9112 | 2026-08-31 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f2a48b95-d000-3e9f-8974-e31bf9e4ba33 | -9.5967 | -47.5983 | 2026-08-31 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| b22ad840-4d63-3956-9795-4004cd40e872 | -7.6251 | -55.2987 | 2026-08-31 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0a1e3ccb-67a3-350f-837d-0b8e1338fe77 | -6.9367 | -55.636 | 2026-08-31 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 67376afa-07e1-3129-8395-796a4858fd2e | -8.7579 | -45.3823 | 2026-08-31 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1cf1e286-872a-3461-a83e-9cc2ac2c5728 | -11.9186 | -45.0685 | 2026-08-31 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 259b7ff5-5515-325c-8929-cd2e45b0a1ea | -7.5659 | -61.362 | 2026-08-31 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f989ee2c-4a5a-3d86-9989-e04c01d0e121 | -8.8175 | -62.4898 | 2026-08-31 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 456c97d1-e080-3a2d-b0fd-883a4b68e692 | -14.5028 | -52.1913 | 2026-08-31 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 51b2f168-5ba4-3215-be7b-53f144927ad0 | -15.3654 | -53.7887 | 2026-08-31 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 3d9fc3b6-3c2b-37db-90cb-3ac903f9100e | -10.7407 | -54.0401 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 6836a626-6169-3605-b28e-eaa09a54608b | -15.8649 | -56.4841 | 2026-08-31 14:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 47cfb4a3-e2e4-3040-abd4-55e6ab0e7f57 | -7.9422 | -44.277 | 2026-08-31 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5212132a-a671-3c76-afa9-23360f956878 | -8.799 | -62.4905 | 2026-08-31 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 68af0649-5055-35ef-8f58-892d614e5675 | -14.4201 | -52.5201 | 2026-08-31 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 231.9 |
| fbe08559-bbfd-3d16-8b2e-ed18dd0f6ad6 | -7.9425 | -44.2538 | 2026-08-31 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 211.4 |
| da19f779-3929-38ca-883e-f505fd81a29c | -8.7579 | -45.3823 | 2026-08-31 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 980dbf09-8df6-3256-8dc5-0d5fdae0aa2b | -11.1919 | -51.2496 | 2026-08-31 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e1c99373-71a2-3604-a21f-5af422f6aefc | -14.4835 | -52.1938 | 2026-08-31 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| d86717e1-5773-31ca-8107-1d2d3affb66c | -15.8844 | -56.4819 | 2026-08-31 14:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8df8631e-43d6-3e55-9245-ff17f1a96760 | -7.5137 | -55.3051 | 2026-08-31 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 7ecf10de-12b1-3ee9-b4f4-03d6de365b6e | -7.9907 | -46.5177 | 2026-08-31 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| d5f58b89-c7c8-3ded-b1d4-154c9e00b363 | -9.153 | -59.5415 | 2026-08-31 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e6057408-3583-3191-af68-bf8d5fc986e3 | -6.7648 | -59.4408 | 2026-08-31 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| a7179c17-5603-311e-a9aa-406d27b1156b | -15.346 | -53.7912 | 2026-08-31 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 179.9 |
| a4d13e65-86c5-317a-8909-a5798203a251 | -10.8046 | -50.5046 | 2026-08-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9fde7252-e251-359a-bf67-da340a7c6555 | -8.87 | -66.8935 | 2026-08-31 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d15c3bc2-7037-3fea-973f-786db37412d6 | -11.0434 | -49.6851 | 2026-08-31 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 9e33d5a9-d996-37af-9c51-10ad0bd878d9 | -11.1916 | -51.2708 | 2026-08-31 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 1d59a63e-30c1-38ca-99c2-068dae557a95 | -7.566 | -61.343 | 2026-08-31 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| bd776817-bb64-3856-885a-b852028866a2 | -6.1108 | -57.7035 | 2026-08-31 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 851ef99a-5325-3780-b613-cb21109c83ca | -7.5846 | -61.3232 | 2026-08-31 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2560cb3e-fd22-312e-8187-a92e7ecb3e61 | -14.1456 | -52.8082 | 2026-08-31 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b8834586-d22b-3429-91b0-74e733e60d28 | -11.3427 | -45.1751 | 2026-08-31 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 3bb77bc1-381a-3654-863f-72ba6533c253 | -13.4327 | -51.7547 | 2026-08-31 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 675b8695-935c-3f6e-8722-1023244c267c | -6.1295 | -57.6637 | 2026-08-31 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 39351042-6453-3fbe-accd-b9b796e8d455 | -9.1906 | -51.546 | 2026-08-31 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c564a112-1b69-31c4-84cd-112c93a057b7 | -14.5868 | -54.1153 | 2026-08-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 6cec9179-f4ed-38bb-a16f-2323e6b67af0 | -7.9236 | -44.2558 | 2026-08-31 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 46503092-ae3b-3753-bf1f-385c00ba7258 | -10.7409 | -54.0196 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 169aa5a8-2621-32ee-89c7-a4c7dabc6ff3 | -13.967 | -54.395 | 2026-08-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 491.7 |
| ce09713b-68fa-34a1-a01d-df14c3d48d3b | -8.7628 | -46.4642 | 2026-08-31 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| c41687d0-0d1a-383d-a014-56692eb1da36 | -13.8371 | -54.0989 | 2026-08-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| f85e8112-2684-3a80-ab0e-ae59518a6272 | -13.9667 | -54.4157 | 2026-08-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 446.3 |
| 4a001a2e-16ef-3944-83fd-d491e3374f1c | -10.8614 | -50.4985 | 2026-08-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| b06cf766-0a02-3708-a424-f15815035925 | -10.7596 | -54.0384 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 30dab4da-1e2c-3036-ac77-44442f0f08d5 | -13.8567 | -54.0759 | 2026-08-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 5f415cdd-0631-3991-9086-63744e0fb48b | -14.4007 | -52.5226 | 2026-08-31 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 10754f26-ff8b-345d-9f3d-29c70ffc7453 | -13.8563 | -54.0967 | 2026-08-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 142.6 |
| b1eafdc8-a121-39c6-829f-bfc5371df76b | -15.6475 | -50.1062 | 2026-08-31 14:40:00 | GOES-19 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| c35496e2-ce20-3eed-8a55-8a8d62202abb | -7.1126 | -42.749 | 2026-08-31 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 094f2d5a-e183-3572-ba5e-e5c9abb205d2 | -7.9797 | -44.2962 | 2026-08-31 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 6c8b0d45-ad85-3e3d-9228-bfbd7d1de34f | -10.9865 | -48.3869 | 2026-08-31 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 3a24af94-af5b-3c56-8283-15387430b344 | -11.8211 | -51.0322 | 2026-08-31 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fe710be0-7d82-3a98-9830-da64953d061c | -7.9605 | -44.3212 | 2026-08-31 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 80b57d5e-8c7f-3c4e-8233-c4548969d55b | -18.2899 | -52.7035 | 2026-08-31 14:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 52016d39-fd48-3a7e-8cb9-2ad309dc8c6b | -10.3394 | -49.9547 | 2026-08-31 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3296eae1-a4aa-3e4a-a98d-f6fdc7b73d77 | -11.2317 | -53.9958 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 153a5181-fccb-3b46-b378-d526c92ce1a4 | -14.8319 | -55.7194 | 2026-08-31 14:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3ccedf88-35cc-3c42-9495-406c7e3b312f | -3.6215 | -60.566 | 2026-08-31 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 453df5a6-9fce-3bbd-9500-fd0862b7f8c4 | -6.9177 | -55.6967 | 2026-08-31 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 59fe175b-aa8a-3a83-9382-dbd5784a791c | -7.9905 | -46.54 | 2026-08-31 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5601010a-be5f-3978-aaa4-f995645d087a | -14.4641 | -52.1964 | 2026-08-31 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 143.3 |
| c4e7ca2d-c5e0-30c4-a4ab-11289575691c | -10.8987 | -50.5372 | 2026-08-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b85d27b0-6799-3167-9d5a-56ac425d013f | -10.8617 | -50.4772 | 2026-08-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| fd0f311f-2d0e-33ab-b993-c7b9e85572af | -5.2362 | -55.9112 | 2026-08-31 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 901dbdc7-fedb-3551-bdf1-1e1926506871 | -15.2475 | -53.8876 | 2026-08-31 14:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 1dd3a501-e6a5-37e8-aa09-ac0c3b6ed3c4 | -6.9368 | -55.6161 | 2026-08-31 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fdf6471e-7d90-3780-bac2-29f94cb9846b | -15.6336 | -56.3876 | 2026-08-31 14:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3df5026c-124b-39cd-84ea-eb8d17db3b08 | -9.1711 | -59.618 | 2026-08-31 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 75819569-efb1-33d7-8f64-b15ebc233456 | -10.3205 | -49.9567 | 2026-08-31 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 32e0d33c-2a21-3651-b0f3-e79725fa7f64 | -15.2478 | -53.8666 | 2026-08-31 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 027e2fe8-be1f-3a35-8d12-4031eb2d9dc6 | -13.4324 | -51.776 | 2026-08-31 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 4478ebe1-2fa5-375a-acb5-1481e8059737 | -10.1538 | -45.6982 | 2026-08-31 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 367.8 |
| 8771976f-9c05-337a-b056-57ed6e549a66 | -5.2363 | -55.8914 | 2026-08-31 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 70970d5c-0aed-30ec-836c-1f91fab4bfa9 | -14.1263 | -52.8106 | 2026-08-31 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ddc549d1-d447-3360-ba9f-56554bf58132 | -7.9794 | -44.3193 | 2026-08-31 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 274.9 |
| c05975b3-a265-3d50-9460-b0bc165074c4 | -4.9788 | -55.8417 | 2026-08-31 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0dc685d5-37ae-3f30-8d64-6160e51c7de0 | -11.5283 | -45.4933 | 2026-08-31 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 909e8034-2d5b-3ec4-bc01-122c931809d0 | -10.1535 | -45.721 | 2026-08-31 14:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 307.5 |
| c50064ee-ecf4-385e-ac05-87849bc5d406 | -10.7598 | -54.0179 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 05e3a5ed-d8a0-3ed3-a3c9-423b7f4a05eb | -5.9451 | -57.6906 | 2026-08-31 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| af65dec5-f772-39cc-a04b-2162bd11ab9d | -9.5778 | -47.6003 | 2026-08-31 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8d01e486-ffbf-3905-ae9e-22795d764792 | -10.5598 | -50.4236 | 2026-08-31 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |


[Clique aqui para ver as próximas entradas](README95.md)
