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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5d10bcb-da34-3bd4-bb0f-da14f0ae1791 | -15.15769 | -56.47794 | 2024-12-07 04:57:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1cb5bf1e-0d06-384d-af62-55e86ca6dc49 | -15.09293 | -59.63595 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc0c619b-6cbc-30ba-9e97-09828beacac9 | -12.92874 | -48.63485 | 2024-12-07 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f4c0f84-5d72-3020-a1a2-6f4cd94617ac | -12.86072 | -51.93494 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48c2149c-542b-3db6-b581-4c41401c1f75 | -11.73169 | -54.30966 | 2024-12-07 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f80d3eb-2c0b-30ff-a5d8-9dee81becdff | -16.32258 | -53.8127 | 2024-12-07 04:57:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0a9bb96-dcd6-30e5-960a-57356f59bfc7 | -17.56258 | -48.01387 | 2024-12-07 04:57:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1972e48c-9026-34dc-9894-b54b9663551d | -14.7686 | -50.535 | 2024-12-07 04:57:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 496b4a45-a1f9-34e2-8621-35498ade30af | -12.84902 | -51.93775 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b789c1c-3d11-3e71-ae87-1abf9b4918d3 | -12.85271 | -51.93831 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb801dea-8f2f-3732-a6c0-04f2d86eeb83 | -15.56905 | -47.8572 | 2024-12-07 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 362a2543-3456-3440-80bf-d9b2ce31b3da | -15.08693 | -59.64862 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f0c47b1-cb6f-379c-b8b2-a80e6dfaea34 | -17.56797 | -48.01161 | 2024-12-07 04:57:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a48e60c0-e5b3-374d-8c35-1a1b77ad4e3c | -12.91878 | -49.68366 | 2024-12-07 04:57:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 602b75df-c19f-3a2b-a3da-49ef769ca83a | -11.82546 | -57.81793 | 2024-12-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cd31d95-f8f8-304a-a5ed-431c6809536c | -15.09059 | -59.6493 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 990a2e29-afe0-35cb-af64-a1f015102d47 | -13.07097 | -52.02968 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a842cdf-d3d9-3fea-b776-8f0b1251396e | -12.23259 | -52.45963 | 2024-12-07 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb2b50e8-9c04-3a90-b1a5-9f5953b3cce5 | -12.85945 | -51.94384 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a71d224f-da41-3bcc-a880-7be786a08de0 | -11.73558 | -54.30662 | 2024-12-07 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21a1b6f2-a01d-3ea5-bd6c-eaa7c4b5fc93 | -15.08615 | -59.65306 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c15894c9-c717-332f-99f7-7757870c8fbe | -12.85207 | -51.94275 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5160ee1-93f6-3d37-bf5e-35c98294f5f1 | -12.91931 | -49.67966 | 2024-12-07 04:57:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b31efaf2-c5d4-3c08-acc2-17311b22cc6b | -12.23616 | -52.46017 | 2024-12-07 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e18b02c-9074-3bd3-b62a-1424fc0b5b44 | -12.67889 | -58.24513 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 101e6ae7-6781-3810-a084-40ab136348ba | -12.23556 | -52.46429 | 2024-12-07 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0364de4-af49-35e4-ad7d-afbcf0ee516b | -12.65683 | -46.57953 | 2024-12-07 04:57:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f4eca67-b13e-3081-af89-c5cbb3bd2074 | -12.9242 | -48.63412 | 2024-12-07 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1fa7c64-b6f8-335b-8c91-3f80c3975372 | -12.85334 | -51.93385 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc412ffe-406a-3e6b-924b-89e7cc22802b | -16.32353 | -53.81167 | 2024-12-07 04:57:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 084913b4-04c8-3474-9142-afce47065af8 | -15.07906 | -59.62878 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e81773a9-23f9-304f-b651-58cf9550c16d | -12.91453 | -49.68314 | 2024-12-07 04:57:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40103e68-6715-3253-a9c1-e5288fc396d0 | -12.84966 | -51.93329 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5672c5dc-1194-386e-86c3-eb29efb8560b | -12.53435 | -57.7378 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1be5aa5-9cb4-3a20-bfe7-f53702461d49 | -15.2581 | -53.56448 | 2024-12-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc5f9419-5595-3c48-bb0e-bc308f190481 | -15.08041 | -48.94469 | 2024-12-07 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f13785b7-9ddc-3d97-87a2-22aee9d1bc97 | -15.26102 | -53.56899 | 2024-12-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 275bfb2c-47ab-3ffa-bdbe-f3212f9ab5ca | -14.38319 | -46.03751 | 2024-12-07 04:57:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 82b4b819-e686-363c-a74b-d0042ae6b1a2 | -13.66265 | -52.94805 | 2024-12-07 04:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce200765-d835-3498-9aca-df7501e85ac0 | -15.07516 | -59.651 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f599c54c-60dc-3f73-aa23-c4eb70db4a84 | -15.09082 | -59.62638 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fe29c7b-6125-3627-9faf-48d5b2430237 | -16.20061 | -48.22417 | 2024-12-07 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dc9f130-0a1e-341a-a98c-1c5fe6f509be | -13.07033 | -52.0341 | 2024-12-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cefc4442-5a95-3767-8dea-5a70e9da75ed | -12.53498 | -57.73394 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea5bbb5-c31c-30ef-b194-d1ac41bae1b4 | -15.25983 | -53.57705 | 2024-12-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc505d24-0aca-3cad-9965-fc2f252c04d5 | -15.08982 | -59.65375 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b1eb1d4-d4c3-36ce-9a0e-997646a53156 | -15.26042 | -53.57302 | 2024-12-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f7a343fc-c2a0-3649-84ae-3705d2ea87c9 | -15.08639 | -59.6301 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea9d5c0c-4fa9-372f-a530-a891ae303104 | -12.41051 | -49.68568 | 2024-12-07 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bfdfd2f-b16b-34b7-96c3-8c825fb2511f | -15.09005 | -59.63079 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ac1e89a-600f-3ef2-82f8-fc8a3104f30d | -15.08272 | -59.62944 | 2024-12-07 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a495eed3-5e68-37cb-afe3-4fa58280470c | -12.67956 | -58.24109 | 2024-12-07 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2130e843-8f6f-3d0e-b391-94abae42f15f | -20.31935 | -48.82526 | 2024-12-07 04:59:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c211714f-9554-3dab-aa38-72b02ea4d744 | -20.32432 | -48.82585 | 2024-12-07 04:59:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b202ecec-c901-38db-a8ea-230dba6ee1b6 | 2.73929 | -60.38982 | 2024-12-07 05:48:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3fd21b2f-3d05-3fb5-9c4c-467f553e0719 | 3.68827 | -60.54187 | 2024-12-07 05:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9609b704-1d52-3e73-8b9b-105feb319399 | 2.1243 | -61.30358 | 2024-12-07 05:48:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9334bca-33bb-371a-987c-3b9178146746 | 2.51271 | -60.98769 | 2024-12-07 05:48:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54e64a65-e250-3831-8a6b-69648d01cd87 | 3.3601 | -60.09566 | 2024-12-07 05:48:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82a66303-bcc0-3ebe-8735-6a233104608e | 2.50742 | -60.97894 | 2024-12-07 05:48:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c5dd4fc6-6208-3da1-85ed-aa9bff3088ab | 2.51197 | -60.98302 | 2024-12-07 05:48:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3dee1751-0ddf-3c81-a5e4-4d7f199aac5a | 3.3397 | -60.09553 | 2024-12-07 05:48:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44dc1a6b-9f82-3baf-aada-4b4454170e77 | 2.74009 | -60.39484 | 2024-12-07 05:48:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ad9ee89-7cdb-3567-b476-5be1cf6eae2e | 2.42297 | -60.64954 | 2024-12-07 05:48:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f34cc53-9f84-3629-a11a-073ab26f825b | 2.94734 | -60.35742 | 2024-12-07 05:48:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1723908-f7d2-399f-9777-9cdba5572dfb | 2.37234 | -61.2545 | 2024-12-07 05:48:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05bc02b3-31cc-3537-9340-3f3f86ee27f5 | 2.50816 | -60.98362 | 2024-12-07 05:48:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a7cd4f65-54e8-3b0d-9171-317ebfd28a6e | 2.51123 | -60.97834 | 2024-12-07 05:48:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea65b8e8-739f-3dc0-bd9b-2d7c94e90e40 | 2.73848 | -60.3848 | 2024-12-07 05:48:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e6e25dde-8441-30cf-89b0-fe059aec018d | 2.59919 | -60.16822 | 2024-12-07 05:48:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fe0e389-b231-3a3c-aebf-6393d8b24b3a | 2.51346 | -60.99235 | 2024-12-07 05:48:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 883f4814-fcc1-39ad-b524-0a6633e4ac5e | -0.64157 | -63.028 | 2024-12-07 05:48:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1d62bfb-1de5-389d-a062-59b6cea727f2 | -0.64449 | -63.03254 | 2024-12-07 05:48:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72956074-f496-363b-a3ed-7a96643caf61 | -0.64511 | -63.02856 | 2024-12-07 05:48:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe2ae6f3-2b1d-38f1-8d7a-47514f7b0a29 | 3.69042 | -60.54487 | 2024-12-07 06:03:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| de6a6f5d-746d-39b1-ae02-aad4a1b53ece | 2.52065 | -60.98179 | 2024-12-07 06:05:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0948a099-089d-3f0e-8575-fdd133887197 | 2.52128 | -60.98925 | 2024-12-07 06:05:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1c142b13-82f8-3b97-958f-18d40f00d6af | 2.51843 | -60.97023 | 2024-12-07 06:05:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ca63fa22-79b5-3a91-904e-afe1c632908d | -15.26417 | -53.56861 | 2024-12-07 06:09:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 62e5a060-ddcc-3d4e-af6a-fc26612a864a | -15.25467 | -53.5516 | 2024-12-07 06:09:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 572db20c-834e-39f6-9584-57b09de53cb8 | -15.25401 | -53.56232 | 2024-12-07 06:09:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| c69611f3-6f1a-3807-910d-12009feaec7d | -15.25274 | -53.56736 | 2024-12-07 06:09:00 | AQUA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 31e2ff05-199b-3b7c-8c8f-2d068e491338 | 2.74215 | -60.394 | 2024-12-07 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c4747ee4-d413-3da0-806e-f1cea9bd4b2d | 2.73804 | -60.38848 | 2024-12-07 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55fcef61-b8b9-3e64-a6f0-e303169b78c1 | 3.34045 | -60.09367 | 2024-12-07 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89294579-6d4e-38b2-9c14-0da4e1c290fb | 2.74401 | -60.38748 | 2024-12-07 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0bc7d41-a2b6-371d-be6a-e636089e0155 | 2.51272 | -60.98117 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a5a7c3c-c98c-37c4-a25e-a6a2aac8c5f9 | 3.34122 | -60.09812 | 2024-12-07 06:09:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa987e69-de05-3ae7-bc17-723bc94441ab | 2.51409 | -60.9892 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3dad79d8-274a-3162-9ec3-d672c6fff482 | 2.73879 | -60.39283 | 2024-12-07 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8560dd21-2a56-34fb-9eb5-d1336e1dc62d | 2.74143 | -60.38963 | 2024-12-07 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24009094-8957-3127-9281-1767c2f79db6 | 2.51279 | -60.98136 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3de3c542-d108-3583-ae0a-1c09b64f0a64 | 2.51411 | -60.98941 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae83f138-fa4f-378f-8727-ea651a282c2a | 2.5134 | -60.9852 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d192de3f-d9db-383c-8bbd-86785aa2a03f | 2.74071 | -60.38528 | 2024-12-07 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e01729df-2074-3088-87fd-2edd8734a967 | 2.51477 | -60.99342 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcea3fe2-0e12-30f8-b225-6e2b84d6205b | 2.51345 | -60.98539 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1153516-f7de-3ac0-9cf9-8cb74240744c | 2.7373 | -60.38414 | 2024-12-07 06:09:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67bba53b-91a7-3e0e-9261-1325b68d7e64 | 2.50703 | -60.98229 | 2024-12-07 06:09:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b6442cf-0478-3ae5-8da0-e6d1437438e9 | 3.68683 | -60.54571 | 2024-12-07 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README12.md)
