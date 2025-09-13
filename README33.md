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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcd689f6-4f54-3886-94ae-c371c486eefa | -11.48836 | -43.63027 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4d850ea-2dce-36ee-90b3-7f36ec14300a | -11.43617 | -43.56161 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21d4daf5-b886-3b75-963e-3000d2bd81ce | -12.12712 | -44.84397 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f17d2f59-8c55-3599-bebb-6fd7f7df69ed | -11.40509 | -50.75101 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b37404f-56be-3100-982e-bc68f3141321 | -14.21089 | -46.28511 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b4b15f15-637a-3324-add0-b5191800d26e | -16.33964 | -51.54157 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 055c9dd1-80a0-3178-887f-78651b768ed7 | -11.7436 | -46.63207 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 13c3dcf4-1564-3ba3-a49f-b41539a9701a | -18.33501 | -49.44597 | 2025-09-13 03:47:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 479c5fe2-67c0-3ed0-a6c9-69b3934f98af | -17.42338 | -49.24879 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1c2b9f1-3a32-3134-88f5-81dc33f275be | -8.66167 | -40.18095 | 2025-09-13 03:47:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b8cb399d-1a2e-3533-917b-e6af1f8a7046 | -19.9821 | -46.90911 | 2025-09-13 03:47:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d653340-8b01-3189-8c26-6dc51b287f65 | -14.17486 | -46.24453 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b4913fc-8a86-3063-850e-3844298e2ba3 | -14.2668 | -45.07041 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3c717b7-045c-3ddd-b1d3-8c96e2a847f2 | -11.14452 | -45.32063 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c93231d4-d50d-3536-90bb-1c17a28430dd | -9.00866 | -45.78403 | 2025-09-13 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78571af1-47fd-3b18-a2a5-b528945146e4 | -12.44938 | -44.74697 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d4c7bb5-84e0-3a9a-909b-1de31add0177 | -10.01281 | -50.39025 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c22451ec-2479-3400-913f-a79e45f2d278 | -10.36934 | -45.43576 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1815936-9a02-3dac-82a8-8f6e55f41688 | -12.56484 | -45.6744 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1db1d68c-fb34-3e23-bb3d-6c9467843f5a | -12.10964 | -47.59793 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f063b8b7-2818-3d35-8e6f-7a950e90d8e5 | -17.41354 | -49.26487 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6921c1d4-3432-3de6-a1e1-650ee2e0a981 | -20.45474 | -46.44304 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b912072c-595d-3226-9d96-9cc3d1264865 | -12.82716 | -47.95734 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f15068f0-bd9e-37db-a8ab-ea0320fe7cea | -14.21349 | -46.27183 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e54fe296-70b3-3449-b94d-685d91ee3a78 | -12.09629 | -44.87421 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb231995-42b1-3551-90bc-c21c8683cf00 | -18.13887 | -48.45599 | 2025-09-13 03:47:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cefc3d99-19ff-36a2-9e85-770d1d20cf6e | -11.73261 | -46.59803 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c8305c0-12f8-3ab7-a1cf-e0a5fd5a1fd9 | -11.4246 | -45.6092 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fce6956c-6ce2-3143-acd8-d0e355e3a3bb | -14.20328 | -46.26775 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c1cc256-e3ca-3bf1-b64e-bc6f18d43077 | -10.84681 | -48.18193 | 2025-09-13 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 682c6303-83a0-33ed-9be6-0526a68c811c | -14.20475 | -46.23235 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c036a57-0bea-3787-a07a-6cbb0c882735 | -14.22727 | -46.30359 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4030150a-1443-3507-a0af-18904337e9ae | -13.26221 | -43.75898 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae58567a-4bb5-3fd1-9136-2c139d604d31 | -10.74826 | -50.54371 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb728863-1e66-397b-90b8-230d1cad127e | -10.2344 | -48.63797 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bef5960-32cc-31ef-90e5-5e9ad23bebb9 | -12.10708 | -44.9001 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e79b56e8-41d9-3934-887b-8a7d76fd8b88 | -13.92465 | -48.2277 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 04dc98ba-555e-3950-a4e5-8acf40af6e1b | -18.3508 | -47.0253 | 2025-09-13 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 387883d4-2c0d-339b-8d97-66034d11b5c4 | -12.95438 | -47.98709 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 156d6ede-cc22-384a-b41c-84eca6bd420a | -15.05032 | -42.25063 | 2025-09-13 03:47:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef4be460-f138-307a-8c47-6c6ac9107cbb | -14.22401 | -46.3026 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b8987e06-bf38-3e5e-93fc-c87d2f9007eb | -11.83794 | -50.57016 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a1535c07-1d2e-3531-b81e-3e95239a8698 | -16.56401 | -49.24028 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a54538c-eed9-34ce-b512-d65508ae80e5 | -12.39971 | -43.82278 | 2025-09-13 03:47:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f2396d6-54b5-3a3b-b590-a120f3f50bb8 | -13.92287 | -48.26331 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16f8c97a-6854-3cc9-83aa-3c46e6f20d5f | -7.5702 | -42.64603 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0a7415ce-e23d-37ef-8e2d-88faad5877ea | -20.02263 | -47.63885 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06a9b434-2ac3-3adf-a78c-9bbc12d39bde | -14.18485 | -46.27745 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1b283aa9-9519-3a7e-a216-a7d98ae2aefb | -14.2783 | -45.03753 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73954aca-7576-3780-bf86-ca8c965b18ae | -14.1741 | -46.27605 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 362c82ab-f13f-36a8-9431-52c1303c2c99 | -18.06326 | -45.45584 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86fb4e23-1350-32a6-a712-ad4bc332b7fc | -13.08011 | -48.26687 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a7b0cb2-dff6-3cb9-b9a8-61e7976e1b7b | -14.21474 | -46.26546 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0f16d6c-5098-3ea8-98f3-09f71ed9e34d | -11.19979 | -48.42889 | 2025-09-13 03:47:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1827092-b1be-3ddb-9a2b-660d8f7cfbc9 | -11.86672 | -46.76643 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| baa36336-09d6-3073-99f2-4e59a91853ee | -16.36024 | -51.54744 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee169de5-2154-3959-8350-50e610d3ae22 | -20.47003 | -42.3921 | 2025-09-13 03:47:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f961254d-9361-3efd-b6ca-e702b61ad5d4 | -12.94304 | -48.01174 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d6a4340-627b-3ea7-b1c9-da84688e46a0 | -16.60369 | -49.47179 | 2025-09-13 03:47:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e5a2d22-3633-3c13-b4f8-7183d078cdd0 | -10.33971 | -48.81746 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b1152dcc-c51d-399c-850e-d4267d3462cc | -12.18238 | -40.40671 | 2025-09-13 03:47:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cfec0eb1-a60e-39c6-ae00-a94b916abac9 | -11.14495 | -45.23173 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51f9d3cd-46ae-3064-9842-6bd1b87f1abc | -14.19316 | -46.29119 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23ffd550-6607-3efa-bf8b-23b15f5835fa | -11.26807 | -41.04197 | 2025-09-13 03:47:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92f8bc8a-dc18-3131-ab04-b47c0a0b03ef | -12.951 | -48.00362 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0622aafb-8b68-37b1-9750-f02036782c9c | -12.80763 | -47.99221 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9d8b536-a71d-3775-826e-84b93482983c | -17.3141 | -46.66713 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f839dad-7a0d-3b7e-ac8f-67f373dd619a | -11.85561 | -50.57012 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 75f5ebda-66a7-3a29-a636-47b47d9fd7cc | -13.14989 | -47.14215 | 2025-09-13 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af10725b-24cd-3797-8e9f-fe621316e87c | -20.02169 | -47.64587 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbb5f934-0231-397b-ab41-620073683ae0 | -14.22427 | -43.51126 | 2025-09-13 03:47:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09e63f37-b4ce-3e60-8f2d-0876adfa58ae | -11.13909 | -45.23408 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3546a10d-a192-3228-852e-92f095612c94 | -20.016 | -47.64713 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b25c7874-3ced-3e86-8e42-6988dffd6792 | -8.18096 | -42.44313 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e77d6929-aa94-318b-a096-c2c197b7a306 | -17.4434 | -49.24343 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3179aa9-5101-3d39-9a2b-f0e1aaa324e3 | -18.47217 | -39.76189 | 2025-09-13 03:47:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 1a41657c-c840-3ec3-b50b-6c106deca25f | -11.47087 | -43.60913 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ceb01ca9-0e9c-34a3-b6b9-42e2f52392fc | -11.81106 | -50.55655 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cac477b2-d297-38d0-8e7d-ddc5a84c12f1 | -14.19597 | -46.24899 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ace6de32-9658-3376-9305-a5d4c295c270 | -17.95635 | -46.93648 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 787430b0-8dad-36e0-b702-e1efe273511b | -17.28369 | -47.25307 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e770589-674c-320c-a838-ceea90a939f5 | -18.96222 | -48.60178 | 2025-09-13 03:47:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e0743b8-0da8-3927-9fd4-156d2d5afb45 | -11.48261 | -43.70508 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef965f43-e64f-3fb5-970a-9dd5fa730488 | -10.32546 | -48.81982 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 750283d1-5329-3b96-9dc8-78f3b8c70ca5 | -12.56422 | -45.6776 | 2025-09-13 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5645dac-2566-3eff-8f28-7edf700be4f8 | -10.35193 | -50.51266 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14be30a6-fda8-3ba2-a5a8-f602f606aee2 | -17.41548 | -49.25607 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3748260a-0440-3ec6-aa14-efd2e23314a7 | -12.13049 | -47.5952 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6f42834-3b9b-3925-b645-c0210c4b319b | -9.06362 | -47.0365 | 2025-09-13 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdc8847d-b1df-3195-95bb-c873ebf2edbf | -7.50143 | -44.68523 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3250bd2-953e-3acf-88d3-e84ca9432965 | -14.2213 | -46.30579 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f548675e-9485-3356-b804-ca8437aaa344 | -17.31345 | -46.67028 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24dc1b0f-3a2d-3c32-b211-20028282a709 | -14.19391 | -46.2874 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9afdb10c-18de-3602-8397-863c57040175 | -14.16875 | -46.1651 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef540afc-d521-334a-b2d3-8ec9b9718879 | -14.18613 | -46.24314 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fb628bf-0a1a-343b-bb41-dff120c9c21a | -14.25605 | -45.07343 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11f36b86-5dce-319f-a34a-a9795692fd39 | -16.55688 | -49.24374 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4e26f7d-f9ba-3ba3-baaf-137ee3bad100 | -14.19476 | -46.25513 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ec3f4f5-b979-385f-a6bd-b726bd23cb57 | -12.10938 | -44.88774 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7b797c1-2090-3e6c-a7bd-67a6f78c463c | -14.18149 | -46.23882 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README34.md)
