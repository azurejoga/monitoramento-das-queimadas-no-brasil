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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d886cbf0-7830-3f45-b29b-8583ab5a8f07 | -11.4381 | -45.62563 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ccd4da6-01eb-31d1-bc06-969425a4c939 | -18.3341 | -49.44064 | 2025-09-13 03:47:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31fa8336-88d8-33ce-9a90-7d6123846638 | -11.12394 | -50.71145 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a1d2f661-7538-362b-bf85-3c5fd9aedc03 | -10.69092 | -48.66505 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b7a34a3b-1648-35a9-8780-a79d52ae0688 | -13.91173 | -48.22583 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17a26420-f9e6-3387-a0b8-72e4371f35b7 | -7.50747 | -44.6825 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f03da0b-d2d4-351f-9ed8-5a888bc9eaa4 | -20.01812 | -47.63453 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a241b10-d389-322a-b4f2-db16340dce8f | -11.7307 | -46.60783 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4ef04c2-4fee-3fb5-8c31-13967d0dbeeb | -7.57253 | -42.64341 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 896e926e-342b-3990-bdf9-2b2ac71dd558 | -14.20228 | -46.2449 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 66516c42-938e-37cf-9e01-3dc1d8a00198 | -16.34689 | -51.53071 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a56e3bd8-2a7a-3ddf-a4b6-4de2f825c41b | -12.80825 | -47.9925 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1068792c-fc5f-3d8c-912e-ba29bbecb281 | -11.41872 | -45.61104 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cfcebeb9-d1f6-310e-bb7a-0eceb2b0d061 | -17.43539 | -49.2513 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9351b33-c714-3302-9cf2-589549303eb3 | -7.56143 | -42.65148 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1cfa0a7-78d2-3dd8-b701-a52be51e4c0f | -14.22142 | -46.28764 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| d24904f8-cb2a-3ecc-b6ab-bd45909dce6e | -7.4383 | -44.40355 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daa7ccb6-70c3-313d-9ebd-07a33a309b25 | -18.06788 | -45.45707 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a90e652f-89e0-356c-a02a-0db8dc74c30d | -8.08977 | -44.51466 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19957e5e-6854-3b44-beed-3dd2419f95ac | -8.06618 | -44.52995 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0bd739c-cabb-3e53-9dbe-eb1b73b45e9c | -20.33641 | -46.6651 | 2025-09-13 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fd56825-f3e4-308f-bf30-fa45e462206b | -7.50812 | -44.6788 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 846e4448-c38a-3193-91e9-18f0ebc5b2ed | -11.45763 | -43.57592 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8ca6842-bd24-3e1b-8ac2-7c3c9e6f7752 | -11.4299 | -45.61044 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c83afb5-dd9c-3569-9c64-55a9f04c7786 | -12.99785 | -46.73623 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c8f748f-af60-300a-b3d6-d9e5bacc7efc | -12.9036 | -47.95651 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36052937-785f-3a5d-8375-ab25d704fa7d | -11.99485 | -47.76411 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 90b1ea45-7692-3df5-8ad5-b32c0532a1a1 | -10.77822 | -50.5502 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 57b936a0-9c55-3b01-8719-7943326b3989 | -12.09141 | -44.90023 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65717899-51cd-3cd7-9f6f-1db451c8a6a5 | -16.2527 | -50.0693 | 2025-09-13 03:47:00 | NPP-375D | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eed248d3-65e7-3920-ab6e-7b62644c5ea3 | -17.28978 | -47.23811 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 910a6e15-f6ab-3002-a447-23d95528ff38 | -12.11781 | -47.59641 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbdd0249-4bff-3391-9412-44804e65761e | -11.86955 | -46.75637 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84914c2e-e628-3d46-962d-669714ffabbd | -11.67083 | -46.51474 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca5cd368-322f-398f-9ac8-ee8c506389ec | -19.33283 | -45.11377 | 2025-09-13 03:47:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 30c7429e-55b4-3bb2-9928-bc0d2c85b4ba | -12.13217 | -44.84472 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8ddda147-25ea-32de-a0fa-67b9f88a5af0 | -11.4893 | -43.62524 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a9fd4d6-003f-3fb0-8a99-1227b8c2e5ee | -12.72099 | -45.07923 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e168ff4e-d4fa-304f-9f3c-40d96cf22492 | -13.13366 | -47.13433 | 2025-09-13 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6de04f9-5ebd-3800-9f77-e3ebc724b0f2 | -17.28068 | -46.10722 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 33141447-ed70-3d81-ad3c-784950aad82c | -17.30126 | -48.74356 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3bd84cfb-7c56-3e39-8edc-6c554ef8177c | -19.90751 | -43.85451 | 2025-09-13 03:47:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dc0c7e24-bb4a-373c-a302-caa31e1d004f | -11.7099 | -46.55488 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9179b908-6fa2-3532-b44a-f7e27bac2b30 | -14.19136 | -46.2445 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 871ba2fc-b62c-34b1-8141-c17710e0e547 | -18.88721 | -47.05307 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44e1280d-cfe1-35c0-99f6-ed43b7123da0 | -9.85123 | -43.14189 | 2025-09-13 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a721842e-067a-3fbd-b1cf-702a4c4730c3 | -16.5599 | -49.22998 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1cca324-8a76-35c5-9533-33740620367c | -13.29329 | -43.77001 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa5c8639-7046-36d4-a553-bed26afcb43e | -20.2599 | -44.18572 | 2025-09-13 03:47:00 | NPP-375D | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 45789337-98bf-3920-a713-f361c982a4d1 | -18.15319 | -49.19364 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 8e9b1c4b-847f-31b4-95fb-0b569df4f95d | -11.18844 | -48.3532 | 2025-09-13 03:47:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15bee6c0-443d-3b85-9f2e-823ca38db84b | -13.90546 | -48.22581 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ca6b223-2ddc-315d-95fd-cff948bee0e1 | -11.80396 | -50.55492 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b63ee63-963f-3592-8be5-8aa2cf02b1fc | -12.12154 | -47.60062 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bfebc71a-92f1-39b7-b13e-7d950edb1509 | -10.71468 | -48.61412 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 005ff598-9ed6-31e1-a764-f57c0a6de724 | -14.17875 | -46.25265 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2befb3d0-4f6d-3813-bda1-9c7bfd2b7714 | -17.31919 | -46.66837 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 479cfbd1-5e51-30cb-878f-3abb8a16a184 | -12.99224 | -46.73529 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01b8b465-41dd-3b2c-98d9-b71d068599bd | -10.77283 | -44.77548 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a75c34a5-a8f4-33ee-bc7a-46d8d63c9da1 | -11.39883 | -43.52938 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc481169-9467-32d3-85a4-654dc4bd82f2 | -19.99322 | -46.90532 | 2025-09-13 03:47:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c8fb731f-94be-3078-91e6-d1ffe64930a4 | -14.19805 | -46.26634 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d9bf8b1-7eca-3e64-bb07-99c775e7b2bc | -14.1754 | -46.26954 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| dfe4ad07-372c-39d2-a09a-c21f034fb51d | -14.26156 | -45.04531 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3b6b301-97b1-3b48-9551-9124a9d39c8e | -14.2962 | -46.06947 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d0b4c456-a667-34a5-9973-6938814e9e13 | -14.21398 | -46.24131 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eacd0bcc-2e45-3090-b7f8-89d6119c4796 | -19.60499 | -44.84102 | 2025-09-13 03:47:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8a0bb8d-c6f1-34ab-abba-1a9010244755 | -16.33803 | -51.54868 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 49ccb288-fb42-3ea6-b2aa-fbfd8190e7c9 | -11.82166 | -50.55504 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4e63f840-d778-3ef8-bf19-4bd97bf0c3a9 | -12.93895 | -48.00106 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 302439fd-1b68-3d39-b870-838d9a6eb370 | -11.42218 | -45.62203 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fb81e3a-0d27-3103-a823-e5a804ff7fcd | -19.99306 | -46.93087 | 2025-09-13 03:47:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31379bdc-4dbc-3987-a1af-fd39725baa90 | -10.77157 | -41.3354 | 2025-09-13 03:47:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f54e1eb-8a8a-3b71-be88-5dec6b944ff4 | -11.41231 | -50.75262 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d77a583d-39b0-3c0b-8d60-c1a6944a9fc4 | -19.9795 | -46.92152 | 2025-09-13 03:47:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf7131b4-d724-348a-ba32-6e1373b9949c | -17.12175 | -48.48296 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64cfc62e-3c4c-3d5f-8786-72ef0af40ab1 | -11.83432 | -50.56532 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9d738a89-9b8d-35d8-835e-223c3dea0286 | -14.17346 | -46.25156 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d10258c5-437d-34e2-9ac3-2a52c751dbc7 | -14.20937 | -46.23683 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d35dea90-cf1b-30d1-99c5-2dcbb8a14383 | -17.3077 | -48.73268 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61a44f16-51bc-3a7b-b513-4d575e1a029b | -11.81843 | -46.74082 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7b91b63-f462-30d0-a347-9e7ab27d3d9e | -17.99955 | -46.94219 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84f80f75-ae9c-302d-9e3f-f9d8f8d4908e | -7.41956 | -44.35601 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b0b5c9a-a57a-3993-9f27-881338886fc4 | -19.26059 | -51.43573 | 2025-09-13 03:47:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53ef789f-8fac-3866-967d-131e2af96a0b | -11.56346 | -50.57762 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12d833b4-4196-396b-98f0-c54dc7fa3741 | -8.48704 | -45.14651 | 2025-09-13 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76734461-f899-35b7-8628-d6b6cacdd358 | -9.01086 | -45.77212 | 2025-09-13 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f06d362e-1e00-3a7b-9a2e-54e5ef41db28 | -14.22085 | -46.28083 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0e2221d5-0e83-30ff-96ca-6ed9a730ce29 | -17.91463 | -44.46235 | 2025-09-13 03:47:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfcd0f58-887f-37ff-9be6-1bad01458390 | -18.59719 | -47.19445 | 2025-09-13 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15bca414-f6e6-3ae4-a179-daffa956338c | -11.15384 | -50.71678 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7402ea63-fb0a-3d91-91ea-0518b50b83fa | -17.99885 | -46.93884 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3697fa3e-15f4-34a8-af0c-7c376aea7295 | -11.85736 | -46.75809 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeeec42a-b5ae-386f-914f-b7d31d6a8569 | -17.28379 | -47.24029 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2446bb94-4655-383c-8844-5d26f1319c08 | -14.70446 | -45.14996 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af4a1dc3-ac51-314a-8319-4b3cbd903456 | -14.34476 | -46.61605 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b1632df-b901-304c-a942-82a110771fb3 | -17.29892 | -48.74493 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0733bcd-bcea-368b-bb48-f57a26c01999 | -10.78517 | -45.99223 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b664ae-132e-31fd-a0ed-c0a4942b5833 | -11.81456 | -50.55346 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fe103f10-6a73-3a72-a69e-999d3b196fd1 | -7.77256 | -43.93895 | 2025-09-13 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README32.md)
