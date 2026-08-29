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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 571c7cbd-4b70-3f4a-b3f1-a966e25ece93 | -11.48318 | -45.10173 | 2026-08-29 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7cfe13d8-827f-3a7d-9d0a-943024d762b3 | -11.02951 | -49.68155 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74037b0b-3ba5-3d18-8963-0bccf4010a22 | -14.59846 | -47.9716 | 2026-08-29 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 967da447-acf7-357b-98b7-bdd44e26b180 | -18.78412 | -45.5952 | 2026-08-29 04:34:00 | NPP-375D | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d606dfe-a000-39b2-a7d2-af89c0a358b0 | -15.64605 | -45.92722 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 935d211e-a642-3ad1-9ec5-a2245bc4fd0c | -17.59277 | -51.61588 | 2026-08-29 04:34:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6a869dd-b246-32cc-8bb7-3aaffbacd4df | -11.03648 | -57.22688 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d2f9963-16e9-39e3-95c3-490d7ac282d4 | -14.1699 | -52.82884 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0bd26bb-9e5e-3fc4-92c0-3c7538138781 | -11.71102 | -54.54032 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1db5a55-c340-3a4b-b613-4111b1566f39 | -12.78564 | -46.45485 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a76515ab-b5b3-3c7d-bf60-71ec31e928b3 | -13.25121 | -41.32636 | 2026-08-29 04:34:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 77e2b4ed-c556-3f51-85f6-6fd6fbe31251 | -14.19624 | -52.85585 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dc8b027-8815-3ed8-b6d7-9944fd05f6f6 | -14.75898 | -48.74834 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfb051df-2919-3f99-90ce-4e3c9f2a52c4 | -11.27057 | -54.03823 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c0f1d16-4c2b-3a10-aa59-11e98ffa641d | -11.61566 | -46.72784 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ca0102-7a55-38be-836a-f3c3c136418b | -15.64214 | -45.9303 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| ae4cd7a7-d272-330a-9385-322f60193de9 | -12.77624 | -46.44965 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 445517a7-abaf-3a47-9f01-5b973f063d1c | -10.80586 | -54.0233 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcda1295-9cbf-33f2-91a8-79f1b6288a1d | -14.15323 | -52.84042 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89d2e3b4-ecaa-34bf-9f37-42adad52fa52 | -11.48373 | -45.09817 | 2026-08-29 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d91ef4b-b51f-3fc8-b592-6ad9e30e8428 | -11.26492 | -54.01385 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e581b79-e7ef-3524-8118-8b804347bb45 | -17.5118 | -40.25797 | 2026-08-29 04:34:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0111086b-36a1-3506-a212-f7f9a73f6d36 | -15.6304 | -45.93949 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e75b86-6692-3689-9a95-566e81df2997 | -15.64662 | -45.92358 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8925fd8f-09aa-3b32-a34a-25a26cdcad88 | -11.83763 | -46.7715 | 2026-08-29 04:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 895a1acf-7279-3cb4-8984-e850882ebd57 | -14.90728 | -56.30833 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 900f13e4-d5f3-3289-94e0-5b80c7a4f5a0 | -13.35584 | -46.90937 | 2026-08-29 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bfffa15-6172-338c-80d9-8a17cca30ff2 | -9.96295 | -53.93718 | 2026-08-29 04:34:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53697e3c-aa0a-3d25-92aa-051e94865964 | -11.48203 | -45.06497 | 2026-08-29 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76138367-a6b6-3b68-ae0a-998ce9c8c740 | -14.41245 | -52.57951 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6551ca12-9a71-323f-9094-bc26006be9e7 | -16.4796 | -49.42554 | 2026-08-29 04:34:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99b841e5-4784-3f91-9c3e-3bdadb3904f1 | -11.0319 | -57.25039 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8d81663-dd6a-31c3-bc02-22a94e7db668 | -13.32502 | -48.18964 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5493c59c-86b1-31aa-b7ba-0fc5d6dd5de4 | -14.9058 | -52.63022 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3b3de9c-fbf0-3bd1-9192-be952568b0a9 | -11.48726 | -46.9486 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 921ce29a-3c90-30f2-8110-834e494b88cd | -15.64774 | -45.9163 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 477e130c-792c-3589-aef3-3e023d69057a | -11.03917 | -57.21309 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 582897e0-0f79-3337-a8be-c7df3d0a2c86 | -11.49061 | -46.94916 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3f291a6-1d18-3c1e-bd24-037b7a1ab319 | -11.61899 | -46.7284 | 2026-08-29 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b610051-c935-3a07-801b-8a5d897e3175 | -12.4106 | -40.92087 | 2026-08-29 04:34:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfbf84dc-1d12-36c9-b863-de58459cc057 | -17.28748 | -46.03059 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 456072be-32a1-3489-9294-6d75cc08e0b5 | -14.89313 | -52.62786 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02a5d1f8-8e51-30c0-b0d3-ea092ce6cb41 | -15.64718 | -45.91994 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b43509e1-a233-30f4-aa30-72f262ca8a2b | -11.03127 | -57.22122 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 62727685-af19-3114-9c42-40f5b79dcbe5 | -11.02955 | -49.68431 | 2026-08-29 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1098114-9cc3-36be-927b-05097cff70be | -12.43371 | -42.89196 | 2026-08-29 04:34:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bda36b6e-923b-3afb-b326-dbe43e75331e | -15.65863 | -48.36898 | 2026-08-29 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 57830fff-8a0d-3755-a575-96372045859e | -12.43484 | -43.41066 | 2026-08-29 04:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1bb49b5-e2b3-3829-9480-f590bf49b059 | -14.41569 | -52.58025 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cdb57ef-4f59-3bc5-ad88-c88357a726f2 | -14.41239 | -51.74219 | 2026-08-29 04:34:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca03792a-033d-35d2-89c2-84bf52a39380 | -17.28525 | -46.02253 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82e320b9-1590-3b08-bdbc-97ed06f76121 | -11.23806 | -53.99016 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0a1374f-5ca0-3970-9554-89d617b2c506 | -14.42756 | -52.58717 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fca9bcd-1282-3d69-8728-8fcbd32d7fca | -10.8023 | -54.01291 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bb4da28-9197-3569-8a26-64696505ee02 | -15.37442 | -52.67626 | 2026-08-29 04:34:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 412c408b-848f-3f34-9bef-8d064af07537 | -14.2072 | -52.84507 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df6ce693-036b-3711-9651-d5582e77e1d1 | -14.19115 | -52.85915 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 296db703-429b-364a-b4c5-39902c246c6d | -14.1762 | -52.84308 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d26a652b-285a-3754-be0b-e342b2014fd0 | -12.19467 | -50.55007 | 2026-08-29 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 780cd807-995d-3d74-8c6e-61b7e4cab69d | -13.31509 | -48.20726 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1158b66-e5e2-3cb6-bd98-4912145fc41d | -13.31635 | -48.19959 | 2026-08-29 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8dcd35c-d26d-3cd6-9089-7a3bfdeb03e9 | -18.78355 | -45.59907 | 2026-08-29 04:34:00 | NPP-375D | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 580aaa2c-b996-3cca-bdbb-3450dae69b19 | -17.28187 | -46.02201 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28652227-4b54-30b2-be01-d3cfa86013f6 | -11.03171 | -57.21738 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2321ff16-e2e3-33e1-8178-d0b470e5a1f9 | -14.4407 | -52.61095 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5484f3b-0b92-38b5-8bc8-dbf218d25581 | -12.76853 | -44.26648 | 2026-08-29 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f333d425-a441-34a0-8b9c-4fe6932d46a9 | -13.65866 | -47.73338 | 2026-08-29 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 731af1ad-57bc-312a-878c-c9e29fa9928e | -14.94182 | -56.33072 | 2026-08-29 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bbcc507-a03a-3814-bd57-fe76d166b56f | -14.39768 | -50.06214 | 2026-08-29 04:34:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c5bb775-23de-37fc-8630-6b5fc85e08db | -11.48652 | -45.10227 | 2026-08-29 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c1ffa076-935e-34d5-b3df-759f1762d69b | -13.35269 | -43.64863 | 2026-08-29 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 065d5f47-dcbd-3373-b85f-6768905955fe | -14.41666 | -52.58047 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d4a0b1d-6148-30aa-a453-fd0d0a5f7dfe | -13.16723 | -55.6593 | 2026-08-29 04:34:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bde71ec-f2dc-3887-908b-cd68fccf676d | -10.55702 | -59.62001 | 2026-08-29 04:34:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4750e20d-2378-3b3e-b6ec-16d6582c793a | -11.62508 | -54.58948 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9134d9f-0dd6-3301-9ef2-6d96db05e25c | -11.03556 | -57.23158 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc80c4ba-076d-380c-b425-27ac8b49c6f3 | -12.78176 | -46.45783 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46a0a1f7-b779-3e59-8f35-15f542058498 | -11.79371 | -47.65807 | 2026-08-29 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7190c281-3e50-32b4-8b37-424628b8654f | -17.28073 | -46.02951 | 2026-08-29 04:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f221b1f4-4f48-332e-9a39-731cd7ebbec7 | -15.6469 | -45.93039 | 2026-08-29 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5fbb6b9c-26d5-3d8f-b7af-dd8a946d6d9f | -14.75625 | -48.75294 | 2026-08-29 04:34:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffdf4183-93aa-3d3e-a358-dee8f5b002ad | -14.16557 | -52.82804 | 2026-08-29 04:34:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f397f0f6-3190-3ebe-a82c-738f14cbc786 | -14.40872 | -52.57061 | 2026-08-29 04:34:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50657240-36cf-3257-a90f-99551aa4cd4e | -10.50678 | -59.63282 | 2026-08-29 04:34:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8f8c93e8-2862-362d-8ff3-cb6cbf3ca785 | -13.86449 | -54.1217 | 2026-08-29 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87c6e6fc-88d9-3c78-a49b-3f584008d02c | -13.35209 | -43.6527 | 2026-08-29 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ca1a08a-d2fd-3940-8b9a-78fd7b934313 | -11.19331 | -55.10763 | 2026-08-29 04:34:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02d72dce-b972-322b-b946-5f0da69d6ab7 | -15.73917 | -51.16796 | 2026-08-29 04:34:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f895c7fc-9699-3d3d-a5f6-c9471adc9035 | -16.17903 | -45.63716 | 2026-08-29 04:34:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06a2139c-1027-3cf1-8f21-1dae9b29cb16 | -16.61372 | -49.40773 | 2026-08-29 04:34:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3f354ae-2e8f-31fa-9b3f-cc92c566e40e | -15.37371 | -52.68022 | 2026-08-29 04:34:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b2cc27e-1bce-3a3e-bdb5-5ab4cf9ab030 | -11.22387 | -53.98814 | 2026-08-29 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59f029a9-0f91-31f7-a050-b3372e1a8842 | -11.25892 | -54.01861 | 2026-08-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cc22031-5b7e-3683-a5a6-c5c34fad220a | -14.41086 | -50.05115 | 2026-08-29 04:34:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0bb6c52-d5e5-3c83-847f-50194418cc3a | -12.43068 | -42.88721 | 2026-08-29 04:34:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c78465f7-f7e8-3b25-8d80-d2272b7c980b | -11.02791 | -57.23613 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f1d9c3b-cc93-36f9-9407-92de564068d6 | -11.04433 | -57.21897 | 2026-08-29 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 909896f6-a6d7-3358-b85f-cbed9b2a67fb | -12.75842 | -46.47579 | 2026-08-29 04:34:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f391bffa-af8c-3988-9a9c-39ee605b300d | -13.25171 | -41.32282 | 2026-08-29 04:34:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 56766e50-527f-3cc3-86a5-0c70064421a3 | -23.15241 | -48.666 | 2026-08-29 04:36:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README39.md)
