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
| e61320ba-a113-3837-b154-a469090e19f3 | -12.72785 | -47.00263 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2424209a-c54a-3e9b-b82b-f33d2e8c7141 | -14.23046 | -43.94442 | 2025-07-30 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0d9b861-f797-382b-a84d-3631c2fbf7dc | -18.77869 | -47.62365 | 2025-07-30 04:04:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73856122-8e64-3108-8350-b2d0547774fb | -12.57832 | -49.79427 | 2025-07-30 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28eaa60a-3164-3966-802e-48685ad4c0ca | -13.08423 | -47.30429 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9748a416-572f-3e0e-a831-93873de6d411 | -16.82979 | -49.24511 | 2025-07-30 04:04:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d88a5bf8-acf5-3203-8caf-60c5f1a6c144 | -12.81054 | -45.44759 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae253c6c-5a10-30ce-ae0c-2c7319cfc29c | -12.55172 | -44.7327 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a7423ba-3278-3e75-b95c-ef6c7467acd0 | -12.47394 | -47.28047 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d493952-4f0c-31da-a26d-ad526cb94629 | -14.23326 | -43.94884 | 2025-07-30 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39649f8e-6900-3564-9b3f-5531ac73d986 | -12.81208 | -45.43845 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b577d477-f9d3-3d09-b4d0-357d0bf9fb62 | -17.04524 | -43.77795 | 2025-07-30 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97ca8982-f57b-30f3-990b-c549d109ccf9 | -19.74282 | -42.09856 | 2025-07-30 04:04:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e73172b3-be69-3e10-b414-cf86009ccd13 | -14.46293 | -47.87158 | 2025-07-30 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8a8ade0-1bc4-38d9-a432-33bc309ae9fc | -12.54883 | -44.72785 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7718e2a-883e-3455-88a7-682ddd2b3eef | -13.08504 | -47.32369 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd6aaabf-d1b2-3786-8d89-619a296907ab | -12.6154 | -48.0638 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 426d2328-61a5-34e5-a2c2-a69591e6bd77 | -15.63626 | -42.55122 | 2025-07-30 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a64f38ba-ddd1-3d60-a326-740d6712bcff | -17.49154 | -46.7413 | 2025-07-30 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a5538c3-e601-30ef-9747-b1321453d6bd | -12.73046 | -47.01179 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b140e3d-a97e-3a8c-a759-cecd0cec0b7b | -13.08785 | -47.308 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0ef552c-e387-32fa-91ea-76cb8d56d195 | -17.97818 | -45.60314 | 2025-07-30 04:04:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8fbe3fe-3705-3690-91f3-f0f5e6ffa29e | -14.74164 | -46.29958 | 2025-07-30 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16467658-1ebc-3a5e-b5e1-d0157becc9cc | -15.21166 | -40.65345 | 2025-07-30 04:04:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d9c96b06-b01c-3bb9-b59a-2032ec0c5a0c | -11.32584 | -48.92155 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b39caa2e-ac6d-33dd-bc30-3c8ac6021b66 | -16.69352 | -41.01363 | 2025-07-30 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a39e750-2353-351c-a6a8-c8ac8bcb4289 | -12.45984 | -44.08913 | 2025-07-30 04:04:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f345e05b-739c-3e37-a395-f3a9b1d7153d | -17.58494 | -47.49456 | 2025-07-30 04:04:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 872ba356-9e62-39f2-9397-2b113419730b | -17.48405 | -46.73991 | 2025-07-30 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e40de73a-6299-3514-a341-5f74c2a464f9 | -13.79653 | -40.07269 | 2025-07-30 04:04:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f4d95461-3587-3836-b5f9-10b13f370236 | -16.69202 | -41.01347 | 2025-07-30 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5bc8f37-bc35-3d77-ba14-b482abf672ea | -11.98336 | -46.9518 | 2025-07-30 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b7d95e4-e2dc-3521-a186-3c2dda1f16a9 | -13.08357 | -47.30797 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66ef2507-ca13-35a1-9ba0-9278fe43f5e0 | -12.4795 | -47.27343 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 17a6c6ec-0c22-3eb2-b6ef-96d5ce3b2c7f | -12.81581 | -45.43909 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60fea935-ee15-3a55-a0de-43154d8e7b53 | -16.1077 | -47.91879 | 2025-07-30 04:04:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a13a5280-7ec9-31d7-908c-4cc8b693f3e2 | -16.63846 | -44.34759 | 2025-07-30 04:04:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87ba859e-ec9f-340f-97e2-d67b85f0e9b1 | -12.47112 | -47.27191 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b4c6e66-38bf-3fe5-8c81-8ec8ae5372e6 | -11.34602 | -51.2491 | 2025-07-30 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7df009b-fa78-3657-8601-af7b800d1ec5 | -13.1466 | -47.34773 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cc9d01c-2c88-3059-a1b5-c10e7b1a1871 | -11.98992 | -46.69817 | 2025-07-30 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d33c237b-c066-3896-bda0-64f0aad17e35 | -11.32137 | -48.91837 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3f1693d-9f5a-37e1-b1a5-e946cbed1758 | -12.81503 | -45.44366 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98291e23-b9c5-3ccf-801a-c76dd721b8f8 | -12.26685 | -47.00257 | 2025-07-30 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fba4f903-be0a-3c4c-ad6c-17c67beda5fe | -11.32487 | -48.92673 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3dd069a-8695-329a-9d8b-f1e4266a459a | -14.4586 | -47.87152 | 2025-07-30 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77f6cc21-f68a-38ea-b303-0a884f7b32f9 | -11.32613 | -48.91927 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08dde75b-9b16-36ca-bddb-4aa8aa598584 | -11.92582 | -44.54572 | 2025-07-30 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82ef2021-da54-37c9-9f0b-79366aab01f2 | -12.57717 | -49.80026 | 2025-07-30 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3a9d306-c0d6-3e59-837f-be2b7284c0da | -11.98269 | -46.95562 | 2025-07-30 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1613dae8-f35d-390c-9db6-3e7469490915 | -12.58147 | -49.79811 | 2025-07-30 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5047ce32-a4fb-3860-bdaf-c951cee59dc3 | -13.08218 | -47.3157 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| add1695e-45fa-3401-a70a-d927736e576e | -11.342 | -51.24653 | 2025-07-30 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62b9d8e1-d44b-32ce-a7cd-e951d70088bf | -11.32707 | -48.91409 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ff1a14d-ddf9-3a21-89e0-0d147d59c503 | -12.57655 | -49.79704 | 2025-07-30 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56d2f08d-4903-3f07-8057-678adacd1733 | -12.47531 | -47.27267 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 70446d00-68dd-34af-ac77-44c9cae82552 | -13.09334 | -47.30134 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d495c8ba-c357-3e2b-a784-c5ea2f08ba0b | -13.06467 | -47.38903 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ba73f3f-e50b-3f25-be54-3fdbfb985df5 | -12.72639 | -47.01091 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1819722b-f5ef-3685-8101-0a1353fd8ea3 | -12.7312 | -47.00758 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85b750f2-0400-30de-944e-7f5f1eb84bd6 | -12.82036 | -43.0918 | 2025-07-30 04:04:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ffc3f74-33f8-34f4-8d43-ca107aa94702 | -13.39355 | -40.11901 | 2025-07-30 04:04:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bc6da6cc-f4e9-3350-82eb-eda3a68464f6 | -11.99147 | -46.92981 | 2025-07-30 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3239e193-9935-3ef7-88e0-6d461d1c3afd | -19.75786 | -43.13243 | 2025-07-30 04:04:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f0f74c3e-cce3-3476-93f9-4d08614655ef | -16.32237 | -43.61956 | 2025-07-30 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9a52774-e18c-3e50-895c-9cf636bbf8df | -17.7177 | -43.45289 | 2025-07-30 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eb169c9-63c0-3b59-a6e0-dc405fc47d1b | -13.22569 | -47.21753 | 2025-07-30 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bc3825b-46c9-30cd-b1ea-ba610b580013 | -12.70939 | -47.79282 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73c6e52b-4fa9-3f74-80e2-336ba88699b9 | -13.14315 | -47.3431 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41e568b9-35a3-3036-9011-e89eb18a8736 | -16.59076 | -44.08215 | 2025-07-30 04:04:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d60c049d-5d9c-301d-9d22-d489f95f6549 | -17.48862 | -46.7359 | 2025-07-30 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e649266f-21a6-3266-82a0-2ac3b99d3af1 | -14.21738 | -43.93824 | 2025-07-30 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 956d5b72-a1bf-3572-a374-c8d40d13fb62 | -15.17966 | -41.35496 | 2025-07-30 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 39c02b16-7f5b-354b-a596-417d10b0cca3 | -11.97924 | -46.95098 | 2025-07-30 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dadf2980-7125-306b-9949-ca7bb679e459 | -17.58422 | -47.49769 | 2025-07-30 04:04:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c85c122a-745b-34fa-9561-1f5d87140dd9 | -20.30007 | -50.95514 | 2025-07-30 04:06:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b0443611-b47b-3a82-a2ff-1cae2a5616c6 | -19.92693 | -49.90783 | 2025-07-30 04:06:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6d09cfe5-83a7-3a5a-b14e-735e52ce0a1b | -22.91591 | -45.37869 | 2025-07-30 04:06:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7da399d8-2c96-374a-bd2c-ad08bcb768c4 | -22.24039 | -47.05686 | 2025-07-30 04:06:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f288f75-0105-38d2-a1d8-0281d4d71999 | -22.17793 | -42.47043 | 2025-07-30 04:06:00 | NOAA-21 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7d92c88e-cef0-304b-90d2-8859c815e630 | -22.78654 | -42.11271 | 2025-07-30 04:06:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 566e0e59-df7b-3695-8ea4-2b053708d449 | -20.45987 | -45.55204 | 2025-07-30 04:06:00 | NOAA-21 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b04f52fa-14dc-38e5-ad18-a1669089f55a | -22.99797 | -43.58363 | 2025-07-30 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b45724a5-eb20-35c1-a29c-4f59f669fe33 | -21.3931 | -48.66986 | 2025-07-30 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d4f243a-3473-3fa8-b0fb-42e6efa584c0 | -20.29791 | -50.95834 | 2025-07-30 04:06:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 69cd644b-207a-35e3-9908-848f992d748b | -21.98569 | -46.82331 | 2025-07-30 04:06:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83c80274-67b0-3324-8573-2cb2ac3d31db | -18.44908 | -54.66521 | 2025-07-30 04:06:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b11fcba0-18ad-3202-8f5c-02a0b3d5fb47 | -21.3921 | -48.67525 | 2025-07-30 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38a4edc8-fb4d-3bff-b6c5-d94fbcd5bfd7 | -21.17155 | -41.86348 | 2025-07-30 04:06:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5af00555-f506-3b7e-a88a-be3fa7191864 | -23.60591 | -45.36992 | 2025-07-30 04:06:00 | NOAA-21 | CARAGUATATUBA | SÃO PAULO | Brasil | 3510500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ae14abcb-0904-37d6-8350-d6545625c032 | -23.36421 | -46.16885 | 2025-07-30 04:06:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dce5b94a-9ae4-3bfe-bc13-266fd1e23a25 | -21.98645 | -46.819 | 2025-07-30 04:06:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c18814d5-3b6f-3ffc-b514-9877cb21e463 | -19.98263 | -46.19079 | 2025-07-30 04:06:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68cea2d7-7f26-39e9-a290-ba72449b1ab3 | -23.60654 | -45.36609 | 2025-07-30 04:06:00 | NOAA-21 | CARAGUATATUBA | SÃO PAULO | Brasil | 3510500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 04af05bf-4906-3282-9081-c663470f1cba | -20.29163 | -54.07543 | 2025-07-30 04:06:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2837a015-daf3-3163-a743-c81c36fc779a | -22.99855 | -43.57987 | 2025-07-30 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 793452d5-577c-38f3-911d-7e77dc2cd866 | -19.92261 | -49.90678 | 2025-07-30 04:06:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a4c368d1-8a7a-329c-98f4-f6127111156e | -22.80921 | -43.39641 | 2025-07-30 04:06:00 | NOAA-21 | NILÓPOLIS | RIO DE JANEIRO | Brasil | 3303203 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f5795b52-163f-3bb1-81cd-7876840cbe84 | -8.5211 | -43.3063 | 2025-07-30 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d916ffbf-a168-3f9e-8fc2-06df2572b356 | -15.7676 | -49.9555 | 2025-07-30 04:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |


[Clique aqui para ver as próximas entradas](README17.md)
