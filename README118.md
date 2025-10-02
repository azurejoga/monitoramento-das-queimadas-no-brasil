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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d08284f7-088f-3957-9d6f-d67f57d0f404 | -11.44257 | -43.89362 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70dfe5c8-b509-3ae5-9a61-0bb0c4c28237 | -12.27792 | -45.36797 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25e5e411-0e18-330d-9ad6-27ef614fe610 | -11.82634 | -44.99984 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5906ca2a-0247-3b6d-8971-4e4df802688b | -14.31574 | -45.88546 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2efafa0a-6f98-367f-9af3-88e5bb67c8f5 | -14.48031 | -48.43454 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 03097292-1df3-3dd7-b39b-92a5cf53158b | -13.32237 | -47.2103 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 405772bf-710a-301e-8774-d023118c7680 | -14.89705 | -47.18262 | 2025-10-02 04:51:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecb8d71c-5484-3c73-a389-8b5f4cdeccf7 | -11.81918 | -45.01499 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f071dfc4-c2ef-37ae-ac71-0bd274179096 | -12.65695 | -46.94273 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b91b373e-b4e2-3373-b5bb-1f31469a66aa | -10.9967 | -46.54432 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6de640c8-7b04-32b0-b628-05c2fbb3ce91 | -10.96378 | -46.65048 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 735739a8-30fc-3922-b264-4145ec24b66f | -15.99859 | -50.90929 | 2025-10-02 04:51:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ce60db17-794b-38b1-b5f6-2f6f0da81cfc | -14.31445 | -45.97717 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0328293-1834-3dba-a190-6a6319eb5851 | -11.19914 | -47.76985 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5521b58e-1e88-38e5-ad82-63c04737a57f | -12.24225 | -47.82917 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e70f8420-4a85-3300-99c1-1d0376e7f662 | -11.817 | -45.03225 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b07c8ae9-7180-35a7-bdc3-dca419c80811 | -9.57899 | -47.08201 | 2025-10-02 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ee8739a-7068-3c06-8ea4-b5ed82e14487 | -14.48504 | -48.43143 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 247e7f04-5448-323c-8c7e-1a148ff3a0e7 | -12.68208 | -48.57534 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d2ede42-52f3-3925-9497-9b00f42eee49 | -12.70563 | -48.5864 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c4e6d3fb-aa3d-33f9-9166-f49476fa4a4c | -12.89079 | -46.90339 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b01f887e-1c54-3e83-8f39-ac8d3424b2c9 | -10.25715 | -50.31791 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f7f3480-707d-3140-9fcf-256ddf069aff | -14.31378 | -45.9828 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a98f36e5-139f-3f2a-8c39-8f592904c178 | -13.75904 | -47.95972 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b42f8a56-276d-3859-b87f-b50b1fe7473d | -11.79798 | -44.97455 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd4a60a8-0bae-3dc0-834b-99a1a85b29b0 | -11.66803 | -45.32268 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6a684c8-c989-3821-a37c-0ef17a249a6e | -16.0447 | -50.87899 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a227eea6-21d7-3f2b-9551-85b82bb1d0b0 | -14.41306 | -46.1332 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9874d04a-e568-38fb-b51a-27bb374d26dc | -11.10201 | -49.80433 | 2025-10-02 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46ce3716-21bf-38e6-97e9-37275721ee28 | -11.80972 | -47.58686 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d269863e-0778-337c-8ed4-c624a5c3e6cb | -11.44262 | -43.50198 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2b974dc-00d6-325d-8bfe-a8d390e6a3d8 | -16.06965 | -51.01065 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| efd27026-cb76-35be-9ba6-eaf4273de5b4 | -11.70512 | -44.30793 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93d41f0d-9587-389a-ab03-351f58a4a760 | -13.85912 | -51.24797 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5642574-b753-31a4-b0ad-cd6866ce988c | -13.75856 | -47.95179 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00ad1a9d-eeac-38b2-b464-3747f0889e53 | -12.26228 | -47.81067 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| da52ed46-bfc6-3bb3-ac43-a5ad3c62f31a | -14.42605 | -46.35742 | 2025-10-02 04:51:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2c2e7be-9bc5-3e68-b506-6f223517c974 | -16.13632 | -46.68486 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 590d2906-855b-3c68-8cd1-03ad80e4d4a1 | -11.73668 | -44.42773 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 535cc39e-59d2-3b41-b5b7-291f26924163 | -9.92832 | -43.76186 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 163e90e2-3943-3c89-be8a-72dfb0b0d056 | -11.47876 | -45.00605 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91ab3fee-bc89-3305-8ca6-45e9315ff423 | -14.40922 | -46.11373 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e8205ac-c2c9-31bd-bc7a-efaf1cfb4899 | -14.3039 | -45.89846 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e94e7ce4-bcd8-3d7b-a645-1b4c4ce00255 | -13.35151 | -60.92255 | 2025-10-02 04:51:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3db1c94-9752-3240-ba63-7c237da57b05 | -10.22178 | -50.33379 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd85c6f0-47bc-33fc-95de-89b4edf275de | -10.66393 | -48.59461 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 231fa8d0-f534-383e-abcf-c2b8991966fb | -14.97937 | -46.92273 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6da535ae-2861-31ae-a23b-55fa90e1c2e8 | -12.38329 | -53.38882 | 2025-10-02 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93157a0a-ef32-3313-8cb6-ace541e84844 | -12.59076 | -49.89963 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6a63a52-0743-33ab-b538-7352da0b1408 | -11.87214 | -45.01129 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 038f6203-1d14-39c5-853a-f9bd64eddd19 | -13.51998 | -47.26244 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2b7533b-4281-3859-91a3-cc9053749663 | -11.59501 | -47.21597 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8015ee5b-931a-3419-8410-9b3b49aa1f51 | -15.28687 | -56.7835 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e0fab35-50fb-3076-8c8b-37c51984db7b | -9.92581 | -43.64906 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0b8e2ca-eb6f-3cda-93e5-a3cf4b051fce | -14.86478 | -48.39465 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ada0812d-77a3-3633-9c92-10505dfbb0ec | -11.48059 | -45.1152 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a59daf88-cc8d-3523-86be-d1e5619b2391 | -15.1725 | -43.62642 | 2025-10-02 04:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a61f7b4d-f5a3-3cd2-91a3-bb7c95114d00 | -13.70292 | -48.61921 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b53eb3f4-1cb4-3aa3-8816-a2957d6bacdd | -14.48296 | -48.41426 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8c0cf3c-4f7f-3b6c-8c95-9f7569a1d3d5 | -16.0486 | -51.02623 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24bcf91d-a365-3e5c-9959-9cdd48cfbbea | -11.8466 | -44.96446 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6709a4f-578a-3db7-a0e6-112598891765 | -11.81046 | -45.00088 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43f600a8-6e84-30a2-b625-498be944355a | -10.64951 | -48.50918 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e5b9c20-54a4-36b3-b363-e9d8a57530d6 | -13.75531 | -47.9543 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7eff4e6e-6750-3379-97c1-b579c2a55b39 | -10.82697 | -46.62227 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4dc06c3b-fa1a-379d-8bb7-ba7884a5a547 | -10.71071 | -48.58017 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e644b2fb-b1de-3b57-ba17-ee1d7e3b6d8a | -12.07706 | -47.83666 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 233b6066-6fbe-3840-b086-755bee486046 | -15.36334 | -56.97478 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e751ebcc-a5b2-3a91-bf9a-bb28f714876a | -11.07761 | -47.80822 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f568c379-fb04-3f96-819e-10b68276f62f | -11.47596 | -44.98671 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb861ae8-18c7-334b-8f3e-ab5068b68f57 | -13.55937 | -47.2874 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a684a83e-8f9b-3f63-9136-04a9d6c84910 | -16.28936 | -45.24414 | 2025-10-02 04:51:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e28d8dc5-3b41-3708-9382-e334753e9a36 | -14.36285 | -45.95516 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cacfcbb-e28e-3f98-be32-a5addf57d86d | -12.83422 | -46.87318 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee4f5067-7800-309e-9257-1d5fb7054db8 | -15.27578 | -49.30737 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11eae17d-131c-3114-a60d-2d12e9a6203c | -12.80671 | -46.86839 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 380a5fb6-2d38-3336-893c-2f59fe8f65b8 | -10.27387 | -50.32891 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7322126c-06ad-3108-944b-86a0cf21a514 | -9.94692 | -43.70319 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf0f2fc1-923d-324b-893a-86a82d85b3c3 | -9.64939 | -62.84623 | 2025-10-02 04:51:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f29f532c-81fc-3035-b3ae-1b1f538c53d0 | -14.10597 | -45.64481 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fee5992-ec4c-3bd2-ba41-d7388b4d14b4 | -9.93457 | -43.71255 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecd77746-b860-3036-b7aa-8c77a9d72614 | -14.4713 | -48.404 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c4939d0-a03e-337b-883f-d5b368dbab13 | -13.2874 | -47.25751 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf3d582e-1ac3-3717-ba0d-3e23c13420a5 | -10.82629 | -43.66737 | 2025-10-02 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4b3ce63-13f3-342a-9c05-cee451d69ab4 | -10.21819 | -50.33325 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0fd2d81-3fdc-35a0-920d-f1f1b0b7c6b6 | -11.17331 | -47.18836 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecebe2be-54b3-3e33-b95c-cc7bd2268723 | -10.99811 | -46.60284 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| d6de0a7e-88b1-30fd-920d-fa81842d8626 | -15.1422 | -48.02173 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e32767a-3e7c-3326-be43-5a963cdc1c4e | -9.931 | -43.74068 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 2fc5cd3f-9108-32b2-b148-c7cd1dbc85cc | -14.87268 | -48.135 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09fb609d-6df5-3bbd-b9a5-d0b17d556e52 | -12.70258 | -48.56995 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be1a139f-42bb-3cfa-b256-de2098cc471a | -14.40997 | -46.10784 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0f3ed935-679a-3249-9538-d469c9a023d5 | -10.26965 | -50.33252 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8166e2ca-6843-3b51-8785-3103dce9a38c | -12.81532 | -46.90765 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 812f1587-8b57-3de1-9c90-6b66ff57a159 | -14.9854 | -46.91275 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e742bd76-0587-3ef5-aa86-9b9e7d0ba2eb | -11.2652 | -47.8232 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6d41481-490e-3efc-b803-5d75bd9bc05a | -14.35646 | -45.96599 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03b2ca4e-86af-3c64-abc1-d568f7ffbefb | -11.80013 | -44.99945 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94e22dd8-f53b-302f-9d2f-4651723e64fd | -13.80362 | -47.51675 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf6a07cf-88dc-3399-985f-606d875b3fc7 | -14.42341 | -46.12125 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README119.md)
