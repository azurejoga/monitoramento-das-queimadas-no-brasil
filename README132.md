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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d267f51d-6171-3bb8-8c4b-44e87134f447 | -6.57922 | -52.92566 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 71f6da8b-02f6-3fbd-b8c0-e4ce8528d908 | -6.57606 | -52.92018 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f92bffc-6ed1-3613-b462-7a37433d8e18 | -6.57532 | -52.9251 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1469dcf1-4921-36e8-98ff-ff1e7b266afa | -6.57142 | -52.92454 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c3a33ca-6854-3c4e-a9c7-e6fb0fbdd1de | -6.23671 | -53.32955 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 638fbee1-c954-3ec8-b4c9-79c661d640f0 | -6.23604 | -53.3341 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 20c3020f-85ba-3717-8c1d-8122e53b46a1 | -6.23226 | -53.33352 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 972271c3-eede-399b-9a82-b227b7329382 | -5.85156 | -53.55701 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1bacc9f-9239-3b95-906f-9d1dd427be95 | -5.85021 | -53.56581 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15a874e1-b063-3a54-9085-d43978c82416 | -5.84718 | -53.5608 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ede48c4-460f-31ff-90f0-38c496c46f39 | -8.7119 | -54.82518 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b944ac28-0f81-3bd4-a7c6-9e6c55fe38a3 | -8.70833 | -54.82442 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67bfa962-5c15-3112-bc44-446bc57db21d | -8.70538 | -54.81949 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23c9ef78-ca37-3374-95e1-1eb40e04c9b0 | -8.70239 | -54.81479 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7657eabb-51e5-3c58-accf-83401112f51c | -8.6958 | -54.80956 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 627b8e07-d4ee-3ac7-a50f-9d646fe24937 | -8.69479 | -54.8068 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c221085-2d99-3774-9f33-77b515cdf2cb | -8.69419 | -54.81078 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bab7f00-cdbb-3c79-93fa-76068f818da0 | -8.69221 | -54.80896 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9583c9b-3cb1-3ee0-b308-03c1a329eea9 | -8.69121 | -54.80616 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e974f1eb-351d-3b66-9978-547404dd0d2b | -8.6906 | -54.8102 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee2ebd30-fbab-342d-b815-571783acfc51 | -8.68921 | -54.80426 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e6f3bf9-41d3-333e-8119-1dbbbd761bc6 | -8.68861 | -54.80834 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1742134-805d-34af-9d08-6b819938b84e | -8.68825 | -54.8014 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 481c6c35-a4bd-3c13-b968-f164944031c4 | -8.68763 | -54.80551 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b8a9a9c-a504-3e60-aac5-435099c25e9d | -10.63406 | -55.20758 | 2024-10-02 05:10:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 762e61d0-4e27-36c6-b4eb-a8cf2824bb30 | -10.62043 | -54.06485 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb107935-ac5e-3034-8217-7a1f4303590e | -10.61729 | -54.05949 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 790d6ffa-6698-3557-8aa5-937b3b58d4ef | -10.61275 | -54.06372 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec6c203a-0bc8-30cb-90f7-b3e679384965 | -10.36626 | -54.87777 | 2024-10-02 05:10:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50262295-525e-377f-a2f5-aea3cf7efe84 | -11.43468 | -54.30887 | 2024-10-02 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8326f98-f677-336d-bf35-a99f5b9dfe79 | -11.43086 | -54.3083 | 2024-10-02 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5d2d9dd-cd00-37d2-b6af-afd8654fe012 | -11.42704 | -54.30772 | 2024-10-02 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 705d714b-c188-3a55-843e-f97982c345fa | -11.42089 | -55.06295 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0347d291-d379-3fbf-9fe8-0854b67bfe4a | -11.41722 | -55.06239 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd45681d-a314-34f7-b086-2ace834e3508 | -11.38343 | -55.1147 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 089db897-46d1-3935-be70-3a8da7295a00 | -11.37977 | -55.11417 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b76ec461-08a2-3fc3-8ec2-2b915bfbee97 | -11.37914 | -55.11848 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a5793d-252f-38fb-b56b-7635b8cf9bf5 | -11.37852 | -55.12278 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af4a135-c8cd-3fea-8401-808455ad552f | -11.37487 | -55.12226 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01987147-f8c8-322c-82eb-061664bb3aaa | -11.36861 | -55.19114 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37c81f58-20df-35a2-823a-c2f2e76a4574 | -11.36496 | -55.19063 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 773de4cc-0246-3091-94d3-845c3280343a | -11.36434 | -55.19492 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f91fd265-5dc3-30fb-b73b-3c87b3d2119c | -11.36008 | -55.19868 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edddfffb-84af-3138-8384-a1cb2c298252 | -11.35644 | -55.19815 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72bf82a4-5e7f-341a-83a5-da24045df7c1 | -11.32181 | -55.20789 | 2024-10-02 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 285ee521-3995-3cbd-b85b-8cb4904c25d9 | -11.30314 | -54.31078 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 824dfd8e-0728-332e-a836-2f916c6d3ef6 | -11.29932 | -54.3102 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a1dd830-8431-3385-a0c6-3c955935f290 | -11.23762 | -54.1827 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b036348-bb74-3695-83ec-d34a2c2959b7 | -11.23377 | -54.18216 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4c30f44-b70e-378c-a51a-ac118540a239 | -10.99946 | -54.25983 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a79a7f-90dd-3419-945c-6bcd503a9f79 | -10.88039 | -54.68701 | 2024-10-02 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d988dfa6-23e9-3b3c-8083-70dcf2294e41 | -6.40644 | -55.4952 | 2024-10-02 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1240ab9b-5725-3283-8099-900e9b73a61e | -7.44205 | -55.46913 | 2024-10-02 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f788707-bd0c-30d9-ba6f-53dce9478371 | -7.40123 | -55.50536 | 2024-10-02 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7a68ab3-9575-3acd-ac24-ee1bbfc1507d | -7.39936 | -55.50531 | 2024-10-02 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e4fc7e5-5fa7-3b73-b39c-6d1a72124652 | -8.19318 | -55.1685 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4176c633-d5c5-35f5-b2ec-2696f98806f6 | -9.9998 | -55.38808 | 2024-10-02 05:10:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fce9f0c-81c8-375e-9b7c-0fc1fdabaea2 | -9.78108 | -56.29539 | 2024-10-02 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44b975b1-9294-31f5-a4bd-bf5a8317063a | -9.69492 | -55.49901 | 2024-10-02 05:10:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e958ba9b-fcbc-3e67-bc8f-2e75ea6d96f3 | -9.57538 | -56.02327 | 2024-10-02 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e80dea1-239d-3406-91e9-982caaf4e9bc | -10.76872 | -56.37759 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6847e730-224b-3ec3-a05a-968d2aa8ef40 | -10.62769 | -55.87796 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e35db370-c34b-367a-bb9f-9735b3d11272 | -10.62711 | -55.88187 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64270fe4-04aa-3791-a54a-4fc8a8acc1ad | -10.6242 | -55.87741 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc66cba3-ae0e-3474-b6d5-cd6e41f228fb | -10.62362 | -55.88131 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a980c97a-912a-3d59-9d18-503bee0bb405 | -10.62304 | -55.88519 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b244a20a-040a-35b7-aa1e-2ddc19916618 | -10.6207 | -55.87686 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b3f46e2-9cbc-3fa2-94d2-0859e94faf2e | -10.62012 | -55.88075 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da045c13-7d70-333d-b96f-8201688ca9e2 | -10.61954 | -55.88462 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9202a84b-6ddf-3984-833b-1607f03aa4b3 | -10.61663 | -55.88019 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 774ded73-1ed8-319d-b5af-85bd0f8b107a | -10.61605 | -55.88407 | 2024-10-02 05:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9598dae-c078-30d0-ac3b-8c64ba863be4 | -10.39473 | -56.34161 | 2024-10-02 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5e2d74a-c243-37fd-b192-65794f366cc5 | -11.32971 | -56.23832 | 2024-10-02 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0e962b2-f227-3cbd-8b6e-a606d47f021d | -11.32913 | -56.24217 | 2024-10-02 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6db06c82-3f92-35e8-b06b-29c82bfb18de | -11.32624 | -56.23779 | 2024-10-02 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33738ac2-a1e8-376d-bda9-f754648b820c | -11.32566 | -56.24165 | 2024-10-02 05:10:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 789081ed-0843-3a73-8f68-dec3fdc2712b | -10.33315 | -57.50934 | 2024-10-02 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dec8f52-1220-3080-90e6-d356d5e32733 | -10.33092 | -57.50174 | 2024-10-02 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b19c740f-dd34-3c37-a472-9a2a140c07dd | -10.33037 | -57.50527 | 2024-10-02 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2420abb2-67a4-3e54-ba20-2adafe7ac1f9 | -10.32981 | -57.50881 | 2024-10-02 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d67d085f-f6d7-3b58-a050-2b0a0688339c | -10.28132 | -58.20341 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c95b4e4e-121a-3661-870d-3db57d7575e4 | -10.06479 | -57.89968 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8a8d5ecd-5340-35d4-988b-6e007056e63c | -10.13153 | -56.76634 | 2024-10-02 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3d1d5f1-0c9d-3463-9689-1f961a6509b7 | -10.12925 | -56.75854 | 2024-10-02 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcd2f675-7c18-3065-8cb8-fe666de24b05 | -10.1287 | -56.76217 | 2024-10-02 05:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e8659d-e5bc-3ac2-b5c9-932d1de0db4c | -9.98265 | -57.88692 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f63d8b5-e1ba-37e5-a7fa-906bda202426 | -9.93111 | -57.50011 | 2024-10-02 05:10:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67c060fb-bc51-3cf0-857d-d29cf1c823d2 | -9.7609 | -57.79035 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0831e48-b44c-3f7a-9dcc-92047d48cc50 | -9.76035 | -57.79385 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b91a640-f0ca-3cc5-b6d4-8094b6abd805 | -9.71189 | -57.93336 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e65ce10-5244-3db4-87ab-1aeee5900153 | -6.98166 | -59.0976 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b65df45-893e-39b8-a49b-658a50a40b67 | -6.97885 | -59.09338 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b46e7bdf-9cf1-3c78-ba2c-fd3ccbdd20a3 | -6.97825 | -59.09706 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08de4c3a-20e0-3a2f-959a-2e36d0680b65 | -6.97766 | -59.10074 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7064c085-6744-39a5-a7de-093e7f9759b0 | -6.97484 | -59.09651 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a9a450-41e3-39a9-ba72-fb4718f2cf11 | -6.97425 | -59.10019 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fcc9940-8271-3368-a8a6-74e1964f5952 | -6.97203 | -59.0923 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea62b77e-ce19-3c28-a765-0f2393fcc1ef | -6.97143 | -59.09597 | 2024-10-02 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3cecae0-7214-37aa-babb-8983f6b1e5ba | -6.50133 | -58.38558 | 2024-10-02 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa0def9b-0275-368d-8d82-da936e83480d | -9.2013 | -58.21024 | 2024-10-02 05:10:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README133.md)
