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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bee40105-8fe7-3cb4-967a-5a3c59edae49 | -1.568 | -53.5187 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 354af6c4-1133-3cdd-a9dc-e4329369cb4f | -1.8066 | -52.749199 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8ec1a24-4d51-3fd4-b16e-7ed3cdec861f | -1.7036 | -52.612999 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2f877e8-c6ca-3cae-b1a9-62d945be7c14 | -1.2809 | -52.1563 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3c66b77-76de-3234-943a-a6bae7efb92f | -2.1056 | -56.047901 | 2024-11-28 00:41:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0db8259b-c0d6-39ba-9446-7415ce9296ed | -1.684 | -52.435299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3791c6f-d0af-34be-ac60-7792f8dead76 | -1.6521 | -55.219398 | 2024-11-28 00:41:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0a21f9f-6de8-3704-b488-cd6f768cc1d7 | -1.1149 | -53.3834 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5219829a-6ea1-31c9-b437-419042554aca | -7.6838 | -42.970501 | 2024-11-28 00:41:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e43b7f0c-5ccc-3178-88c9-1607ae562f79 | -1.3953 | -53.621101 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37535217-8ca0-3195-b61e-9927ad6dc49d | 0.979 | -50.128502 | 2024-11-28 00:41:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 833a0faf-794a-3a24-bb6a-579e2c9e6f9d | -1.075 | -53.206299 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d807e0fc-0abb-3689-b44d-d59db85a0ad5 | -2.157 | -54.807701 | 2024-11-28 00:41:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3568616d-024c-3e4c-bdd2-9da1fbec67dd | -2.1586 | -54.8148 | 2024-11-28 00:41:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a599eaf-6682-371d-b9a9-df87646def6d | -1.3696 | -52.548901 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 541e1baa-2347-36de-9100-2fd5cd099695 | -1.1364 | -53.707001 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f766db-96a0-358a-8d34-c98f975d91e5 | -1.6655 | -52.946098 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7bb3298-5535-34af-896e-1f271827ca8d | -0.8936 | -51.720299 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d16049f4-480d-358d-9adc-13df49447349 | -0.2767 | -51.497898 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 889af34a-6fcf-33ba-8483-56c997faada7 | -1.6836 | -52.479198 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8e85445-5065-3b28-bd49-b6310972935f | -1.6903 | -52.4631 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20546191-c68e-39c4-a669-85de368a2a75 | 1.2506 | -55.959999 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c94ca0e-31ed-32cb-87c9-ea7b80482854 | -1.566 | -52.278099 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d516273b-6ce2-3d26-b1c8-8cdafc39fbe3 | -1.1312 | -53.729599 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 424b6276-b94b-35f6-9f1a-0b6dfd0ebe80 | -1.3855 | -53.623299 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86420b05-d259-38fa-bc39-3b16c589d726 | -1.3864 | -54.999901 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36f2a0fc-377c-395a-9aa8-0ab92902601c | -1.6872 | -52.4492 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 355ccfb2-ab32-3599-8eb2-17e1176af619 | -2.0002 | -53.2873 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b251a98-0284-3954-8554-ba900e85b226 | -1.715 | -54.7201 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1ed63e-dc31-3a5d-8836-b8f862c51d64 | -1.5885 | -52.013302 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8e931f-fa77-35ac-88f8-3e3a4ece776c | -1.6198 | -52.2882 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 315b845b-d787-3dd7-8e2b-561f81e206f7 | 1.2425 | -55.9506 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5c30666-0af5-39b5-b288-73d76d7ccdc3 | -9.1677 | -44.721901 | 2024-11-28 00:41:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd64bdfc-e311-3e8e-af73-a75e1831dc89 | -1.7235 | -53.2486 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc5c4a6-59a5-3209-96f9-cda1154957f4 | -5.7677 | -47.909901 | 2024-11-28 00:41:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3b577310-710b-3301-aae3-de8d002fab0c | -6.4963 | -47.896 | 2024-11-28 00:41:00 | METOP-B | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d6b7915-56b6-321e-a184-1f1270a8ccaa | -1.0082 | -51.725601 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7f012e3b-0019-385a-850b-ed5c03d747c9 | -8.49 | -43.2757 | 2024-11-28 00:41:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b82dd985-2843-3b29-b7a3-0011bcd265f9 | 2.6613 | -50.9254 | 2024-11-28 00:41:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 100e74ca-3355-32fd-9fd3-7bc1b826935e | -1.099 | -53.358299 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90209733-8674-31d7-9826-209767b2a66c | -1.3239 | -51.755001 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b6cae5-fe1c-337e-9c65-a72c04a8c7ad | -0.6007 | -51.700401 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 997b3857-4990-334d-9645-acf5235c94e8 | -6.8316 | -44.390202 | 2024-11-28 00:41:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 913b98ce-ce48-318a-9689-a20477c7fbf9 | 1.4306 | -55.893501 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b734904-080c-3201-9287-fa29054b1fa3 | -1.2796 | -53.017399 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6544950-e56b-38fb-8dd9-db0ae13d332e | 1.2441 | -55.943401 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db95d34f-62e2-3c8e-9115-a03bd22b567e | -6.1922 | -44.423401 | 2024-11-28 00:41:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5de7d410-22d3-3a56-adc5-73a97e9ac6e3 | -1.6469 | -52.726898 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16cbd631-de2c-3bc4-814b-30083fe5ecab | -1.7952 | -52.744598 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec2b9aea-696c-3b2d-92b1-641effc1b227 | -1.6266 | -53.870201 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22787d57-f54e-3907-bdd7-939ab5b1ddc0 | -5.5116 | -46.256199 | 2024-11-28 00:41:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 432a0d1c-efc6-3e22-a44d-c82c54a9eaeb | -1.6723 | -52.4744 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b853ba07-1f19-32fd-88bf-47d3727a1955 | -1.6454 | -52.720001 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f8b250-f019-3d7e-84f9-db5032b7f9fc | -6.0973 | -43.9487 | 2024-11-28 00:41:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f8bfd09-59f4-3ee8-bb67-b896c0b41b3d | -1.3774 | -52.127399 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 161db9cf-58ff-337d-978a-951d017ac528 | -1.3978 | -55.004799 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfd92aeb-ede7-3df9-a1ba-a1d79e39d58f | -1.2909 | -52.109402 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff6046d6-06f3-3768-9349-9772cc4ab57b | -1.1361 | -53.6143 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2c639af-e702-377d-ada7-19c517a27421 | -1.5673 | -52.010601 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d1e323c-f9ee-3ea2-82c3-af0890309c8b | -1.168 | -53.664299 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bb9774e-5fec-3a32-b031-b04f167dc59d | -1.2159 | -51.733101 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8df846f2-af15-3857-a7ed-ecb8e401635e | -1.1947 | -51.7761 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40272d72-1b29-3fdf-8233-bfa223294261 | -1.4165 | -53.395199 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4b63d1a-a405-3e0a-96f8-53e51f89c010 | -1.5955 | -52.2715 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b37e2fbf-c6ad-3066-9ed4-7532e3bb188d | 0.1409 | -51.243999 | 2024-11-28 00:41:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ad9be4a8-9ccf-3a47-ba26-b6bacd6fe224 | -1.6805 | -52.465302 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15da287c-aa81-3bcc-b757-f00891794907 | -1.7921 | -52.730801 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a63c1a1-a284-34dc-b97e-aaceef71d0fe | -1.3794 | -52.546799 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18dff9c7-638d-3376-a54c-6f42970f3bb0 | -1.0938 | -53.380901 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9f8cb15-e1fd-39d7-acfb-e511deca7181 | -1.3191 | -51.915501 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 014a33d2-9a26-3f49-8973-20b13c5907c7 | -2.0219 | -55.9035 | 2024-11-28 00:41:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f926fbd1-5c86-3272-b210-bb6d60f0c60d | -1.3405 | -51.4188 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e42971-3414-3792-a8d6-7e45bbb37584 | -1.7165 | -52.624599 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c836b00-f2fa-31b2-869b-67f1dfbdf2ab | -1.6578 | -52.455799 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e22e10c-39f6-3935-9832-bd9bd88a3af6 | -5.9875 | -45.363201 | 2024-11-28 00:41:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47457be7-7fd5-3a17-9f10-281003f0c1db | -1.102 | -53.371899 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a693df2-f803-3780-a529-e00b8de30f89 | -1.5222 | -52.631401 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a631c2-65a4-3804-b45a-9f2deae3d024 | -1.6779 | -52.727299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3ff7a5-10fa-3407-a2c8-41b88a63262b | -1.1432 | -53.691299 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1516b11c-421f-3440-b122-3202fdcd17ad | -1.6732 | -52.7066 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccc3eb8c-3c9e-3dd0-beb7-dc96dbd1172a | -1.6558 | -52.492599 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eff07ac-0ddc-3fd1-94a7-100ab966632b | -1.2013 | -51.759399 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 775ed59f-535e-3c12-b758-76bdaf4000b1 | -1.5719 | -55.778702 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf794e2f-2e1c-3f59-bc68-b7acfaa866d0 | -1.6567 | -52.724701 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 157023cd-7612-303e-9c63-67285f255c2d | 2.6632 | -50.916801 | 2024-11-28 00:41:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 574380a6-dfae-32a7-b676-3347cda6e993 | -6.0876 | -41.955601 | 2024-11-28 00:41:00 | METOP-B | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0dcbbc3f-c4ed-3df6-b93b-5a0501a10fb5 | 2.0808 | -50.6245 | 2024-11-28 00:41:00 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6c20b99e-0ae2-3c4c-a2e9-72661a08e302 | -1.8035 | -52.7355 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c61411f2-0858-313b-9f86-aa1d9d298070 | -2.364 | -55.8689 | 2024-11-28 00:41:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49baa21c-f0bd-357d-a303-5bd3a1bfd47a | -1.6609 | -52.4697 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78be3d73-197a-3b22-a17e-6751c3340eaf | -2.1421 | -54.833302 | 2024-11-28 00:41:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acbf4dd0-51d5-3fb1-8e86-da59fc0027aa | -1.0984 | -53.629799 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c376a7d-60a8-305f-9f27-0cfad03c3844 | -1.2662 | -51.591099 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17ab8a10-6404-39b5-99ea-203a25b5e7ef | 0.9712 | -50.117298 | 2024-11-28 00:41:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 19175b3a-d8a0-3cf9-ac21-0386509ad322 | -0.5909 | -51.702599 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cf996ac1-6efa-3824-9d22-69b58948e193 | -8.5042 | -43.291599 | 2024-11-28 00:41:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d4a6378-ef7a-3c0a-8a01-a7f277d906ea | -1.5102 | -54.450699 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c18e279-eb28-3758-bfea-0b9a6d7c757b | -6.1017 | -43.966801 | 2024-11-28 00:41:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0475d67-3ccb-3b2b-9c01-5febc211a3e3 | -1.2089 | -53.891102 | 2024-11-28 00:41:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d728ab1-37aa-3ab9-a1b0-42e2bc813fe1 | -7.8354 | -48.1968 | 2024-11-28 00:41:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
