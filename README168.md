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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 420c619c-f98a-3943-907b-97bc6090d5d0 | -7.02483 | -35.19429 | 2026-10-10 15:39:00 | NPP-375 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 9fb042f2-80dd-3d9b-8f47-c52a20cdbba4 | -7.78875 | -37.78662 | 2026-10-10 15:39:00 | NPP-375 | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 15385a2d-827b-360a-b04a-d2bad90652a7 | -13.37319 | -40.89889 | 2026-10-10 15:39:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 58c152b9-3698-3f8c-9761-2ed18599a92a | -7.17178 | -35.41579 | 2026-10-10 15:39:00 | NPP-375 | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f803f975-cd1f-330f-b4d2-1a46527d30bc | -14.52465 | -41.47542 | 2026-10-10 15:39:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f8d20385-cc85-32e2-be7d-94e4f7cacee4 | -8.83493 | -37.06595 | 2026-10-10 15:39:00 | NPP-375 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f34b3d63-d81f-3813-b141-f94bf7a149dd | -13.99524 | -42.4558 | 2026-10-10 15:39:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 47.0 |
| 0e195a87-8ce5-3f6b-8833-b0091a2b7d84 | -12.49258 | -42.21661 | 2026-10-10 15:39:00 | NPP-375 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 38.2 |
| a26abf4a-8c4f-344f-8b99-d000c0ed9190 | -7.69264 | -38.64076 | 2026-10-10 15:39:00 | NPP-375 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4a0ec589-7158-38ba-b697-f0e5c342b6f7 | -13.72871 | -42.31862 | 2026-10-10 15:39:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 56.5 |
| f8ce9011-0b68-33a9-8e2d-61edfb46ce82 | -7.98661 | -39.58841 | 2026-10-10 15:39:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f4ba2109-7e19-3704-9808-8450e8795e85 | -8.78401 | -41.12134 | 2026-10-10 15:39:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 106.5 |
| bd53a84e-9775-3683-8644-ee36d44aa12a | -11.28434 | -41.80204 | 2026-10-10 15:39:00 | NPP-375 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 4327a13f-bd0f-3e71-b907-944a253c2ec3 | -15.05596 | -41.81132 | 2026-10-10 15:39:00 | NPP-375 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 96.4 |
| 96465f3f-e51f-3675-969f-a2929fef6b12 | -15.2325 | -41.54962 | 2026-10-10 15:39:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 34.5 |
| 1d0a1d52-f635-38b3-ba7b-6ade9ac30c82 | -7.90582 | -39.65062 | 2026-10-10 15:39:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 89187fea-0be4-3694-b812-8d4b64b90b62 | -14.75157 | -40.96601 | 2026-10-10 15:39:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 856eadd2-ebd7-3278-8e03-0e3cb6fa1d45 | -8.23203 | -40.57574 | 2026-10-10 15:39:00 | NPP-375 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 40e2ef79-3146-3dd9-9a33-3f42e16f656b | -12.03057 | -41.79784 | 2026-10-10 15:39:00 | NPP-375 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 96327f42-29b3-3cc2-86d3-3daa81d8ad21 | -13.59687 | -40.71133 | 2026-10-10 15:39:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caating | nan |


