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
| 90538a2d-eb1b-3b96-9487-666b7957909d | -15.26713 | -51.48235 | 2025-01-21 05:05:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7773fb94-aaa3-3087-a60d-c421b544c30f | -20.19284 | -50.38231 | 2025-01-21 05:08:00 | NOAA-21 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d06c9438-2b2f-38d2-bf42-5ec1a35862de | -19.04152 | -52.86009 | 2025-01-21 05:08:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7a7e2bc-0184-3c69-9897-d3c53868b7d3 | -21.57349 | -53.80132 | 2025-01-21 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 34b83776-e49c-3938-b594-914a35853e05 | -21.09621 | -56.27522 | 2025-01-21 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b364b0f8-24cd-368b-a82f-09d95c410f80 | -21.56895 | -53.80455 | 2025-01-21 05:08:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ea145318-88ae-3d71-a4cd-9fa28f7f73f6 | -21.09563 | -56.27948 | 2025-01-21 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67b2d3c7-7f65-32b8-90aa-3397e2c20075 | -20.80265 | -47.2848 | 2025-01-21 05:08:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbf3fb95-1e7e-3ec8-8bed-76f545844950 | -20.71633 | -55.38132 | 2025-01-21 05:08:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88df7c6b-224e-30eb-9fa4-3520238da746 | -18.99517 | -51.37304 | 2025-01-21 05:08:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b7a7b5b-a894-32a4-81eb-bc4685df7ddb | -27.52863 | -51.46085 | 2025-01-21 05:10:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3dee87d6-c590-3f9d-89cf-94e5b5f30b23 | -29.63836 | -54.16952 | 2025-01-21 05:10:00 | NOAA-21 | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| f7e008ba-fc4e-3661-b4fa-2f724dc95f51 | 2.62495 | -61.45858 | 2025-01-21 05:50:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7612962e-fdb4-3f28-94ae-2ffd2b37c0ad | 1.0111 | -59.51711 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec796feb-a542-39c7-9aa7-d1f3d623d745 | 2.17165 | -61.82243 | 2025-01-21 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 975eb7a4-f255-303d-bc9a-07278ac99027 | 2.88459 | -60.76873 | 2025-01-21 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99180ace-6c25-328b-9942-6999345db563 | 0.70797 | -59.68912 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89ac4ba5-2cf6-3f3e-8c97-36db30ff37ed | 4.51293 | -60.67973 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e0c1802-a6f0-33ba-bf92-fdcde903fe6b | 3.72724 | -60.64566 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb76455f-b41b-32a3-b937-f9c7fb5e7b2f | 0.70329 | -59.68986 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc169369-c1e8-3748-b253-5dc5dcafe3fe | 4.59099 | -60.72449 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23ff3e14-5a9e-3035-bcb4-768d822baef8 | 0.81078 | -59.89791 | 2025-01-21 05:50:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4b6a7ba-4573-30e7-b22e-23d478d8f9b5 | 2.62584 | -61.45852 | 2025-01-21 05:50:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 495499d4-018e-32a5-b184-a30cfac50d02 | 4.51618 | -61.05151 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 113d2b0b-e1a6-3067-9790-d7265dde2839 | 0.92961 | -60.3294 | 2025-01-21 05:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26ccd755-09d3-3eeb-9b58-bda11d67898e | 3.60037 | -61.41886 | 2025-01-21 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42cb97e8-4d55-33d7-97e0-95fcdd9f9b25 | 1.13926 | -59.55079 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 252f186b-bd1f-305c-ba5c-8f147193e59a | 2.82766 | -60.8751 | 2025-01-21 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7b728a4-ba4b-39ee-a7b1-1a5905fb6173 | 0.81974 | -59.95436 | 2025-01-21 05:50:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c8dd4c-4499-3448-b597-ae7db9e3a638 | 1.10377 | -59.70416 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b1963f6-4f1f-34c5-84ab-5da365a2168d | 4.07514 | -60.38924 | 2025-01-21 05:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a69da13e-4f8f-3326-bba1-2f0f75e1cfde | 2.82349 | -60.87577 | 2025-01-21 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f8a1db6-166e-3756-a4bf-34dc256d8c65 | 2.15721 | -61.01364 | 2025-01-21 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a0dee0f-f961-301e-a96e-4224d6b252be | 0.90087 | -60.43687 | 2025-01-21 05:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf00679b-15d8-39bd-b040-1e61809549b4 | 1.13677 | -59.54874 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a6e734b-0495-37b7-a11a-d6a97957220a | 0.76312 | -60.01121 | 2025-01-21 05:50:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f92b1fd-fbb6-3f1f-8895-a96f222b90ff | 3.60434 | -61.41822 | 2025-01-21 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89ef95cb-57f6-3a14-b9c2-3f8d593501e1 | 3.24668 | -60.54487 | 2025-01-21 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd07d42c-610c-35b3-90ac-8ac9bcbda556 | 3.22548 | -59.89825 | 2025-01-21 05:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d983321b-022d-3df6-b7dd-3e1d6c2ffa81 | 0.89377 | -60.0927 | 2025-01-21 05:50:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a10dbf7-a6e8-32c6-8656-4a550afc6424 | 2.80877 | -60.91706 | 2025-01-21 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b95e6ab-abb3-3c97-b41a-2dfcbe195d85 | 4.51677 | -61.05503 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bec2294-bdf5-304a-8e47-8d68fd4ddf4b | 0.75286 | -59.65421 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5e0c746-7875-3ccd-a2fc-8231ae510667 | 0.74792 | -60.03568 | 2025-01-21 05:50:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90ab6f2e-ef0d-3e2b-989b-df6a395856f4 | 1.14395 | -59.55001 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b296bee-9664-39da-bb66-6c316b97c828 | 0.88444 | -59.40251 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a411c22-ad8e-3867-84a0-4aac55d4f8af | 0.94009 | -60.42627 | 2025-01-21 05:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de347eba-d65f-3831-87ba-6a9cb8a91cc6 | 0.70527 | -59.6868 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8990a844-bef0-31f4-bb69-3c072becb43d | 0.7633 | -60.01416 | 2025-01-21 05:50:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6da4dabe-6339-3a89-abf7-e39e9409ae2c | 2.82949 | -60.88652 | 2025-01-21 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30edd161-7ef4-3490-9981-e1780b4234e1 | 1.16154 | -59.88964 | 2025-01-21 05:50:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 808370f5-a9af-387e-bd98-8002b5bbd5de | 1.00975 | -60.58415 | 2025-01-21 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b2336b6-c2bc-304c-a98c-15d83f2bf464 | 1.00908 | -60.57995 | 2025-01-21 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd916a43-b051-3046-9a47-3c277205e31c | 2.82827 | -60.8789 | 2025-01-21 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93616bb5-84cb-317f-9958-5d3291348e89 | 1.35699 | -60.02432 | 2025-01-21 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce986a77-162e-3ae9-9f5c-0b20bff557a9 | 4.59508 | -60.7238 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b019538c-2db1-38d7-98c2-e986a2592285 | 4.07577 | -60.39316 | 2025-01-21 05:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7684f569-49fb-3879-b6d5-f7170e72aeba | 3.60775 | -61.41415 | 2025-01-21 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f78ee5dc-3cd5-31d3-bae1-e24c9da29b90 | 1.01451 | -59.51712 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c048476-064a-3fe4-bf52-4899b547d3f1 | 0.86474 | -59.61938 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fd9e7b5-06a3-34d8-953a-9870495f8692 | 2.18367 | -60.25923 | 2025-01-21 05:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| becd67a0-6a7c-379e-bdf9-aec63ebfb5bd | 3.91736 | -60.83499 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5f2469f-66df-35dc-998a-d5f576088634 | 3.83619 | -59.93857 | 2025-01-21 05:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36e4cd91-cdce-3fa5-bc82-4d3246251eff | 1.12582 | -59.4088 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4890102-8c6e-37f6-84c1-a8c513c884e0 | 3.56185 | -61.08641 | 2025-01-21 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2182f47-fafe-3b3b-8375-797c523beb66 | 4.02391 | -60.82302 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 287faac3-5be2-3b9f-b038-8ec65d668c9e | 4.07523 | -60.38965 | 2025-01-21 05:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58d6d651-a226-3568-a109-60fb9d71854f | 3.4242 | -61.11142 | 2025-01-21 05:50:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00a7544c-e3f0-3244-8081-7bbc17915f88 | 4.02454 | -60.82692 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 156fd974-a596-381f-9fe6-45df4aa4787c | 0.75206 | -59.64922 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fa97080-f182-3869-99fe-f4d858253b82 | 3.91677 | -60.83132 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ec5b97f-10eb-3a76-aeed-925acc039535 | 3.6026 | -59.97173 | 2025-01-21 05:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b049d0cd-1db8-31b3-a8e5-bf6767ad2035 | 3.73638 | -59.99076 | 2025-01-21 05:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46a960aa-8ba2-3261-85e2-ac9a7ad13c1c | 4.80962 | -60.29543 | 2025-01-21 05:50:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 660f059b-183a-317e-82c4-867fbd809b82 | 0.75676 | -59.64852 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29198006-3df0-3f95-b42d-b600e9ec5568 | 3.21732 | -59.90406 | 2025-01-21 05:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d6409bd-13b4-36a4-8842-5db1352af840 | 3.72306 | -60.64633 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99cb57e9-1ee1-3fa3-9235-a44ceca01d9c | 1.13457 | -59.55153 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d2d3dca-f237-3de5-b677-c0fa901cd9ab | 2.82888 | -60.88271 | 2025-01-21 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d83fb87-a07c-30a6-8da6-b854cccd0e69 | 4.15112 | -61.17029 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 636dcc23-e249-3747-855b-1f037d0fb7c6 | 0.70606 | -59.69163 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12e35a22-4aa4-3540-a0ae-0f6ac9514509 | 0.92515 | -60.33011 | 2025-01-21 05:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 498d54d7-c1bc-3f07-a1ca-10a505066afd | 2.17082 | -61.81734 | 2025-01-21 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b4a3d51-2435-3305-a5d8-da379ce89e3a | 3.83544 | -59.93403 | 2025-01-21 05:50:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2a4b80d-75c2-33e7-b9e5-bedf435ef0d8 | 0.68142 | -59.70342 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53ca539a-aa72-35a0-9535-41df78634801 | 4.51233 | -60.67606 | 2025-01-21 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e3bc620-ddd5-3eec-89f3-a4d0481e4c87 | 3.22175 | -59.90335 | 2025-01-21 05:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7eed22e5-8435-3543-befb-f9847544b6f3 | 0.86558 | -59.68463 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 477d7e7b-2013-340d-a7b6-6ef74cff7df9 | 1.13755 | -59.55372 | 2025-01-21 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15e6f1ac-9369-3878-a2b1-259b19c43a0e | 2.18187 | -61.8103 | 2025-01-21 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 667ad11c-36e6-3b36-8098-2a10f04f2ce3 | 0.19585 | -60.62025 | 2025-01-21 05:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83236d4f-e344-3bd9-ac77-f1e4bda8c35b | 0.46515 | -60.44407 | 2025-01-21 05:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3a413fb-5e98-3d65-a39c-4155eb0f6cf1 | 0.19518 | -60.61591 | 2025-01-21 05:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 231a2be0-b9d1-3401-a104-1787693de14b | -15.39 | -43.78 | 2025-01-21 12:00:00 | MSG-03 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66a7725a-8c4e-3dd9-abc9-a8b8d2d0a213 | -15.42 | -43.79 | 2025-01-21 12:00:00 | MSG-03 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9c7dbe-3d60-3020-b22a-2539df94d481 | -15.73 | -45.95 | 2025-01-21 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b985e4c0-520f-3160-a22a-4149b4adc74c | -15.76 | -45.96 | 2025-01-21 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 293abc56-3bf4-38b3-84ec-a36ed10617a1 | -5.57232 | -35.736 | 2025-01-21 12:21:00 | TERRA_M-T | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 26db5311-2225-34d3-b533-ac144cdef66e | -5.34825 | -37.0829 | 2025-01-21 12:21:00 | TERRA_M-T | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 20.8 |
| c6fdffc3-d19b-38a8-a4a5-68c25e4208fe | -13.21574 | -40.49252 | 2025-01-21 12:23:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |


[Clique aqui para ver as próximas entradas](README5.md)
