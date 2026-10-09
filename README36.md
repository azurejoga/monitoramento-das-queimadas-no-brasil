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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 067f2cac-4e21-3424-bf4c-d7209b8cf2a2 | -5.99352 | -55.36926 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c344b8fa-5581-3a4c-ab9a-56601e43ca16 | -6.67087 | -63.02567 | 2026-10-09 00:35:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| fa76c45d-2d20-3b56-ada5-60191a54c028 | -6.85555 | -59.03984 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 019d99f2-24b0-317a-9665-2f99bc65ca0b | -6.38774 | -55.26141 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ead39988-e088-370e-80c4-14ebf7db1d7c | -6.31538 | -55.32679 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 52a0ea32-3820-30f6-9c8e-10930b98a850 | -5.69921 | -49.09098 | 2026-10-09 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 01581054-115e-33ce-a574-7b290ff4d5f3 | -6.67905 | -63.03097 | 2026-10-09 00:35:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| bba6d8e9-94bd-377f-87e8-a63037c60baf | -5.70383 | -53.44784 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2e05e4d9-b24d-33e1-9bfd-81f41dde5d20 | -7.21185 | -55.1564 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f5061294-c34b-39be-b94a-1e91da6bda53 | -6.73442 | -55.1116 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 43e89da9-ee47-377f-bc54-f2e8d01a2736 | -5.69746 | -53.45545 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 0d87b5bd-699a-367a-8faf-f860ab3dd079 | -8.49463 | -54.62273 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e659d020-cc68-312b-b567-5d47c4f69179 | -6.12385 | -55.70415 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| ad5a134e-36e7-3e41-82e3-9e914feb81f7 | -7.89551 | -54.71953 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| acfd27b1-030f-31b5-8ee6-b85dda38d1e1 | -9.85644 | -47.47127 | 2026-10-09 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d2354f54-7f1c-3543-adfe-601094480f04 | -5.71414 | -53.48714 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 487c29cd-f581-3fee-af96-fbeb258eebeb | -12.22172 | -57.13531 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| dce6b3a2-8869-302d-b65d-ff75edd2fe10 | -6.7295 | -55.14921 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 9556daa5-b6e2-3570-b496-416b60886ca6 | -9.22992 | -60.87537 | 2026-10-09 00:35:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2d45616b-9cc4-38c9-b74f-6c9b5b88433b | -6.13057 | -55.68017 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 58933468-e41a-3f40-b681-29a0f545e2db | -6.72773 | -55.13715 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| f714cbf8-9806-3ddd-87e1-b7f90a6fccfe | -6.6726 | -63.03934 | 2026-10-09 00:35:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2c88df9e-e9cb-3bee-aa84-95c89743a8eb | -6.73302 | -55.17323 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e30a8c82-ac22-3d70-b2aa-64a04d809260 | -6.43651 | -55.03685 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eac9c500-2fe2-3a2f-9e1c-62d286cff10c | -6.74987 | -55.14613 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e0f556ac-ee60-3083-af75-47580681b091 | -6.68345 | -63.03793 | 2026-10-09 00:35:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 55d3e917-55f0-3a4e-872c-47208629f44c | -6.48954 | -62.87008 | 2026-10-09 00:35:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| fdd5c7fb-2a4f-38b2-b77c-4eecc489c2f2 | -6.13227 | -55.68546 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fbc8074b-d0fd-308d-8aba-b436e65fe30f | -9.10405 | -59.38831 | 2026-10-09 00:35:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e3f64a51-652e-358d-a646-26b283b91e80 | -8.18257 | -54.72007 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ea4a05e5-614e-35c0-a97b-2f2ca4c9b2a4 | -6.91714 | -59.27861 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 72f53d11-7a42-3d73-885f-bbd2b395db9f | -5.99369 | -55.36339 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 53203b4a-4a32-3003-bac4-6cf388284bd7 | -6.47008 | -55.4766 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| ce53a891-25a9-3492-9862-c4034b76e2ae | -6.59704 | -60.04758 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 24ed4ad9-7085-35d0-b85f-98891851cc7c | -6.47107 | -55.48237 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2bd82bc2-b525-3114-855d-5bfc171fc5b1 | -11.92771 | -63.42158 | 2026-10-09 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 53da4881-5198-3565-849a-024456d9b0cb | -6.84649 | -59.3039 | 2026-10-09 00:35:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 365ed922-76ef-3830-ab37-bba2dab0b752 | -5.7166 | -53.50409 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 7b49cca7-f59b-3401-8c25-170e236e2cfc | -7.90582 | -54.7179 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5f6cfaa3-469a-3360-87d9-7b7aea95d630 | -5.88649 | -57.7564 | 2026-10-09 00:35:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 07790b92-814f-3f3a-919f-57f8c43b3880 | -13.15439 | -54.33823 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e37a49fc-47c9-355f-b0e2-746649f61fe4 | -13.20987 | -54.37516 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| e48911b0-21c5-3ea8-a181-3e66030d6e9d | -5.96495 | -55.37987 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cf4428fc-2830-3c61-b756-319b31111c31 | -8.6553 | -54.53523 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 91c1fa49-41f6-3565-9d3c-59aa9e3869ad | -6.46937 | -55.47089 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 07a0f279-db6c-383c-b76e-845e0d52acee | -6.74965 | -55.07264 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c3b8f0ee-af87-355d-9450-3e96905d7b45 | -6.46336 | -55.5012 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e1a5f35b-5b50-3220-9f58-bd673b6dd922 | -6.44683 | -55.03535 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 26b8d831-fcd1-30d5-9c99-5f22ca9d7342 | -14.87657 | -50.28654 | 2026-10-09 00:35:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 38cf3522-2373-3293-8e13-b7c006cc6f9d | -7.56189 | -64.54107 | 2026-10-09 00:35:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2438ca69-6427-3338-b1c4-849ddcf6f054 | -5.95135 | -55.35733 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 28f55b80-640e-366d-baac-666d6266e2be | -5.85695 | -53.4537 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e4ea9bed-8b55-3637-9061-2e79ab28a1fb | -5.97828 | -55.68532 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 500eb7aa-132b-39e0-87a8-b7455d7c26ea | -11.45846 | -54.30602 | 2026-10-09 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a52afe3f-f604-3e6e-978b-1515c0997943 | -6.75136 | -55.08446 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e3c2c8d8-1e1e-3fbb-b213-7d499d156bb2 | -12.22681 | -57.10695 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 5b8ac4c0-5a09-3d41-9246-645f8f56afb3 | -4.62578 | -49.22243 | 2026-10-09 00:35:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 6d70b3c5-997d-3184-835e-cf2779e4a26c | -14.87883 | -50.30178 | 2026-10-09 00:35:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 8d8301d9-5ac4-315a-9e34-e83ce7a2b499 | -6.73949 | -63.04456 | 2026-10-09 00:35:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0d69ef21-5ca2-3a7b-812e-a2ec1912a3a7 | -14.26262 | -52.79563 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a8223ab7-419f-35a6-aa83-4191ffeda00f | -7.57006 | -63.34788 | 2026-10-09 00:35:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d5664d3c-4417-35e9-8a25-dbb9e24fe306 | -6.38943 | -55.27306 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| d69181c9-b600-35e3-a9cc-cde1a749f76d | -6.73126 | -55.16123 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9e665ce4-c4d8-305d-80b5-f7d8a8eaba82 | -6.42556 | -54.96242 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9a601c8e-a5c3-35c9-b287-1b2e03668910 | -9.21061 | -60.87799 | 2026-10-09 00:35:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 52bf9b75-c8f3-317b-bc4c-62bbb1d3af40 | -12.20404 | -57.13792 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 19f9da94-5528-316c-abed-951f4f41e9d3 | -6.67221 | -55.10219 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e3c136a5-0bb2-3ec6-80a3-389b804207b5 | -12.21288 | -57.13662 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6b95e121-e149-32c3-931f-3409a5298737 | -8.24453 | -54.72997 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d354321b-9fbf-3c49-9054-be8cfc76c124 | -8.23663 | -61.388 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 17dce214-ef3f-3927-a152-73ffd03279f1 | -7.21359 | -55.1684 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 48c6d4cf-e405-33db-a2cb-ac927b1623ff | -6.54014 | -56.0434 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fc56eb10-6cea-3778-ae69-1803ab4167a7 | -7.50591 | -55.00237 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 38fca908-4382-3ad7-b4e2-2033d38cb16c | -7.08474 | -52.69442 | 2026-10-09 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 42f431b2-d543-3a09-bbe9-8451c335b602 | -6.46172 | -55.48962 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f0656cf4-368d-3c6e-a19b-204841461981 | -13.218 | -54.36256 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| d8dff923-fcf3-37f8-a275-5280c2fcf84e | -9.20847 | -57.72108 | 2026-10-09 00:35:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d62e95b1-6178-394e-a7f5-b7c7a68e5f59 | -12.12465 | -57.16512 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 82b81043-8195-36e6-8f82-5bfae2d1efcc | -6.73619 | -55.12375 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 063b6f77-2f2a-3440-93eb-6a4f27ed5f74 | -10.67364 | -58.74071 | 2026-10-09 00:35:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c4e340b8-f067-3df5-8af7-c19b2d76ae83 | -9.0963 | -59.39879 | 2026-10-09 00:35:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9b76ed8a-5ac7-3d02-999c-4bd9929892cb | -6.67047 | -55.09012 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fab37018-fc08-3f65-9258-a0fd63e3e4a1 | -13.17057 | -54.3125 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a08d98d0-c017-364c-82aa-94cb965d5a28 | -6.72733 | -55.06309 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 72f8eab9-3bac-373f-914d-1d55d542bf7b | -6.49851 | -62.85545 | 2026-10-09 00:35:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 09c68358-6f9b-3415-817f-4961f1921e38 | -5.7024 | -53.48929 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 34c4272f-521a-324a-b192-3d48ae3ea1f7 | -5.95977 | -55.34377 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f969a085-0400-38ca-b850-78dcad024100 | -11.96624 | -57.61282 | 2026-10-09 00:35:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 49f626c2-60e8-36e3-b99b-62602a0bfbcc | -7.10074 | -55.7307 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9e923a21-6512-3e6b-a604-759e9914b611 | -9.49324 | -57.25141 | 2026-10-09 00:35:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5980050c-f17a-3e56-9fd5-63b5f99e1cbb | -12.21797 | -57.10825 | 2026-10-09 00:35:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7658a704-a3d3-3ddc-ab30-a6ffe2a9ba34 | -11.99272 | -57.60897 | 2026-10-09 00:35:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c1585feb-8553-3f5b-9155-554e4ed53236 | -6.49915 | -55.32346 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| d8ae61df-1303-35c6-8ab8-8913e0514f06 | -5.88521 | -57.74726 | 2026-10-09 00:35:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1056c714-22fd-3b9c-ab8d-e43d46ed34b1 | -9.95376 | -55.33785 | 2026-10-09 00:35:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8d0a5ac6-e195-3efc-9f2b-92c8a82f8b5b | -5.89032 | -57.71855 | 2026-10-09 00:35:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 8cea91ec-750d-32b9-94fd-f3a97a835fe3 | -13.16247 | -54.32534 | 2026-10-09 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 996fc2e7-883f-3573-b49d-e3f6fb186e45 | -8.49646 | -54.63499 | 2026-10-09 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 40758bac-33f4-3cb2-8d3d-e0a55462e8d3 | -4.61284 | -49.21931 | 2026-10-09 00:35:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 155b6b02-571a-39c6-a8fc-3657b626cc43 | -6.49745 | -55.31173 | 2026-10-09 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |


[Clique aqui para ver as próximas entradas](README37.md)
