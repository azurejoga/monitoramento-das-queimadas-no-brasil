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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e04b5e85-565a-3346-bb21-5d73a268ebed | -12.83677 | -47.3805 | 2025-06-11 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82e617cd-afb2-3420-bf4b-c8c129b1ece5 | -11.70914 | -54.04077 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b479c81-009d-3081-ade9-5c29b15ce6a1 | -10.07675 | -52.74774 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2b09274f-8b37-3cd0-a877-d011363e4376 | -12.03996 | -54.68638 | 2025-06-11 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c85c835e-d613-36a8-b327-9d74f5e4b054 | -12.20332 | -49.62888 | 2025-06-11 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4baffd4f-ca3a-34a4-b42c-7738efb41a25 | -9.8246 | -61.40324 | 2025-06-11 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d74763d-2da5-3684-99b5-6d5c7818cac0 | -10.05165 | -48.66558 | 2025-06-11 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc46c41f-ee78-3b31-a5a7-bf607d52ee8b | -12.29045 | -50.10563 | 2025-06-11 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72c3ec59-0951-380c-b265-9766bc4c9fb3 | -12.06414 | -47.32273 | 2025-06-11 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79306dc2-5995-3097-ab39-3b89aa714878 | -10.36818 | -57.50418 | 2025-06-11 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f820eb2d-5d54-3644-b90d-3ba9a201778e | -10.19143 | -49.58469 | 2025-06-11 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| faed08cc-88d7-3fd4-a856-74ce5f7a1ef5 | -11.33725 | -45.21499 | 2025-06-11 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3106d5b-bbbb-3f91-a59a-260f0aad8ba8 | -9.699 | -49.48172 | 2025-06-11 04:49:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 398b18e1-eaad-3882-8244-ec9ed99a9f79 | -8.42065 | -48.30486 | 2025-06-11 04:49:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07214294-23f9-3426-9887-b64232dd0f58 | -10.23956 | -52.23489 | 2025-06-11 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e9bdaab-4828-3792-9e60-f6ee83f7f486 | -12.77978 | -48.72469 | 2025-06-11 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84c6879e-7d4b-3a2d-b75b-838139769af1 | -12.13135 | -54.65751 | 2025-06-11 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66204a93-7369-3f19-a4fc-0048a9647168 | -15.69904 | -43.42154 | 2025-06-11 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e445d824-4037-338b-afc0-53d41b0ade5c | -14.03913 | -55.13085 | 2025-06-11 04:51:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b0f44a7-33f7-31ca-a6a6-62d7aef9d41e | -14.66824 | -53.37809 | 2025-06-11 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f839eafd-d0bc-3895-844f-11fa7260717f | -13.64392 | -53.94044 | 2025-06-11 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 567d885e-ace4-31b7-85f2-9c0d8a5e4dee | -20.75691 | -48.5317 | 2025-06-11 04:51:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d9d0512-fe7f-3cc3-a1d1-aee9fdca70f6 | -14.52964 | -47.80157 | 2025-06-11 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e208d563-d386-3cdd-a95e-d275acec643d | -19.47313 | -49.29038 | 2025-06-11 04:51:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 779ac398-03d2-3e64-9dea-4b76f83f2be1 | -15.36226 | -48.08678 | 2025-06-11 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d933a349-65d5-3cca-82c2-1b2da02414db | -20.76113 | -48.53226 | 2025-06-11 04:51:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a000c34-fc53-33d6-b1e2-d60a963ba676 | -15.79711 | -46.93343 | 2025-06-11 04:51:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 418b35bd-3d55-347d-830c-b8d4f655caa6 | -21.03876 | -55.6316 | 2025-06-11 04:51:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37034adc-f940-3372-8aed-54bd0a76dbb5 | -15.72478 | -43.492 | 2025-06-11 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d80cf634-0707-3248-9428-73b6802fd1ff | -15.84011 | -42.60091 | 2025-06-11 04:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 109b6247-6e78-399f-942e-dc95740fd1d0 | -15.37833 | -47.90263 | 2025-06-11 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a92f891-3b29-36c7-b5c2-bf131ad45c18 | -19.05087 | -53.46175 | 2025-06-11 04:51:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1398f4b2-91d5-3135-9442-2512b846a8c9 | -16.30252 | -54.88592 | 2025-06-11 04:51:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72e68247-d282-3c13-b815-598518f22ecf | -17.73299 | -54.10271 | 2025-06-11 04:51:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e41375e4-efa5-3a85-8fce-5ea47862442a | -21.04212 | -55.63223 | 2025-06-11 04:51:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cffa269c-99bf-3c55-8fdf-ae587538ed83 | -14.04131 | -55.13931 | 2025-06-11 04:51:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4af34427-be12-312e-b1e3-a1dfb52463a9 | -18.09034 | -54.29841 | 2025-06-11 04:51:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2fe251df-71ef-3ad9-b0b3-8a112d1dd604 | -19.56711 | -49.09631 | 2025-06-11 04:51:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7b42378-d0b9-3f08-8035-1f39fdcc42a9 | -15.37567 | -47.89128 | 2025-06-11 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abb6f085-3b1a-3ac0-8abd-be475b78c8a3 | -14.03848 | -55.13475 | 2025-06-11 04:51:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aa59c73-8529-378c-ba02-170f17498875 | -20.76163 | -48.52813 | 2025-06-11 04:51:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e75982de-50fd-34a7-b080-e7a3da5375bb | -13.58728 | -54.28666 | 2025-06-11 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 583454ca-6b3f-3b3d-9587-40940ef65012 | -17.41799 | -46.57551 | 2025-06-11 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdfa23d0-2bed-3d6d-8533-d455ff3fedfb | -15.38336 | -47.89602 | 2025-06-11 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbd3a3f6-5f7c-3407-85e2-1454511e701a | -15.71928 | -43.49133 | 2025-06-11 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3918bcc7-e49c-340c-ae45-75f9cd82dc7e | -15.69352 | -43.42086 | 2025-06-11 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d60bb95-98dc-3836-946c-a12b2f48378e | -20.09856 | -50.86965 | 2025-06-11 04:51:00 | NPP-375D | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5ddb1a5f-b6a4-36fc-88b3-71a903927e34 | -19.47708 | -49.29095 | 2025-06-11 04:51:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcada342-ac40-3f58-a64b-a70fd32deece | -20.44495 | -53.77433 | 2025-06-11 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbc6b4ee-4e96-338e-aa87-aca73355daf2 | -16.62256 | -52.13506 | 2025-06-11 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c8ebe25-5226-355f-b235-26fadbb321e3 | -14.04195 | -55.13539 | 2025-06-11 04:51:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 042418cb-eff8-31e7-a655-dd2180350c04 | -15.69359 | -43.42198 | 2025-06-11 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d78e214-d420-3c34-b9e7-e7183ed675cf | -14.84731 | -52.28009 | 2025-06-11 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4cf01fd0-2433-3998-8429-c13cb1bbd820 | -18.08816 | -54.2983 | 2025-06-11 04:51:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65bf7822-456b-3107-9f9c-99b04c726a62 | -18.40821 | -54.5724 | 2025-06-11 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e73f0aa-3a0b-315b-a319-8a93dfc98aef | -14.67709 | -53.38691 | 2025-06-11 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3c55bcf-8c69-39d0-8f78-1157670838af | -15.8343 | -42.60004 | 2025-06-11 04:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d232f88f-74f0-3ab5-8826-ca80e172f1ef | -14.67433 | -53.38278 | 2025-06-11 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0f86a71-d615-39df-a5fc-438135fa388c | -15.91148 | -51.20561 | 2025-06-11 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04123398-3bfc-388f-8b98-e1eb705ad619 | -14.03435 | -55.13804 | 2025-06-11 04:51:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d4eb6b-2d2c-3b3d-88a8-61f7836e0005 | -17.67288 | -47.5319 | 2025-06-11 04:51:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90bc7448-a24d-381a-bfa3-dc91d16b1c67 | -20.54322 | -54.12912 | 2025-06-11 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c4146793-04f4-3236-a6ee-9af41bb9d4f5 | -13.469 | -56.85382 | 2025-06-11 04:51:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 787e1d1d-ad25-3af0-98b3-e2db00e09077 | -14.6544 | -48.06577 | 2025-06-11 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf34013a-c569-30ce-a95b-42ab53296a33 | -20.09491 | -50.86907 | 2025-06-11 04:51:00 | NPP-375D | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f7a19ffe-11e8-3585-a3c0-4e56ac31bb95 | -14.03783 | -55.13866 | 2025-06-11 04:51:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e264c6ef-cb8f-3309-89ef-2dc5d3783718 | -15.38744 | -47.89656 | 2025-06-11 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ecb2453-f1cf-3697-8815-0b4ebf0703c4 | -16.68231 | -43.88696 | 2025-06-11 04:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f56b8e4b-375f-3150-95f7-277e7fa9091e | -13.78998 | -54.30875 | 2025-06-11 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c19864e2-2eee-34b6-ab8e-56f7a01bf0a8 | -17.0239 | -50.30112 | 2025-06-11 04:51:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6ea082e-6069-376c-8e1c-cb57794b5cf9 | -19.05421 | -53.46233 | 2025-06-11 04:51:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3250d47-7a51-30b3-8ece-24e23917c930 | -13.47198 | -56.85923 | 2025-06-11 04:51:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78753d61-70ef-3c7b-883a-7f657046e089 | -14.67376 | -53.38635 | 2025-06-11 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c82463d8-712c-3bd1-bb02-97b9c5027b9b | -16.62594 | -52.1356 | 2025-06-11 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8746492c-e776-3b9b-862c-3cff5b6926f4 | -13.2281 | -57.12618 | 2025-06-11 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6403550-0ece-38d1-a74d-91edf84318be | -14.671 | -53.38223 | 2025-06-11 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 432abb7a-0208-3353-827c-6c634a01099c | -20.44321 | -53.77476 | 2025-06-11 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d41e82c-82bc-32a1-906c-b76c95c6aa29 | -14.03282 | -55.12571 | 2025-06-11 04:51:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6d2b140-9114-360e-8d5c-f80298754ce7 | -17.41341 | -46.5749 | 2025-06-11 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea093e45-8104-3791-8ca2-2c4e516c29ef | -20.10221 | -50.87023 | 2025-06-11 04:51:00 | NPP-375D | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f299fb09-b5ef-351c-9db4-46f99d7428f6 | -14.66881 | -53.37451 | 2025-06-11 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2943b00d-7494-3d03-973f-0b1ed19d80c2 | -15.36275 | -48.08306 | 2025-06-11 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93cfa0a5-3f3c-3f94-ad35-fbbe32bdd8d2 | -20.76549 | -46.77047 | 2025-06-11 04:51:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 305f250a-4c02-3470-b38c-a1deac4a993a | -13.47281 | -56.85448 | 2025-06-11 04:51:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45a47454-afbf-3bee-918b-60736fcf14a7 | -13.5919 | -54.2798 | 2025-06-11 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7a2a394-ebbc-3514-87b9-c316e410ec8d | -20.47707 | -53.67681 | 2025-06-11 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 689b561f-e132-3552-911a-2ad6a1f7cb0f | -15.07793 | -48.94548 | 2025-06-11 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e852537-d8bb-351c-94f3-11f674811b89 | -21.03938 | -55.62783 | 2025-06-11 04:51:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4ff8ede-b14a-382e-9e07-6570c75b65ef | -21.04275 | -55.62844 | 2025-06-11 04:51:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3603b7f8-24ad-3d16-9a52-8d9ce79fdf8f | -16.30653 | -54.88276 | 2025-06-11 04:51:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b621638e-be14-305e-b0db-899af7f8778b | -15.69911 | -43.42265 | 2025-06-11 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 239cacfc-50fc-357f-8529-c7b4d6bf54ca | -19.47466 | -49.28831 | 2025-06-11 04:51:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e240fab3-9dac-3a73-845d-6d608f8c21ec | -15.69864 | -43.42522 | 2025-06-11 04:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dddd1eb4-1a83-3b9d-a8e5-7fd77919cfba | -15.3788 | -47.89905 | 2025-06-11 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d37b88f7-781c-326d-9ae2-b58549fd1f39 | -17.9169 | -45.54482 | 2025-06-11 04:51:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0df23f57-38a9-3cdd-aac3-ff54bde42a09 | -14.67157 | -53.37865 | 2025-06-11 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da719be0-b25c-3290-bf3c-679b62ed4b47 | -21.49368 | -53.05495 | 2025-06-11 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02a9aabb-0a07-3e15-ac3b-af598c74a5f5 | -14.53368 | -47.80227 | 2025-06-11 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2c89cd3-5143-3017-aae9-eb1cba8953a1 | -13.64729 | -53.941 | 2025-06-11 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51c8ce2d-faf7-35a2-aa2f-eda70cb774ae | -15.38472 | -47.12565 | 2025-06-11 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
