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
| 2b3516fb-7581-3225-91a8-e0f50e807694 | -18.84674 | -53.62045 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d54aa23-c34f-3d40-b3f4-6654faad7a00 | -12.41048 | -49.67756 | 2025-06-05 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07817605-1771-38b1-abbb-5f5c66493240 | -11.54383 | -56.43312 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4765dfd-76c9-342a-a8a7-21751b2990f1 | -18.84307 | -53.61985 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2fab639-7b0b-340d-a1b4-8cc05ec47bf8 | -13.51452 | -56.55598 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afc06ed2-b411-3628-a366-69062a7d48a5 | -12.36625 | -54.17027 | 2025-06-05 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fafb1467-aa38-3cb3-9d96-e0b5f9428ee3 | -13.50784 | -56.55486 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 788676e4-dece-3138-8342-4e688bea5a6a | -11.62679 | -55.3842 | 2025-06-05 05:01:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dbd4a4b-6890-3ba2-8b87-8e18f8266f17 | -18.84901 | -53.6231 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20cfd2d7-dd9a-34ff-ab40-2e93dcce9146 | -12.6647 | -58.21889 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da542884-57fc-3a8e-9346-75df6cf3ef5b | -11.53654 | -56.4356 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5732433-a3e8-3e83-acb8-76f453180be5 | -11.54661 | -56.43726 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24fad30d-d082-350e-ba45-952a410fa123 | -11.54996 | -56.43782 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2860315-4654-3367-ad5b-3d36b170e588 | -13.51442 | -56.57802 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 258a3b16-b270-348c-a207-beb841b88548 | -11.62734 | -55.38067 | 2025-06-05 05:01:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21d168e5-f8ce-32f4-bf4f-a0e00828c54b | -13.51844 | -56.55296 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaba33de-2254-360d-8960-e0b78b49e019 | -14.23329 | -45.47672 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 851870fa-5695-310d-a58b-519fc6ef8212 | -13.51004 | -56.56258 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73638b43-817d-3a53-9540-7060549485f1 | -13.5317 | -56.57723 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7068a350-e843-3be1-a451-cc0951305fb2 | -18.8412 | -53.63314 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4d32f212-ee08-39b5-9120-6e6b1225b936 | -11.55286 | -56.41987 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7df7f0a6-c4b1-3c9d-84d2-ddf67a900cd4 | -14.227 | -45.48018 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7431e9d-cce8-3e48-861d-d20ab518ab09 | -18.8369 | -53.637 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 41cac184-3e22-3d78-81ee-4791fdc7d94b | -13.5234 | -56.5648 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 671127f5-7b52-3cf6-a4eb-8da5d2e15d9b | -13.50669 | -56.56202 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8969ffdd-1fce-3374-a813-6b427c4aca4c | -13.52788 | -56.55821 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91dc9d7c-3b01-3805-a58b-80cdca75e227 | -13.52053 | -56.58273 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f9a8f32-7dbc-3964-aa38-03b0a625692b | -14.22777 | -45.4831 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03d2d89b-8b26-3b72-bedc-f713c512552a | -11.55112 | -56.43064 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dce72ef3-f2fc-3da2-b17b-9f9e97c65a69 | -13.08328 | -49.24746 | 2025-06-05 05:01:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0127d082-acb0-3a69-bc7f-e910d0238591 | -13.51776 | -56.57858 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8299ae9d-fe3a-3f4a-9c28-eacf7200b579 | -13.52502 | -56.57611 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0efe0d89-b271-3358-862d-df13f835091d | -14.7326 | -45.10332 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6747a834-4bea-3c44-bd80-4865a57606ff | -13.5212 | -56.55709 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5bd6dbd-93da-3bcf-8387-fdc3c9a26780 | -13.53227 | -56.57365 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a4ca71e-6849-3799-bfea-311396e4f76c | -11.81063 | -58.84957 | 2025-06-05 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a03c55c-224b-329c-a5ef-e5f4b97d56cb | -12.65274 | -54.11891 | 2025-06-05 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d44dcc83-da98-3bd1-8d90-26c48bccf82e | -14.22653 | -45.48435 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f18a561-e1e7-3f88-b22d-88d04afb79d8 | -13.50727 | -56.55844 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bb57f18-c854-3bd6-8b11-4098b72e86de | -18.83448 | -53.62753 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4402386-e463-3f50-bc64-7e9e44c5b7c7 | -18.8351 | -53.62309 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f36a7dea-c742-3b45-a9cb-7bebf78dae5c | -13.50393 | -56.55789 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37095b31-98bf-3e51-8f3b-6d9e003af3d4 | -13.52617 | -56.56894 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f580a2bd-dedc-3f49-96d9-73cf3ed92152 | -13.50946 | -56.56616 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c128edc-0ba2-39ea-ae40-c823d6fa1577 | -13.53399 | -56.56291 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db0b4388-fb4c-3c91-8dad-b9b646a4c35a | -18.84737 | -53.616 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4687f57-8f48-382d-b491-043c410ec1bb | -13.51834 | -56.57499 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 039b22e1-b0e8-3136-b223-c0edaba0cd07 | -18.83385 | -53.63199 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfe88be0-7c62-3288-80a8-e156d664ca4d | -13.08943 | -52.04685 | 2025-06-05 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35852a91-8306-3324-a854-086d1d5b5a90 | -14.22827 | -45.47893 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b600f13f-344c-3669-aba5-985cd4601bb7 | -13.72251 | -58.67536 | 2025-06-05 05:01:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f60b8c0e-20a0-3d3c-b39b-c74a784462aa | -11.55344 | -56.41628 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c99ba413-98f0-34d8-94ea-c69af8112498 | -13.50612 | -56.5656 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0dc9200-e727-3fbe-84d1-994ee6ba5736 | -13.51165 | -56.57388 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66a29d36-f6e7-38f3-86a9-8df14c55f35a | -12.66821 | -58.21951 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9032ef0a-4ded-3fa2-a881-7d6ae1964254 | -11.62346 | -55.38366 | 2025-06-05 05:01:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4a3b66f-b7d2-3d15-b8ff-bebebe719691 | -13.14827 | -56.81255 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bedc51b-c647-3654-9688-7d34fa461bcd | -11.55228 | -56.42346 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5cebd8d-dfcb-31ef-928b-69ee6f97cc7c | -18.83877 | -53.62369 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ef593d9c-9027-3392-8d72-1bd33ac48cab | -13.53285 | -56.57006 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9699253b-1ca1-3bac-8747-45975824f14f | -11.73823 | -56.44253 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bf7f43c-b5cc-3270-9b4e-077492e31bc5 | -14.15648 | -45.48691 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afc752a5-a036-347b-9634-300f4021020b | -13.52006 | -56.56425 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 49549906-5ecc-3473-b37e-621b9d8b7b1f | -18.84182 | -53.62872 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 60b072d4-bfd0-37f3-84bb-2eef694523ed | -13.51719 | -56.58216 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d69fa87-1815-3225-9968-f8c1fe749018 | -19.40035 | -54.46616 | 2025-06-05 05:01:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96d6a3a8-490a-3163-85d8-d57200377a1a | -13.51395 | -56.55956 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ee5fed99-7730-372b-bea4-f737794921c3 | -13.53122 | -56.55877 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de1f279e-d5da-32b6-95e5-a8212baefe1e | -13.52235 | -56.54994 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b47f78e-ed14-3405-ad7f-268d8b0afa18 | -13.52454 | -56.55765 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee8497c6-5fe9-3a8f-83fe-e7cb6f87be89 | -19.07691 | -53.45947 | 2025-06-05 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31e8eb55-6b03-3319-828d-910b13af5ec6 | -12.28079 | -57.27066 | 2025-06-05 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38482933-11a2-315e-b212-3f1ac4a0a11e | -13.51786 | -56.55653 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8c5cd28-8b3d-3790-b094-bd5e53fa072a | -11.78578 | -54.77544 | 2025-06-05 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 49ac52d9-35a6-3d60-b529-1b7e0c48e631 | -13.50497 | -56.57276 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc8776e8-71b2-37e6-ad9c-a361c48def35 | -13.51176 | -56.55184 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d95f362-eb69-3da4-a8a6-5f8bcb25ab5b | -11.74159 | -56.44309 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bb04117-2645-3ec9-8a1c-303fcde77f8e | -12.17155 | -54.3236 | 2025-06-05 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3eb2339a-299c-3ce8-9b48-fa23fb3de6ae | -18.83815 | -53.62813 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 75cbf60a-fc20-3d8d-be58-91a03c5fcc3a | -13.52444 | -56.5797 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e973e4c-ffd2-3c28-b9d4-206112b0721e | -12.36569 | -54.17395 | 2025-06-05 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86295ff8-41d0-31e7-b188-e37954f4b534 | -13.51557 | -56.57085 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| aa01e949-0724-3909-bda0-478f08347d12 | -12.64767 | -54.12948 | 2025-06-05 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 134c0a21-6022-3adb-aa8e-dec06c6df75d | -11.65238 | -62.76734 | 2025-06-05 05:01:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84fea995-dda4-37ea-a1c7-b00593bfde2c | -13.52512 | -56.55408 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52e47e8a-32a0-31fc-a2dc-bb46d45ac57a | -19.06768 | -53.44392 | 2025-06-05 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1b05eb0-ef26-3053-a2fc-0a4c09876037 | -18.84961 | -53.61866 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33f9bfcc-4967-39d3-b140-86e21cdcf851 | -13.50335 | -56.56147 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c8ac7e7-0830-32da-b6df-054383df1c94 | -11.53595 | -56.43919 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3368bb2a-a0cb-3cf2-b33b-79af1e534e01 | -13.51338 | -56.56314 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ba5b71fb-1743-3b47-8020-91fc7688c49c | -11.63067 | -55.38121 | 2025-06-05 05:01:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba8dd5bf-e04b-3838-94c3-db1e341b5e6f | -13.51891 | -56.57141 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| b4e7ada4-893a-35f7-a729-2673332c8edd | -11.63455 | -55.37822 | 2025-06-05 05:01:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfa3ccf9-8abe-33af-9135-534783a6e533 | -12.67172 | -58.22013 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 46313f04-442e-3cf7-9eac-ae215a68277f | -18.84244 | -53.62429 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 368f2028-2eb1-3a37-8478-54d3f8a70759 | -12.36681 | -54.16658 | 2025-06-05 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df386845-8d28-325c-a626-3d1a65bbc5ec | -13.08387 | -49.24302 | 2025-06-05 05:01:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 050f95e2-33f1-318d-bb91-898eb1f68fad | -14.1623 | -45.48763 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b73559a-75cc-3f12-b098-89e779ec62cb | -18.84002 | -53.6148 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f71ffbe8-2895-343b-8543-843780b35a05 | -13.51729 | -56.56011 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |


[Clique aqui para ver as próximas entradas](README17.md)
