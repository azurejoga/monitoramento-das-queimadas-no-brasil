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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bbc1a9f-0592-35f7-95ae-0530e4cef909 | -15.19846 | -47.1994 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89107cae-883c-3f66-8c1e-dc2ea60b6b76 | -13.17718 | -48.45174 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 721b6ecb-cab2-3930-9cce-1f04e74933ae | -18.83066 | -41.95494 | 2025-10-29 04:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c71e12a6-5dee-34e6-9707-8f8996e9a220 | -11.94283 | -44.30719 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f5e52b1-5fd9-384e-ade0-bbc3e5781c99 | -17.48687 | -44.06723 | 2025-10-29 04:25:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17cb6166-2a89-3ebc-95d6-fb3c493f20c2 | -19.28239 | -43.72424 | 2025-10-29 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aefd6a04-4f4e-3b86-a285-f912f8770239 | -14.1992 | -48.35546 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceaa34c4-d0c4-3ade-ab80-9ff17882cedb | -13.94296 | -48.47358 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cdfacd2-dafa-3f1b-b4ec-0a3d442725a7 | -11.78275 | -44.16877 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be65d232-93cc-313c-9145-bbb3e592e03d | -17.26098 | -45.29009 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1cf41a4-ad28-398e-b3e0-6d80711d2849 | -14.31179 | -48.01278 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3785a08c-f216-309f-b22d-4d86d77ea299 | -13.42747 | -47.3718 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b6171b14-5478-33d3-8299-e9e28c494b6b | -13.33195 | -47.48294 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfcfe7b4-3397-3d8d-8b58-53b15d2da0a6 | -18.58404 | -44.02526 | 2025-10-29 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec3c5bd6-e748-3099-9fab-baffbee7c08a | -13.34732 | -47.67274 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560e3cfa-90c1-3006-98ce-ec7ecd0cfea6 | -13.27073 | -47.73174 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10cfc8c8-effe-3ff2-a15c-d34c025d78b6 | -12.40452 | -46.78648 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3211c67-ba71-33fd-abe2-80bc0b144c13 | -11.99998 | -46.77826 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2e1f3b5d-b4b5-312b-bd0b-0442b7aae844 | -14.4827 | -49.32994 | 2025-10-29 04:25:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3542c1d8-4c7e-3034-b384-e15e2d2e11a6 | -17.20239 | -44.45054 | 2025-10-29 04:25:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18e55553-90a5-3967-8a8f-252224776e4e | -13.69773 | -47.68626 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d79c4bce-1c0a-3fcc-ab2d-a6615725ac61 | -13.36516 | -47.38412 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dc14914-54fa-35b7-a4f5-9919c975c816 | -15.16003 | -47.22596 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31f1391e-4cc5-376f-afec-522404e2253e | -13.6539 | -48.27109 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdd12ed3-cf1f-3d10-91f5-9b885b7b7776 | -11.37119 | -47.01688 | 2025-10-29 04:25:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2a3347e-486d-33f1-b2de-2c843105d839 | -14.19516 | -48.35859 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3da783c3-7ec7-3a48-a1b0-1e1af9884d6b | -13.91487 | -48.47213 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47d429bb-c1ad-31df-8edf-77bd084d5aaa | -13.25022 | -48.00685 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 882c9a0a-21ba-3d76-a6b1-32505be88c20 | -13.61311 | -46.51146 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30a6d161-dca8-3070-b8e6-707f2e6c43d8 | -18.92509 | -45.04034 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cf6dbb07-5505-3bdc-822c-3009af06c986 | -12.14692 | -47.70118 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9573d854-9426-3143-8874-7a39cc8e17d9 | -13.66447 | -47.18251 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0481a8e-1efa-3e68-8201-258239b2d361 | -16.11971 | -45.75042 | 2025-10-29 04:25:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 03bd9e8a-362f-3936-8fb2-92d64b5d3223 | -12.10521 | -44.59336 | 2025-10-29 04:25:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70f8d5ab-8d23-3674-9921-8466d565d907 | -13.55098 | -47.17059 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa0b5f20-9753-3b82-ba55-745b24d03194 | -12.85981 | -48.62666 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37d53c83-67b8-38d6-ab7d-932a61a98f3e | -13.68452 | -47.18582 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 104c77aa-e0e9-3ae4-b640-0df293c4ff4d | -12.58621 | -43.36861 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e99a9a77-4cad-3fb7-8f2f-af7939d1ce64 | -13.23324 | -47.06287 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6a8c127-d07e-39c9-ac7f-ae8c6789a3cc | -12.21573 | -46.48531 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0cc3d37-329d-3554-b2b0-bd418e22f5bd | -15.45851 | -47.68683 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56cbdbdc-7649-3ab2-85cb-97d377ff61fd | -11.78617 | -44.16931 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cd59e60-5977-325e-bcd6-626088d890be | -13.69101 | -47.68497 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31d320f5-ded8-34ef-a8c0-1aa0645c54ec | -13.61991 | -46.50504 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0aa32fdb-ec30-3f84-a8c2-8f4f9f400579 | -14.79142 | -46.17479 | 2025-10-29 04:25:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8698d50e-c484-3c43-9947-6c57bb12f6dc | -16.04802 | -43.71157 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaf19acd-5687-37f6-b326-2580b575c0a0 | -15.74527 | -45.11364 | 2025-10-29 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86ac2cb0-ccf1-35fb-813c-cdbeaa164273 | -12.85987 | -47.23322 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4150143d-72ce-39a0-887a-534d0602897f | -12.78077 | -47.37289 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1a96cbc-ff58-31ae-a58f-676d7fb0d995 | -12.05653 | -47.8277 | 2025-10-29 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| feced856-4a5a-3eb3-90e7-57c83d4d91ef | -12.86331 | -48.62724 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95951404-156e-383e-9f2e-860e803359b8 | -13.91866 | -48.44925 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37a9e184-8aae-340d-89e1-d1b89605b427 | -12.00001 | -49.84969 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33249e45-ebcf-3c96-a75f-b332650897d0 | -15.63712 | -46.97116 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0457f61-cbc3-336d-879c-7c2faf779a63 | -13.93771 | -48.44098 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3404e140-bf0a-348e-a903-abad80dc4703 | -11.03833 | -47.85046 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15f74111-dbc4-3485-980c-e5d09e128dc6 | -11.93522 | -51.33447 | 2025-10-29 04:25:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 153f7b46-0c98-3c7e-94b4-af8cfc402a73 | -13.2132 | -47.05952 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e205566b-68cb-3228-ad2a-a9243113c798 | -13.64187 | -47.0463 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5821b6d-9f82-3ecc-9652-8a55bbcf5972 | -13.60918 | -48.41773 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ab3e1d2-d12e-3507-825e-8b79d6f3423e | -13.30345 | -47.467 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33607747-3847-3f8d-b55b-193032b6d064 | -13.64245 | -47.04269 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48ba338c-1ad1-3924-8044-9c60aed9a17b | -18.92978 | -45.03268 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b27b3147-fe25-3846-9d7c-aa91dde150ee | -14.12009 | -44.19101 | 2025-10-29 04:25:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53032552-24b2-3362-8bd7-2b96a79bbb72 | -12.74319 | -46.93382 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faaddb5b-0d51-3fc4-92fd-9ef4e458bc9d | -13.64591 | -47.02123 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d1884f5-98cc-3386-8748-9425137c581c | -11.9994 | -46.78183 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c7b356a2-dfc2-3d7b-9ffa-73994205c8d3 | -13.35071 | -47.67322 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 333b851b-1d9b-3143-8ecb-41c4e715cab4 | -11.2284 | -49.92391 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35acd6fa-062c-3423-9f8e-31e56db4550d | -13.23143 | -48.56464 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fd25d5a-69a9-3735-8dc3-7ee3e6adce4a | -14.24384 | -48.10803 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da41358e-2fe3-3e83-b4e8-018b56e02e41 | -12.70103 | -46.30729 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 59dd834a-d89e-323a-afab-25b8f59ff80e | -13.63371 | -46.52554 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28cc6c57-cc0a-3024-aabb-848c9618302f | -17.26287 | -45.28683 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 112d9087-86ac-35dd-8d30-505615997ac2 | -13.9911 | -44.54405 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed17e718-9fe0-38e1-b708-0f96438ea696 | -12.28807 | -47.00587 | 2025-10-29 04:25:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72e89df7-8d68-3f36-b89c-bb1f0c3aee7d | -10.85535 | -50.1254 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ecd7552-3ce5-3d14-9f9b-bfbd9d4e023c | -11.07521 | -48.32335 | 2025-10-29 04:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0d3ade6-5a5e-3d30-81db-568ac43324e3 | -13.24051 | -47.06036 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a2dde20-bfe0-3bab-815b-f47090fd2fe6 | -15.17173 | -47.2169 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8729e53e-e8e4-3927-9ba4-8cb8d0a833ba | -13.30729 | -47.07159 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e309526-35fe-3e4b-9976-728636f622c3 | -18.92099 | -45.0439 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| a4ba4304-4e67-3a55-a747-abcf8c4398a7 | -13.65189 | -48.45195 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8c31b49-11ea-3ffb-823d-c4d0ee518f23 | -14.32121 | -46.52244 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8caf7736-d981-3731-9418-bcb1669b01c1 | -13.32438 | -47.44444 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9adb2509-5c1c-3ee3-819d-0bfd9b41a033 | -13.62971 | -48.43624 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73f412b1-c593-370b-ac14-fcb18841ea96 | -19.33708 | -43.05207 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b47b4a77-5fa6-385a-a1a1-0ef0805a44cb | -13.04483 | -43.82084 | 2025-10-29 04:25:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 579e3eec-5b46-3287-b357-ed9e0d7b049d | -15.19513 | -47.19886 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd490d8c-2280-3eaf-a1b1-59639fa1a368 | -13.47337 | -47.81831 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 418eda49-f699-3128-8cf6-10c39c12c2bd | -13.20477 | -47.06921 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f5f5d81-4a05-3049-bb78-5550a97b5d9c | -13.35784 | -47.38684 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52947ce0-e1fe-3c81-a01a-2b865ab4e03c | -12.06321 | -45.71878 | 2025-10-29 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 733dfbf3-44a8-367e-9c96-b841ecfab29b | -12.41179 | -44.70831 | 2025-10-29 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81fa2a00-4508-38a3-91ed-69d332bee607 | -14.61947 | -48.41459 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd0e991a-89a9-3709-bdfb-747c1c7141c4 | -13.23348 | -47.72576 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e169e4ee-e2b2-3c94-9031-01d07cc7c3b9 | -14.52026 | -47.99908 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bcb008e6-717f-3668-9719-b66d8669ebb9 | -11.70055 | -46.7031 | 2025-10-29 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f673fbd-56cf-3275-963d-77f82c793005 | -12.05901 | -46.62365 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 558ca05d-e587-3b14-9d93-973d61618e86 | -10.8637 | -50.10364 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README47.md)
