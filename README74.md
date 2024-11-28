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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60a3aaa5-66c6-32e6-af92-9571dcd0a2d3 | -0.36236 | -49.95266 | 2024-11-28 05:16:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef99ddd7-fc23-3c27-aa23-187bd030e404 | -1.74755 | -52.05106 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7a9de21-a81b-3c9e-978b-6a81206162d1 | -1.09072 | -53.37694 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1394a853-2e37-38d5-b4f7-625f90d6c8f6 | -0.46117 | -52.01657 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 185709d3-7126-39ca-8309-581184dc9b0a | -2.60546 | -46.83881 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2abcfce-4e4b-3c03-bd60-24c809ff8b30 | -1.48671 | -52.33505 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7f61677-3e6c-3ede-bdd1-e141206ef8ad | 0.19668 | -60.61132 | 2024-11-28 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05aad341-3a7a-3fab-8ceb-8360f09912e5 | -1.35628 | -54.62956 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3854180d-d58c-33fa-ac84-99be0202ad15 | -0.93577 | -47.55528 | 2024-11-28 05:16:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef530e6d-4ac5-3ec8-9613-bd4ef1df0bb8 | -0.46182 | -52.01722 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 947d1fb1-25b9-3442-9529-3d45f1f09ba6 | -1.62137 | -53.87481 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f25453d5-d0ee-338e-966f-7df9957cdd6b | -1.30515 | -51.73608 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac2bc2db-bd99-3b10-b0dd-32f2d63f73d9 | -0.26779 | -51.5057 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9e0e761-3870-36b7-8d38-87702814b468 | -2.43678 | -48.24389 | 2024-11-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e8efeb0-796d-32ae-b8f7-93c3330d9b6f | 1.44393 | -55.90289 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a127a4c-fda0-31f1-9075-f5c665b6ea75 | -1.23112 | -51.80513 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63b9ae78-6a17-33e2-ae09-b4fe1926eca2 | -1.64572 | -52.73212 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9829d875-224d-31ad-9421-47b41dc62e31 | -1.6871 | -52.4946 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc23df82-1997-34d1-bcb8-8ad04a7e64b6 | -1.67931 | -52.43398 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76c52ec2-10f7-32db-aced-86580669ade9 | -1.33382 | -51.95547 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abe163f1-3ca4-333c-b188-f4a2a4e80cd5 | 1.47542 | -56.0478 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89b48ef1-c173-3504-87fe-d6c86fe115fb | 0.98799 | -50.25343 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3153810-580a-3d62-ab10-5c3341ac5a15 | -1.65982 | -52.7114 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4162f875-0903-33bc-a172-a5c629ba552e | 0.94357 | -50.7402 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd72a7f6-570a-3dac-acbf-c46d46df2ff1 | 0.98574 | -50.12643 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7bdce815-fa7f-310d-89cd-b5c54412b118 | -1.0953 | -53.61144 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a4ae849-5ac9-3183-a1fa-2bd9fbfbfad7 | -1.6653 | -52.73132 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 05ebc24a-0bc9-3ea8-8d9d-ff66c195d9e0 | -2.01244 | -51.1894 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| df6409d2-ff49-3cd5-b3b6-5af084fbad10 | -1.15764 | -53.56714 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3d1d9c0-108e-3868-942d-e665fb4e96eb | -1.16814 | -53.67776 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eff19761-56ab-386c-872d-d1af747e9671 | -1.56378 | -55.78556 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0744c850-1150-348f-bdc9-15d34ab74bf4 | -0.95153 | -51.63206 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 068dda39-732a-3e18-a823-17eec54ec8f9 | -1.93889 | -52.09905 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a4e4854-5eeb-3c6d-b11b-ce6ab729f850 | -1.78433 | -52.74476 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68373780-5b72-3b7e-8a32-d4d8aea04d25 | -1.13283 | -53.15879 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a570bdb4-665c-38b8-b8bc-687f8155b121 | -0.99524 | -51.72823 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65b4bbd1-97ac-3624-a6d0-22eaebb0b008 | -2.8571 | -46.83801 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0124fb49-ff3d-3ae1-8073-f19ff1a88bea | -1.72321 | -52.48809 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4659087-e7bd-33fd-a1d1-5d45f95824c2 | 0.9896 | -50.26334 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e11aa7e4-c829-3ff3-a8d1-af7ce64364e9 | -2.86667 | -46.84699 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5f52536-242f-362f-9045-9ee75072b035 | -1.58946 | -52.08723 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b40d920-162a-3ecf-a874-b250444f39da | -1.36038 | -54.65192 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05db53f7-7aa6-3c2d-82b6-316ce1341bc4 | 1.43606 | -55.89676 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7cd4a89-945e-389b-b5d9-638879b1eebd | -1.60508 | -55.37799 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbe7616f-abe9-3763-9e81-d7453491e9bc | -1.63276 | -52.73389 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e704ef92-6d64-3fc9-8890-9b0ebf753b68 | -1.56547 | -52.01199 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18376862-98e1-32d2-9e85-15b6fde2ff74 | -1.23244 | -51.79667 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef6f0422-bd5d-344c-b153-7457a46ea833 | 2.08853 | -50.6292 | 2024-11-28 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e231384d-13de-37aa-a6f5-16eee8583ca2 | -2.38708 | -47.16542 | 2024-11-28 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3499be5-adde-3b1a-9743-86fcf7b156cc | -1.6538 | -52.94685 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a1e37ba0-a53f-37f8-aade-52d30518ec3e | -0.94789 | -51.65555 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5598b6c-4667-3575-934c-33db8b67059a | -2.84867 | -46.85168 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 831633d5-363b-3125-b2ab-11d3024c6d25 | -2.31025 | -47.86478 | 2024-11-28 05:16:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a69239ca-1604-3418-b9c8-1ac7cd0db0c5 | -2.8681 | -46.8499 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a294397d-f9d3-304f-8721-835bf5f8e47b | -1.70069 | -52.63707 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32d500b6-1f62-3251-baf1-0d6e3e2fd9d4 | -1.19956 | -51.74821 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc646b8e-a2c3-3632-a597-01b7be671ed6 | -1.78959 | -52.73794 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef73e8ea-9c0a-3911-bb2f-0f59a9eaea6d | 0.98101 | -50.12725 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4676e52b-e5d8-301a-bff5-959998f9f34c | -1.38334 | -55.00892 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1f719a6-903a-33cd-9c66-9e6291b2db72 | -1.18631 | -53.88191 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9aca788-6435-37ae-a304-9487986e0f7f | -1.47466 | -51.542 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6527c9e5-ebcb-3eef-8361-e5073a61c6bd | -1.7543 | -52.70309 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d80d69c9-c088-382d-8b31-c69064b48d42 | -1.1353 | -54.21506 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7397ee2e-946a-30ac-8f1c-73884fb22916 | -1.63054 | -53.86621 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d33735bd-eb82-38b5-b2a3-ef5f4f7a0318 | -1.36112 | -51.96204 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 416c0792-5e43-33f3-b83d-9f824730aa3d | -1.6865 | -52.49845 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3fbc536-0384-3792-88cd-2911dc86d20e | -0.24464 | -51.59745 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c02e90cd-9ab4-3c50-b458-f4d9590224c6 | -1.47346 | -52.67982 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a81473c8-5b73-3592-a793-f04f2d37fdf2 | -1.07815 | -53.38024 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0fbdc55c-d772-34d8-bb4e-ab85a89ee9d0 | -1.79372 | -52.73859 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b60f4eb-b3d7-330c-ac08-29053b3d6990 | -1.35181 | -54.63442 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c7e20ec-ebcf-3da8-87e4-01b8727e1f3f | -1.61867 | -52.46424 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11f60a24-3823-30b9-b3f7-bd086afd36a8 | -0.26755 | -51.62253 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a2839051-72b5-3e6e-a9c6-36854887789e | -1.45201 | -54.51954 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37cbf280-8c9b-3a2d-b53a-3e37587b98c3 | -1.5364 | -46.06673 | 2024-11-28 05:16:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 968c15fb-5e0c-370f-9d8d-4de98cb6c2f7 | -1.33078 | -51.94653 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 505e41ec-6026-30e0-bf77-d6c1000b61d2 | -2.87222 | -46.85281 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 843a2a48-f2e2-3f21-9888-8f9b12040171 | -0.46058 | -52.0205 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1cab944f-6c82-3a23-9765-886f04e6461c | -1.19826 | -51.75671 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f384987f-535d-3182-90ff-26a8482817ba | -1.66284 | -52.71951 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5211414d-cf07-3e62-9e89-17e377f0687e | 1.45398 | -55.94544 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bbc9f2d-1981-32d2-91f9-06dd20f1cac7 | -2.01706 | -51.19011 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 52e52835-9b99-3e19-a419-9b41f90e1e64 | -1.69265 | -52.49121 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38486c3e-e6ae-3bf5-92ff-6375c9b820e6 | -1.09221 | -54.03914 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfd830df-81e0-314a-8cbe-324f699bc4ff | -1.16117 | -53.67185 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cdceba9-8a03-3fa1-956f-2e14692dbaa7 | -1.3598 | -54.63125 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d8f9b66-9d9d-3110-9dc5-472a9c772128 | -1.15573 | -53.68143 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e86f633-385c-3686-9501-6060230cece4 | -0.94748 | -51.65776 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30739e91-043b-35ca-9de5-38c832309f62 | 0.98491 | -50.2641 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c8b5ddd-7db4-3298-b342-f45bb22a2eef | -0.9928 | -51.71491 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa652135-36ad-3d02-9859-23731d9dc3fc | -1.65275 | -52.71417 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3be6a384-5fd5-348c-8fe0-8fee9094cb4a | -1.6913 | -52.49525 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c4b9bca-0005-383f-8e88-886ca839b744 | -0.95525 | -51.63703 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa0265d4-21e4-372e-a454-098b969d7e7b | -1.31329 | -51.74173 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b95d6760-9450-35e7-8ae2-518cb3ae89f7 | -1.58807 | -53.83517 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e0d1d9c-048c-3a1b-b26f-5021efe910d7 | -1.39141 | -54.98074 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35eeda86-4e37-3203-9c74-42943a3a5c2d | -1.16346 | -53.68242 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5145253f-e74c-3ffa-b1e6-035af0b88381 | -2.84656 | -46.85366 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c71c73ea-51c5-3239-ae69-e2c6d780df0d | -1.68787 | -52.49442 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a52b06d-42ad-3924-9ab2-f2bef60ce5b2 | -1.44815 | -52.4444 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README75.md)
