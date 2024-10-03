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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 533123c7-15d3-36e3-abd3-8c725029013e | -12.86638 | -62.45796 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db1c2b80-6f86-3a4f-a44a-130e8124174e | -12.86575 | -62.4618 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8fcdcca-7604-3394-89f8-9f390ce006de | -12.86259 | -62.481 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcf3fc2b-751c-3504-a43e-208ebaf6dec3 | -12.86104 | -62.46888 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e5aa0fb-5bd3-3cb9-8019-5907a4fce6ea | -12.8557 | -62.47981 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c65774e8-a374-32fe-bdac-feaf10b830ad | -12.84538 | -62.47802 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfef9598-a718-3272-88ff-cbfbc15b7cd5 | -12.82754 | -62.47891 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2592fa59-5f1c-3fe4-9c01-5f46d19f6033 | -12.82002 | -62.48157 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| da158c3c-3f31-3b1b-b2e1-8ccd66ec99eb | -12.81938 | -62.48541 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 57425573-e77b-3014-92c2-8591b934ed24 | -12.81657 | -62.48097 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 712b1208-5c0f-3fda-b2e9-a732d304df92 | -12.81337 | -62.50019 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fd70224-bd85-3ba6-8f31-79e424181af3 | -12.79241 | -62.50526 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9227f6b6-8b94-3ced-9b1a-5f62ac0117d0 | -12.79142 | -62.50431 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5c20de8a-af2d-3795-96be-63b7ef7d945e | -12.98156 | -62.71127 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 715f6402-f07e-36aa-b534-24a214cf0739 | -12.98091 | -62.71518 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c729873c-8bee-308f-bc6c-a621f5efad22 | -12.9781 | -62.71067 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 913a80a5-5ad6-3771-8157-c08e1154e802 | -12.91948 | -62.70948 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9674d2e4-5745-39e6-8c48-a7d9db097522 | -12.91883 | -62.71338 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9c0103e2-ac67-3320-b878-eaffe29cc90e | -12.8834 | -62.77579 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72d9dd84-e837-308c-805e-a023f696105f | -12.87927 | -62.77912 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cb3fb96-cb75-3787-9e32-21fd044715bd | -12.87579 | -62.77851 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65875081-2d8c-317a-aaf7-4162d71a91f7 | -12.8756 | -62.75828 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eefe0742-f26c-34df-a668-a665e1ac312e | -12.87213 | -62.75768 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58ed4d47-c9d1-3e6a-98cd-696aed8d24ef | -12.87165 | -62.78184 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95a35414-f511-3c6c-896f-7d3c61d4fd71 | -12.86865 | -62.75707 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a335051c-8f05-3b0b-bf3a-6e81cee29ce5 | -12.86751 | -62.78517 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2b726ab3-c8bb-3703-a5c0-88f0c208678a | -12.86403 | -62.78457 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f55f0cb-bd5d-3a63-b887-3c7f810796c2 | -12.85553 | -62.78372 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d0f2fc38-daf4-3a0d-8bc8-722dafa7224e | -12.85424 | -62.7916 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e434d58-bdde-3ad3-8805-d89fd3e3961f | -12.85359 | -62.79553 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37889d74-3037-3616-bb02-8b53bbc976d3 | -12.85358 | -62.78276 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ba5732c-42d6-3d6f-8db6-0816a108027a | -12.85226 | -62.79063 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d63cfde-856b-3619-8ba6-407cfaf3bdc3 | -12.84662 | -62.79433 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8082d15-0957-3c40-9539-6958c378b2cc | -12.84598 | -62.79827 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83793e8e-121f-32f2-9c95-841a7278264e | -12.84403 | -62.81011 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c33bd1bc-bd1b-30a7-a1b1-26e90cd48539 | -12.83771 | -62.80495 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e30e922-1431-336b-9466-6ebd8fb79e36 | -12.79377 | -62.72448 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cfc4e8e-572a-3706-b3a3-b503865271a7 | -12.767 | -62.75618 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fb9aaed-81b1-3092-9f28-2e38501a0953 | -12.76502 | -62.76798 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| beb6d2f9-f625-3a38-9246-a1dac09d6a19 | -12.76286 | -62.7595 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 428661c8-0917-32af-8d11-99701bee2271 | -12.47035 | -62.72807 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 241bb6e6-63af-3c50-8728-4194b09e1686 | -12.4662 | -62.73142 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a521e6d9-eafc-362a-9fdc-af6e731224d8 | -12.4581 | -62.75846 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ed0f30e-c08f-3cf9-829c-cb5df906e143 | -12.45744 | -62.76242 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3308ff0-1cf5-317b-bac9-ffa7031111c8 | -12.44445 | -62.71141 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 611d283d-f966-3ca6-a2e1-3ab1be086529 | -12.41148 | -62.99321 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 047bee9e-1002-373e-a3c4-0b2a8353b108 | -12.4108 | -62.99726 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| dd80375e-1abe-34b5-ac78-6e335c93d931 | -12.41012 | -63.0013 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 6605a1c9-2e6a-30c2-bdec-92a66ad23f2f | -12.40795 | -62.9926 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d290d235-945d-3cbd-9f00-caef35e42a55 | -12.40727 | -62.99664 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 68f3183c-32d1-3001-b05b-cf763fad372a | -12.40659 | -63.00069 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 05f61937-09be-3f82-a464-e28785ee057a | -12.40511 | -62.98792 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4feeaee9-84f9-3a2d-91f8-761110799285 | -12.40443 | -62.99197 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7a241a26-dc69-3747-b1fd-c31061e8de02 | -12.40374 | -62.99603 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| a8dead18-b9c1-3b4d-a638-97641dcdfedd | -12.40306 | -63.00006 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 0bb85460-0588-36e5-b64b-b8ccd0955079 | -12.40238 | -63.00411 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4e4b4e44-942b-307f-8432-bd32043a8396 | -12.40158 | -62.9873 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c300d2f-ea02-3c95-8372-e292f244120f | -12.4009 | -62.99136 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e86ddcf-7d8d-3c5a-9149-0747ec295816 | -12.39953 | -62.99946 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7b05a667-ace8-384b-b47b-1fb906a72fb3 | -12.39885 | -63.00349 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f7a08c68-6533-30e7-9ff0-1b9b1fd87601 | -12.39806 | -62.9867 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f66f89a9-9d37-32e2-852f-55fe59999b22 | -12.39737 | -62.99074 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df846fe3-f755-3f99-b722-62c5fe76c706 | -12.396 | -62.99884 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a182a4c-68b5-346a-b0d3-51db2fe1a9e3 | -12.39532 | -63.00287 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ed4ffaf8-4071-3735-acc1-c278efab1b65 | -12.39453 | -62.98608 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6524e2a3-3925-35cc-a61b-9497ae8c88cb | -12.39385 | -62.99014 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23df90cd-5bbf-3cf0-be39-0c5e4ce6fcb6 | -12.39248 | -62.99823 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91957505-85c0-3b03-a884-b4a84e8bb5ef | -12.39179 | -63.00226 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de011862-3b7e-39e5-8207-88dded3a371a | -12.39111 | -63.0063 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d89fb5b2-e665-3f7b-9444-850645a48dbf | -12.391 | -62.98548 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9e88956-eaf0-3304-b800-789ba3b132a1 | -12.39032 | -62.98953 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4feefe6c-d802-3df5-a9d9-b1a69c998f75 | -12.38963 | -62.99357 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68a9e84a-b023-315a-9b43-7b818c1539e9 | -12.38895 | -62.99761 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a988d03c-2a07-3ac9-8280-a5c11ba84273 | -12.38826 | -63.00164 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3b754a0-d5a3-375f-8fa4-6c740b465556 | -12.38532 | -62.99785 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3f096fa-f489-3015-b0ff-d2e1922dcb2c | -12.38474 | -63.00102 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f327bd21-920b-33c0-89d1-218e4bffff9b | -12.38465 | -63.0019 | 2024-10-03 05:16:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bafa503b-2932-3024-a706-8ef425f7d49b | -7.91119 | -63.46233 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fca0f6ca-a178-35d7-92aa-e07fdcb573ae | -7.58714 | -63.35713 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72a2fcf0-a2d1-35da-988f-6f77f5965646 | -7.58634 | -63.36186 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa013813-d159-3023-ae88-dbd31fadabdf | -7.03493 | -63.08588 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e51f17c2-c5f1-3d6c-aa6b-a1de5052d514 | -7.03486 | -63.08334 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eff0eb10-ad7e-3e35-bedf-81fff077fd49 | -7.03417 | -63.09053 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60eaa7cd-d38b-3554-b77b-20ef1e0bc0a2 | -7.03407 | -63.08799 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9800bd3-e0e6-31db-977a-624911a84af2 | -7.03328 | -63.09264 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4d133fc-b93f-38a3-b955-e00131d80fc5 | -7.03114 | -63.08525 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b3205de-2af5-3f82-82b5-7eff964fa352 | -7.02734 | -63.08461 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c890916-66c5-38f7-95f3-64b44e13ca24 | -6.85808 | -62.90897 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3fc326b-f474-3d58-baa3-aa9ae8751960 | -6.85806 | -62.91133 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0621932c-31f2-3b45-bb53-18eb1927f599 | -6.85734 | -62.91355 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41d5da7e-7912-3dd7-be6d-21d4241321b1 | -6.8543 | -62.91069 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bff9e021-88d7-3808-956d-1454640b2a09 | -6.85358 | -62.91291 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21ba1e92-6cb2-3a81-9f26-14f4d06165ec | -6.85056 | -62.90772 | 2024-10-03 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca459a60-279f-3c7c-9502-acbf92db9d4c | -9.25716 | -63.34903 | 2024-10-03 05:16:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4cc88990-a646-364c-8384-120813db23c4 | -9.30506 | -63.83356 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 954fb133-21f0-3d8b-a41c-7b2fe7f37939 | -9.29893 | -63.40498 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2564c5c-1c3f-3da1-8923-83795789d41b | -9.19771 | -63.45127 | 2024-10-03 05:16:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| afeec2dd-2610-357a-b8e7-bad726b7f744 | -9.19395 | -63.45062 | 2024-10-03 05:16:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbfdd803-f2ec-3158-9fe1-656a315255ab | -9.19098 | -63.44535 | 2024-10-03 05:16:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f4bd323-1025-32bd-81ae-fe7d20661197 | -8.96115 | -63.6112 | 2024-10-03 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README170.md)
