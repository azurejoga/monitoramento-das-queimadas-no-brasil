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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9131f32e-333a-38c5-a1e5-7ff2c743765a | -11.47718 | -50.7907 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b64cb62-7469-3aa5-82a7-4f4db166f5b2 | -11.86293 | -50.49755 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6cce271-dc6f-3c5d-ae8c-991579d9eeeb | -11.45518 | -50.80151 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64e4acbb-0695-371e-970d-df66476d108f | -11.86993 | -46.75768 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8225bd1-2746-308f-a57c-f8b99b919821 | -12.11887 | -44.83533 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04eba2c8-fe08-3684-b2e8-25aecd817cad | -6.98813 | -44.54423 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0327a12e-7454-3f10-9478-c4ad0f7124e9 | -12.14234 | -47.59601 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87c5f3d4-969a-3910-942b-6e4822df4f0c | -12.0427 | -46.54091 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ddf6a74-b375-309d-baf0-3b868ba22d09 | -13.26066 | -43.79372 | 2025-09-14 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 345d5d6e-b2b0-3ef4-b20e-29692b1f700f | -11.89762 | -50.53895 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81804a9c-0e10-3880-a2c0-76fff7d5e890 | -12.93141 | -47.94715 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4cd5c05-85f8-39f4-bbd8-6b6e7751f107 | -11.13507 | -45.32742 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f5eace9-2974-3d57-954c-ca652002aaad | -10.35414 | -50.48744 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f21a1837-11e2-39d6-a2b4-2a5596173b2e | -11.4502 | -50.76844 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab3e5fd0-101a-3cd8-96a7-36303e299e14 | -12.25524 | -46.79412 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a12c7f3-5b62-30b9-8191-d60ba7d4fc8c | -9.80581 | -48.39637 | 2025-09-14 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7febb96-dd86-3437-89ae-b082fdfa8e27 | -10.43109 | -48.59715 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcb30f58-a0ca-3cba-92c7-17cb041eebe2 | -12.06909 | -45.63349 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3888ebe0-c982-315f-ab94-a032793afe50 | -13.94087 | -44.83234 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 5acd7f6b-b2f7-36ad-a083-69edbbb0ad9e | -11.47385 | -50.74714 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08bf23ef-04f5-36db-8522-8aa74cdf00de | -12.97058 | -47.99609 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68f75a1f-e8bc-38b0-88e3-64eb8f0aa350 | -13.93867 | -44.84952 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 7c7ca258-ca85-3b67-a6fc-247c9c2533ba | -12.92784 | -47.9465 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0baae4a-edbd-3754-b46e-ed9dc811723e | -11.48211 | -50.75922 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a4999ed4-245d-386a-bcce-81eb669fa6f3 | -11.37843 | -47.34256 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 341eb733-4634-34ef-ad63-cfa9820e0e66 | -12.14294 | -47.59177 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f18dd518-2bc8-3415-94df-9be27da21791 | -12.78983 | -47.14151 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 246fbaef-ebca-3ca4-834d-3121e529a64a | -10.40004 | -50.5875 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1231c78-2aef-3d55-b54a-5dcc9ab1b362 | -8.13674 | -43.66443 | 2025-09-14 04:40:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f0c1d78-2fdb-39b4-8695-ddd83fe2c4e7 | -11.46012 | -50.79155 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e501a30-3225-3f7d-8c00-2de7aaad2345 | -13.93043 | -44.84406 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35451d0c-aab6-3a1d-8245-935f70d4989c | -12.79688 | -47.9758 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f736d42e-e899-3f6f-8527-db8ba221bd15 | -10.89504 | -48.19039 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cedba87a-d2c9-38a6-9e47-b7d59477d161 | -10.3459 | -50.49684 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c3c5e6a-f299-398a-9729-686a8e29b27f | -11.49424 | -50.78986 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 403a4689-e4bd-30c5-b066-b3f5d42945a3 | -10.89676 | -48.17881 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d76b7561-3394-315a-b118-fc61e6b660c3 | -10.34096 | -50.50677 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60295524-f052-33e5-a02d-065a4efc3da0 | -8.17721 | -46.77828 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2deffcfe-e1ec-339a-b8f9-f92edf97ff78 | -12.80174 | -47.96756 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9d8dbb0c-031b-3695-8dbc-106b652a9b45 | -12.93012 | -47.95591 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ece593c-e6b2-3617-a27b-56defd5208af | -11.44495 | -50.47303 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a1ebcf17-9466-3ab8-86f9-3a7b2c4cceb0 | -8.93454 | -46.15844 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e863b81-cbd5-368f-b2ad-d73a90795afd | -13.93098 | -44.8397 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0df22b94-382e-395b-b2c4-ac8015677b18 | -11.37538 | -47.338 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca0fac28-1869-3d32-a4fe-690e54800977 | -10.88923 | -48.18157 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f171690-a834-3878-b989-71c3f75158dc | -11.48818 | -50.7853 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ecfb1a3-fdf1-38a6-932d-b85b83c22704 | -11.13309 | -45.31193 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27caf056-f190-3bde-a283-42fdcd37b534 | -12.96889 | -48.00775 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 953c785a-9a74-376a-b419-bf46a5fb3d09 | -11.30335 | -50.83757 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 475ea5ed-0164-3f00-b21f-ded915062d94 | -7.7255 | -45.3189 | 2025-09-14 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52044281-2440-36fe-9003-2e5077d4093d | -10.21114 | -46.75455 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c2ce928-d5d9-3d95-9fba-8458b686d5f0 | -11.48466 | -43.61213 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f0af80c-4d8f-3fb0-85c8-9f340e508ee2 | -11.46558 | -50.73505 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25170805-c146-3c8f-a700-d9bef53ed284 | -9.17529 | -45.58113 | 2025-09-14 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d4b0c1f-8dfe-35e6-8b51-51b50134aef1 | -7.56894 | -44.38474 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48f007b9-874c-3063-aead-d96cd2975527 | -12.9825 | -47.98959 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 178932ea-5c92-348d-8f35-4591b4221b3e | -12.78674 | -47.13636 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95235813-4862-3871-b61c-8b7ee19243a9 | -8.14229 | -43.65657 | 2025-09-14 04:40:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1941688e-ed57-3e84-9f5a-c4b6ee3e5ec6 | -11.45076 | -50.78646 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36e4a80d-2616-3d3a-93c6-1a7ef990a0dc | -11.46837 | -50.78212 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb4a4ed6-5bd6-3ecd-a119-7c7cdfd95e2b | -12.09024 | -47.56408 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5f2ba33-6ab6-3020-8f7e-9a3343effa7c | -7.6074 | -49.60487 | 2025-09-14 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9053d81b-386c-3b25-82a9-3bc543090ca1 | -7.22688 | -49.31727 | 2025-09-14 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cd9a72e-5191-3c23-8453-4337486176a9 | -12.08511 | -44.72598 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 796c1900-c449-37f0-a738-195e783bcec7 | -12.76956 | -48.01287 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1322d02f-4f40-3e0e-a17f-c475f37a838f | -13.28791 | -43.78808 | 2025-09-14 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5c24cca-15d2-343f-9d56-1b0a4c7bb087 | -9.70802 | -46.92475 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dcbd67e-660b-3b28-9e23-52c2e99883c6 | -11.49918 | -50.7799 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f4d883d-ffc7-3723-b627-c7bf0aaddec4 | -11.3039 | -50.83407 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52093144-c94f-377a-b75a-b3ff210699e0 | -11.47312 | -43.59808 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cccc5df8-9066-3e35-b331-7cc467256732 | -12.76896 | -48.01701 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63e967dd-6278-32d1-9c75-9db4b32e9989 | -7.88164 | -49.50224 | 2025-09-14 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbc7494b-4343-3134-a452-51a25bd863cc | -12.81709 | -47.16438 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fb05a82-9b26-3fe0-a6f6-24c5ff0ad400 | -11.32531 | -51.14987 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7619a6c-948b-3e34-8151-a3801597df8a | -13.28853 | -43.78304 | 2025-09-14 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3962df7-53c5-3364-9d4d-690f98bd9c6c | -10.39509 | -50.59743 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98e11af5-76a6-3d1d-bc41-06a0eb6a0a14 | -11.13739 | -45.30741 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bddef49b-0a3d-39ad-8b5a-a29e5327d42a | -11.86733 | -50.49106 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c20674dc-e609-301d-9ae2-714035c3b133 | -13.94922 | -44.80222 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26bdf79c-1053-370a-abc5-7d6130c15db3 | -8.50556 | -44.7261 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7370001b-f46f-353c-b3fd-71d22ddac4af | -12.04051 | -46.53816 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8441008a-90de-34d2-a955-635bacba8890 | -9.62301 | -40.61977 | 2025-09-14 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6264a59a-c4c6-32fe-9307-3ccec3db51c6 | -11.47439 | -50.74364 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a0e9742-fa70-3d15-998c-9138264d1546 | -11.78485 | -46.64844 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 269f57b4-9432-3043-9bcd-a2672937fcc6 | -7.44378 | -44.38617 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf4f8923-5c30-327a-b958-f90b172dd9b9 | -7.85214 | -46.09436 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 558bf04a-b8b8-348e-9194-ab39865bec7a | -7.52322 | -47.63447 | 2025-09-14 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa7e7e29-3100-37d8-a428-36725540b56e | -11.5036 | -50.79494 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3cb6fe15-9eb4-3f55-8b75-1c4d4116d147 | -9.49134 | -46.40583 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8a53d23-dec6-34bc-8682-917ec7afef72 | -10.78894 | -45.9849 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90dd618e-467f-31b8-a8f5-130c220d1164 | -10.4396 | -48.61006 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e098a28-8f4d-3292-a0f0-76bf22f0a481 | -11.46288 | -50.79557 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a21fccd8-607b-3771-a02a-afcd52645e40 | -10.96266 | -49.56575 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf427d5c-057d-39dc-9e02-afb104494af4 | -10.35798 | -50.48448 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0762e03c-3dd9-3dfa-9ba8-cc5ba03307c1 | -11.83979 | -50.49385 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18dfd082-75e3-3504-9984-7a087181bbe9 | -12.93435 | -47.95205 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b72c987-12fd-3ca6-9731-279818d12df8 | -11.14407 | -45.31979 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e63ffd75-d080-34b4-99b2-6e9d23330f0c | -11.31373 | -51.15879 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f079986b-8222-3a62-bdfe-3cb7f3999ea9 | -11.77678 | -46.62336 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8db2802-8c9c-320f-9faa-3bf2974ed993 | -11.45792 | -50.78402 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README39.md)
