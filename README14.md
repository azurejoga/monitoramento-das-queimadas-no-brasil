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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7d01351-8498-360c-a423-59e310a18f6a | -11.01943 | -54.31756 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35eac302-53c3-39d0-9e48-f4489ce2b8ae | -11.00473 | -54.30925 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 815ba5fc-7a3c-3281-90ea-b6db4ad6f797 | -12.2268 | -57.28218 | 2026-06-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a8ed1b3-6b7f-32d2-b2f3-9581e76a003b | -11.88213 | -57.8293 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a53bbc18-6f36-3b65-b9a9-75768ad0c04b | -10.90943 | -54.13525 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c90db653-900a-32c9-bd3b-091ef906cd16 | -12.73319 | -54.74286 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37115462-3510-3caf-8ac8-2cce3365f415 | -14.1005 | -59.38298 | 2026-06-05 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8b59be5-de3f-3964-9926-7f3a7637698f | -14.7772 | -52.6768 | 2026-06-05 05:31:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e172a7af-e465-3de3-aeb6-8078d1655535 | -10.02789 | -59.34333 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d71a92b-7a49-3dc0-95c1-19d80e5a121e | -12.43449 | -58.47979 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f33070e-23e2-310c-86f3-16ca7bc88785 | -12.45195 | -58.47065 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 309b97ac-28a8-3a80-b8eb-440883806a9c | -11.55389 | -52.80576 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29f2fd50-54c5-3eb3-9acb-f8d8ec3babb0 | -12.45544 | -58.47482 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b4dce2c-a7a9-3427-aaa8-942cc31ccd3a | -14.09665 | -59.38244 | 2026-06-05 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24f6d0ce-10e1-3ab3-9933-b0b1de98f813 | -16.6043 | -58.23837 | 2026-06-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 94fb1e7e-bd0c-3ab2-a59f-a236b2411a6c | -11.27265 | -53.9704 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c488526c-54e6-37e9-ad55-203a6a83ee64 | -10.03096 | -59.34687 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72e60bb2-c2d3-34af-9b30-93d6a324a30d | -10.86925 | -53.73606 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4db9ebd-7128-3215-b76a-0e2ea66a699c | -12.80992 | -54.86288 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed091d96-26ee-3fa2-aaa6-75d37687c146 | -11.88315 | -57.82168 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a47faff1-64c3-3824-91ac-4fdd892b30e2 | -10.7695 | -54.10072 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1b9005b7-42ed-31d1-a892-b36bfbd337aa | -12.44701 | -58.47714 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3037c277-c7b6-3082-a660-44512ad48c6c | -17.78454 | -50.46872 | 2026-06-05 05:31:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b40b2ab8-af3f-31e9-abbb-b50009e63c64 | -15.05054 | -54.97811 | 2026-06-05 05:31:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d338fe6-76f5-3c81-95ad-cf8644f5f2b6 | -11.57652 | -54.57803 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 287779c7-face-376f-9de6-cb05e074a49e | -12.22252 | -57.28158 | 2026-06-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c28deb2d-1c65-38be-9c8e-e663f9fb17bc | -10.03155 | -59.34387 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2767db9a-de3f-3bdc-baab-403c21b424d0 | -9.63541 | -67.21616 | 2026-06-05 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99a2bdaa-4848-30d7-bb94-4bf827d1e72f | -12.44405 | -58.4085 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 790ec5d5-6962-3515-b7b9-5fbe811aebf0 | -10.57772 | -57.31861 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06ded9b-d6a8-39e8-9b0d-11cc277a7661 | -12.44352 | -58.47298 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e058a1c3-dcc5-35c2-aba7-5a6a991b5d96 | -11.01466 | -54.31376 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e112045-4ce0-3c7e-aa26-0245ebbd30fa | -11.01902 | -54.32067 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39a2a4dd-4d79-3403-aeea-49a34973ae23 | -11.0099 | -54.30997 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60347258-e177-39bb-b514-caf768cc53ee | -12.46388 | -58.47243 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87e552ad-2ef2-3253-8fd6-093272ed8a10 | -10.03219 | -59.33821 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79b1d806-a363-3276-93f0-cc207d532918 | -9.40121 | -63.74 | 2026-06-05 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c8407d6-90f0-3dda-9743-e22b729482b6 | -11.56666 | -52.80682 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 87a00b1a-32bc-3df8-8fda-b59377bb0666 | -11.89037 | -57.83042 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c83cf52d-b9f0-3695-a108-f97c824f7234 | -12.44244 | -58.48096 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f10c5d15-d1db-357b-9e21-0e58ab95bddb | -12.4391 | -58.41504 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b10bdf7-eb10-31d4-93eb-103eebedad37 | -10.57353 | -57.31805 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53961b43-02ac-3222-a2ff-6c640d48c209 | -11.98947 | -57.80114 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1b23dac-85f6-3687-a976-db0017e1487a | -12.73546 | -54.72419 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3371c089-49fe-3f2e-b2d1-1e96c16ee35c | -12.4457 | -58.48684 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d5d1e45f-80fc-3c69-a827-08b056fe6f49 | -12.44357 | -58.41205 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b2e7c16-acca-3cce-a3fc-fe3babc886a4 | -12.81029 | -54.85976 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98c1b78d-d4a2-37ec-9f34-6320cb0cccbc | -14.10434 | -59.38352 | 2026-06-05 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4eecfe5-ec5a-3786-ae0a-676c56f5632c | -11.55339 | -52.80978 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 184f662e-544f-3007-9f11-84d6b8a38a75 | -11.54865 | -52.80085 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6edd8eec-978a-3209-aee9-073ce9537b71 | -10.85054 | -53.75481 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8835051-2655-3721-8372-45a67b8e6799 | -16.60002 | -58.23778 | 2026-06-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8e17ac3c-2465-3a67-a92e-cd0a53e265e2 | -16.18771 | -58.46485 | 2026-06-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 84b6dc09-b806-39ed-84d4-8c8bc5dc8559 | -10.77471 | -54.1015 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28297545-57f7-3b6e-8b21-2c04b4498d09 | -12.09143 | -51.99395 | 2026-06-05 05:31:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fd80f3a-1196-34db-8002-607ddc31ee1a | -12.45146 | -58.47421 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 57dccdea-2ddd-3228-9ab6-b0175644a635 | -14.09528 | -59.39234 | 2026-06-05 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e715e76-54f2-3bcf-988c-72898313779e | -11.54816 | -52.80486 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c21109b7-72f9-3353-92c0-f6b2a04f45a9 | -12.74098 | -54.72182 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7014c15b-37fe-3eba-b207-a3ec11242b70 | -17.78211 | -50.46452 | 2026-06-05 05:31:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d4c171e-d7d5-3982-8caa-912db5c65ae1 | -12.23164 | -57.27869 | 2026-06-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e7a3531-03ad-3bd8-b783-dc1526996bc5 | -12.74021 | -54.72812 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbba9bd4-f1f0-31ff-b6cb-8053b43cb030 | -12.17927 | -54.54054 | 2026-06-05 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5cd4194-282a-34a0-957d-72c539d316b2 | -12.43208 | -58.47745 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d897ed77-0c49-3068-a471-165bec8bb799 | -10.03219 | -59.33955 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70c8c433-a2b1-3e34-b39d-a0e4c313e501 | -12.73508 | -54.72733 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a082bd8-bfcc-33d7-ba5a-fb1602c19966 | -10.90421 | -54.13454 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d0ad7a6-e21b-3e08-8825-637cf26b5ad0 | -11.57102 | -54.58047 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 360e28b4-262b-3009-b2c5-5cb59367a1f5 | -12.44304 | -58.47654 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3103728-c19d-3c72-9337-46c8fce92a66 | -16.19087 | -58.47338 | 2026-06-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 21294aed-bd59-397a-9ca9-194d3f12d24f | -14.09596 | -59.38741 | 2026-06-05 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0672539c-e78d-381e-96d0-38b5f2d0a737 | -12.80954 | -54.86599 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05ae46da-090a-3433-a741-008409442b11 | -11.54989 | -52.80045 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3041a66d-93d0-3204-979a-ad85dedb2f5c | -15.05017 | -54.98133 | 2026-06-05 05:31:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f27a2a0-a1cd-39a4-bf49-ca7b7801c7b1 | -12.72882 | -54.73588 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffa537f5-6910-3a22-a70c-84f350cf6548 | -10.57301 | -57.3219 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34b84000-bcb9-34bd-8736-054a77fa3c19 | -12.45592 | -58.47126 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddadd122-c372-32a4-9603-fd8bd7c44ac0 | -10.513 | -57.60723 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7594a95c-db64-3b38-9661-bab8018b9173 | -9.63155 | -67.21548 | 2026-06-05 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 604174d3-a572-3225-b3ca-ec7a4c28176b | -12.22736 | -57.27809 | 2026-06-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34b9313d-91f2-31a5-88be-c3e92ceee3fb | -11.54942 | -52.80447 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0c1d8d9c-8ed6-3c0e-bfcc-91b8c6f6a9b3 | -14.09913 | -59.39287 | 2026-06-05 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 741b3406-45bd-3644-8b6a-e4f0fbeebf10 | -13.52166 | -54.30867 | 2026-06-05 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 314832c7-5802-3e1f-852f-df950e347a1b | -11.27223 | -53.97366 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ac5bf8c-896e-3c9b-8875-8eb7c3b52ced | -12.43134 | -58.48275 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 815e1c91-b6eb-32ec-ad44-018a66228339 | -11.63846 | -58.24712 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cdd722c-0118-33bf-9a15-0fe6f671f719 | -11.01426 | -54.31685 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2f99a2c-25aa-34b1-b432-b7bf57eaf511 | -10.01016 | -67.76127 | 2026-06-05 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3f84aa8-a4fd-3b3f-9d76-8da8b87e276e | -12.73394 | -54.73671 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c32be330-ef2e-3b43-a38e-20f129eb031b | -15.48123 | -55.83178 | 2026-06-05 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c27f79c-4df2-3b3b-a67f-89ff91b71ca0 | -11.57614 | -54.58105 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5bf41e2f-3734-3a51-92fa-ad77df01a7e2 | -11.88264 | -57.8255 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b0c0184-d4ea-3c5f-867e-f1ccf3be115d | -11.05406 | -56.9229 | 2026-06-05 05:31:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58b71f16-b2ec-3ccf-9b84-3baff90a17b6 | -14.77163 | -52.67168 | 2026-06-05 05:31:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2d9c0bc-8c5d-3d3a-8434-08be42d319c7 | -11.60266 | -55.34019 | 2026-06-05 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0759a8ab-49a5-36fc-9cf0-83720e3b6068 | -11.73345 | -56.84296 | 2026-06-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbc5596e-dd0f-3b1a-9de6-e2b9c69ac0e1 | -12.09196 | -51.98934 | 2026-06-05 05:31:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e517bd28-424b-33dc-92f1-f254fb103894 | -9.54527 | -64.5043 | 2026-06-05 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 455475bb-6f7c-303a-b24e-1fe8839dcbe3 | -12.18105 | -54.54026 | 2026-06-05 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0a7193c-60ff-3e79-bd75-8bff50eccca5 | -12.7347 | -54.73046 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README15.md)
