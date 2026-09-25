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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ae4a308-3e84-3f22-8657-d303b3d1dc12 | -18.4236 | -47.20275 | 2026-09-25 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23efc33e-1d7d-380b-96cb-b208e61e8936 | -15.1841 | -56.05622 | 2026-09-25 04:46:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 561eff09-48c1-3554-92cd-60d6a2b00d87 | -17.10444 | -46.46953 | 2026-09-25 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0d5aa6b-e7f6-3041-81c9-0592b6cd0da4 | -13.52158 | -59.31429 | 2026-09-25 04:46:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6170f5bf-8872-3ff8-ae9a-a2f5b21c0ce4 | -16.11786 | -49.94543 | 2026-09-25 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9692c0e7-05b0-3365-848a-1c8cb7b76672 | -15.81848 | -53.11278 | 2026-09-25 04:46:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aae69b06-b153-3152-8e46-3147d2f667a5 | -15.63941 | -49.58746 | 2026-09-25 04:46:00 | NOAA-20 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 224b2794-6626-3e00-a85d-da8e8976880c | -18.08945 | -51.146 | 2026-09-25 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8ef8a4a-4e8b-38ae-9fbf-716dab53a65b | -14.55788 | -54.12606 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 323f8974-8041-3d3f-94a6-0dfa58fcce81 | -18.95639 | -46.9519 | 2026-09-25 04:46:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 123d43f7-343c-3b41-8e79-8bd2f417fd92 | -15.07521 | -52.80077 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a46fa0a7-eb53-3f0c-a5ba-270445857dc7 | -18.95688 | -46.94803 | 2026-09-25 04:46:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46f025c0-a7b2-3161-a30a-3f2fd24d1b44 | -19.37567 | -46.3214 | 2026-09-25 04:46:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f130e51e-c7b5-37bd-be5e-99d5de07b76b | -16.53235 | -52.4688 | 2026-09-25 04:46:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2ed90d5-3d9d-34ea-9d19-26377aba1d1c | -14.46836 | -53.64868 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d68233df-9982-3205-a799-e2e6a7d4103b | -19.11196 | -43.87389 | 2026-09-25 04:46:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d77b9e-40dc-332d-bd98-7b6838b1fce5 | -15.81337 | -53.11197 | 2026-09-25 04:46:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e011cc05-3f55-330c-9d0b-1d1c8c354710 | -16.05101 | -45.02621 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a916927-34bf-3487-8dfa-0c87a3b6750c | -17.34459 | -46.93559 | 2026-09-25 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5245b9a-d1f1-3cbe-bd81-ed78b7d56927 | -14.46966 | -53.64096 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e987bbbc-29f6-3b62-ace2-dbcc49336977 | -17.04898 | -50.87641 | 2026-09-25 04:46:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 599f8266-704d-3715-959f-9984fcf115ac | -19.11164 | -43.87677 | 2026-09-25 04:46:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99193b18-3136-331f-ba9b-0263fab891ca | -14.55721 | -54.13008 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa9b1ac3-1bd3-3a31-9a40-8655ae3dfe2e | -17.95782 | -48.79252 | 2026-09-25 04:46:00 | NOAA-20 | ÁGUA LIMPA | GOIÁS | Brasil | 5200209 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 048768a3-561c-3fa9-ad89-80611040a980 | -16.69871 | -50.66534 | 2026-09-25 04:46:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 449b5bbd-a95f-36aa-b0b3-952ec884dbb7 | -14.5549 | -54.10077 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88c17229-4679-386d-828d-604100394542 | -16.00369 | -56.32442 | 2026-09-25 04:46:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1fe5226c-b31d-30fb-89fd-6355e138b9f2 | -15.43563 | -48.48907 | 2026-09-25 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 231098ab-c78d-3812-bb47-2831725c5009 | -14.99378 | -56.31218 | 2026-09-25 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b4b56c9-f550-3a35-b293-f330fdf07d8f | -18.60691 | -48.25691 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1fc9349a-c53d-38f1-8416-6ee28a2541bd | -18.60591 | -48.25879 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 334f7c66-c033-3811-9624-e50a65af419b | -17.76417 | -46.63153 | 2026-09-25 04:46:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ecf94dc-378e-3387-8946-1f76cf68fa6c | -19.18505 | -47.3601 | 2026-09-25 04:46:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8feea6f-e93f-396c-a05b-be731e43cd94 | -16.69815 | -50.66907 | 2026-09-25 04:46:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cda5386c-6b89-3913-8ae5-a5130acf6121 | -17.58935 | -54.04994 | 2026-09-25 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76931272-bd3b-3bcf-a7e1-123d7d4fc555 | -14.55869 | -54.12542 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea500148-049d-3706-9768-02f2483081be | -17.10392 | -46.47345 | 2026-09-25 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 943ed5df-89c6-3c58-99ec-7fc495a5ae44 | -17.09975 | -46.47293 | 2026-09-25 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c939355-96b5-3a91-a0a2-3a7e32beb739 | -14.57341 | -54.12377 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89f100c8-acb5-362f-8b8d-4ac283bac7d0 | -14.4703 | -53.63713 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b1c4953c-5c24-3963-b5cd-445c05104079 | -14.55841 | -54.10133 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ecc5f4a-002b-3bb3-9f3c-5bd6a8fa09c5 | -17.17004 | -56.64412 | 2026-09-25 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f455311d-0178-3e7f-95ed-dae4db22dbc0 | -14.56013 | -54.13805 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d67b95b8-329f-342b-80d9-f120806cee3a | -15.33308 | -48.11426 | 2026-09-25 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3747258a-b4a9-3bd9-8c73-642288530c77 | -18.11774 | -54.51907 | 2026-09-25 04:46:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44d9f96d-6dda-3437-98ee-4a9ecba28a2f | -18.42684 | -47.20339 | 2026-09-25 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 411154e5-b58b-3ce0-a3ce-ab57a1c3898f | -15.43203 | -48.48846 | 2026-09-25 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22870f90-fd06-3c3b-93d7-15b1341512e2 | -16.05159 | -45.02155 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 637c41ec-f020-3062-ac3f-21f43bbbf762 | -14.46901 | -53.64481 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c3996ef-5a98-3087-b601-4e6893d0aff2 | -16.00457 | -56.31948 | 2026-09-25 04:46:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d20363a2-6805-34be-82b0-ebac846c5b5e | -14.558 | -54.12944 | 2026-09-25 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14d4d0f8-5b46-3eaa-8a08-d9e3b4d15625 | -15.81397 | -53.10831 | 2026-09-25 04:46:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5385b569-9f86-33d4-bd81-93651280a259 | -5.35129 | -49.03797 | 2026-09-25 04:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87e47ce9-bdb9-3227-a75c-71c501e090a2 | -10.56319 | -59.48498 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a80bb30-64e4-30df-9b1c-954809fa6ffc | -9.01782 | -49.64985 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a49ab8e3-3f35-39ce-8496-37602c8def53 | -8.94641 | -45.89051 | 2026-09-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44484ada-a04c-3c62-a466-db7c820d67eb | -6.67958 | -55.04982 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dc2c711-47a5-368d-915c-24a5053c10f1 | -9.62564 | -43.96338 | 2026-09-25 04:46:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 97bd015b-378c-35ec-b502-9cef9b149e47 | -9.40995 | -44.52809 | 2026-09-25 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 205fb876-a924-3eff-a238-d3fc015d9ac5 | -8.33236 | -55.27901 | 2026-09-25 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74bc2c0d-005e-3f1b-9269-87e3219bec7a | -5.35074 | -49.04143 | 2026-09-25 04:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e59cdb2b-fbba-3bf1-b3e8-2f7a4d8adc94 | -9.01928 | -60.52335 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 384e9a24-40a8-3fd9-8954-a4e643f158fe | -10.92493 | -43.85989 | 2026-09-25 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9efeeb18-b8bf-35ec-b595-d7620e809593 | -8.31927 | -44.12997 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44fac7e0-e184-33b3-a212-ea1312f03678 | -6.65595 | -58.56908 | 2026-09-25 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa85d1a2-b9cd-3498-9fab-5c055aec0655 | -10.62646 | -51.35077 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d552a89-dc4d-3f2d-9c53-7e6f9277249a | -5.97702 | -55.37508 | 2026-09-25 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0a0a387-51de-38de-a435-6cd42f47cc03 | -10.2371 | -44.62395 | 2026-09-25 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 247eb364-12e0-3459-8207-40190bfc3adf | -12.21367 | -50.79092 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c15d66dd-b3d9-3868-8c95-9e9eb354854f | -10.294 | -49.95638 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14112882-5771-3480-ac7f-a5f5a0b0f7e1 | -11.27922 | -51.30587 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6294509-ccf1-33f0-aae0-169dabf608e0 | -12.22526 | -50.80364 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d74dd12a-d856-3b68-b521-b93c2c20c744 | -12.19491 | -50.78064 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd64ea3c-6c38-311d-bc71-f218a3faa101 | -11.27258 | -51.30478 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ead34198-0544-389e-a5c0-76dfb481bcaf | -12.21478 | -50.78388 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9ce2bcae-1fc8-3263-a174-95ea5bfe4f00 | -9.73282 | -54.80629 | 2026-09-25 04:46:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b4c8cac-5722-3cd6-89e8-7c08086da664 | -11.72102 | -50.55612 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b676f025-8fd6-3dc5-b3d1-37ac32b8c9e6 | -12.22198 | -50.75977 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 9fddd396-f467-3656-bea7-476eff658f28 | -10.55686 | -59.49029 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10638434-cd8e-33c8-b94b-9589ec398f2e | -12.23024 | -50.79362 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 695bd3db-b4e6-3671-9631-56ba24c968f1 | -6.1378 | -57.80346 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85099a0f-f276-369c-b391-742b3afb34b6 | -11.27597 | -51.28362 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87780bf9-2430-39d1-8e57-e0dfc745e8a2 | -9.14729 | -59.48893 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4f19d30-89c5-3b36-ba5d-52b53840457a | -9.14741 | -59.47845 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b71e4dc-068e-3e26-bba6-8e92119b7825 | -12.21757 | -50.7446 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3d682d7-7787-39d9-a052-5170db067d97 | -8.33202 | -49.5194 | 2026-09-25 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f03a476-bc47-35f0-ba6d-537c653710b2 | -12.22361 | -50.79254 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73b89436-af49-3e04-a25e-24111412c871 | -11.15129 | -50.65818 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 52cdac55-081f-36ab-8ce4-63e0a3623152 | -11.15406 | -50.64066 | 2026-09-25 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59cde836-6a4b-3aed-9870-828a32f6a5ce | -10.72533 | -53.9909 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4611d52d-1966-3a06-8ab5-65f9d716499c | -10.4181 | -53.78874 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65076ae1-c1c0-39ab-9da1-ad57ad1f0da1 | -11.27209 | -51.28659 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bcdfe5e-666a-3a48-a828-5dff11dce08b | -9.18026 | -58.06788 | 2026-09-25 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a905665-c36a-33d1-b793-46b6203b81aa | -11.70391 | -50.55689 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4beff72d-398e-3371-bf5f-6d55ed2c78bc | -6.67566 | -58.57922 | 2026-09-25 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef372a35-9749-30a6-8ecf-8b6be5eeb39f | -6.19638 | -57.79176 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6de07c7-80c5-3d1b-8152-b1a6e40b2757 | -10.89729 | -53.93015 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c65c9e0a-3f4c-31e8-a1b4-5fe5d6b9b05f | -11.97524 | -50.70926 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c709292d-d145-3dd0-8794-60c535a93735 | -12.19879 | -50.756 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d054b946-2c81-34fc-92fc-f4e178525fdf | -7.38933 | -44.76991 | 2026-09-25 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
