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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d84bb8cb-77b0-3f23-9600-10d1ee888708 | -3.07998 | -54.24856 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 300340b5-36f0-355c-9816-8356488c2952 | -3.65764 | -60.62694 | 2026-10-07 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad2e4e22-1e18-36af-b0f1-0284a7c9b1b1 | -3.01002 | -54.13159 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ba3d056e-6591-31f0-aa9a-591047121436 | -3.06489 | -54.25252 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9fcb89f-23aa-3c6a-ad63-cdf82436e927 | -2.15178 | -59.22528 | 2026-10-07 05:59:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a16f7bd4-3142-38d9-b6ec-4c8db3ace7c1 | -3.67965 | -55.95388 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7d21a74-ba79-35e2-9ce3-51fdf49581c1 | -3.07191 | -54.254 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ad4b3d4-52bc-31c0-b5cf-7ff88a645853 | -3.10182 | -54.27766 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3fb4da83-4f5e-38d7-8ae8-885058ebc86c | -4.44436 | -54.97993 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e922ad9a-eb8b-30dc-a840-0291518a1fff | -2.93846 | -54.14972 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 42ea2011-8b11-3b94-b85d-7d6495724623 | -1.28063 | -54.56273 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a59d223-7326-3380-aeb8-e1aa69721245 | -1.12376 | -54.12365 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0d1c9e2-251c-3642-86af-712708dddebb | -3.54644 | -59.47941 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e15181a3-6979-37ee-b061-bd572ca52821 | -2.30529 | -57.08975 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4864966b-dd85-3f8b-bc90-76c552abf4c2 | -3.3543 | -59.50246 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee359a94-17da-34ad-82c1-fb815ae40ef7 | -3.01281 | -54.13947 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f8319a00-015a-33d2-9520-9162d8428528 | 0.79211 | -59.1999 | 2026-10-07 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03a84141-709c-3284-8ce2-a55e07b230b4 | -3.38592 | -58.20766 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a5806c1-fe8a-3e58-8048-3b156a46fc5b | -3.98619 | -56.22511 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f155de0f-53e4-30cf-a3ca-10a46795e062 | -4.44399 | -54.98178 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 408c28ab-759b-3804-8b54-adbaaec89c42 | -3.34172 | -59.48201 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad44dace-8ee0-3baf-ba70-502c3d2ba098 | -3.00671 | -54.13158 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c34c5ff-b2f2-382c-ac4d-8b65ede86227 | -3.67318 | -55.953 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5075fc9e-f2ed-3b37-ab82-9188b73297a8 | -3.66307 | -60.63033 | 2026-10-07 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 53125e7f-b51c-30eb-b4b3-46f2ed7c6c48 | -2.77279 | -54.0885 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c18b7333-ba9e-30bf-9fb2-cd5d28a30d8b | -3.56396 | -54.48135 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 477c00e9-7192-36ad-8487-7d3f32a07475 | -4.3783 | -59.90612 | 2026-10-07 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d620b880-12ec-3e4e-94cc-dfd85d803d44 | -3.65832 | -60.6296 | 2026-10-07 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bed66d6f-1f80-3021-af32-7692cd15fe57 | -1.28282 | -56.98348 | 2026-10-07 05:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bbf5e69-1b3f-37b9-909b-bf0e259a00eb | -3.89096 | -59.32883 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7afa3b29-47b2-3ae9-9c4b-f1623e3a0aef | -2.13467 | -54.80535 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3d04d34a-40e7-3b74-bd6d-3a814ed168b3 | -4.15713 | -55.15887 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc04e6e8-ab4f-3852-8c15-cc8a69b47ec2 | -3.56137 | -59.48473 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8822045-312c-3943-a134-de9068db8049 | -3.09079 | -54.30395 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 46e46f68-754d-31b7-afdb-b7451a125955 | -2.52377 | -58.09831 | 2026-10-07 05:59:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 863bd510-9486-31af-b8d2-99993d99c286 | -4.44521 | -54.97403 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 067c8c79-855a-300e-8583-97667dcb79d0 | -1.28106 | -54.56964 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 79666257-4ab4-3bad-9863-85a3b564013e | -3.08472 | -54.29597 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8de36b11-bbd7-312b-abea-45a97f674eec | -3.73433 | -59.44719 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39ea12e1-84b3-3f64-8059-0afa382bad3c | -3.49853 | -54.65227 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68ba784d-f4f5-3de6-b298-1e5b0a2d6f41 | -2.86879 | -54.15117 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75284a4a-b63d-34d9-a99c-013ee8e0dd94 | -3.10162 | -54.17863 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bad758e4-48ae-3563-87f1-bbc84eda412c | -4.15145 | -55.15784 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 474484b1-66fb-31a0-ab27-106ae1d37a91 | -3.51142 | -54.66146 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10af846e-882a-3add-8f13-028a3f27ae03 | -3.84651 | -55.99404 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fd60d4d1-e32a-3e2a-a381-3b78ad58fb84 | -2.78875 | -57.6574 | 2026-10-07 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ce702fc-6352-3b91-b89d-1457fbcff3f6 | -3.47754 | -59.46837 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ea8ed8b-60b4-3dfb-a331-c0030e918750 | -3.08355 | -54.25382 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd230603-7ada-3c46-ae68-121c5e5ae5f9 | -2.49444 | -58.06769 | 2026-10-07 05:59:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0f990b5-21fd-3d9b-97bb-68ce1b71e328 | -9.34329 | -64.71219 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfb27f20-9a91-31b1-89a7-a1cc8e11f1c2 | -8.629 | -67.05272 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bb3a5711-8daa-38cb-9296-dd890cac4991 | -8.18908 | -70.10607 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b72934f6-b855-358b-8cbc-fe3849c1ee6e | -8.62375 | -69.98106 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbad3915-c3dd-358e-acf4-79a888e9c630 | -9.13676 | -65.41437 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad63971c-cf1f-3843-862a-73c01dbb7e0f | -9.75262 | -65.06242 | 2026-10-07 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e938ec2-28d4-30ed-b216-7cde16253c6f | -9.01458 | -68.34964 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd1076fe-be69-3340-b7d1-fa4611b030e1 | -8.84168 | -66.78659 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8873f2f7-c472-34f4-a6db-271085e1cb50 | -9.08677 | -67.68095 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f87d194e-c3ee-364c-9215-e0ba93b205d8 | -8.15165 | -64.07258 | 2026-10-07 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33105401-54c9-3d61-8a76-1dde58a95282 | -9.457 | -67.09013 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14ac5eb8-39b8-3277-bc9a-27b4ee5b0872 | -9.49886 | -70.43904 | 2026-10-07 06:01:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0a5cb86-43e8-3f3c-a944-ff3b5586dfd6 | -9.47746 | -66.79053 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b875118-e0dd-3255-85ed-4f5c7615a072 | -9.43792 | -67.099 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc01f003-0a0c-3eb1-b93b-f11b9af999a0 | -7.88684 | -72.35773 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d2aa0ebd-885f-334a-8e56-c057fcd93781 | -9.09693 | -67.68253 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29f189e7-658f-3e09-94d5-4af589b4ff00 | -9.3309 | -63.67599 | 2026-10-07 06:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62f4da28-0750-345e-9bf8-deca9eb9e93d | -9.40294 | -67.60172 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9f0e349-328b-38b4-a68f-217772185782 | -10.24371 | -68.30437 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fba27279-bb43-3ab8-97bf-c1c222342058 | -10.03486 | -67.75062 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5edc3982-c9b0-3596-9e03-c59bad679db3 | -9.146 | -65.29877 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cbaaba4-41f7-3f20-b72a-442134af742d | -9.46105 | -67.08682 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c3cca08-b452-30f5-9b77-d7458f6b7caa | -8.46618 | -70.83999 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daffbf2e-b664-3d22-9ce8-d6026c1b40af | -9.49209 | -66.78874 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b9806a1-d86a-3c2c-b92a-364378917a77 | -9.10587 | -65.36314 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a7f8f598-7fac-333e-b9f7-e630aeef8301 | -7.53112 | -70.03325 | 2026-10-07 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fcdd596d-251d-306f-8ce0-b216d3acb687 | -9.48681 | -67.67094 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a321641-59a8-30b7-b200-8e3454a292f5 | -9.43329 | -67.10615 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ba7c086-a7a1-3161-806b-05f596416d9a | -9.11399 | -67.86389 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8953df70-e36d-3070-a8ad-48daaa32359c | -8.38065 | -70.82966 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52600910-3098-3bac-9a71-e28459cda0e7 | -9.11792 | -67.8608 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71ebf8a1-1a8b-3706-98ba-682d705f2fe7 | -10.61342 | -68.67705 | 2026-10-07 06:01:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aaf5cb0f-dd79-31e2-ae51-896234927f67 | -9.42239 | -67.75117 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5e176bf-5e64-36d8-92eb-34148bfc70d6 | -7.82104 | -72.71149 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cb05f57-8913-38bd-b8af-81eda4d94643 | -6.92449 | -71.47992 | 2026-10-07 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb7f22f9-0371-3343-9267-95aadbdd6ea1 | -7.82716 | -72.51328 | 2026-10-07 06:01:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b585b7a9-e7fc-3da1-bd31-89e2676e97e2 | -9.44702 | -68.40713 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 098ba7b5-e2ff-30a6-a4ed-5f237a657d46 | -8.97852 | -65.44374 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 155e4310-a128-38d9-99ce-de2767049f64 | -8.51422 | -70.59272 | 2026-10-07 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15f5fa08-f092-3082-b00a-29c7b67a5a4e | -9.07157 | -65.48534 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ef8a005-8b1f-39dc-a566-451948025f0c | -10.03826 | -67.75114 | 2026-10-07 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 382ec4a5-84a5-3b09-b03e-c09b1e883f36 | -8.6291 | -67.05789 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dcf9d172-6619-3055-8bc5-e22bcad472ac | -8.97479 | -65.44317 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 343c0422-683a-32f0-9616-ab4b99be3309 | -8.20713 | -71.01106 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a30cd81f-bc19-31b6-9864-71af26049ac9 | -9.14223 | -65.29819 | 2026-10-07 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc9ca27-a953-306c-8a0a-4042158723ef | -9.11388 | -67.70762 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0618df9-693d-30d8-8da8-8c231f80717c | -8.91462 | -68.87989 | 2026-10-07 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 268c82fe-59ac-38e2-8fc2-6c8f5c21b24d | -9.39538 | -68.3479 | 2026-10-07 06:01:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 059c3400-b9f1-3d61-8417-a5187657afd7 | -8.16385 | -70.99624 | 2026-10-07 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 123f415c-c598-314f-a76a-271304968f53 | -7.81732 | -72.71086 | 2026-10-07 06:01:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 691ff453-b540-3064-b326-64da6f30fca6 | -9.271 | -67.87333 | 2026-10-07 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README120.md)
