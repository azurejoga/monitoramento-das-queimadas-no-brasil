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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d271ba76-7334-3ff0-a804-76ca5e95e41c | -3.05586 | -53.24212 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 883091e7-ea1b-3d7e-81bc-7c9aeb3c401b | -3.04963 | -53.25962 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9396c67c-9d9c-3502-acf5-24d84f7f9cda | -3.7159 | -52.29536 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ae71c66-4122-32f0-921c-3e2981161d9b | -3.71312 | -52.29139 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa599b3f-2b1d-39b6-9010-ae07ba135374 | -2.66242 | -52.57618 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da44699a-4e0e-32f8-b83a-64ef1faac796 | -2.66186 | -52.57971 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3f6fae6-6b42-3ba8-b364-490799f1bd8f | -2.65907 | -52.57566 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5a27d13-712d-3043-b595-94b1b71988b2 | -2.65851 | -52.57919 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ba30d0a-31f8-343b-9fa7-cf4d82c424b5 | -2.32166 | -52.94048 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28bf805b-c03a-3f45-b915-e586dc11f2ce | -2.09141 | -53.40033 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 602707de-d7be-38cf-ae9e-c721c542b66c | -2.09082 | -53.40403 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c2d004d-aafe-31c1-be2e-21795200dc26 | -2.08798 | -53.39979 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 992db29b-5623-3eb2-aac3-2b27d59dc5a0 | -2.08337 | -53.40667 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ac4e427-43bd-3651-bc3d-1ea650f2c9e6 | -2.07994 | -53.40614 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60e023e7-751c-300b-9b5f-edd635fcba47 | -4.17606 | -53.55751 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b99a6858-671e-3683-8d43-9fa12695fc5a | -3.95208 | -53.40723 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79a388c1-1a80-3f4b-9b57-ada69fbf4dc1 | -3.89399 | -53.64021 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9e13a69-cae2-314d-94fa-b8e8722493aa | -3.89343 | -52.41243 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d91b80-24c5-38f7-b862-791f0adff522 | -3.88994 | -53.5348 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 953221e6-169e-3467-a387-f54aa23a4fb8 | -3.88334 | -52.34692 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e273166c-acc5-3dc5-b170-1e862f71e838 | -3.95547 | -53.40776 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea3f5c45-530b-3c87-95de-53702fb3432d | -3.88721 | -52.34398 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2d67f70-31d3-3566-ab0d-db25fae0374a | -3.88666 | -52.34744 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc5c51a-be1d-3881-a13d-560333276ea6 | -3.84806 | -52.35857 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a67cea7e-37a0-3a3f-b5a0-0ad86cedcc26 | -3.75434 | -53.39917 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adc4ce42-9b17-3c89-8ead-878060471734 | -3.74785 | -52.41041 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| b3c91464-d4ad-3540-83f7-2490b063d911 | -3.74453 | -52.40989 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eafe85ec-4ddd-3f08-b70b-ddb3636ebe4f | -3.74254 | -52.32087 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8558799f-9bfa-331c-a82f-cd528588cfd7 | -3.7128 | -52.40143 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ca2964-d638-3c94-9bf9-b05870e9de89 | -3.70948 | -52.4009 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73541c59-8b61-3fbd-81a4-184b259623be | -1.32597 | -54.66549 | 2024-10-19 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 805877a0-cee5-3c04-89ae-aa00ef97d21e | -1.03559 | -53.73395 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7454696a-d4f0-3b2b-84b5-f2681416def5 | -1.03485 | -53.73459 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f121b482-435e-3434-a451-e8c80b2053d3 | -2.09232 | -53.57215 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ecc090a-c299-3148-953c-3b415562d811 | -2.09172 | -53.57589 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ab13fdc-98cb-342e-853a-e7fa9503885e | -2.08827 | -53.57536 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11c0d9a7-e873-34b5-ada8-334b2a268175 | -3.32825 | -54.08137 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d58d59d-dc92-3f86-9306-adce53edd103 | -3.32477 | -54.0808 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 458901c5-cad0-36fe-b9c3-7719fabcd99e | -3.59229 | -54.68256 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88716abe-c4f6-3129-ac73-debe7f4ad139 | -3.59023 | -54.68363 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 985e141e-8f96-3f83-bc5c-0a1559464966 | -3.58808 | -54.68599 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31aabaa2-07e9-3d44-bb9f-6e1391d6d123 | -3.53905 | -53.85022 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a2eefee-fad6-3eaf-9be0-79ffdb068902 | -3.53845 | -53.85396 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3495c9bb-e0d0-37d1-b9d9-eeccf306cd4a | -3.52921 | -54.56321 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fbb2f99-28e1-350d-80c3-a10e634b5ee1 | -3.49657 | -54.45298 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b8c551-1e94-3201-9abf-1b6012a6b00d | -3.49595 | -54.45691 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c74fe5c6-bcfa-3e21-b3d6-ed48c5e5846e | -3.49304 | -54.45242 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 278a869d-370f-33c1-bd3d-85b8f9568181 | -3.49242 | -54.45635 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 315b4edf-7345-373d-89de-7c5165b487f6 | -3.44918 | -54.63674 | 2024-10-19 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7865c10c-a2d8-3af3-84b5-c652a84eba29 | -3.44077 | -54.14587 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f165c25e-006e-3548-8c24-7089fbab7530 | -3.44033 | -54.1261 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26ac97a0-55c2-33d2-930c-4bfed614883b | -3.44017 | -54.14972 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58d4334d-8d72-36fc-80dc-f5422bb7b95b | -3.43729 | -54.14528 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c90c0339-fb71-3cae-b03f-acaf1137d180 | -3.43685 | -54.12552 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45b80528-6e10-3bc6-b030-1450bbf9ef30 | -3.43668 | -54.14914 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d0f728e-fe27-38a3-9e63-93b2f0e0bbc7 | -3.43607 | -54.15299 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d7fc34e-e463-3fbf-85f2-2dd7b016c80d | -3.4332 | -54.14856 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 294bdfb6-eac6-32d1-ae9f-1c6b28a899cf | -3.42972 | -54.14797 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92fdff67-15e2-33cd-995c-956481ac92f4 | -3.42623 | -54.1474 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc52c049-19ac-3d9f-8f80-c27064d88062 | -3.42275 | -54.14683 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d197e3ab-3500-3a3a-8619-96919c53d7f8 | -3.41926 | -54.14626 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 266fc51c-2e08-3edd-b212-311c53c27693 | -3.41424 | -54.67231 | 2024-10-19 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb448e8a-ea8a-38b0-a447-ee275f62af35 | -3.41066 | -54.67176 | 2024-10-19 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a279fb-fd7e-3d77-8ad5-ac04c11fd565 | -3.39952 | -54.06869 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea8a9355-1b30-36ce-b935-301ee384f1cb | -3.39891 | -54.0725 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb80001b-9a2f-3473-a151-674ddc615ea8 | -2.61868 | -54.00897 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7227b91c-7515-3110-9544-5930c9b76b23 | -2.56734 | -54.01303 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbdf9de3-8589-3c50-8b8a-79d5aaadc0da | -2.56446 | -54.00861 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8c75d85-ae36-3945-9665-945d444e283a | -2.56385 | -54.01247 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 486819c7-2389-3766-a710-33ace6e17289 | -2.37321 | -53.82737 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfef9b27-9eae-3af8-841e-3661bf169b24 | -2.32965 | -54.37696 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86d39cc8-2eb4-3436-9433-4587cdb78660 | -2.32902 | -54.38097 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5dd9362c-6baf-3f05-a715-2863fff37cdd | -2.32839 | -54.38499 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e7a82095-1288-3786-8e5b-9dc54af3f7b7 | -2.32546 | -54.38041 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 560632bb-58ba-3028-944c-95072194a981 | -2.32483 | -54.38442 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29bc9efd-0a7f-34b7-96a9-fba99a449d89 | -3.66271 | -53.84294 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8962477a-dffe-3f9a-b318-28c9926f3121 | -3.66213 | -53.8466 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 759793f5-c6be-3bf1-8f8c-561cfac5804d | -3.01326 | -54.35998 | 2024-10-19 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62206695-c4f6-30c3-a08d-a684a577634b | -2.95393 | -54.14652 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea60d8b8-9082-331c-ad27-9948ffec1597 | -2.95207 | -54.15812 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05d1c5bb-da8e-30b1-988a-37862711d07c | -2.95164 | -53.70296 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06676a27-d44f-33a1-a06c-241f9290ff5a | -2.95105 | -53.7067 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f49f3861-9dd0-3cc9-9f2e-e9b7d1c6d5fd | -2.95043 | -54.14595 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7618ad4-eaae-3de3-9d50-fe56cb8d4f80 | -2.94981 | -54.14981 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d681c531-1a1c-39d0-8df6-35e06ce1536d | -2.94857 | -54.15754 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 632e8490-8269-3bb0-bc3f-62d97bb612bb | -2.9482 | -53.70242 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2c3fd96-3cbb-310d-89d1-df244ecb36f9 | -2.94761 | -53.70615 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d2db8c5-f85d-3dff-94c4-4fcf17509c18 | -2.94357 | -53.70934 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 095f6f92-192c-3d7e-8bf9-b8fcf63a9ec4 | -2.94013 | -53.7088 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf030d5d-ec33-332d-8924-eecf7e5af524 | -2.91756 | -54.03086 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4be5581a-49e9-3b89-a11b-f060ea7006ab | -2.91695 | -54.0347 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37d881cd-65c5-3a21-9b82-96eb19704048 | -2.8853 | -53.98652 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3876a1af-c5e3-3419-8b33-4d2b408c4fca | -2.87563 | -54.18263 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 151af771-030f-39fa-a12a-695b45b973ed | -2.87501 | -54.18651 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 203e18d3-4655-3cc5-af57-d16d9731d6f2 | -2.87212 | -54.18207 | 2024-10-19 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80946b0c-744e-33c7-9013-18bc362b91d4 | -2.83073 | -54.86756 | 2024-10-19 04:49:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c8b7c82-e2e7-3ec1-90c5-f4668caac170 | -2.80578 | -53.98666 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 49126848-b7b0-3c21-8af7-0a9ff080b1be | -2.8023 | -53.98611 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ca56bc15-bd23-3770-9b41-85ebaad10902 | -2.79881 | -53.98556 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcf0e378-2183-3db3-a8b1-cfd70c6757a4 | -2.79821 | -53.98939 | 2024-10-19 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
