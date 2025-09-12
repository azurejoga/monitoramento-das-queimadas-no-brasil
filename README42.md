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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee586231-7a87-3531-8c8b-79fea58100b0 | -15.09758 | -52.4645 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b449806-2e9a-3a7d-809d-f5af1f573b0b | -18.3856 | -43.99342 | 2025-09-12 04:06:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac5853aa-b494-3643-845d-858c37f33d11 | -11.98519 | -51.13692 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1eb7c68f-d5e8-34ec-9eb5-a18815c76875 | -12.84612 | -47.95489 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4b018ff9-b03d-3720-a4b9-af216d4cf0eb | -18.05437 | -45.43425 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a4e10060-82a8-317d-88f5-44fbe42d6b0a | -13.24391 | -43.79691 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 619e5b4f-0762-3fb8-8cff-8b9185f595a9 | -17.72253 | -44.40928 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a42ad7f0-8680-3fda-a6ea-c711fb2acdb9 | -14.71492 | -45.26548 | 2025-09-12 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8ce2129-6476-3c16-9429-45500894e920 | -14.41625 | -47.31592 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1ff227e-a141-3039-97d9-621d72927d8d | -14.4195 | -46.39897 | 2025-09-12 04:06:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2aafd039-1b6c-30e1-8075-a8ed6c8121bf | -11.97957 | -46.64692 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 52bbe629-22ac-3643-98e7-adb90e785b53 | -12.86019 | -47.95325 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a560f0ee-7b19-3541-99c0-1b6dfff82758 | -13.78099 | -46.28668 | 2025-09-12 04:06:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e34895c-e3b0-3ce0-8ccf-3c1475c82f7c | -11.9809 | -46.64728 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18e5034c-4ba8-3baa-9aef-8dce70b47d28 | -11.86441 | -47.5303 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e3215ff-703c-3285-97d4-8d39bf59e3a2 | -13.90831 | -48.23856 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f410f092-dfb6-3ef3-8f8e-734f537700ac | -12.46733 | -47.48719 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adfe5e8c-d87a-3bb2-a247-85a46b8c9908 | -17.32544 | -46.66627 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5df4b15a-be31-3703-be70-30c24fb81da7 | -17.35526 | -46.69755 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 091e9c75-d5e4-38ce-8a8c-3ff277787afc | -17.34125 | -42.51616 | 2025-09-12 04:06:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 379c192b-f9e2-355d-82e4-ad7989ed8cad | -12.83655 | -47.957 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4950d3ee-c131-3aeb-8298-3c5e1b0609b4 | -17.21567 | -48.68883 | 2025-09-12 04:06:00 | NPP-375D | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2db0c528-4f67-3643-9163-d90027766027 | -12.00683 | -47.77271 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94778266-9073-34f3-b768-956879ffcabc | -17.90744 | -44.59861 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c2fb032-e2e5-3dd2-85b6-cb485356a371 | -12.42929 | -47.79274 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49ec55bb-255e-3a41-8c61-7b6f090d810c | -12.91494 | -54.75631 | 2025-09-12 04:06:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d291de89-e80c-389b-8fd3-438325031036 | -14.43024 | -46.4067 | 2025-09-12 04:06:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3fdbda35-1fa1-335f-b0b0-91b485ad94ee | -17.13463 | -48.49456 | 2025-09-12 04:06:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f508673-c0fa-37b1-89c2-ab4b00225ad9 | -13.89397 | -48.24159 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| feecb324-bfe5-3420-889e-a690e1de9fe7 | -17.14809 | -48.49343 | 2025-09-12 04:06:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1855ae5-c69a-38fc-9b8c-da7480fe8db3 | -11.20148 | -55.08611 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fc02449-389e-36cb-b885-4b66a08a3a30 | -14.17311 | -46.18465 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79665372-10c6-3d93-8d25-6413de54374a | -13.91319 | -48.26178 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1eccd9f-d4fe-384d-86f1-7d670515bf96 | -15.68939 | -47.02792 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 788e2e34-8235-3c37-b911-372ce452c1e8 | -17.47272 | -43.72572 | 2025-09-12 04:06:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 470cc6fb-2548-3659-b55f-ecbc81c15aab | -12.00488 | -47.76994 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 532b37b4-72ef-3602-bd40-a1837e7bd4fc | -12.82886 | -47.96105 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0ad6437-d2a5-388f-98df-507e893e893d | -11.18725 | -55.09543 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3ef0b70-4903-3fe7-8913-f37aa3dc7a95 | -16.20182 | -47.98256 | 2025-09-12 04:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c65f7133-1e10-3169-99b8-5df9dd957b61 | -15.08486 | -52.4342 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c68ed179-d962-304b-96fc-6ffde8c2c60a | -11.53255 | -50.59985 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e3cb2453-cb9c-32a7-97cc-4f27edc4ec85 | -13.3059 | -42.38329 | 2025-09-12 04:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 90f8c7de-b31c-37fb-9925-e15e1a77c368 | -13.31349 | -44.08938 | 2025-09-12 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5b105bc5-2223-34cc-915e-033b8bb8b87f | -11.63843 | -50.58134 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c55916a5-aa5d-3e24-89a4-3d9a015e1e87 | -17.73492 | -44.41957 | 2025-09-12 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b37150f-3448-313f-b274-4f1e2a3790e1 | -11.5177 | -50.5896 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9af69b1b-c33f-3fdf-96f8-68122079cef3 | -13.31888 | -44.64975 | 2025-09-12 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14ac4e31-268d-39a4-8bf6-a3d88d74c162 | -15.15137 | -52.40575 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25d9f1cb-4a41-3cd7-b5f0-1cd89b791fa8 | -11.19299 | -55.09129 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddd5be40-8337-342b-8a2c-7c1b5cdf3e8e | -13.30532 | -42.38688 | 2025-09-12 04:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f7a71614-1256-3493-a22a-4d08244c3bfd | -14.50438 | -53.91462 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 619c37f3-3e28-345c-94a8-480f3c35a950 | -11.51914 | -50.3976 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91573eb3-64e7-3072-85af-f695435cd32e | -17.93987 | -46.93062 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3894e67-6c56-3cf8-a384-432dade9ca8a | -16.60622 | -49.79186 | 2025-09-12 04:06:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dc314980-c0eb-3917-bcfe-f164d3ef32be | -12.83902 | -47.95565 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fc19fba-e21f-3c2c-a2a5-f07a22958cf1 | -12.92171 | -54.75779 | 2025-09-12 04:06:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| b989e103-6999-369b-802d-459ac4d4328e | -15.54156 | -49.74591 | 2025-09-12 04:06:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e411c9c4-a891-3db2-bf0b-8c8fc8eddf3e | -15.88212 | -48.18498 | 2025-09-12 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3e29ae63-e76f-3005-be2c-20aa9e780f40 | -16.70803 | -43.92944 | 2025-09-12 04:06:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60bfefac-9460-318b-8d7f-7fc516f708a8 | -12.83591 | -47.96042 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84cd0bdd-64c7-34b3-87b0-c6e91819fd30 | -16.83947 | -47.8405 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fb4889d-840e-38a6-bb62-efe678a5f9ce | -17.33684 | -46.66848 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35758adf-27a1-3939-8813-571eba4d26b2 | -13.14342 | -47.14262 | 2025-09-12 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8b5f481-5a9e-3c84-ba9b-bf32b7afc520 | -13.90141 | -48.25095 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62f55341-149b-3655-8ef2-7ed04a7d1d88 | -14.17056 | -46.19905 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09f896cf-8ac4-3e5c-a99e-9f50962ab6c6 | -12.00569 | -47.76556 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2b70aaa-86ba-31ef-8954-ff9278741a36 | -15.60811 | -52.74587 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ddc59dc-51b0-35eb-90c4-66d4b6627cd4 | -14.26656 | -54.79198 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2360731-1ea6-38be-9b9a-64062e8dd46d | -16.11054 | -43.63332 | 2025-09-12 04:06:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36bb4f2f-9c96-3635-8abc-e59e0065b8bc | -17.34648 | -46.68056 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f15a3fca-bb99-3195-b49d-49ec6bfaf272 | -11.53544 | -50.41083 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ad185d0f-751d-3ab7-85d8-004eb66404c5 | -14.41562 | -47.31936 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66efd802-b702-3a1c-b335-58acb5d254bb | -16.49224 | -51.97649 | 2025-09-12 04:06:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82b19dc8-67c7-3137-9838-1e2a79934d44 | -11.53055 | -50.61034 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bd3f12b5-b878-3f63-9be0-c135fd5b3bee | -14.98399 | -41.11379 | 2025-09-12 04:06:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2d5ea60-b1dc-3671-b7b8-029365137865 | -12.49865 | -47.43655 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b59f5de-023d-3f6e-8b1f-10cc44508ed7 | -15.79578 | -52.23099 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 070bc9f2-b885-3fd8-a335-b46830a8960c | -12.91254 | -54.76225 | 2025-09-12 04:06:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| da0c9795-fe97-313f-a33e-0bd387cf85ae | -13.91159 | -48.27044 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cfb7b3fe-f7fd-36a3-b716-4eff96fba8b6 | -14.23687 | -44.24873 | 2025-09-12 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2895e09e-f629-384c-96ab-a241615fab8d | -15.53443 | -48.55137 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5faac3cd-d687-322e-8552-a12f59199b20 | -11.793 | -50.56868 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b393e6d-616d-398c-ba2e-2cd21de6a1fe | -11.49167 | -49.2672 | 2025-09-12 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e09a42c-8603-37bb-9425-4b7621676cf1 | -11.18891 | -55.07526 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b4e18ed-3579-379d-9412-bf1b89d80fd0 | -11.52338 | -50.38731 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2a5b518e-5bc6-3d89-8e05-503427430901 | -15.10442 | -48.00266 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8899f8c-fa89-3c3f-9991-9fd48857c23a | -15.79116 | -52.23006 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7980f89a-abf4-3133-8042-9cd4a0fc4b6c | -15.53338 | -48.54983 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 489eb444-381f-3304-bb08-733483fffc63 | -16.43596 | -49.03209 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f28144a1-211d-32ee-b545-421d5b864ced | -12.90432 | -43.57684 | 2025-09-12 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c029182e-d052-3334-af32-104d01d18950 | -17.2773 | -46.08519 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb315613-07bf-33ef-9037-93b36bb730b3 | -15.68074 | -47.0532 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e10cc913-7c89-3eac-940e-392bb44415ce | -13.78197 | -46.28125 | 2025-09-12 04:06:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dc4a6ebc-bff1-3ac7-957a-2f00491bbebc | -13.15108 | -47.14815 | 2025-09-12 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d786c64-b050-37b8-bb17-481a6444f439 | -17.26905 | -46.08878 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6853e946-0478-32c3-b59f-f72f874a8f46 | -14.38364 | -52.95847 | 2025-09-12 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97177aee-c250-36cc-b15a-d502d84a60b0 | -15.11357 | -48.09594 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 768ab62c-2846-3220-ae7c-ccecb1c91f13 | -15.24337 | -48.17166 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 331c4df2-df5b-3a15-a8b7-9112556dad7f | -18.0589 | -45.44212 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21478a40-4540-3042-87e2-692b0bcc6e89 | -14.12883 | -45.37536 | 2025-09-12 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README43.md)
