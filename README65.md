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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a48ccab-64a1-3cdd-b339-354f3ba9df22 | -20.76691 | -56.93959 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d7b667f-0cf2-3fc4-804c-5b03731a35af | -22.20729 | -48.35708 | 2025-09-14 05:10:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c11349d-4bb0-3d95-813b-284dcde25734 | -15.18566 | -52.46898 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a027bef2-0768-3a38-8e8d-76b17c8015b6 | -16.87343 | -49.34991 | 2025-09-14 05:10:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af3eb951-a625-3dd2-9d07-5c75559cad44 | -15.18602 | -52.31187 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fa778dc-9788-3c84-bff8-324a863e872f | -14.7642 | -60.21781 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e9ca469-d082-3899-a332-0427aa6ba6fb | -15.92807 | -47.2443 | 2025-09-14 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47f277a8-e71c-3fa9-ba29-99d2daeeedd4 | -16.71509 | -54.96419 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6098b84-7c6b-3e89-ab64-c6c87924472a | -21.65751 | -50.1189 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 02f6674b-663a-3684-8450-e87314c4905d | -16.32916 | -51.52287 | 2025-09-14 05:10:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1b84cf7-b38a-3893-9ff0-5637db502409 | -18.15668 | -49.20158 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 217e13bc-40d8-33f1-a974-0cd43b1ca47e | -18.14613 | -49.19979 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 95537331-0b77-30b3-a8fc-9ee5d8558a7f | -17.31331 | -46.08691 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fbfee94-b2f4-3360-815e-6d8b38012d63 | -16.57878 | -55.16706 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9c2d3145-3751-3496-84b0-e93cc15d5596 | -17.99595 | -46.96665 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 595ba2d4-3918-346f-8b9d-b4c61f1526bf | -14.95421 | -55.95158 | 2025-09-14 05:10:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c43093d-edd3-32a6-949b-09941a6e8075 | -15.76518 | -52.24811 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bbf33449-9045-3932-acf5-bbb77c7b3017 | -15.29485 | -53.77647 | 2025-09-14 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d571514-284f-3881-b9f1-25dbf51ab94d | -15.17747 | -52.46775 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 582aa4f2-496a-3366-8117-b0249143012a | -22.20146 | -48.35591 | 2025-09-14 05:10:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7b1f9a8-c523-3e57-a52b-ec6aa2c59c66 | -21.65746 | -50.11551 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 23579fc0-c0f0-3f1d-b1bd-249ee587f6b5 | -17.36588 | -52.91183 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e60aae54-cff8-31a9-9a63-7ecf95320f5f | -15.57607 | -54.77575 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67793fcc-a90e-3424-a08c-ab675326f308 | -17.31465 | -46.08306 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 615ec06c-b1d8-39dd-9f86-3e0216a00055 | -17.25938 | -49.26017 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef56865e-21ed-3554-a293-bfaa2a9e7076 | -15.20211 | -52.49391 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac7dba4e-1984-3a42-9e5e-d07dfffe1cec | -19.66835 | -57.0055 | 2025-09-14 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 590695bb-8597-332a-9346-22232197da45 | -17.36177 | -52.91131 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5313aa4a-a2c9-3723-ba9a-fbf5d475a164 | -18.15737 | -49.19548 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 151f4fae-9627-373c-8e87-c344f0142bea | -20.76227 | -56.94704 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6108ba33-59c7-3ae5-8245-5157da12a9f2 | -15.08336 | -52.46556 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ba78d09-0086-3054-92e9-107ab5374d6d | -15.76067 | -52.24877 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a4b57a3e-4f43-36c5-9822-94fa720964dc | -20.2517 | -47.79855 | 2025-09-14 05:10:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f67ad6ae-80fb-3870-b31f-827d689cfe3b | -20.84595 | -56.89404 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75cb5978-b641-3cea-b28e-20e3976603bd | -17.2583 | -49.26955 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27403c52-bc97-35a4-aa4e-76a973fb42c8 | -15.77295 | -52.22089 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1041e7d3-4ea5-391a-b35e-39d9488773f3 | -16.32806 | -51.53153 | 2025-09-14 05:10:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f990037-7399-32ce-bb4c-60b1ff402a5b | -14.74168 | -60.22284 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fca42bde-6eb7-360d-91b9-175080695e80 | -21.30734 | -48.55509 | 2025-09-14 05:10:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbceeb6e-8dba-3d0f-b3f8-f0c2108e5cbb | -14.76351 | -60.22193 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0fbf99c-3206-3bad-98da-d5103420a5ed | -15.11507 | -52.49728 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 860f5253-8c54-362a-9cc7-d8da62ed1b1b | -18.91438 | -48.01663 | 2025-09-14 05:10:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f9598c72-7aa5-3add-abd0-9a6ca71e3776 | -18.1412 | -49.1958 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5ceb9452-c3b3-325c-b3bd-482bf289e7a0 | -15.09411 | -52.49833 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 857b1350-ea4d-37a7-94f2-d02bf18c542c | -15.29732 | -53.78648 | 2025-09-14 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a04c43c-ae87-30c4-8a05-f0ee1aa3efd0 | -15.17632 | -52.32129 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbbd6821-6648-3947-b284-730d0f4f499e | -17.31421 | -46.08774 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c93ca8c4-fec2-3b22-95bf-7e29c7944147 | -15.30112 | -53.787 | 2025-09-14 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54d5915c-0d23-38ee-a6a2-63e14f819747 | -16.50083 | -55.16187 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a3e4b822-4977-3f52-bb98-d9ced0d581ba | -20.77038 | -56.94012 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 379197f2-ef1d-3b08-98f2-adf73c3ff81a | -15.58164 | -54.73701 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0ea8fab-dd45-31ee-a0bf-0b9307cbc04f | -15.20001 | -52.47803 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1193783-569a-350f-a6a8-25c824b8651f | -15.80108 | -52.202 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a80cc71f-9062-31ac-b5df-0336b1acf468 | -15.18045 | -52.32194 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 555b7c26-d3cc-3913-a9b6-3164bc66a90a | -15.80427 | -52.21041 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f155d708-132a-3db8-b65f-0096209071d4 | -17.31098 | -46.11003 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36f1fd13-49c5-3eed-8fd5-767959dc987e | -15.76717 | -52.23262 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e9471c2-9a53-321c-8857-1b35d313ba44 | -15.43027 | -58.77925 | 2025-09-14 05:10:00 | NPP-375D | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8998194-d32e-39c5-a7af-3e291d0575e9 | -15.1525 | -52.46699 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fec382b-6886-3b22-a0ca-c7ed21393c15 | -15.12937 | -52.48381 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b37c3afd-7eb6-3204-a85f-d9a89b36fdac | -20.79228 | -56.96038 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b99a216-125d-3a36-aed9-8c7f4346b229 | -16.36491 | -51.77139 | 2025-09-14 05:10:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2b1f7e0-d19e-3d74-b66d-85bce88e19c8 | -14.91234 | -55.9533 | 2025-09-14 05:10:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 711eea9f-e018-3d16-83fa-75767dedac88 | -16.55106 | -49.19707 | 2025-09-14 05:10:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4cb59b3-6543-3b80-8ab2-c63d02862ac2 | -14.74589 | -60.21927 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01a985a9-4f29-3e5a-965d-d20a9f053e13 | -15.69213 | -54.34463 | 2025-09-14 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce891daa-91fd-3633-ad4a-df0dcff506a1 | -17.83385 | -50.42277 | 2025-09-14 05:10:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ea52430-647e-35bf-8104-4c10b9feca98 | -20.7981 | -56.9449 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75b0a534-4d85-3caa-b388-53f76f18ff34 | -15.57142 | -54.73095 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 109aa463-b549-3854-874a-cfd0d17a21b3 | -15.76567 | -52.24428 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e9fd96c-7642-3078-a5dd-55513520aaca | -18.14559 | -49.19286 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c2a72a58-017b-322d-9659-dc072f6ec359 | -16.36054 | -51.77079 | 2025-09-14 05:10:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4f8da27-da47-305f-a405-3845a897e8d3 | -15.78317 | -52.27401 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b3e3f9-835d-337c-ada3-ae6d4f6a2a16 | -15.76666 | -52.23661 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ac223a0-9d19-3701-92fa-c2bd56c968b1 | -15.76888 | -52.25251 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 429c291f-3c0a-399e-ae0a-dfcc355826c0 | -15.59055 | -54.77769 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95af7657-99a5-3c19-9a9e-91dd07faa226 | -15.51998 | -48.52746 | 2025-09-14 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11fa0a8f-a9b3-32c1-aaae-dce7dedcb90c | -18.90968 | -48.00996 | 2025-09-14 05:10:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 040096a7-8586-34b1-8ba5-aee2c9c6ceae | -15.93657 | -49.97974 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14d94d37-beee-3706-88a0-ba55fc224afc | -16.2795 | -45.68551 | 2025-09-14 05:10:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6b42dc7-a35f-341c-8e30-5e124832edba | -22.61413 | -47.66325 | 2025-09-14 05:10:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6f05ba6d-b54c-35a3-885d-196b7a163ea1 | -16.4949 | -55.15224 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7240ebd5-9fbe-313d-8833-bf9a17f426bb | -20.79171 | -56.96432 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91da901f-5986-3c5c-a1ff-5d50b7b0e2c9 | -17.42064 | -49.23943 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d347346-2f8c-3eef-bb4c-30950972cb2e | -15.7633 | -52.22933 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa5ce4e2-5579-3ff3-a56c-f23c9d0de633 | -15.20261 | -52.4901 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8a00fe7-d29d-35c2-9882-0d24523ac7fa | -15.09007 | -52.46544 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15989999-ea09-3090-ba8e-5f14fda46992 | -15.43085 | -58.77563 | 2025-09-14 05:10:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e4f7d06-fbb2-3598-b830-804a95022082 | -21.65785 | -50.11546 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aed2bbd6-cf9f-3703-b940-649bb041d0b9 | -16.57938 | -55.16284 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 295e9ac7-32f2-3e3a-8d79-da269714f070 | -17.27168 | -46.11611 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 851ccfee-44dc-3e9e-856a-dd24b11b0e11 | -17.38487 | -52.92623 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36b9739f-0fe6-373c-86ac-89291840eb96 | -15.86441 | -51.84734 | 2025-09-14 05:10:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06977b33-a33b-3935-8adc-0aef621a1130 | -17.36275 | -52.90393 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63641521-5737-3765-b097-99d4c3e33796 | -15.59487 | -54.74777 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf80af37-46f0-3464-9fdb-765455ac75d4 | -18.16045 | -49.20487 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 71d93ef3-26de-3e02-9ecd-2e398fca7895 | -17.40757 | -49.26186 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 557c346d-9c60-3231-9f62-706073dda595 | -15.77713 | -52.22161 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93be691d-af80-3289-9175-2ba444de46af | -17.29919 | -46.11018 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 749503d6-30cb-3771-a3c1-7b9a9a606636 | -15.76301 | -52.2317 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README66.md)
