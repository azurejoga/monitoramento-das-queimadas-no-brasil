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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 923fa1a4-a204-3dc3-b3b5-e848a3d2deec | -11.15226 | -55.1782 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14b43922-eda1-3140-8486-bfaeb78b81aa | -10.08464 | -60.50376 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcb80b25-a7a8-380b-942c-ec0142ccc462 | -10.46498 | -58.68676 | 2025-06-19 05:12:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0b8a140c-7947-3724-9e67-7e41039a5183 | -11.52545 | -56.98776 | 2025-06-19 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f325bde-6dd8-3fe9-81b0-0235a5ca1b47 | -12.42975 | -54.87631 | 2025-06-19 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f964d6dc-f1f8-361c-b25d-c8708d119578 | -11.52828 | -56.99197 | 2025-06-19 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 649030aa-9580-3881-b446-fc405009a151 | -10.36009 | -57.2324 | 2025-06-19 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a0a0b54-942e-31a8-9d2e-b8696258d43e | -11.57428 | -47.43417 | 2025-06-19 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22f826bb-d200-37fa-95ec-95c83ee37660 | -13.50917 | -55.65612 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a27d859f-5d7b-3bb1-bfd2-57ebc7538024 | -9.79782 | -47.18049 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| aac77985-94d1-3205-82ff-cc131390fd6f | -11.64522 | -54.14222 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab320cec-16c6-335a-863a-51804ad31671 | -9.26361 | -56.2911 | 2025-06-19 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ef84e5f-52ab-3f88-9c9b-e77619edabc8 | -11.07069 | -55.04432 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 405a7190-c12f-3d4a-a793-c3c4ebf1cb42 | -10.59148 | -49.46168 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 749e8b65-2d92-36e4-94d5-07ff0204ba80 | -12.13484 | -54.66833 | 2025-06-19 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 493656d8-0f7d-37cc-89c6-68c8897969c5 | -11.15653 | -55.17442 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d39a091-9354-365f-93f6-75d10309b02b | -9.24815 | -50.03108 | 2025-06-19 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5db9fe1-a7dd-3518-9a19-2af47c0f3012 | -10.28319 | -60.536 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8a98f1-19a5-3b8d-8fd4-a43e974c7785 | -10.35846 | -57.24311 | 2025-06-19 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef4acc3f-4473-3be7-9777-46dc04b23a95 | -10.02294 | -57.32573 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e130fa9-87b5-304d-a7aa-a5a987240e78 | -14.06869 | -53.39861 | 2025-06-19 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ee2e1d94-7724-30b2-ac05-46b8be6a9aa9 | -12.79813 | -48.73075 | 2025-06-19 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 751de973-9ac1-3748-8d42-7be5011a1c54 | -10.87335 | -54.32189 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e2619e4-1da4-3e96-a7ee-a6337210a824 | -11.08406 | -55.05518 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fd810df-a5c9-32b8-8d01-7bbf6158ac2d | -9.37849 | -47.63388 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b91c1c4d-1938-3e3f-abb3-dff109c1051b | -10.23515 | -52.23527 | 2025-06-19 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 384d1df8-9fb7-32cd-a198-4e52cbd9f94e | -11.61523 | -58.29193 | 2025-06-19 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed5507b0-7f61-3ea2-aeaa-c5eda1e3f0da | -11.64911 | -54.14274 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42e6c95e-e071-32a3-a365-4969d5311c58 | -14.21769 | -45.51112 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d9d839fd-a4f2-35d8-bc68-308270262d77 | -9.51256 | -55.96595 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df3db046-dc67-3206-955f-b643a85635e5 | -9.79861 | -47.19257 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2311b00c-7a31-36f2-bee4-78c0d192c720 | -10.67963 | -56.55217 | 2025-06-19 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9b7d8db-ef94-3506-af7b-3a8f1389e6de | -10.86458 | -53.7689 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a64cf10-e0a9-367a-b7c0-46684160a4aa | -10.85788 | -53.7608 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a363417b-8ede-38ea-86fe-7546c5ceec1f | -11.95479 | -58.75233 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e4f87492-5332-3197-b930-10911676009e | -10.85601 | -53.77286 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09dba644-c8be-3cfe-a7af-ea1deaf9f5f6 | -12.52301 | -57.20398 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad7a6e90-06c7-332f-94c7-950c82d38e3a | -11.07738 | -55.04975 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f84fc8b-b4a2-3593-b1f1-0a8f268841fa | -9.38241 | -63.42936 | 2025-06-19 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f848608a-6973-3d85-8fd8-ee1951d95293 | -14.2161 | -45.51237 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5542e62f-423f-3b88-9c57-73d576453a97 | -11.9394 | -58.76422 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2536735e-efeb-3243-8d93-619311c7fc8d | -10.85277 | -53.76725 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0661b581-51ce-3145-b7af-b1b26086c1e1 | -11.07674 | -55.0541 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2921b4d-569a-3277-828d-ff18de17497f | -11.80333 | -57.35233 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9f009d7-29d6-3999-9771-2cc775389846 | -9.49428 | -56.08761 | 2025-06-19 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a4d9e90b-4278-325c-979c-8cc36aa87a10 | -12.79481 | -48.73483 | 2025-06-19 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 639bcd2a-ca0e-35c9-aec4-f47f3f885eb8 | -10.35792 | -57.24669 | 2025-06-19 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8eb9440-8eab-3b8e-b113-71dda833e44b | -13.58178 | -59.20525 | 2025-06-19 05:12:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81849454-1719-30f4-aa4d-ab00774eb89b | -10.19228 | -54.24161 | 2025-06-19 05:12:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaa7b8d0-d77c-388b-b9f8-7e76a58eac10 | -11.12973 | -53.93473 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ba0a2db-137c-3bcc-94c6-bac99c1e58e1 | -10.63953 | -49.46163 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b341bec-7f8f-302a-9f1b-78d0ada0df80 | -10.85424 | -53.78606 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 788b1bd8-1b55-352b-92cc-bb3071ce9bcd | -9.32934 | -47.83523 | 2025-06-19 05:12:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 659cbe2d-b8db-3ac2-94e9-5c081b35d0fd | -10.99246 | -49.54856 | 2025-06-19 05:12:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ae7d411-3a9e-3817-a02c-553e3c42fde6 | -10.72816 | -49.56283 | 2025-06-19 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0643bf25-ba24-3214-a987-a122c2d6351f | -11.94599 | -58.74373 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4f8002e-b140-3d0f-b5a2-299b346ced9e | -11.80724 | -57.34921 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5d758b4-d35c-30a4-928f-518f78bfbe9b | -12.13494 | -54.6664 | 2025-06-19 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a499f42-ed0c-31a1-8850-0374284b485a | -12.23726 | -63.59993 | 2025-06-19 05:12:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db043749-dc87-3c0a-b132-e1829b11992c | -9.01576 | -49.58825 | 2025-06-19 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a698be0-94a3-3840-b748-8e66facc18a4 | -11.95863 | -58.72781 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b335fbee-afbd-3f6b-ac66-f4d32d86a617 | -14.22244 | -45.52011 | 2025-06-19 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40970ff8-2fce-3d10-ac82-2bd3b6782cf4 | -12.47715 | -60.13901 | 2025-06-19 05:12:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 965bd44c-4569-385b-bf39-2075648b9871 | -9.01028 | -49.5905 | 2025-06-19 05:12:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8bdda89-3af6-3661-a056-c8b8ca6a949c | -11.95864 | -58.74936 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| b1ee970c-fdb4-3593-8fd9-805b36886d7a | -11.95919 | -58.74586 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 575bd99d-eb94-3ead-a1b4-9516dce39312 | -9.89299 | -48.0216 | 2025-06-19 05:12:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf95d3d1-70c7-3187-bc60-1fd46f84d805 | -12.47536 | -58.46917 | 2025-06-19 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74a8b4f2-fd75-3ba0-be82-8b3c4708eeb6 | -10.07901 | -52.74385 | 2025-06-19 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12611ff5-1f9e-3b61-9213-71f1ed6771d0 | -11.93995 | -58.76072 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0792cd43-72b4-38a1-adf8-448468458b77 | -10.63912 | -49.46484 | 2025-06-19 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89771b73-b642-3ba1-b194-d2df464433aa | -13.57903 | -59.20119 | 2025-06-19 05:12:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1b28777-9d66-393b-a776-02bfea984ce6 | -8.96244 | -47.97646 | 2025-06-19 05:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ab8fd94-cb6d-32e7-a975-409f5f9459a7 | -11.13293 | -53.94033 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8aeb202-0832-3361-ab49-1941341d21d8 | -10.75401 | -54.77771 | 2025-06-19 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbbfb861-a7c1-3c85-91f9-5268981154ce | -10.8471 | -53.7799 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 718522d0-2fff-3437-9497-3f3f88165d35 | -11.94819 | -58.75127 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e0544cc-15c3-3cd5-bdcc-cbed6b78f0e5 | -10.85569 | -53.77597 | 2025-06-19 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c4205f3-92d6-3338-ae6a-87ad20917f85 | -12.79765 | -48.73476 | 2025-06-19 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72fb597d-9ac6-3662-a49b-8e880cb1f149 | -11.95755 | -58.75637 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ffd2a0cf-9ae1-3370-af95-2d2f1e4c4a5e | -11.29287 | -53.97264 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 060f1c9a-37b5-39a1-8501-17383214f207 | -14.07921 | -53.38382 | 2025-06-19 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98ccf119-d152-3c3c-9739-76a078285d2b | -11.84198 | -62.8358 | 2025-06-19 05:12:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e47426ca-67a7-3b30-be9f-fb6379f6f85c | -11.64982 | -54.13774 | 2025-06-19 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32992c89-b04f-3777-a50b-08242e4f1ed1 | -12.48582 | -58.46723 | 2025-06-19 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a6629f6-f4f4-3e19-b977-93c36dc76370 | -11.94544 | -58.74723 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e602415f-c6b5-3d2c-802f-9af4c1721c4e | -9.40033 | -65.51474 | 2025-06-19 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cb48461-836d-314b-8e70-4fa3c8fe8e1d | -14.43967 | -48.90412 | 2025-06-19 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 14f44405-2141-31f3-8dc9-8dc2affca415 | -10.09672 | -52.73861 | 2025-06-19 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51ecd2bf-e54e-3d05-9a5f-6d5d3917997b | -11.95809 | -58.75286 | 2025-06-19 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e9c97502-aba3-3a4d-bbd1-994fd1b60079 | -11.14926 | -55.17331 | 2025-06-19 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25fd8353-d1e8-3f99-a342-815b74405fab | -8.11555 | -54.87044 | 2025-06-19 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2fa7c07-a0f9-3acd-ad2f-be047f5ca731 | -11.57268 | -47.43733 | 2025-06-19 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f38ee8b-f647-312a-951b-3adf92f9b628 | -9.88258 | -47.81136 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09bf4cc9-fb60-30df-8092-7d3c664750a5 | -14.07395 | -53.39123 | 2025-06-19 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aaf93eb-e479-30bf-a584-2feb606f81ba | -12.43089 | -54.8745 | 2025-06-19 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e5d3310-2b3c-3625-a852-f972d4260bed | -10.28194 | -60.5436 | 2025-06-19 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0787ec5-17f8-35d8-a084-533be6233fa1 | -10.51023 | -53.58389 | 2025-06-19 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28198109-02a7-34ea-ac28-8e84fa8ebdb7 | -12.5272 | -57.20779 | 2025-06-19 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5ceb6c4-dab8-31be-a64b-5a1becd8a892 | -9.38378 | -47.63886 | 2025-06-19 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
