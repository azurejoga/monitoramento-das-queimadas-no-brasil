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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 635c03a4-f3dc-3c77-8332-5eac2390edd2 | 0.68464 | -60.07311 | 2026-03-02 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc84c0dd-45e3-35ce-a991-0ac9133bfdc8 | 1.11699 | -59.20564 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da1ada15-ebb7-3fe8-94ad-1cb7f723b9de | 1.49742 | -59.91219 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e53d345b-e6d2-3229-834e-72088f0af308 | 0.85105 | -60.51181 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e94dea44-9bdb-3fea-b2d6-8ad11252c44b | 3.64582 | -61.03964 | 2026-03-02 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e318a10f-ae6e-3319-b201-8e2363ebc8ad | 3.64643 | -61.04359 | 2026-03-02 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ae92aa5-8bfe-35c3-963c-c95e19ab3d6a | 3.01684 | -60.69421 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cf15a6a7-1265-3738-b5cf-672365080074 | 4.25649 | -59.89629 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95e9df4a-13b2-3c68-bf5a-b872adf23ff4 | 3.41047 | -60.83546 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84826e86-507a-36fd-867b-a7965ddd653e | 3.17069 | -59.91191 | 2026-03-02 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 25358787-6ad5-3cfb-b9f9-965a8949882e | 1.49816 | -59.91695 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 753c46e5-937f-3496-8424-f96fe4e7d1c7 | 1.4936 | -59.91282 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| caffb560-5f48-39eb-ba63-f002c0d33107 | 3.1778 | -60.68751 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f78f311f-8542-3066-850e-2480e3fcf7b6 | 1.51493 | -59.924 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4205df87-7ef0-3e57-9b1a-9e8de409f1f2 | 1.86701 | -60.40138 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9fd0c33-7c92-3120-b342-dc048d1a80cf | 1.08961 | -59.24767 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da8ea844-c3c0-333d-a49b-074c2265cacb | 3.41247 | -60.8385 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48fee65d-a923-3f69-b0c5-863b86b08a96 | 2.8585 | -60.82735 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 108489ab-079c-38b5-827a-5dfd9a1a278c | 1.48358 | -59.92392 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b9a075b-43c5-3659-8bac-59a46ddcb432 | 3.46519 | -60.79195 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a2e1c35-1531-3432-a789-936c0d38bf99 | 3.16582 | -59.90967 | 2026-03-02 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a51003c7-2dd7-3494-af9c-6fe8ebb5828b | 3.45513 | -60.78175 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9c554aa-189e-3779-9ab3-23f7b6bbf06d | 3.88387 | -59.63096 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 432c8dcd-2e3b-398a-8a4b-2f2f6719ff97 | 0.56583 | -59.91022 | 2026-03-02 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c1106b1-31f3-34d5-b724-14e0c79cd698 | 4.25399 | -59.90685 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b7035685-ba66-3b1a-9300-7e1ec1065c97 | 1.20891 | -60.6208 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9cb8968-bc4c-3dfc-b6aa-aaad3c15a1fd | 3.41914 | -60.82589 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d5dd744-306c-3c53-8f3d-ecb8cade6701 | 1.48431 | -59.92859 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7938c9bb-3070-3654-b4d5-f9f06bc2c74c | 3.98825 | -60.08727 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1a95a04-d892-33dc-80ec-bad3807e355f | 1.49197 | -59.92749 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52fec2f3-63b9-33e6-ad60-0314f1aaa8d5 | 1.11567 | -59.19709 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1816532f-4c09-363e-9d8f-591c0701f3db | 3.08072 | -60.00913 | 2026-03-02 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39dc4717-b3a9-36c2-88ba-e2e5a6ae0afb | 0.9214 | -60.52473 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4c107c1-65a4-3900-b297-3f46ac598a83 | 3.16306 | -60.69361 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51446f4c-0637-366e-816f-caea797e7a9d | 1.51569 | -59.92884 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18a0a13a-58a4-3611-85ad-a03ff5010da1 | 1.48903 | -59.90862 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f5435071-7af7-3f2f-aec6-c045108ab6bc | 1.50344 | -59.9257 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5a311940-affe-31e8-8d7a-cb2bd1e6dc99 | 1.50123 | -59.91157 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0c511adc-b3e4-30f3-864f-4ac48cabb827 | 0.05661 | -60.98005 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df53cb29-70b0-39b2-b7b7-444fe4a414a5 | 2.80916 | -60.78135 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea8bcc82-1cc8-3e9a-862c-e0234fa4d6b0 | 3.64823 | -60.27049 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a2dc6b8-a15b-39ce-a056-aade7e1fd7a2 | 3.05423 | -60.66919 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90b0930f-c5d7-344d-b6a2-6645e2e4f70f | 2.85197 | -60.83981 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 60ecc8c8-3e0c-3080-9f1a-42a3e9725eda | 1.52579 | -60.71036 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5456b7ef-0b62-3b9a-bc2b-e83cc36b8617 | 1.07565 | -59.25421 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c118fbd4-90f9-33eb-a24c-e1eca1f93b78 | 1.86227 | -60.39687 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 022dc408-a4f0-319e-b1cf-abfbf626731a | 1.45317 | -60.07195 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18bb457d-66e0-3e64-a62b-416c62453a69 | 4.07553 | -60.33606 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4153a52-aa04-3999-b7d5-7b7671da4620 | 0.69931 | -59.97159 | 2026-03-02 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 424306a7-300e-3859-bb33-fab3a2d531ee | 3.01329 | -60.69851 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f832b6d-8b0d-32fd-8f84-7543515ca4f6 | -3.12489 | -58.12365 | 2026-03-02 05:10:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00eb88d7-3354-34f2-970c-5a33ae7e21d4 | 0.85501 | -60.40684 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32361446-fa3b-398a-8200-055f9fe3eb40 | 0.31313 | -60.44463 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7baf6ccd-59c8-3133-963d-e929d293ba5e | 1.07796 | -59.24509 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27d080f2-6f8a-39ea-a60f-74cb7a8986a3 | 2.8611 | -60.82731 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0916ddab-6056-3052-b7b1-473d934fab89 | 4.37557 | -60.61841 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6a651429-e80e-348f-bcd9-13990cd55f01 | 0.30661 | -60.44738 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9aa7f731-9783-347f-ba4d-88267ac2d2fb | 1.82751 | -60.85067 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75e49627-b3bd-30a5-a0d1-7e6e3d94f442 | 0.23204 | -60.51225 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c37e7ab3-581a-3136-8ca3-cb3fb10ff2ff | 3.93739 | -59.99227 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6ca9e07-c382-3e47-9acb-1d51d6f0970d | 1.49125 | -59.92283 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a62e6045-fea1-31c3-a8fb-d343dfab8bc2 | 4.37975 | -60.61781 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a6c08db-f440-3b44-a96f-ab23bb470ed4 | 1.87502 | -60.91433 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af7a855e-9074-3aa7-a50e-23e439b78eff | 0.70792 | -59.51323 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30aebdab-49b9-3613-9a55-8caa0eb9131a | 3.05509 | -60.66973 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84727668-3a67-3cbf-8d68-ea16071b9e5c | 0.49401 | -60.51762 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5c55d5c-a1ee-332e-a066-b71544ca3421 | 1.48596 | -59.91402 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4218745d-965d-3f00-87a8-61b4693b02db | 1.49667 | -59.90744 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c0ef15d4-4862-3ffd-97db-6863fc6e34f5 | 3.64926 | -60.26939 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc908028-2355-33e3-95d2-6552a74baaa9 | 4.07666 | -60.14589 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0058aeae-9108-33f6-b636-0b84b73b3919 | 2.85792 | -60.82361 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 966411cc-a77e-336b-b1c5-75278f8d014d | 3.41608 | -60.83409 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02dfa1a7-82b9-3ffe-87ea-e4fb8f7f1aa0 | 4.25551 | -59.88963 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45534463-79a3-3692-902c-206851627931 | 0.49714 | -60.512 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60efe51e-17d9-31f9-a1c4-e0ccc11e6a8c | 2.85022 | -60.82856 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7ca522bf-2ad1-3489-8cf8-4e0068c86a4d | 3.6093 | -61.65508 | 2026-03-02 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7bacf1fe-b9e1-35ba-aa00-bc7a45930ac5 | 3.46045 | -60.78875 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e53574b-1423-3024-80c2-29d1cbeb02c0 | 1.71833 | -60.29642 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2f2c481-440d-3fa5-871e-10efae958b2a | 3.41665 | -60.8379 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfee2806-3ec2-3921-8456-46e0ffc872fc | 2.86083 | -60.84232 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f284e85-6b46-35ea-b79e-e859ea38d9bf | 4.2535 | -59.90347 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37a3a0d6-49dc-3a0d-82f1-d724f9b30d70 | 3.0245 | -60.6893 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b67dd98-ecf3-3c3c-ab9c-ffe1c98b85c5 | -1.33289 | -53.21307 | 2026-03-02 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa5a2a4f-aad1-33ac-921a-8119ca599a19 | 0.0979 | -60.63369 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 999e16b3-ba38-399d-8cc4-4bc01486c96a | 1.47666 | -59.9298 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0d69ee2-1e27-39da-a3de-8425810bc3c7 | 0.1886 | -60.44571 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcd8efa6-18be-3489-b778-3c9d6394f0bc | 4.25747 | -59.90293 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8598deb-4fd5-37b6-a10b-4bc59dfbd385 | 0.09077 | -60.56364 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d721404-1d20-35a8-80c1-ece5f118cae2 | 2.84964 | -60.82482 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dbc21e73-a0d4-369f-abe0-575ad8dfcf40 | 3.16947 | -60.68812 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b78c5fa5-cc07-3069-8302-0c206ec0fd29 | 1.48814 | -59.92804 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6e2e4c3-c1c3-301d-9a29-43b6db183544 | 3.88243 | -59.62939 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b46cf98-3168-3633-8975-f00f36a74de2 | 1.49434 | -59.91756 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b5d45733-ff56-3226-b75f-9074a4114b76 | 1.47285 | -59.93046 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a52a805-851f-3909-8c82-863b4b314c2d | 3.41552 | -60.83029 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97167f32-98b6-34ea-a4c5-651eab1b4789 | 0.85399 | -60.40415 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bf26354-5840-33a2-b93a-1e44c0ebb3f6 | 2.86141 | -60.84607 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdb3fd7a-f738-39c8-9b0f-f7d51f9e5d98 | 2.6747 | -60.42263 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e64d4521-ecb8-326a-917b-5a902f5ece4f | 1.51036 | -59.91982 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a2035b42-99d1-3fbe-b013-c4bc971be8dc | 1.87855 | -60.91005 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README5.md)
