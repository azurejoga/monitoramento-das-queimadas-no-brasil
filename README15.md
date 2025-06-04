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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ced68629-f8bd-3e0c-82fa-c4604114e3bd | -10.71161 | -48.77889 | 2025-06-04 05:21:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66b03eae-20c5-376e-b465-8a2c71866b31 | -12.51305 | -57.18586 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ee94e71-314d-36c9-b335-968d11922404 | -12.28125 | -57.27068 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a3f5cce-f61d-3085-938b-4e5939418d40 | -11.91925 | -54.81581 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6830206b-69e9-37a2-9955-51b6c7fcee46 | -13.09068 | -52.0242 | 2025-06-04 05:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa27a39a-c87b-32e1-9a75-08448ae1f91d | -15.27432 | -51.47697 | 2025-06-04 05:21:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d9fe3c8-69c2-33b5-9d00-53f88a40e96e | -11.82312 | -57.81623 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f24f5fb6-0ca4-340a-b4a3-e5e5f485ecd6 | -13.90686 | -54.66505 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc552c9c-74f8-3bdc-9f70-942e2024e51f | -10.26063 | -48.45882 | 2025-06-04 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb41b6b7-13e6-39eb-a627-3a861fbde718 | -11.90493 | -54.78821 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16ec0b2c-c07a-3975-b509-3e21e83f8c86 | -11.8378 | -51.28846 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 91b42adf-eb4d-3f44-b67d-a0cc42883f37 | -11.70501 | -54.56038 | 2025-06-04 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07f059bb-84ba-3cf6-bc43-7b33c1aeb94c | -13.14537 | -56.81002 | 2025-06-04 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1805cf1b-68ae-3d8c-84be-4429e18dd4b1 | -10.29328 | -57.14106 | 2025-06-04 05:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbfef4c6-f380-3c5f-bb9f-7690005bc989 | -12.64504 | -54.11897 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4443b2cd-ec8d-3ac7-b9f4-888e1fd1ac3c | -14.01778 | -55.12162 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88ccb736-4133-3a75-80a4-e0d09f06f556 | -12.64944 | -54.11955 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9db8d157-b9f0-3d69-9997-dd10dc29e6e7 | -11.80792 | -57.35717 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c474395-1973-39bf-9ae3-361a028e4bf2 | -14.0296 | -55.13008 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bb9872c-ae87-3174-94ac-45afc54a3cfc | -13.09106 | -52.02117 | 2025-06-04 05:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b809a899-1b8e-3bc8-bc5e-54478f26e2be | -10.69399 | -57.64114 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91a17bc6-fce0-3b2e-9350-aed1ece06c6f | -11.4089 | -54.71933 | 2025-06-04 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41774623-74aa-35d2-8624-9effa0a6ae1f | -12.71938 | -56.56213 | 2025-06-04 05:21:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15c50f30-fccb-3b64-8a7b-647718759660 | -11.91781 | -54.81704 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ca1e5b2-1266-354e-aaaf-9ff551e6cbfe | -10.30039 | -57.14217 | 2025-06-04 05:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21d2a819-423e-39ae-82a6-7e27ec27a170 | -11.55955 | -56.41473 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57cda5ad-97b0-3f6e-947a-cdc7e1f6c183 | -14.03275 | -55.13854 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28bbe1db-9936-31b2-b95c-fcd47d2f0cc6 | -11.40512 | -52.94321 | 2025-06-04 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ebe8cef-22c3-37a8-af8b-ea2cb4c6167e | -11.90001 | -58.67795 | 2025-06-04 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e7e9e3c-1741-3cc8-9ab0-d0b2d2df2bdb | -10.8701 | -49.55111 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a33edb2-d4d7-3caa-b1ed-b6b22c6709bc | -11.91366 | -54.81643 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51981c59-d3d8-3968-8569-3018d56ed7ea | -12.51369 | -57.18156 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1ce288e-1ca4-3984-a54d-84cee7eff34f | -11.9048 | -47.44755 | 2025-06-04 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 206d2627-2d97-3580-9bda-5a6dd1a2d174 | -11.83696 | -51.29121 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef8d044e-dd02-3220-90a4-7f875723c2d1 | -11.5558 | -56.41418 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40a6e8a9-52e5-31af-8630-87099b6179b1 | -10.49514 | -53.65332 | 2025-06-04 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 634cafce-4362-379f-b831-3d614c5fe5ca | -12.27947 | -64.27626 | 2025-06-04 05:21:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dc6e202-ddf5-324d-88c4-678fee21a8c1 | -11.89509 | -56.41145 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93dac8aa-55c2-3e1a-a2b5-6c347ff3eebe | -12.52333 | -57.19179 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e89a2d4-be20-3f74-a5e0-723fbd01287b | -14.33325 | -54.13842 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee40e4b8-20f6-3656-a7b0-a544dedb6089 | -12.64449 | -54.12323 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 747a9603-3a33-314e-b97a-2f2d4f8a96ec | -10.36421 | -57.22588 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87beea62-1c5f-3a07-815a-00ab67357278 | -11.84265 | -51.29242 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f21f0b3-8d30-34ab-bc80-75ba92ebbb5f | -9.96121 | -64.96391 | 2025-06-04 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a50b6ff0-e8da-36e5-ac39-f105351c3a33 | -10.35698 | -48.73166 | 2025-06-04 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15d09531-c3e9-38e5-b7ac-02fc1e3cea7c | -13.14147 | -56.80719 | 2025-06-04 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 287aefb1-cdcc-33c2-98c1-e74bec94980a | -12.65049 | -54.11747 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38091975-9296-39d6-a3ee-4d7da5d34573 | -14.68069 | -52.689 | 2025-06-04 05:21:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e085b80-a8ec-3e37-b716-ce8d7a07d39e | -11.84183 | -51.29521 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e9e3ccb-2515-3f49-b2e1-18a9d4f4231e | -10.29683 | -57.14164 | 2025-06-04 05:21:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 323a7ed0-6155-3f1f-aa29-20440cc783c4 | -11.89608 | -54.7908 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 208f964a-939b-354c-b855-ff3e9a5bad6d | -11.90415 | -47.4534 | 2025-06-04 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83177444-382d-3049-b9a6-3028c5bc1e25 | -11.90342 | -58.67849 | 2025-06-04 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc06a741-3552-324c-a2ca-bc564edf1ecf | -11.83735 | -51.28796 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5bf0253-1225-301e-b7f5-fba75e56136e | -14.02856 | -55.13795 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dda56a63-f302-322a-a8ac-3957e7166feb | -11.9142 | -54.81264 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5b6afcc-0859-3709-b115-8c38a1f01b51 | -14.02908 | -55.13401 | 2025-06-04 05:21:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 796cfdda-d8a6-393c-8a23-e51b8ac9cdd9 | -9.59763 | -63.25615 | 2025-06-04 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf4d5f09-7a9c-3419-8784-c763061c8377 | -12.3717 | -54.16549 | 2025-06-04 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 535a4308-95fd-3c15-837b-80935c0fbc63 | -13.58799 | -54.27396 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f489f2d-0b44-35ae-b8d1-99941dc70b87 | -11.83822 | -51.28519 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f4f60c7-666f-32ff-94b5-2da74d04ac31 | -14.32934 | -54.1333 | 2025-06-04 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b049850-e850-31c9-ade8-74e6c3a623f1 | -10.38628 | -53.50961 | 2025-06-04 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab803bb1-91e7-3420-9a95-05619a194cd6 | -12.45952 | -54.91274 | 2025-06-04 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8d721d8-0029-3a6a-a2ec-4a5ea7d5bf17 | -11.84262 | -51.28867 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c6b68f9-9978-3737-8fd4-0011a4aab91e | -11.90116 | -47.45356 | 2025-06-04 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9164266a-b7c5-3806-9b24-51a46f3ee318 | -13.14601 | -56.80545 | 2025-06-04 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ede39e88-90b7-30ad-8d43-206287a4056d | -10.69283 | -57.6489 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd7454bd-3012-3926-b541-0c4851a85cac | -11.89971 | -54.79518 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02d82523-e896-373e-a388-3b5b29f06ae4 | -9.61974 | -62.81242 | 2025-06-04 05:21:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c07c5677-5768-33ff-bb0b-b253cc898c62 | -11.90858 | -47.44854 | 2025-06-04 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cd3fd7b-bbed-3198-ab19-b19d9b2f4b27 | -11.90398 | -58.67477 | 2025-06-04 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 144ad769-48af-32cd-a837-2de0fcf99c5f | -11.14288 | -53.94288 | 2025-06-04 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a339776-c275-3181-b38c-25e1e9509e7e | -12.27916 | -64.27769 | 2025-06-04 05:21:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 384ce28f-6c16-328a-b818-5d6757c66819 | -13.14227 | -56.80491 | 2025-06-04 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9646eebf-9207-3093-ae7d-030407944f6d | -10.49955 | -53.6539 | 2025-06-04 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e5ddaa43-48f0-36af-9747-13a8e3b497b8 | -11.94514 | -62.84248 | 2025-06-04 05:21:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6954436-1bec-3d9b-b7fb-f3c4217aa094 | -11.91975 | -54.81203 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c416502b-30be-36ef-913a-e231c870384b | -11.91727 | -54.82082 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5474243-bb3c-3e9f-9c82-a346498d04bb | -10.76017 | -54.78492 | 2025-06-04 05:21:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7303e860-6b66-3289-b141-b18d4f7bfd20 | -12.50942 | -57.18531 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc8c3644-5b97-3fcb-a634-b63b06ff34e0 | -11.71169 | -56.45618 | 2025-06-04 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f858b8a5-12c3-3893-9678-024662b85c53 | -11.83775 | -51.28469 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c45d8ef1-38d4-3628-9f9e-8dbaca6f1781 | -15.26846 | -51.47985 | 2025-06-04 05:21:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46f931bf-92be-3bdf-bdc0-b98b5d25150c | -9.62335 | -62.81301 | 2025-06-04 05:21:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6434b350-7ddc-354d-a865-689f07287744 | -11.80137 | -57.35194 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a725b083-376b-3d85-a28d-97fdbb116579 | -9.96465 | -64.96824 | 2025-06-04 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ae2e7c3-8907-31d4-97ab-51e41b6be27a | -15.26887 | -51.4763 | 2025-06-04 05:21:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4dcc063-5624-37f5-8874-b556e654f339 | -15.0891 | -56.33955 | 2025-06-04 05:21:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7a2a48d-4864-32a3-9961-a6554744bc81 | -12.31674 | -47.25628 | 2025-06-04 05:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08e2ee11-56b5-32c1-bdfb-95ecba61fba3 | -11.83656 | -51.29445 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e78ba0b-a98b-353c-98de-f2db54d73ba4 | -11.83696 | -51.29493 | 2025-06-04 05:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4af075ea-2390-36f4-bc01-f14331d00a16 | -11.91312 | -54.82023 | 2025-06-04 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f108ee1-9dbd-31c0-b19d-607281e09fe1 | -12.51432 | -57.17726 | 2025-06-04 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fb68018-0d01-39b3-9f2c-a86e542159d2 | -10.12486 | -58.20454 | 2025-06-04 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02164d08-99e1-38f2-b16d-a8674032ebeb | -11.64213 | -58.01331 | 2025-06-04 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a46ede7c-56e9-3865-82d6-10795db44045 | -14.55998 | -59.49644 | 2025-06-04 05:21:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 252b1a37-1010-3615-8ce0-145edaf05d6a | -9.96059 | -64.96751 | 2025-06-04 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c64de9c4-d4ba-3b09-be4a-531043d28a98 | -12.27799 | -50.09858 | 2025-06-04 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68a71b51-4dda-3dd6-a2c7-91daf5029699 | -15.26806 | -51.48335 | 2025-06-04 05:21:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
