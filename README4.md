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
| 56bc9489-adb1-35de-8b4f-44b72777ab2e | -8.60031 | -39.542 | 2024-12-26 03:59:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6264d5d5-c3a1-32b3-a232-305e30630d39 | -11.41529 | -42.54654 | 2024-12-26 03:59:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 315a6c79-59f0-358e-9cc1-bc425060c4bd | -10.14075 | -42.16675 | 2024-12-26 03:59:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3739bacf-61ba-3a5e-abb0-616277ea2923 | -9.98215 | -44.75529 | 2024-12-26 03:59:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c9d7a34-eaba-341d-834a-bf65156ab398 | -12.01762 | -43.0054 | 2024-12-26 03:59:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 747a9dfb-2ca5-31b5-bdd5-999c63d8d288 | -9.05331 | -40.25154 | 2024-12-26 03:59:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da97b4ac-8ee2-3835-a009-6d0746d71e89 | -12.02042 | -43.00972 | 2024-12-26 03:59:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fac65594-08f1-3129-9cae-278ad9cb9777 | -12.02445 | -43.00654 | 2024-12-26 03:59:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e3da8a7e-f7b7-3eaa-ade9-ccb341475087 | -10.16206 | -36.24733 | 2024-12-26 03:59:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 9f4b56a2-c18f-3e1c-bdd7-86b9f484d427 | -12.02103 | -43.00597 | 2024-12-26 03:59:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7dcfc719-aec7-35e5-b956-c7ce7e420beb | -12.0164 | -43.01291 | 2024-12-26 03:59:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb4199ff-c4b0-35b4-9e65-2dd83b6c10b7 | -10.13737 | -42.16619 | 2024-12-26 03:59:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76b1587a-5b42-38c8-b243-bd9e7ea932a4 | -11.49922 | -40.47869 | 2024-12-26 03:59:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 4ea23d2f-9d04-3d1a-a378-3281e419b8f8 | -9.9838 | -44.72217 | 2024-12-26 03:59:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b35f7c1-b0bd-35f1-bf7f-3d73fb46ab43 | -10.15888 | -36.24181 | 2024-12-26 03:59:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 76d54f0b-3e53-3165-ad66-45de08e02ff0 | -10.16276 | -36.24238 | 2024-12-26 03:59:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 952f3956-3892-3f3e-a865-2bc1b93a7c9a | -10.16595 | -36.24789 | 2024-12-26 03:59:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 58aae568-20a6-369b-8b90-3c5a0184457a | -12.76137 | -38.48336 | 2024-12-26 03:59:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a183176f-36ca-34b2-8353-42708193dec0 | -14.83945 | -40.90914 | 2024-12-26 04:01:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 03ec1309-4d7a-32d8-ba01-15d913554ad5 | -17.78068 | -42.80825 | 2024-12-26 04:01:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb80826e-60c7-3668-bb8f-82b97f8133d0 | -17.37697 | -42.48405 | 2024-12-26 04:01:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f4ecfb9-da4f-3fce-b4b6-cebb3551d483 | -27.32487 | -52.06014 | 2024-12-26 04:04:00 | NOAA-20 | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8015c8dc-6460-3ebf-9399-5a6ff93f2926 | -29.87193 | -51.15894 | 2024-12-26 04:06:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 510984c3-1d87-3c31-afee-208609b074a4 | -29.87332 | -51.16023 | 2024-12-26 04:06:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 2bb30308-39b0-334c-a143-6c4474915a03 | 1.08718 | -59.63226 | 2024-12-26 04:50:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7758cb82-e5c9-3713-9e7f-557eb6506cca | 1.08671 | -59.6292 | 2024-12-26 04:50:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45bfcc75-d194-35f9-a331-867dddaaafa6 | 1.12163 | -59.4257 | 2024-12-26 04:50:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aeaa787c-7044-3164-ac22-51a7906af345 | -3.45175 | -46.30571 | 2024-12-26 04:53:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b0aedf0-cf25-39d7-82c6-29d480063f79 | -2.99413 | -52.84783 | 2024-12-26 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e10e9125-e244-3154-b809-5d55bf7596b6 | -5.69633 | -44.80819 | 2024-12-26 04:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c387ceed-a94a-3b51-a23d-ac5af37daff4 | -2.57635 | -54.00256 | 2024-12-26 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce77551-016b-320c-b0bd-f3a5f96ce06b | -1.73325 | -52.6006 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da460319-54a4-3b21-850b-ff955997acce | -1.73602 | -52.60459 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b617a6c-b7e6-3fa7-9947-8c86aaababad | -5.94104 | -44.44405 | 2024-12-26 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 05ba2576-feae-3a0e-89fe-ed89470f9252 | -3.99691 | -43.25312 | 2024-12-26 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1960a9e9-c42f-3357-8d31-7696d34387ae | -1.69726 | -52.61289 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01ab7416-0600-3dd5-b85d-5da3fa94be8b | -5.94606 | -44.44475 | 2024-12-26 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7bcad54f-cc4e-321d-b8b3-a7f5e4ff9a85 | -3.99645 | -43.25637 | 2024-12-26 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e2e0a2d7-24c2-3a2b-b9aa-5f2b51e32b6f | -1.55207 | -45.8186 | 2024-12-26 04:53:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5eaa9f7-7e0d-320b-b39d-96e5a82f54f2 | -2.94391 | -53.05834 | 2024-12-26 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e86b68de-b8ad-39bf-8038-53cf930e06ec | -1.24848 | -53.83149 | 2024-12-26 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03cbeab6-823a-35ef-ae1e-e241b90c0370 | -3.418 | -44.59355 | 2024-12-26 04:53:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8da1ffa-de63-3555-9fb1-ca9d64dc66c4 | -1.70501 | -52.41138 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbb9c63d-5b23-3d43-b418-0a1f8a8edb40 | -6.17541 | -39.28259 | 2024-12-26 04:53:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 65ed11f4-ebdd-3387-b65d-9f502ba89663 | -1.75374 | -52.81849 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3fbcca7-df89-3dd1-b1b6-28a3842d174f | -1.71111 | -52.41586 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce0eae2a-352e-3ea6-a4e4-61cb08bf50ee | -1.71334 | -52.4233 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e6fcd37-88d1-33a1-ab30-2a47d4da5991 | -3.99163 | -43.25227 | 2024-12-26 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a4dac88-4a80-3626-851a-71cc8d963c85 | -3.99117 | -43.25554 | 2024-12-26 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 668dcb93-8670-3c56-879c-5e294b644ad7 | -1.70833 | -52.41189 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08f95c38-186b-3500-9f1e-8f67e6a7b226 | -5.94062 | -44.44691 | 2024-12-26 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 30262b67-03d8-3233-8a8b-30adfdd62ec1 | -1.24503 | -53.83096 | 2024-12-26 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc4cc9c3-38c1-33cd-9c21-aefae872d304 | -12.02282 | -43.00695 | 2024-12-26 04:53:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa5dbaeb-9bce-35fc-ab63-023d4f030414 | -1.7128 | -52.42676 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21daf462-dd92-3d73-9144-3d4d948afc5c | -1.24562 | -53.82719 | 2024-12-26 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3df5ae7e-ce92-39a7-a302-1e8fd47dcfe5 | -3.49276 | -50.33854 | 2024-12-26 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d5be3ad-72fc-3d7f-8e5f-66d4a9ef92ce | -12.02334 | -43.00235 | 2024-12-26 04:53:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cc8171dc-02f2-356a-9734-d42ed166184a | -1.69781 | -52.60941 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4759220-2dc4-3c35-9706-1a751bfa766c | -5.99092 | -45.39206 | 2024-12-26 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42f03fc9-93bd-3fde-91dd-6ba55099acea | -12.02021 | -43.00617 | 2024-12-26 04:53:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e7f3818b-0018-3de1-9e97-afae8ef8bebf | -1.75428 | -52.81498 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e356c295-2082-3696-87fa-e068832e1153 | -1.81319 | -52.69851 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 872b4120-7621-3915-993c-d6f736921076 | -2.7436 | -52.64476 | 2024-12-26 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04410036-bb4d-332e-9c07-8294f9a6e691 | -5.94564 | -44.44762 | 2024-12-26 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5895538c-3e21-39aa-9d63-883d46d129cd | -1.77362 | -53.70558 | 2024-12-26 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53c5ce8b-7fd4-3d3d-a98c-dbd2e20f2bf1 | -5.93601 | -44.44336 | 2024-12-26 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d32cd8b2-dd07-3c3b-9b11-2b741112b6c5 | -4.34544 | -45.9515 | 2024-12-26 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcde8731-0a0b-3c83-96f5-771cfaeffe4d | -2.7638 | -54.06239 | 2024-12-26 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c3d6caa-0921-3267-a51f-5dd0344bdba3 | -12.02076 | -43.00158 | 2024-12-26 04:53:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d767fc64-8d57-3158-8938-b2e6b0d957b6 | -1.70438 | -52.56766 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ffc843a-602a-330e-b792-1fa037c4ae71 | -1.55094 | -45.82077 | 2024-12-26 04:53:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c30ce25e-0579-3d9b-9242-e60ad23f6e20 | -3.06633 | -40.07972 | 2024-12-26 04:53:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df22b9c8-5b17-388a-83fc-c56e9cd5c4a5 | -2.29374 | -53.6604 | 2024-12-26 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41ed2c0b-efef-3f35-b39c-4743532f86a2 | -4.34533 | -45.95296 | 2024-12-26 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3e077e1-667d-31dd-9735-d8746c9d98a2 | -1.7327 | -52.60408 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11a9b102-5ccc-369a-8357-0ab18eee1f83 | -1.70779 | -52.41535 | 2024-12-26 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afe8c02b-7187-3ace-8235-4f206abd1ed1 | -9.98626 | -44.75407 | 2024-12-26 04:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f020453-a5a1-3f46-b250-3854b9098cff | -19.02383 | -57.622 | 2024-12-26 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e74ff537-4d26-36e4-82e1-f19cc6c54706 | -9.98576 | -44.72231 | 2024-12-26 04:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 248512c5-3036-30dd-94c9-f402fbbc5fe8 | -1.73531 | -52.60063 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74530c2d-2aa8-3338-ad1d-53f6c0ae15b6 | -1.75466 | -52.81434 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6290618a-42b0-3c93-b3e9-6ab8274e3693 | -1.73056 | -52.60374 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| babd6d36-5a3a-35c9-a813-fd7720223e75 | -1.70797 | -52.41756 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c3f71ba-8e74-3429-81cc-ef295de34cea | -1.70435 | -52.41306 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2594a5a-93bd-3ac6-b7c2-a5cdbf084cd7 | -1.73472 | -52.60437 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1454177d-a479-3a9d-9357-ebea5f304842 | 1.08514 | -59.6331 | 2024-12-26 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26f70c33-771a-3d6c-aab8-5300051828bc | -1.7541 | -52.81797 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daa62520-2354-3d5a-abd5-73d0a92e9378 | 1.08803 | -59.62875 | 2024-12-26 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0595359e-c5d9-31de-8e45-1f310afe8c21 | -1.24768 | -53.82957 | 2024-12-26 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f915c293-06de-3fcb-8df0-e6f60bbe61bd | -1.70856 | -52.41371 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a00edaa-9b9f-3585-91d3-32fab3cf8173 | 1.08455 | -59.62929 | 2024-12-26 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e052df9e-3b53-34d2-ae3d-1effbdaf42c6 | -1.71159 | -52.42206 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd6b0a76-d354-329a-8079-da14f89f89f9 | -1.711 | -52.4259 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4aabfad-c770-31fd-bc0e-d782fd20fc8f | 1.12377 | -59.42598 | 2024-12-26 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6300ff0-f253-3303-be1a-59ed615beb66 | 1.12032 | -59.4265 | 2024-12-26 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27b9c871-435b-3be6-9391-2ab234a7a629 | 1.12319 | -59.42225 | 2024-12-26 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 266f9325-cf86-380e-9e4d-b296a4975f90 | -1.69497 | -52.61359 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 059e8995-81da-3571-ad30-c42f597b6566 | -1.69554 | -52.60985 | 2024-12-26 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59123319-c3d1-3ca8-86b9-bd92e7396961 | -5.94472 | -44.44778 | 2024-12-26 05:33:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 44fa0d33-576b-3017-a02e-6ddfd0c34ccf | -3.9993 | -43.24619 | 2024-12-26 05:33:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README5.md)
