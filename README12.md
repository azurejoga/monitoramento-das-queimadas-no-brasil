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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26fe1d1e-0b51-3b4a-b154-04f496c53722 | -10.59481 | -53.51309 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c04cf0cc-5d7b-3f83-9289-632cdb649725 | -12.6913 | -54.5774 | 2026-06-18 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bbe9813-c5a1-3f09-9b90-babcd1f38940 | -18.83355 | -51.47386 | 2026-06-18 05:23:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4e2aaa0-8e3f-32d9-a90c-30675f963d7a | -9.44378 | -59.20715 | 2026-06-18 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0808be04-1f31-3770-8cb1-b861dc38d3d9 | -10.91284 | -56.85298 | 2026-06-18 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6621e6b7-793d-3af7-9c2e-f06a344fa1eb | -8.97501 | -47.97913 | 2026-06-18 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a31f7946-1bac-35b4-9e5a-52abeafbc603 | -9.21081 | -47.93367 | 2026-06-18 05:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8ea468ec-0561-3982-b644-a1f82176f2af | -8.97449 | -47.98304 | 2026-06-18 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5f1f096-5d9f-3686-b8aa-00fa37c055a6 | -12.69107 | -54.57979 | 2026-06-18 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5789fb25-516b-3dee-8bb3-30b0ca7e6c24 | -14.09847 | -59.46745 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62458c52-08ca-309f-8564-fd44c361ced1 | -10.55891 | -46.23476 | 2026-06-18 05:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca7f68c6-7b38-3976-adb7-caf919dfa21b | -11.26287 | -53.9548 | 2026-06-18 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54f97f8b-04fc-3986-ae4f-521e7d0cfabd | -9.20929 | -58.06972 | 2026-06-18 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 574d686d-cbdf-3730-a587-ac01b8d492a5 | -11.24714 | -46.64003 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 643c1654-1152-3090-84b4-c856557fd538 | -10.04156 | -48.11102 | 2026-06-18 05:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6bffa79-b742-364f-bd0f-8add54496d4d | -11.79413 | -57.35503 | 2026-06-18 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f19207bd-1f9d-3ede-8b90-a5ad2b870b03 | -14.09125 | -59.4699 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c452f819-643e-3397-b6de-e99433cfe222 | -10.58209 | -53.48563 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 151a6e3c-3c5c-39b4-a866-f19b153a1fdc | -11.24706 | -46.64268 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02b5bb08-80cf-308f-9963-603a96dac114 | -10.98074 | -47.74561 | 2026-06-18 05:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ea53275-0453-3631-ad03-9e929f2e90ab | -8.97508 | -47.9812 | 2026-06-18 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2e76a73-7331-3542-8d92-d1f85780109d | -18.82385 | -51.46627 | 2026-06-18 05:23:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40408a32-4681-3107-b329-7a2a17ecf15b | -9.6482 | -65.70821 | 2026-06-18 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 643e52de-0784-3e11-a1c9-7b97a7ba381f | -11.24882 | -46.62724 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44144313-d2ce-3ad4-b1b7-8d012ed9df8f | -12.20521 | -52.77699 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af8a9cc-7097-3eed-958e-aa9e7aa3fadf | -12.69058 | -54.58236 | 2026-06-18 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98cc8449-1c89-359d-b4a9-b72ab5520641 | -12.21389 | -52.77829 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a89bf34-d9d8-318b-bcbc-77be60c39e16 | -10.58665 | -53.48257 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c45b32a9-93af-3b7a-a938-1de4434097b7 | -11.54593 | -52.79174 | 2026-06-18 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 074e89eb-2f9b-3bf8-a3e6-a74ab2d6241e | -10.15043 | -56.61508 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b8d1e3a-591f-3a2b-91d3-fba6dd354920 | -9.37076 | -50.53559 | 2026-06-18 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c665373-2282-335e-b7b0-b855e9c18ad1 | -18.82349 | -51.46948 | 2026-06-18 05:23:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba1cf6bd-756c-3c9c-9d55-3ef38dec35cd | -12.07799 | -47.55557 | 2026-06-18 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a8531e5-7813-3f5e-9544-c27b9c70565f | -11.25422 | -46.63555 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c0cad9a-9782-312c-b280-3c6240cdab97 | -14.09181 | -59.46634 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60f85c7e-1dca-321f-8b36-4867a6e8c929 | -9.74885 | -47.87185 | 2026-06-18 05:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6954a598-48e8-333c-bdfb-8c708fcdd8bc | -12.20577 | -52.77278 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0b96241-def3-3b86-93b5-951b16736f0e | -9.21647 | -47.93399 | 2026-06-18 05:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1a9ab4a6-0e75-37ba-890a-362c342759c2 | -11.26097 | -53.95689 | 2026-06-18 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60ad8a6c-f919-321c-bde3-ceaa1eb494c3 | -18.41517 | -54.54688 | 2026-06-18 05:23:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55853531-c366-3eb3-a2fa-ac3df786de6f | -14.08962 | -59.45866 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aed599e6-ac44-31c4-9caa-9c75bad8229b | -10.04918 | -48.09451 | 2026-06-18 05:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7577db5-77c6-3c58-881f-4818ffa3a2b1 | -11.81066 | -52.52431 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc8bd073-f5d0-39a6-a4b3-840a28669ecb | -10.91627 | -56.85351 | 2026-06-18 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d872f482-6483-3e14-9469-2e6f312a710d | -10.27711 | -60.54306 | 2026-06-18 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b788cb8d-3105-3e37-92f1-265ca6a90cdb | -9.21699 | -47.92989 | 2026-06-18 05:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 87bdde90-9a0a-359e-9f31-c7f106242727 | -10.7702 | -54.10735 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49d53150-9ecd-3d24-8d54-af9b2d47e709 | -10.5598 | -46.2346 | 2026-06-18 05:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52d89af3-c3a8-38b6-8f77-debeee1d0973 | -10.55326 | -46.23379 | 2026-06-18 05:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3a3f106-be76-3fe1-b79d-1793a54806b8 | -8.98074 | -47.98005 | 2026-06-18 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b111ca9-ce36-3336-987c-a8d4a1271fc1 | -11.48435 | -52.9193 | 2026-06-18 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9faf0682-2f83-3f47-9333-eaeedc52a543 | -10.04146 | -48.1092 | 2026-06-18 05:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc96c729-7086-3912-a48b-11dbb8d68be6 | -14.09627 | -59.45977 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3bc9312-1bdd-351c-adda-4f5b425117e8 | -10.05449 | -48.09905 | 2026-06-18 05:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67b58926-db7d-3352-a373-1f7fec940e1c | -10.15443 | -56.61188 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f31480f5-819b-3126-b126-671d4a810405 | -12.20955 | -52.77765 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e2482a8-92b5-3d35-b802-33bc84b124e9 | -9.20596 | -58.06919 | 2026-06-18 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39293a31-5acc-3956-a20f-7f070e1abcda | -10.1533 | -56.61934 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8603987d-6676-371b-9a08-123226a6f8a1 | -12.24606 | -56.17246 | 2026-06-18 05:23:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d485d36-23a0-39fd-979a-c06770c2d7d6 | -11.25361 | -46.64053 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb3c389d-c931-337c-82c0-adc520115a86 | -12.20464 | -52.78122 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcdbc3d2-8524-3dd3-a913-b895525951e8 | -13.20325 | -50.34269 | 2026-06-18 05:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c655d12-11a6-3fcc-9bec-110fa665436f | -13.6515 | -60.62101 | 2026-06-18 05:23:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f9a320a-cca0-31d6-814a-476e58641779 | -11.25412 | -46.63805 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0179fbb-891b-3ca7-892a-83eee385674c | -14.08905 | -59.46222 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26da084a-cab2-38d1-94d1-2e528b8a52b5 | -10.04097 | -48.11315 | 2026-06-18 05:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4235f8cb-72e5-3500-a6f4-e7d496edb5b4 | -9.77563 | -48.97031 | 2026-06-18 05:23:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78949828-4e78-38d3-a27c-dc687df5bd5c | -14.09018 | -59.4551 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ff4064c-5444-34f5-9efd-e64cf715a940 | -10.78377 | -53.58008 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89449ea0-a933-354f-8371-06092b874aca | -11.35495 | -55.82659 | 2026-06-18 05:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6482881e-ab83-3ca5-b935-823a23997b66 | -9.74248 | -47.87503 | 2026-06-18 05:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a824f48-2d27-3fa1-8cd0-3d0d11351412 | -10.71051 | -49.53609 | 2026-06-18 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1341d0ad-1896-373b-a01d-2948a4614128 | -10.58242 | -53.48625 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8d339ed-d851-31bc-87b3-1a6acb511225 | -10.71947 | -59.26907 | 2026-06-18 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 07a14615-121e-35d7-9aa8-55268afe75d4 | -10.59431 | -53.51665 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7586833-a499-330e-8ed6-ac086b96b0aa | -10.04869 | -48.09845 | 2026-06-18 05:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f151e266-7e73-3e21-be5f-63f08b2d77e3 | -12.07184 | -47.55479 | 2026-06-18 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01958a9c-f5b3-3a48-98fa-453c02fee8f8 | -12.21333 | -52.7825 | 2026-06-18 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dc22ccc-f7ea-3212-8d4f-9955f4c298c9 | -9.19153 | -58.05254 | 2026-06-18 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21ac9a66-614f-3c5b-a931-a925cdab22aa | -10.58295 | -53.48265 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a369a324-d129-31f0-9f8c-401873938999 | -10.81627 | -56.59105 | 2026-06-18 05:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21b40a6f-d739-370d-9b9d-1bdaac93961d | -10.12204 | -52.17926 | 2026-06-18 05:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7cea111-fc79-3f58-a845-fa2aedd7cd3d | -9.18876 | -58.04851 | 2026-06-18 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d323c26-4a18-3d36-94d6-b24c4a564e4d | -14.09351 | -59.45566 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a505550c-438f-3d63-a89a-a80dde11ae01 | -10.91341 | -56.84924 | 2026-06-18 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8514cc1e-2695-359e-8c80-6cb6a241bbff | -11.24777 | -46.63481 | 2026-06-18 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ac5783b-a9f8-3ece-a633-b27d09da2175 | -10.04725 | -48.10992 | 2026-06-18 05:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ede99eb-0b8b-342f-845e-ac078a38b916 | -10.59381 | -53.52021 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c600a765-a34f-343a-b49b-08e4f81264df | -21.58327 | -53.81185 | 2026-06-18 05:23:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5dc3185-75e0-3b4d-8103-57fd3ce4eff8 | -9.21136 | -47.92958 | 2026-06-18 05:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7aaf1eeb-cde5-3631-8e87-92cb5142b0a4 | -10.81569 | -56.59488 | 2026-06-18 05:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdd93158-5a7f-32f5-becf-3d17eb32ab93 | -9.18821 | -58.05201 | 2026-06-18 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65fc50ef-be3a-3caf-a24f-3d986eb4b2b2 | -11.35556 | -55.82246 | 2026-06-18 05:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 107ec9d2-f807-3a24-9c03-c72b6bb631d5 | -10.54391 | -53.72226 | 2026-06-18 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46966a15-1b89-3da7-a3d9-bb121d4fd606 | -9.19209 | -58.04904 | 2026-06-18 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27ad4011-c4c0-3e1b-896e-17413cd83ecf | -14.09238 | -59.46277 | 2026-06-18 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc52f0ee-9e8c-3e57-a3c2-0964c448f290 | -9.77517 | -48.97374 | 2026-06-18 05:23:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f54fb9be-6641-3d8b-ac49-5f47a1853386 | -10.71889 | -59.27261 | 2026-06-18 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df32074f-1ffe-3241-b173-2c78d0bd0a48 | -13.19247 | -50.34432 | 2026-06-18 05:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17ea81d7-756f-325b-a7da-7edba823ddbd | -10.15386 | -56.61561 | 2026-06-18 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README13.md)
